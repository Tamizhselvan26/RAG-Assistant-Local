from typing import List
def chunk_pages(
    pages: List[str],
    chunk_size: int = 900,
    chunk_overlap: int = 150
) -> List[str]:
    """Combine PDF pages and split the text into overlapping chunks."""

    if chunk_size <= 0:
        raise ValueError("chunk_size must be positive.")

    if chunk_overlap < 0 or chunk_overlap >= chunk_size:
        raise ValueError(
            "chunk_overlap must be at least 0 and less than chunk_size."
        )

    full_text = "\n".join(page or "" for page in pages)
    text_length = len(full_text)

    if text_length == 0:
        return []

    chunks = []
    start = 0

    while start < text_length:
        end = min(start + chunk_size, text_length)
        chunk = full_text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end >= text_length:
            break

        start = end - chunk_overlap

    return chunks
