import logging
from fastapi import APIRouter

from src.settings import settings

logger = logging.getLogger(__name__)

router = APIRouter()
