RISK_SCORES = {
    "brute_force": 70,
    "impossible_travel": 90
}

def calculate_risk(alerts):
    score = 0
    for alert in alerts:
        score += RISK_SCORES.get(alert["type"], 10)
    return min(score, 100)