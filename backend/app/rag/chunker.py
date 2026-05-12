from langchain_text_splitters import RecursiveCharacterTextSplitter


def create_chunks(text_list):

    print("\nCreating text chunks...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    all_chunks = []

    for text in text_list:

        chunks = text_splitter.split_text(text)

        all_chunks.extend(chunks)

    print(f"Total chunks created: {len(all_chunks)}")

    return all_chunks