
import ollama


def query_llm_with_context(query: str, context: str) -> str:
    """Generate an HR answer using the local Qwen model."""

    system_content = """
    You are an HR policy assistant.
    Answer questions using only the supplied HR policy context.
    Do not invent policies or assume facts not present in the context.
    If the context does not contain enough information, clearly say
    that the HR policy context does not provide the answer.
    """

    response = ollama.chat(
        model="qwen2.5:7b",
        messages=[
            {"role": "system", "content": system_content},
            {
                "role": "user",
                "content": f"Question: {query}\n\nHR Policy Context:\n{context}"
            }
        ],
        options={"temperature": 0.2}
    )

    return response["message"]["content"]
