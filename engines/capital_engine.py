def run_capital_engine(roi, priority, risk):

    allocation_score = roi * priority * (1 - risk)

    if allocation_score >= 0.5:
        decision = "INVEST AGGRESSIVELY"
    elif allocation_score >= 0.2:
        decision = "INVEST MODERATELY"
    else:
        decision = "HOLD / REVIEW"

    return {
        "allocation_score": allocation_score,
        "decision": decision
    }
