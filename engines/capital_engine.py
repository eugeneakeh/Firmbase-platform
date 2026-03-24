def run_capital_engine(inputs, financials, risk):
    burn = max(0, inputs["cost"] - inputs["revenue"])

    runway = (inputs["revenue"] / burn) if burn > 0 else float("inf")

    score = 80 if runway > 12 else 50 if runway > 6 else 30

    return {
        "burn_rate": burn,
        "runway": runway,
        "score": score
    }
