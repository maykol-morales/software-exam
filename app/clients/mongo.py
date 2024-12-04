from os import getenv

from pymongo import MongoClient
from pymongo.errors import PyMongoError

from app.models.event import Event
from app.models.ticket import Ticket

from app.utils.logger import error, info

MONGO_URI = getenv("MONGO_URI")
MONGO_COLLECTION = getenv("MONGO_COLLECTION")


class Connection:
    client: MongoClient = None
    db: None


connection = Connection()


def connect():
    try:
        connection.client = MongoClient(MONGO_URI)
        connection.db = connection.client[MONGO_COLLECTION]
        info("Connected to MongoDB")
    except PyMongoError:
        error("Failed to connect to MongoDB")


def disconnect():
    if connection.client:
        connection.client.close()
        info("Disconnected from MongoDB")


def insert_track(route: str, method: str, status_code: int, start_date, end_date):
    try:
        connection.db["tracks"].insert_one({
            "route": route,
            "method": method,
            "status_code": status_code,
            "start_date": start_date,
            "end_date": end_date,
            "latency": end_date - start_date
        })
    except PyMongoError:
        raise


def get_tracks(query: dict, limit: int = 10):
    try:
        return connection.db["tracks"].find(query).sort("start_date", -1).limit(limit).to_list(length=limit)
    except PyMongoError:
        raise


def new_event(event: Event):
    try:
        connection.db["events"].insert_one(event.model_dump())
    except PyMongoError:
        raise


def new_ticket(ticket: Ticket):
    try:
        connection.db["tickets"].insert_one(ticket.model_dump())
    except PyMongoError:
        raise


def find_event(event_id: str):
    try:
        return connection.db["events"].find_one({"event_id": event_id})
    except PyMongoError:
        return None


def find_ticket(ticket_id: str):
    try:
        return connection.db["tickets"].find_one({"ticket_id": ticket_id})
    except PyMongoError:
        return None


def find_available_ticket(event_id: str):
    try:
        return connection.db["tickets"].find_one({"event_id": event_id, "state": "available"})
    except PyMongoError:
        return None


def save_ticket(ticket: dict):
    try:
        connection.db["tickets"].update_one({"ticket_id": ticket['ticket_id']}, {"$set": ticket})
    except PyMongoError:
        raise
