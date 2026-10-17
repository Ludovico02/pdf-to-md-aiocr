import pathlib

from fastapi import FastAPI, UploadFile

from pdf_service import PdfService

app = FastAPI()

STORAGE_DIR = pathlib.Path("../storage")
MARKDOWN_DIR = pathlib.Path("../storage/markdown")
PDF_DIR = pathlib.Path("../storage/pdf")

pdf_service = PdfService(STORAGE_DIR, PDF_DIR, MARKDOWN_DIR)

@app.post("/uploadedFiles/")
async def pdf_upload(file: UploadFile):
    return await pdf_service.pdf_uploader(file)

@app.post("/pdfToMarkdown/")
async def pdf_to_markdown(file: UploadFile):
    return await pdf_service.pdf_to_md(file)