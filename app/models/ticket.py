from typing import Optional

from pydantic import BaseModel
from enum import Enum

class TicketState(Enum):
    AVAILABLE = 'available'
    SOLD = 'sold'
    RESERVED = 'reserved'
    CANCELED = 'canceled'
    USED = 'used'

class Ticket(BaseModel):
    id: str
    user_id: Optional[str] = None
    price: float
    expires_at: int
    state: TicketState
