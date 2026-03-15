def run_risk_engine(severity, probability):

    risk_score = severity * probability

    if risk_score >= 4:
        level = "HIGH RISK"
    elif risk_score >= 2:
        level = "MODERATE RISK"
    else:
        level = "LOW RISK"

    return {
        "risk_score": risk_score,
        "risk_level": level
    }
