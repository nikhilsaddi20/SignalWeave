from datetime import timedelta

MAX_TRAVEL_TIME = timedelta(minutes=30)

def detect_impossible_travel(events):
    alerts = []
    user_events = {}

    for e in events:
        if e.event_type == "login_success":
            user_events.setdefault(e.user, []).append(e)

    for user, logs in user_events.items():
        logs.sort(key=lambda x: x.timestamp)
        for i in range(len(logs) - 1):
            if logs[i+1].timestamp - logs[i].timestamp < MAX_TRAVEL_TIME:
                if logs[i].ip != logs[i+1].ip:
                    alerts.append({
                        "type": "impossible_travel",
                        "user": user,
                        "severity": "critical"
                    })

    return alerts