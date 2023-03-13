import logging

from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session

from src.misc import dependencies

from src.config.settings import settings
from src.app.claim.models import Claim
from src.app.claim.schemas import ClaimIn

logger = logging.getLogger(__name__)


class ClaimService:
    def __init__(self,
                 db: Session = Depends(dependencies.db)):
        self.db = db

    async def save_claim(self, payload: ClaimIn):
        try:
            claim = Claim(**payload.dict(exclude_unset=True))
            self.db.add(claim)
            self.db.commit()
        except Exception as e:
            raise HTTPException(detail=f"Error => {e}", status_code=500)
            
        return {"message": "Claim successfully saved!"}
