def calculate_risk(alerts):
    score = 0
    for alert in alerts:
        if alert["severity"] == "high":
            score += 70
        elif alert["severity"] == "medium":
            score += 40
    return min(score, 100)