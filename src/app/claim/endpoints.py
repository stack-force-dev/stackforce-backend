from fastapi import APIRouter, Depends

from src.app.claim.schemas import MessageOut, ClaimIn
from src.app.claim.services import ClaimService

import logging
logger = logging.getLogger(__name__)

router = APIRouter()


@router.post(
    "",
    name="Leave claim",
    response_model=MessageOut,
    status_code=200)
async def leave_claim(
    payload: ClaimIn, claim_service: ClaimService = Depends()):
    return await claim_service.save_claim(payload)
