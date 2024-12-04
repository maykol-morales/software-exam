from app.clients.mongo import find_event, find_available_ticket, save_ticket
from fastapi.testclient import TestClient
from app.main import app
from uuid import uuid4


client = TestClient(app)

def test_save_ticket():
    #ARRANGE
    ticket_ID=str(uuid4())

    #ACT
    response = save_ticket(ticket_ID)


    #ASSERT
    assert response == True, "Ticket not save"






