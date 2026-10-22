
from typing import List
import ollama

EMBEDDING_MODEL = "nomic-embed-text"


def embed_chunks(chunks: List[str]) -> List[List[float]]:
    """Generate local embeddings for document chunks."""
    if not chunks:
        return []

    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=chunks
    )
    return response["embeddings"]


def embed_User_query(query: str) -> List[float]:
    """Generate a local embedding for the user's question."""
    response = ollama.embed(
        model=EMBEDDING_MODEL,
        input=query
    )
    return response["embeddings"][0]
