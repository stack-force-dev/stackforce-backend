from fastapi import APIRouter

from src.app.claim.endpoints import router as claim_router

api_router = APIRouter()

api_router.include_router(claim_router, prefix='/claim', tags=['Claim'])
