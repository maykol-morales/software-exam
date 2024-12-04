#TEST DE INTEGRACION A LA BASE DE DATOS

#crear conexion a la base de datos


#3 TEST de integracion.
#crear funcion que agrega un elemento a la base de datos

#crear una funcion que busque en la base de datos.

#crear funcion que borre de la base de datos



import string
import random
from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)

USERNAME_RANDOM = ''.join(
    random.choices(
        string.ascii_letters +
        string.digits,
        k=5))
PASSWORD_RANDOM = ''.join(
    random.choices(
        string.ascii_letters +
        string.digits,
        k=5))
EMAIL_RANDOM = ''.join(
    random.choices(
        string.ascii_letters +
        string.digits,
        k=5))
EMAIL_RANDOM = EMAIL_RANDOM + "@gmail.com"


def test_create_user():
    """
    crear usuarios
    """
    # ARRANGE
    json_body = {
        "username": USERNAME_RANDOM,
        "password": PASSWORD_RANDOM,
        "email": EMAIL_RANDOM
    }

    # ACT
    response = client.post("/users", json=json_body)

    # ASSERT
    assert response.status_code in (
        201, 200), "create user not return 200 status code"


def test_login_user():
    """
    testeo de login
    """
    # ARRANGE - login-user-no-admin
    data = {"username": USERNAME_RANDOM, "password": PASSWORD_RANDOM}

    # ACT
    response = client.post("/auth/token", data=data)

    # ASSERT
    assert response.status_code == 200, "Token not received, login unsuccessful"
    assert response.json()["token_type"] == "bearer", "Token not received"


def purchase_ticket():

def reservation_ticket():

def cancel_ticket():


