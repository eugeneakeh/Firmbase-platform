def run_financial_engine(inputs):
    revenue = inputs["revenue"]
    cost = inputs["cost"]

    profit = revenue - cost
    margin = profit / revenue if revenue else 0

    score = max(0, min(100, margin * 100))

    return {
        "profit": profit,
        "margin": margin,
        "score": score
    }
