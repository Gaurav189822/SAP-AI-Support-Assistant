import faiss
import pickle

from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

index = faiss.read_index(
    "vector_store/faiss_index.bin"
)

with open(
    "vector_store/chunks.pkl",
    "rb"
) as f:

    chunks = pickle.load(f)

def retrieve(query, top_k=5):

    query_embedding = embedding_model.encode(
        [query]
    )

    distances, indices = index.search(
        query_embedding,
        top_k
    )

    results = []

    for i, idx in enumerate(indices[0]):

        results.append({
            "chunk": chunks[idx],
            "score": float(distances[0][i])
        })

    return results