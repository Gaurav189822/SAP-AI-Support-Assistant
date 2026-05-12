from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer(
    "sentence-transformers/all-MiniLM-L6-v2"
)

def generate_embeddings(text_chunks):

    embeddings = model.encode(
        text_chunks,
        convert_to_numpy=True
    )

    return np.array(embeddings)