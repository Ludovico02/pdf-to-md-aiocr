import pathlib
import uuid

import aiofiles
from fastapi import HTTPException, UploadFile


class PdfService:
    def __init__(self, storage_dir: pathlib.Path):
        self.storage_dir = storage_dir
        self.storage_dir.mkdir(exist_ok = True)
    
    async def pdf_uploader(self, file: UploadFile):
        if file.content_type != "application/pdf":
            # raise HTTPException(status_code = 422, detail = "Wrong filetype.")
            raise Exception("The file is not a .pdf file")

        file_id = str(uuid.uuid4())
        async with aiofiles.open(self.storage_dir /f"{file_id}.pdf", "wb") as f:
            bytes_written = 0
            while chunk := await file.read(1024 * 1024): # 1MB
                bytes_written += len(chunk)
                await f.write(chunk)
        
        return {"id": file_id, "filename": file.filename, "bytes": file.size, "bytes_written": bytes_written}
                
    def pdf_to_md(self):
        pass
