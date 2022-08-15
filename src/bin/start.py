import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '../..'))

import logging
from src.logger import configure_logging

configure_logging()

import uvicorn

from src.app import init_app
from src.settings import settings

logger = logging.getLogger(__name__)

app = init_app()

if __name__ == '__main__':
    uvicorn.run('src.bin.start:app', host='0.0.0.0',
                port=settings.SERVER_PORT,
                workers=settings.SERVER_WORKER_NUMBER,
                reload=settings.ENABLE_WEB_SERVER_AUTORELOAD)
