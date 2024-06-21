import os
import pinecone
from langchain.vectorstores.pinecone import Pinecone
from assistant.embeddings.openai import embeddings

pinecone.Pinecone(
    api_key=os.environ.get("PINECONE_API_KEY"),
    environment=os.environ.get("PINECONE_ENV_NAME")
)

vector_store = Pinecone.from_existing_index(
    os.getenv("PINECONE_INDEX_NAME"),
    embedding=embeddings
)

def build_retriever():
    return vector_store.as_retriever()