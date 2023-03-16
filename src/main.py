import os
import sys
sys.path.insert(1, os.path.join(sys.path[0], '..'))

import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from sqladmin import Admin
from src.admin import get_auth_backend, init_models
from src.misc.database import engine

from src.app import routers
from src.config.settings import settings

from src.config.logger import configure_logging
import logging
configure_logging()

logger = logging.getLogger(__name__)

app = FastAPI(
    title="StackForceSiteAPI",
    version="0.0.1",
    docs_url=f'/docs',
    redoc_url=f'/redoc')

app.mount("/static", StaticFiles(directory=settings.STATIC_PATH), name="static")
app.include_router(routers.api_router, prefix=settings.API_PREFIX)

admin = Admin(app, engine, title='StackForceAdmin', authentication_backend=get_auth_backend())
init_models(admin)

if __name__ == '__main__':
    uvicorn.run("src.main:app", host='0.0.0.0',
                port=settings.SERVER_PORT,
                workers=settings.SERVER_WORKER_NUMBER,
                proxy_headers=True,
                forwarded_allow_ips='*',
                reload=settings.ENABLE_WEB_SERVER_AUTORELOAD)
