import os
import base64
import logging
from mimetypes import guess_extension

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.misc import dependencies

from src.config.settings import settings
from src.app.claim.models import Claim
from src.app.claim.schemas import ClaimIn

logger = logging.getLogger(__name__)


def write_b64_file(b64_string: str, folder_name: str):
    file_info, b64_string = b64_string.split(',')
    content_part = file_info.split(';')[0]
    content_type = content_part.split(':')[-1]

    logger.info(f"Content-Type => {content_type}, B64 => {b64_string[:20]}...")

    file_name = settings.DEFAULT_ATTACHMENT_NAME
    extension = guess_extension(content_type)

    if extension:
        file_name += extension

    b64_bytes = b64_string.encode('utf-8')
    new_file_path = os.path.join(settings.STATIC_PATH, 'claim', folder_name, file_name)
    
    with open(new_file_path, "wb") as file:
        decoded_data = base64.decodebytes(b64_bytes)
        file.write(decoded_data)

    logger.info(f"File uploaded => {new_file_path}")


class ClaimService:
    def __init__(self,
                 db: Session = Depends(dependencies.db)):
        self.db = db

    async def save_claim(self, payload: ClaimIn):
        main_payload = payload.dict(exclude_unset=True)

        file = None
        if 'file' in main_payload:
            file = main_payload.pop('file')

        claim = Claim(**main_payload)
        self.db.add(claim)
        self.db.commit()
        self.db.refresh(claim)

        if file:
            try:
                write_b64_file(file, f"{claim.id}")
            except Exception as e:
                raise HTTPException(detail=f'File upload error => {e}', status_code=500)
       
        return {"message": "Claim successfully saved!"}
