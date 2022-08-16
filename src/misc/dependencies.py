import logging
from contextlib import contextmanager

import aioredis
from sqlalchemy.orm import Session

from src.settings import settings
from src.misc.database import SessionLocal

logger = logging.getLogger(__name__)


def db() -> Session:
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()


@contextmanager
def db_context(expire_on_commit: bool = True) -> Session:
    session = SessionLocal(expire_on_commit=expire_on_commit)
    try:
        yield session
    finally:
        session.close()


redis_pool = aioredis.ConnectionPool.from_url(
    settings.REDIS_URL, decode_responses=True)


def redis() -> aioredis.Redis:
    return aioredis.Redis(connection_pool=redis_pool)


