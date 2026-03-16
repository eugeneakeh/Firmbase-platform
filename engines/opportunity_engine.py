def run_opportunity_engine(value, risk):

    score = value * (1 - risk)

    if score >= 7:
        decision = "PURSUE"
    elif score >= 4:
        decision = "MONITOR"
    else:
        decision = "DEFER"

    return {
        "opportunity_score": score,
        "decision": decision
    }
