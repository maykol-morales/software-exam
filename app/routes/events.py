from fastapi import APIRouter, HTTPException

from app.models.event import Event
from app.clients.mongo import new_event

router = APIRouter()


@router.post("/new")
def read_root(event: Event):
    if event.ticket_price <= 0:
        return HTTPException(status_code=400, detail="Event ticket price must be greater than 0")

    if event.ticket_amount <= 0:
        return HTTPException(status_code=400, detail="Event ticket amount must be greater than 0")

    new_event(event)

    return {"detail": "Event created successfully"}
