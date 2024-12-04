from fastapi import APIRouter

from app.models.ticket import

router = APIRouter()


@router.post("/purchase", description="Purchase a concert ticket.", status_code=200)
def purchase_ticket():



    response = {
        "message": "Ticket purchased successfully."
    }

    return response

@router.post("/reserve", description="Reserve a concert ticket.", status_code=200)
def reserve_ticket():

    response = {
        "message": "Ticket reserved successfully."
    }

    return response

@router.post("/cancel", description="Cancel a concert ticket.", status_code=200)
def cancel_ticket():

    response = {
        "message": "Ticket canceled successfully."
    }

    return response
