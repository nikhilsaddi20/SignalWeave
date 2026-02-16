from datetime import timedelta

FAILED_THRESHOLD = 5
TIME_WINDOW_MINUTES = 5

def detect_brute_force(events):
    alerts = []
    events_by_ip = {}

    for e in events:
        if e.event_type == "failed_login":
            events_by_ip.setdefault(e.ip, []).append(e.timestamp)

    for ip, timestamps in events_by_ip.items():
        timestamps.sort()
        for i in range(len(timestamps)):
            window = timestamps[i:i + FAILED_THRESHOLD]
            if len(window) == FAILED_THRESHOLD:
                if window[-1] - window[0] <= timedelta(minutes=TIME_WINDOW_MINUTES):
                    alerts.append({
                        "type": "brute_force",
                        "ip": ip,
                        "severity": "high"
                    })
                    break

    return alerts