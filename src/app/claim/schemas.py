from typing import List
from pydantic import BaseModel


class MessageOut(BaseModel):
    message: str


class ClaimIn(BaseModel):
    name: str | None
    email: str | None
    phone: str | None
    message: str | None
    type: str | None
    is_adaptive: str | None
    state: str | None
    start_date: str | None
    files: List[str] | None
