from embedder import embed_User_query
from vectorstore import search_chunks
from llm import query_llm_with_context


def process_user_query(query: str):
    print("\nSearching the HR policy...")
    query_vector = embed_User_query(query)

    matched_chunks = search_chunks(query_vector)

    if not matched_chunks:
        print("No relevant HR policy content was found.")
        return

    context = "\n\n".join(matched_chunks)

    print("Generating your answer...")
    answer = query_llm_with_context(query, context)

    print("\nHR Assistant Answer:")
    print(answer)


def main():
    print("=" * 40)
    print("       LOCAL HR POLICY ASSISTANT")
    print("=" * 40)

    while True:
        user_query = input("\nAsk an HR question (or type 'exit'): ").strip()

        if user_query.lower() == "exit":
            print("Goodbye!")
            break

        if not user_query:
            print("Please enter a question.")
            continue

        try:
            process_user_query(user_query)
        except Exception as error:
            print(f"\nError: {error}")


if __name__ == "__main__":
    main()
