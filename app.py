import os
import asyncio
import streamlit as st
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_mini_complete, gpt_4o_complete, openai_embed, gpt_o4_mini_complete
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger
from dotenv import load_dotenv

load_dotenv(override=True)

setup_logger("lightrag", level="INFO")

WORKING_DIR = "./data"
if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

async def initialize_rag():
    rag = LightRAG(
        working_dir=WORKING_DIR,
        embedding_func=openai_embed,
        llm_model_func=gpt_o4_mini_complete,
    )
    await rag.initialize_storages()
    await initialize_pipeline_status()
    return rag

async def generate_response(query):
    rag = None
    try:
        rag = await initialize_rag()
        mode = "hybrid"
        full_response = ""
        
        result = await rag.aquery(
            query,
            param=QueryParam(mode=mode, stream=True),
            system_prompt="Bạn là một chuyên gia về An toàn bảo mật và Hệ thống thông tin. Bạn có thể trả lời các câu hỏi về An toàn bảo mật và Hệ thống thông tin. Nếu câu hỏi trắc nghiệm chỉ chọn 1 đáp án đúng nhất, giải thích các đáp án sai. Trả về câu trả lời dưới dạng markdown."
        )
        
        response_placeholder = st.empty()
        async for chunk in result:
            full_response += chunk
            response_placeholder.markdown(full_response + "▌")
        
        response_placeholder.markdown(full_response)
        return full_response
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return f"Error: {str(e)}"
    finally:
        if rag:
            await rag.finalize_storages()

def main():
    st.title("💬 ChatBot ATBM HTTT")
    st.subheader("Hệ thống trả lời các câu hỏi về An toàn bảo mật và Hệ thống thông tin")
    
    # Display chat messages from history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # Input for new message
    if prompt := st.chat_input("Nhập câu hỏi của bạn..."):
        # Add user message to chat history
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # Display user message in chat container
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # Display assistant response in chat container
        with st.chat_message("assistant"):
            response = asyncio.run(generate_response(prompt))
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main() 