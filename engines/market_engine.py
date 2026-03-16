def run_market_engine(size, regulation):

    priority_score = size * (1 - regulation)

    if priority_score >= 700000:
        decision = "ENTER MARKET"
    elif priority_score >= 300000:
        decision = "MONITOR MARKET"
    else:
        decision = "AVOID MARKET"

    return {
        "priority_score": priority_score,
        "decision": decision
    }
