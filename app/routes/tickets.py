from fastapi import APIRouter, HTTPException

from app.models.ticket import TicketLogic
from app.clients.mongo import find_event, find_available_ticket, save_ticket

router = APIRouter()


@router.post("/purchase")
def purchase_ticket(logic: TicketLogic):
    event = find_event(logic.event_id)

    if not event:
        return HTTPException(status_code=404, detail="Event not found.")

    ticket = find_available_ticket(logic.event_id)

    if not ticket:
        return HTTPException(status_code=404, detail="No tickets available for this event.")

    if ticket.price > logic.user_wallet:
        return HTTPException(status_code=400, detail="Insufficient funds.")

    ticket.user_id = logic.user_id
    ticket.state = "sold"

    save_ticket(ticket)

    return {
        "detail": "Ticket purchased successfully."
    }


@router.post("/reserve")
def reserve_ticket():
    response = {
        "message": "Ticket reserved successfully."
    }

    return response


@router.post("/cancel")
def cancel_ticket():
    response = {
        "message": "Ticket canceled successfully."
    }

    return response
