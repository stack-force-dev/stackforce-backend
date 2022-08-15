import logging

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

from src.settings import settings

logging = logging.getLogger(__name__)

engine = create_engine(settings.DATABASE_URL,
                       echo=settings.ENABLE_SQL_ECHO,
                       echo_pool=settings.ENABLE_SQL_ECHO,
                       pool_pre_ping=True,
                       pool_timeout=1,
                       pool_size=10, max_overflow=20,
                       connect_args={"options": "-c timezone=utc"})

SessionLocal = sessionmaker(autocommit=False, autoflush=False,
                            future=True, bind=engine)

ModelBase = declarative_base()
