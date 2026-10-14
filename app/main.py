import pathlib
import uuid

import aiofiles
from fastapi import FastAPI, HTTPException, UploadFile

app = FastAPI()

STORAGE_DIR = pathlib.Path("storage")
STORAGE_DIR.mkdir(exist_ok=True)

@app.post("/uploadfiles/")
async def pdf_rewrite_and_data(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code = 422, detail = "Wrong filetype.")

    file_id = str(uuid.uuid4())
    async with aiofiles.open(f"{STORAGE_DIR}/{file_id}.pdf", "wb") as f:
        bytes_written = 0
        while chunk := await file.read(1024 * 1024): # 1MB
            bytes_written += len(chunk)
            await f.write(chunk)
    
    return {"filename": file.filename, "bytes": file.size, "bytes_written": bytes_written}
