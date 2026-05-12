import faiss
import numpy as np
import pickle


class VectorStore:

    def __init__(self, dimension):

        self.index = faiss.IndexFlatL2(dimension)

        self.text_chunks = []

    def add_embeddings(
        self,
        embeddings,
        chunks
    ):

        self.index.add(
            np.array(embeddings).astype("float32")
        )

        self.text_chunks.extend(chunks)

    def search(
        self,
        query_embedding,
        top_k=5
    ):

        distances, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k
        )

        results = []

        for idx, distance in zip(
            indices[0],
            distances[0]
        ):

            results.append({
                "chunk": self.text_chunks[idx],
                "score": float(distance)
            })

        return results

    def save(self):

        faiss.write_index(
            self.index,
            "vector_store/faiss_index.bin"
        )

        with open(
            "vector_store/chunks.pkl",
            "wb"
        ) as file:

            pickle.dump(
                self.text_chunks,
                file
            )