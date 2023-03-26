import logging
import uuid
from datetime import datetime

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import Column, DateTime, String, Text, Boolean

from src.misc.database import ModelBase

logger = logging.getLogger(__name__)


class Claim(ModelBase):
    __tablename__ = "claims"
    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    email = Column(String(255), nullable=True)
    phone = Column(String(255), nullable=True)
    message = Column(Text, nullable=True)
    type = Column(Text, nullable=True)
    is_adaptive = Column(Text, nullable=True)
    state = Column(Text, nullable=True)
    start_date = Column(Text, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __str__(self):
        return f"Claim #{self.id}"
