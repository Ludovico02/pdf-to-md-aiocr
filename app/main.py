import pathlib

from fastapi import FastAPI

from pdf_service import PdfService

app = FastAPI()

STORAGE_DIR = pathlib.Path("storage")

pdf_service = PdfService(STORAGE_DIR)

app.post("/uploadedFiles/")
pdf_service.pdf_uploader()