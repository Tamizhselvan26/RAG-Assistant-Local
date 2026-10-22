
import chromadb
from typing import List

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="hr_policy",
    metadata={"hnsw:space": "cosine"}
)


def store_chunks(
    chunks: List[str],
    embeddings: List[List[float]],
    namespace: str = ""
):
    """Store HR policy chunks and embeddings locally."""

    if not chunks:
        raise ValueError("No text chunks were extracted from the PDF.")

    if len(chunks) != len(embeddings):
        raise ValueError("Chunks and embeddings must have equal lengths.")

    collection.upsert(
        ids=[f"chunk_{i}" for i in range(len(chunks))],
        documents=chunks,
        embeddings=embeddings,
        metadatas=[
            {"chunk_index": i, "source": "HRPolicy.pdf"}
            for i in range(len(chunks))
        ]
    )

    print(f"Stored {len(chunks)} HR policy chunks in ChromaDB.")


def search_chunks(
    query_vector: List[float],
    top_k: int = 4,
    namespace: str = ""
) -> List[str]:
    """Retrieve relevant HR policy chunks from ChromaDB."""

    total = collection.count()
    if total == 0:
        raise RuntimeError(
            "The vector database is empty. Run dataprocessor.py first."
        )

    results = collection.query(
        query_embeddings=[query_vector],
        n_results=min(top_k, total),
        include=["documents", "distances"]
    )

    documents = results["documents"]
    return documents[0] if documents else []
