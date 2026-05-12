from app.rag.embedding_generator import generate_embeddings

sample_chunks = [
    "SAP MM purchase order issue",
    "ABAP syntax error in report"
]

embeddings = generate_embeddings(sample_chunks)

print("\nEmbedding Shape:\n")

print(embeddings.shape)