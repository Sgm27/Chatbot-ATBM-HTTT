import os
import asyncio
from lightrag import LightRAG, QueryParam
from lightrag.llm.openai import gpt_4o_complete, openai_embed
from lightrag.kg.shared_storage import initialize_pipeline_status
from lightrag.utils import setup_logger
from dotenv import load_dotenv

load_dotenv(override=True)

setup_logger("lightrag", level="INFO")

WORKING_DIR = "./data"
if not os.path.exists(WORKING_DIR):
    os.mkdir(WORKING_DIR)

async def initialize_rag():
    rag = LightRAG(
        working_dir=WORKING_DIR,
        embedding_func=openai_embed,
        llm_model_func=gpt_4o_complete,
    )
    await rag.initialize_storages()
    await initialize_pipeline_status()
    return rag
INSERT_FILE = True
async def main():
    rag = None
    try:
        # Initialize RAG instance
        rag = await initialize_rag()
        if INSERT_FILE:
            with open("./atbm.md", "r", encoding="utf-8") as f:
                content = f.read()
                await rag.ainsert(content)
        mode="hybrid"
        result = await rag.aquery(
            "Tôi muốn tìm hiểu về các phương pháp tấn công phổ biến",
            param=QueryParam(mode=mode)
        )
        print(result)
        with open("./result.md", "w", encoding="utf-8") as f:
            f.write(result)

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if rag:
            await rag.finalize_storages()

if __name__ == "__main__":
    asyncio.run(main())