from time import time
from fastapi import Request

from starlette.middleware.base import BaseHTTPMiddleware

from app.clients.mongo import insert_track
from app.utils.logger import info, error


class Metrics(BaseHTTPMiddleware):
    total = -1
    counts = {
        "2XX": 0,
        "4XX": 0,
        "5XX": 0
    }

    async def dispatch(self, request: Request, call_next):
        Metrics.total += 1

        response = await call_next(request)
        status_code = response.status_code

        if 200 <= status_code < 300:
            Metrics.counts["2XX"] += 1
            info("success on execute: " + request.url.path)
        elif 400 <= status_code < 500:
            Metrics.counts["4XX"] += 1
            error("error on execute: " + request.url.path)
        elif 500 <= status_code < 600:
            Metrics.counts["5XX"] += 1
            error("error on execute: " + request.url.path)

        return response

    @classmethod
    def calculate_availability(cls):
        try:
            availability = Metrics.counts["2XX"] / Metrics.total
            return availability * 100
        except ZeroDivisionError:
            return 100.0

    @classmethod
    def calculate_reliability(cls):
        try:
            reliability = (Metrics.total - Metrics.counts["5XX"]) / Metrics.total
            return reliability * 100
        except ZeroDivisionError:
            return 100.0


class Tracking(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time()
        response = await call_next(request)
        end_time = time()

        insert_track(request.url.path, request.method, response.status_code, start_time, end_time)
        return response
