import os
import socket
from pathlib import Path

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
