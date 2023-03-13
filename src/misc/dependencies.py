import logging
from contextlib import contextmanager

from sqlalchemy.orm import Session

from src.config.settings import settings
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
