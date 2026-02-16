from datetime import datetime, timedelta

FAILED_LOGIN_THRESHOLD = 5
WINDOW_MINUTES = 10

# In-memory tracker (OK for demo)
failed_logins = {}

def detect_bruteforce(event):
    if event["event_type"] != "failed_login":
        return None

    ip = event.get("ip")
    now = datetime.utcnow()

    failed_logins.setdefault(ip, [])
    failed_logins[ip].append(now)

    # Keep only recent attempts
    window = now - timedelta(minutes=WINDOW_MINUTES)
    failed_logins[ip] = [
        t for t in failed_logins[ip] if t > window
    ]

    if len(failed_logins[ip]) >= FAILED_LOGIN_THRESHOLD:
        return {
            "type": "brute_force",
            "ip": ip,
            "count": len(failed_logins[ip]),
            "severity": "high"
        }

    return None