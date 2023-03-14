from typing import List
from uuid import UUID

from pydantic import BaseModel


class MessageOut(BaseModel):
    message: str


class ClaimIn(BaseModel):
    email: str | None
    phone: str | None
    message: str | None
    type: str | None
    is_adaptive: bool | None
    state: str | None
    start_date: str | None

