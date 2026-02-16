from datetime import datetime, timedelta
from typing import Dict, List

FAILED_LOGIN_THRESHOLD = 5
WINDOW_MINUTES = 10

failed_logins: Dict[str, List[datetime]] = {}


def correlate_auth_event(event: dict):
    if event.get("event_type") != "failed_login":
        return []

    ip = event.get("ip")
    if not ip:
        return []

    now = datetime.utcnow()

    failed_logins.setdefault(ip, [])
    failed_logins[ip].append(now)

    window_start = now - timedelta(minutes=WINDOW_MINUTES)
    failed_logins[ip] = [
        t for t in failed_logins[ip] if t >= window_start
    ]

    if len(failed_logins[ip]) >= FAILED_LOGIN_THRESHOLD:
        return [{
            "type": "brute_force",
            "confidence": "high",
            "entity": f"ip:{ip}",
            "window": "10m",
            "count": len(failed_logins[ip])
        }]

    return []