import pathlib
import uuid

from glmocr import GlmOcr

import aiofiles
from fastapi import HTTPException, UploadFile
from ollama import ChatResponse, Client


class PdfService:
    def __init__(self, storage_dir: pathlib.Path, pdf_dir: pathlib.Path, markdown_dir: pathlib.Path):
        self.storage_dir = storage_dir
        self.storage_dir.mkdir(exist_ok = True)
        
        self.pdf_dir = pdf_dir
        self.pdf_dir.mkdir(exist_ok=True)
        self.markdown_dir = markdown_dir
        self.markdown_dir.mkdir(exist_ok=True)
        
        self.parser = GlmOcr(config_path="config.yaml")
    
    async def pdf_uploader(self, file: UploadFile):
        if file.content_type != "application/pdf":
            # raise HTTPException(status_code = 422, detail = "Wrong filetype.")
            raise TypeError("The file is not a .pdf file")

        file_id = str(uuid.uuid4())
        async with aiofiles.open(self.pdf_dir / f"{file_id}.pdf", "wb") as f:
            bytes_written = 0
            while chunk := await file.read(1024 * 1024): # 1MB
                bytes_written += len(chunk)
                await f.write(chunk)
        
        return {"id": file_id, "filename": file.filename, "content_type": file.content_type, "bytes": file.size, "bytes_written": bytes_written}
                
    async def pdf_to_md(self, file: UploadFile):
        uploadfile = await self.pdf_uploader(file)
        file_id = uploadfile["id"]
    
        result = self.parser.parse(f"{self.pdf_dir}/{file_id}.pdf") 
        markdown_text = result.markdown_result
        
        with open(self.markdown_dir / f"{file_id}.md", "w", encoding="UTF-8") as f:
            f.write(markdown_text)
        
        # result.save(output_dir = self.markdown_dir)
        return "Task completed"