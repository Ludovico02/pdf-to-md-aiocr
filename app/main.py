import pathlib

from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import FileResponse
from pdf_service import PdfService

app = FastAPI()

STORAGE_DIR = pathlib.Path("../storage")
MARKDOWN_DIR = pathlib.Path("../storage/markdown")
PDF_DIR = pathlib.Path("../storage/pdf")

pdf_service = PdfService(STORAGE_DIR, PDF_DIR, MARKDOWN_DIR)


@app.post("/uploadedFiles/")
async def pdf_upload(file: UploadFile):
    try:
        return await pdf_service.pdf_uploader(file)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))


@app.post("/pdfToMarkdown/")
async def pdf_to_markdown(file: UploadFile, download: bool = False):
    try:
        response = await pdf_service.pdf_to_md(file)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"OCR conversion failed: {e}")
    
    if not download:
        return response
    
    return FileResponse(
        path=response["md_path"],
        media_type="text/markdown",
        filename=f"{response["id"]}.md",
    )
