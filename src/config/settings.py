import os
from typing import Optional, List

from pydantic import BaseSettings, PostgresDsn, RedisDsn


class Settings(BaseSettings):
    API_PREFIX: str = "/v1"
    SECRET_KEY: str
    LOGGING_LEVEL: str = 'INFO'

    SERVER_PORT: int = 8000
    SERVER_WORKER_NUMBER: int = 4

    DATABASE_URL: Optional[PostgresDsn] = None
    REDIS_URL: Optional[RedisDsn] = None

    ENABLE_SQL_ECHO: Optional[bool] = True
    ENABLE_WEB_SERVER_AUTORELOAD: Optional[bool] = True

    ADMIN_USERNAME: str
    ADMIN_PASSWORD: str

    ADMIN_PAGE_SIZE: int

    STATIC_PATH: str = 'static'
    DEFAULT_ATTACHMENT_NAME: str = 'file'

    class Config:
        env_file_encoding = 'utf-8'



settings = Settings()