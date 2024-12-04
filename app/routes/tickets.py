from fastapi import APIRouter, HTTPException

from app.models.ticket import *
from app.clients.mongo import *

router = APIRouter()


@router.post("/purchase")
def purchase_ticket(purchase: TicketPurchase):
    event = find_event(purchase.event_id)

    if not event:
        return HTTPException(status_code=404, detail="Event not found.")

    ticket = find_available_ticket(purchase.event_id)

    if not ticket:
        return HTTPException(status_code=404, detail="No tickets available for this event.")

    if ticket["price"] > purchase.user_wallet:
        return HTTPException(status_code=400, detail="Insufficient funds.")

    ticket["user_id"] = purchase.user_id
    ticket["state"] = "sold"

    save_ticket(ticket)

    return {
        "detail": "Ticket purchased successfully.",
        "user_wallet": purchase.user_wallet - ticket["price"]
    }


@router.post("/reserve")
def reserve_ticket(reserver: TicketReserve):
    event = find_event(reserver.event_id)

    if not event:
        return HTTPException(status_code=404, detail="Event not found.")

    ticket = find_available_ticket(reserver.event_id)

    if not ticket:
        return HTTPException(status_code=404, detail="No tickets available for this event.")

    ticket["user_id"] = reserver.user_id
    ticket["state"] = "reserved"

    save_ticket(ticket)

    return {
        "detail": "Ticket reserved successfully."
    }


@router.post("/cancel")
def cancel_ticket(cancel: TicketCancel):
    ticket = find_ticket(cancel.ticket_id)

    if not ticket:
        return HTTPException(status_code=404, detail="Ticket not found.")

    if ticket["user_id"] != cancel.user_id:
        return HTTPException(status_code=400, detail="Ticket does not belong to this user.")

    if ticket["state"] != "reserved":
        return HTTPException(status_code=400, detail="Ticket is not reserved.")

    ticket["user_id"] = None
    ticket["state"] = "available"

    save_ticket(ticket)

    return {
        "detail": "Ticket canceled successfully."
    }


@router.post("/use")
def use_ticket(use: TicketUse):
    ticket = find_ticket(use.ticket_id)

    if not ticket:
        return HTTPException(status_code=404, detail="Ticket not found.")

    if ticket["state"] != "sold":
        return HTTPException(status_code=400, detail="Ticket is not sold.")

    ticket["state"] = "used"

    save_ticket(ticket)

    return {
        "detail": "Ticket used successfully."
    }
