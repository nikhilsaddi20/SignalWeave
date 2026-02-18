from datetime import datetime, timedelta

FAILED_LOGIN_THRESHOLD = 5
WINDOW_MINUTES = 10

failed_attempts = {}

def correlate_auth_event(event: dict):
    if event["event_type"] != "failed_login":
        return []

    ip = event.get("ip")
    now = datetime.utcnow()

    failed_attempts.setdefault(ip, [])
    failed_attempts[ip].append(now)

    window = now - timedelta(minutes=WINDOW_MINUTES)
    failed_attempts[ip] = [t for t in failed_attempts[ip] if t > window]

    if len(failed_attempts[ip]) >= FAILED_LOGIN_THRESHOLD:
        return [{
            "type": "brute_force",
            "confidence": "high",
            "entity": f"ip:{ip}",
            "window": "10m",
            "count": len(failed_attempts[ip])
        }]

    return []