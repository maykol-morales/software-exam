from typing import Optional

from fastapi import FastAPI, Query

from contextlib import asynccontextmanager

from app.utils import parser, middleware
from app.routes import example
from app.clients import mongo


@asynccontextmanager
async def lifespan(_: FastAPI):
    mongo.connect()

    yield
    mongo.disconnect()


app = FastAPI(
    title="Example",
    lifespan=lifespan
)

app.add_middleware(middleware.Metrics)
app.add_middleware(middleware.Tracking)


@app.get("/", description="Example Description")
def read_root():
    return "Hello World"


@app.get("/metrics")
async def get_metrics():
    availability = middleware.Metrics.calculate_availability()
    reliability = middleware.Metrics.calculate_reliability()

    return {
        "total": middleware.Metrics.total,
        "availability": f"{availability}%",
        "reliability": f"{reliability}%",
        "counts": middleware.Metrics.counts
    }


@app.get("/monitor")
async def monitor(
    method: Optional[str] = Query(None, example="GET"),
    status_code: Optional[int] = Query(None, example=200),
    limit: int = Query(10, example=10),
):
    query = {}

    if method:
        query["method"] = method
    if status_code:
        query["status_code"] = status_code

    cursor = mongo.get_tracks(query, limit)
    report = parser.parse_iterator(cursor)

    return report


app.include_router(example.router, prefix="/example")
