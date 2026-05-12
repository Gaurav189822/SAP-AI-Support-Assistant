from app.rag.data_loader import load_all_datasets
from app.rag.data_cleaner import clean_data
from app.rag.chunker import create_chunks

df = load_all_datasets()

cleaned_df = clean_data(df)

chunks = create_chunks(
    cleaned_df["combined_text"].tolist()
)

print("\nFirst 2 Chunks:\n")

print(chunks[:2])
