from pydantic import BaseModel


class Event(BaseModel):
    name: str

    ticket_price: float
    ticket_amount: int
