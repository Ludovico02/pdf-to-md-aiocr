import pathlib
import uuid

import aiofiles
from fastapi import FastAPI, HTTPException, UploadFile
from fastapi.responses import HTMLResponse

app = FastAPI()

STORAGE_DIR = pathlib.Path("storage")
STORAGE_DIR.mkdir(exist_ok=True)

@app.post("/uploadfiles/")
async def check_pdf(file: UploadFile):
    if file.content_type != "application/pdf":
        raise HTTPException(status_code = 422, detail = "Wrong filetype.")

    file_id = str(uuid.uuid4())
    async with aiofiles.open(f"{STORAGE_DIR}/{file_id}.pdf", "wb") as f:
        bytes_written = 0
        while chunk := await file.read(1024 * 1024): # 1MB
            bytes_written += len(chunk)
            await f.write(chunk)
    
    return {"filename": file.filename, "bytes": file.size, "bytes_written": bytes_written}

@app.get("/")
async def main():
    content = """
<body>
<form action="/uploadfiles/" enctype="multipart/form-data" method="post">
<input name="file" type="file">
<input type="submit">
</form>
</body>
"""

    return HTMLResponse(content = content)
