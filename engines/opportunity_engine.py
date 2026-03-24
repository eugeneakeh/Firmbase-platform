def run_opportunity_engine(inputs):
    growth = inputs.get("growth_rate", 0.1)

    score = min(100, growth * 100)

    return {
        "growth_rate": growth,
        "score": score,
        "insight": "High growth potential" if score > 70 else "Moderate growth"
    }
