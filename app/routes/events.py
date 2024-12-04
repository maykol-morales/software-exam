from uuid import uuid4
from fastapi import APIRouter, HTTPException

from app.models.event import Event
from app.clients.mongo import new_event, new_ticket
from app.models.ticket import Ticket

router = APIRouter()


@router.post("/new")
def new_event(event: Event):
    if event.ticket_price <= 0:
        return HTTPException(status_code=400, detail="Event ticket price must be greater than 0")

    if event.ticket_amount <= 0:
        return HTTPException(status_code=400, detail="Event ticket amount must be greater than 0")

    new_event(event)

    for i in range(event.ticket_amount):
        new_ticket(
            Ticket(
                ticket_id=str(uuid4()),
                event_id=event.event_id,
                name=event.name,
                expires_at=event.expires_at,

                price=event.ticket_price,
                state="available"
            )
        )

    return {"detail": "Event created successfully"}
