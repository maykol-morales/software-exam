from enum import Enum
from typing import Optional
from pydantic import BaseModel


class TicketState(Enum):
    AVAILABLE = 'available'
    RESERVED = 'reserved'
    SOLD = 'sold'
    USED = 'used'


class Ticket(BaseModel):
    ticket_id: str
    event_id: str
    name: str
    expires_at: str

    user_id: Optional[str] = None
    price: float
    state: str = TicketState.AVAILABLE.value


class TicketLogic(BaseModel):
    event_id: str
    user_id: str
    user_wallet: int
