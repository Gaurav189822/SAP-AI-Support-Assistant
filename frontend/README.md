# SAP AI Support Assistant

Enterprise AI-powered SAP troubleshooting assistant using Retrieval-Augmented Generation (RAG), semantic search, vector embeddings, FastAPI, React, and FAISS.

---

## Features

- SAP issue troubleshooting chatbot
- Semantic search with vector embeddings
- Retrieval-Augmented Generation (RAG)
- FAISS vector database
- PDF upload support
- Enterprise React frontend
- FastAPI backend
- Dockerized backend
- Semantic similarity references
- Conversation history support

---

## Tech Stack

### Frontend
- React
- TailwindCSS
- Axios

### Backend
- FastAPI
- Python

### AI / RAG
- Sentence Transformers
- FAISS
- HuggingFace Embeddings
- Groq Llama 3

### DevOps
- Docker
- GitHub

---

## Architecture

Frontend (React)
        ↓
FastAPI Backend
        ↓
Retriever
        ↓
FAISS Vector Search
        ↓
SAP Knowledge Base
        ↓
LLM Response Generator

---

## Setup Instructions

### Backend

```bash
cd backend

python -m venv venv

venv\\Scripts\\activate

pip install -r requirements.txt

uvicorn app.main:app --reload
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## API Endpoints

### Chat Endpoint

```http
POST /chat
```

### Upload PDF

```http
POST /upload-pdf
```

---

## Future Improvements

- Authentication
- Persistent database
- SAP ERP integrations
- Cloud deployment
- Fine-tuned SAP LLM
- Multi-user conversations

---

## Author

Gaurav Sharma