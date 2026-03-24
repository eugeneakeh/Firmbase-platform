def run_risk_engine(inputs, financials):
    margin = financials["margin"]

    risk_score = 100 - (margin * 100)

    return {
        "risk_score": risk_score,
        "level": "High" if risk_score > 70 else "Medium" if risk_score > 40 else "Low",
        "score": 100 - risk_score
    }
