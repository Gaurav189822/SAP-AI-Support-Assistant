from fastapi import UploadFile, File

from app.rag.pdf_loader import extract_text_from_pdf
from app.rag.chunker import create_chunks
from app.rag.embedding_generator import generate_embeddings

import pickle
import faiss
import numpy as np

from fastapi import APIRouter

from app.models.schemas import QueryRequest
from app.rag.retriever import retrieve
from app.services.llm_service import generate_response

router = APIRouter()


@router.post("/chat")
def chat(request: QueryRequest):

    retrieved_docs = retrieve(request.query)

    context = "\n".join([
        doc["chunk"]
        for doc in retrieved_docs
    ])

    answer = generate_response(
        request.query,
        context
    )

    return {
        "query": request.query,
        "answer": answer,
        "references": retrieved_docs
    }

@router.post("/upload-pdf")
async def upload_pdf(
    file: UploadFile = File(...)
):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:

        buffer.write(
            await file.read()
        )

    # Extract text from PDF
    pdf_text = extract_text_from_pdf(
        file_path
    )

    # Create chunks
    chunks = create_chunks([pdf_text])

    # Generate embeddings
    embeddings = generate_embeddings(chunks)

    # Load existing FAISS index
    index = faiss.read_index(
        "vector_store/faiss_index.bin"
    )

    # Load existing chunks
    with open(
        "vector_store/chunks.pkl",
        "rb"
    ) as f:

        existing_chunks = pickle.load(f)

    # Add new embeddings
    index.add(
        np.array(embeddings).astype("float32")
    )

    # Add new chunks
    existing_chunks.extend(chunks)

    # Save updated index
    faiss.write_index(
        index,
        "vector_store/faiss_index.bin"
    )

    # Save updated chunks
    with open(
        "vector_store/chunks.pkl",
        "wb"
    ) as f:

        pickle.dump(existing_chunks, f)

    return {
        "message": "PDF uploaded successfully!"
    }