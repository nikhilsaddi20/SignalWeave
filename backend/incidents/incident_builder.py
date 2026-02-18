import uuid

def build_incident(signals: list, risk: dict):
    if not signals or risk["risk_score"] < 70:
        return None

    return {
        "incident_id": f"INC-{uuid.uuid4()}",
        "severity": risk["risk_level"],
        "signals": [s["type"] for s in signals],
        "status": "OPEN"
    }