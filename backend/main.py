from fastapi import FastAPI
from backend.ingest.ingest_api import router as ingest_router

app = FastAPI(title="SignalWeave SOC Engine", version="0.1.0")

app.include_router(ingest_router)