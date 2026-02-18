from fastapi import APIRouter
from backend.ingest.parser import parse_auth_log
from backend.storage.opensearch import store_event
from backend.correlate.auth_rules import correlate_auth_event
from backend.risk.risk_engine import calculate_risk
from backend.incidents.incident_builder import build_incident
from backend.ingest.schema import AuthEvent

router = APIRouter()

@router.post("/ingest/auth")
def ingest_auth_log(log: AuthEvent):
    event = parse_auth_log(log.model_dump())
    event_id = store_event(log)

    signals = correlate_auth_event(log.model_dump())
    risk = calculate_risk(signals)
    incident = build_incident(signals, risk)

    return {
        "status": "ingested",
        "event_id": event_id,
        "signals": signals,
        "risk": risk,
        "incident": incident
    }