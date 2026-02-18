def calculate_risk(signals: list) -> dict:
    score = 0

    for signal in signals:
        if signal["confidence"] == "high":
            score += 50
        elif signal["confidence"] == "medium":
            score += 30

    score = min(score, 100)

    level = "LOW"
    if score >= 70:
        level = "HIGH"
    elif score >= 40:
        level = "MEDIUM"

    return {
        "risk_score": score,
        "risk_level": level
    }