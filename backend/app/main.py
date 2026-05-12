from fastapi import UploadFile, File
import shutil
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router

app = FastAPI(
    title="SAP AI Support Assistant"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router)


@app.get("/")
def home():

    return {
        "message": "SAP AI Support Assistant Running"
    }

@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    upload_dir = "uploads"

    os.makedirs(upload_dir, exist_ok=True)

    file_path = os.path.join(
        upload_dir,
        file.filename
    )

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(
            file.file,
            buffer
        )

    return {
        "message": f"{file.filename} uploaded successfully"
    }