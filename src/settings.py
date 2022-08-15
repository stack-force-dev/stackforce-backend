import os
from typing import Optional

from pydantic import BaseSettings, PostgresDsn, RedisDsn


class Settings(BaseSettings):
    API_PREFIX: str = "/"
    SECRET_KEY: str
    JWT_SECRET: str
    LOGGING_LEVEL: str = 'INFO'

    SERVER_PORT: int = 8000
    SERVER_WORKER_NUMBER: int = 4

    DATABASE_URL: Optional[PostgresDsn] = None
    REDIS_URL: Optional[RedisDsn] = None

    ENABLE_SQL_ECHO: Optional[bool] = True
    ENABLE_WEB_SERVER_AUTORELOAD: Optional[bool] = True

    class Config:
        case_sensitive = True
        env_file = os.path.join(os.getcwd(), '..', '.env')


settings = Settings()
