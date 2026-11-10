import os
import socket

from fastapi import FastAPI

APP_VERSION = os.getenv("APP_VERSION", "0.1.0")

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
    return {
        "status": "ready"
    }
