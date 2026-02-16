from fastapi import APIRouter
from backend.ingest.parser import parse_auth_log
from backend.storage.opensearch import store_event
from backend.correlate.auth_rules import correlate_auth_event

router = APIRouter()

@router.post("/ingest/auth")
def ingest_auth_log(log: dict):
    event = parse_auth_log(log)
    event_id = store_event(event)

    signals = correlate_auth_event(event.model_dump())

    return {
        "status": "ingested",
        "event_id": event_id,
        "signals": signals
    }