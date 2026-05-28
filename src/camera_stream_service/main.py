import os

from fastapi import FastAPI
from pydantic import BaseModel


SERVICE_NAME = os.getenv("SERVICE_NAME", "camera-stream")
SERVICE_VERSION = os.getenv("SERVICE_VERSION", "0.1.0")


app = FastAPI(
    title="FIT4110 Lab 04 - Camera Stream Service",
    version=SERVICE_VERSION,
    description="Dockerized camera service used for Lab 04 packaging and health checks.",
)


class HealthResponse(BaseModel):
    status: str
    service: str
    version: str


@app.get("/health", response_model=HealthResponse)
def health() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service=SERVICE_NAME,
        version=SERVICE_VERSION,
    )


@app.get("/")
def root() -> dict[str, str]:
    return {"service": SERVICE_NAME, "status": "running"}