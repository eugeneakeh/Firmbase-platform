def run_ai_feedback(financial_roi, risk_score, opportunity_score, allocation_score, market_priority):
    improvement_score = {
        "Financial": financial_roi / 0.3,
        "Risk": 1 - (risk_score/10),
        "Opportunity": opportunity_score / 7,
        "Capital": allocation_score / 0.4,
        "Market": market_priority / 600000
    }
    optimized_decision = {}
    for key, val in improvement_score.items():
        if val > 1:
            optimized_decision[key] = "Increase Focus"
        elif val > 0.8:
            optimized_decision[key] = "Maintain"
        else:
            optimized_decision[key] = "Review / Adjust"
    return {
        "improvement_score": improvement_score,
        "optimized_decision": optimized_decision
    }
