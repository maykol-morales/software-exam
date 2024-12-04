from fastapi.testclient import TestClient
from app.main import app

client=TestClient(app)



def test_purchase_ticket():
    # ARRANGE
    data = {
            "event_id": "string",
            "user_id": "string",
            "user_wallet": 0

    }

    # ACT
    response = client.post("/tickets/purchase", data=data)

    # ASSERT
    assert response.status_code == 200, "Error purchase"

def test_reservation_ticket():
    # ARRANGE
    data = {
  "event_id": "string",
  "user_id": "string"
    }

    # ACT
    response = client.post("/tickets/reserve", data=data)

    # ASSERT
    assert response.status_code == 200, "Error reserve"

def test_cancel_ticket():
    # ARRANGE
    data = {
  "ticket_id": "string",
  "user_id": "string"
}

    # ACT
    response = client.post("/tickets/cancel", data=data)

    # ASSERT
    assert response.status_code == 200, "Error cancel"


