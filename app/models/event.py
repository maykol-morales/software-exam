from uuid import uuid4
from typing import Optional

from pydantic import BaseModel


class Event(BaseModel):
    event_id: Optional[str] = uuid4()
    name: str
    expires_at: str

    ticket_price: float
    ticket_amount: int
