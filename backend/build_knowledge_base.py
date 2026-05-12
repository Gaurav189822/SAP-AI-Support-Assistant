from app.rag.data_loader import load_all_datasets
from app.rag.data_cleaner import clean_data
from app.rag.chunker import create_chunks
from app.rag.embedding_generator import generate_embeddings
from app.rag.vector_store import VectorStore

print("\nSTEP 1 — Loading datasets")

dataframe = load_all_datasets()

print("\nSTEP 2 — Cleaning datasets")

cleaned_dataframe = clean_data(dataframe)

print("\nSTEP 3 — Creating chunks")

chunks = create_chunks(
    cleaned_dataframe["combined_text"].tolist()
)

print("\nSTEP 4 — Generating embeddings")

embeddings = generate_embeddings(chunks)

dimension = len(embeddings[0])

print("\nSTEP 5 — Creating vector database")

vector_store = VectorStore(dimension)

vector_store.add_embeddings(
    embeddings,
    chunks
)

vector_store.save()

print("\nKnowledge Base Created Successfully!")