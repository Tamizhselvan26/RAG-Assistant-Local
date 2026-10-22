from pathlib import Path

from pdfreader import read_pdf
from chunker import chunk_pages
from embedder import embed_chunks
from vectorstore import store_chunks

PDF_PATH = Path(__file__).resolve().parent / "resources" / "HRPolicy.pdf"


def run():
    print("Reading HR policy PDF...")
    pages = read_pdf(str(PDF_PATH))

    print(f"Read {len(pages)} PDF pages.")

    chunks = chunk_pages(
        pages,
        chunk_size=900,
        chunk_overlap=150
    )

    if not chunks:
        raise RuntimeError(
            "No text was extracted. Check whether the PDF contains selectable text."
        )

    print(f"Created {len(chunks)} text chunks.")
    print("Generating local embeddings...")

    embeddings = embed_chunks(chunks)

    print("Saving chunks to local ChromaDB...")
    store_chunks(chunks, embeddings)

    print("HR policy ingestion completed successfully.")


if __name__ == "__main__":
    run()
