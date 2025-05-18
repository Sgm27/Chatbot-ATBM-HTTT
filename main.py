import os
import openai
import chromadb
from chromadb.utils import embedding_functions
from dotenv import load_dotenv

load_dotenv(override=True)

OPENAI_EF = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-large"
)










