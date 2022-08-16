import logging

from fastapi import FastAPI

from src.settings import settings
from src.tic_tac_toe.endpoints import router

logger = logging.getLogger(__name__)


def init_app() -> FastAPI:
    app = FastAPI(docs_url=f'/docs', redoc_url=f'/redoc')
    app.include_router(router)
    return app

