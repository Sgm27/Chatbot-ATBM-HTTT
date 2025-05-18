import chromadb
from chromadb.utils import embedding_functions

import os
from dotenv import load_dotenv

load_dotenv(override=True)

EF = embedding_functions.OpenAIEmbeddingFunction(
    api_key=os.getenv("OPENAI_API_KEY"),
    model_name="text-embedding-3-large"
)

