import os
import socket
from pathlib import Path
from time import perf_counter

from fastapi import FastAPI, HTTPException

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")
READY_FILE = Path("/tmp/ready")

app = FastAPI(
    title="OrderFlow Orders API",
    version=APP_VERSION
)


@app.get("/")
def root():
    return {
        "service": "orders-api",
        "status": "ok",
        "version": APP_VERSION,
        "hostname": socket.gethostname()
    }


@app.get("/health/live")
def liveness():
    return {
        "status": "alive"
    }


@app.get("/health/ready")
def readiness():
    if not READY_FILE.exists():
        raise HTTPException(
            status_code=503,
            detail="Application is not ready: dependency unavailable"
        )

    return {
        "status": "ready"
    }


@app.get("/work")
def cpu_work(duration: float = 0.5):
    duration = max(0.05, min(duration, 2.0))

    start = perf_counter()
    deadline = start + duration

    result = 1
    iterations = 0

    while perf_counter() < deadline:
        result = (
            result * 1103515245 + 12345
        ) % 2147483648

        iterations += 1

    return {
        "service": "orders-api",
        "status": "completed",
        "hostname": socket.gethostname(),
        "duration_seconds": round(perf_counter() - start, 3),
        "iterations": iterations
    }
