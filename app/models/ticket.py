from typing import Optional
from pydantic import BaseModel


class Ticket(BaseModel):
    ticket_id: str
    event_id: str
    name: str
    expires_at: str

    user_id: Optional[str] = None
    price: float
    state: str = "available"


class TicketPurchase(BaseModel):
    event_id: str
    user_id: str
    user_wallet: int


class TicketReserve(BaseModel):
    event_id: str
    user_id: str


class TicketCancel(BaseModel):
    ticket_id: str
    user_id: str


class TicketUse(BaseModel):
    ticket_id: str
