def run_market_engine(inputs):
    size = inputs.get("market_size", 100000)
    growth = inputs.get("market_growth", 0.1)

    score = min(100, (growth * 100))

    return {
        "market_size": size,
        "growth": growth,
        "score": score
    }
