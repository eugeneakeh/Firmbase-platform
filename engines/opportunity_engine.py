from core.schema import build_response


def run_opportunity_engine(inputs: dict):
    """
    تقييم فرص النمو:
    - معدل النمو (Growth Rate)
    - قابلية التوسع (Scalability)
    """

    revenue = inputs.get("revenue", 0)
    growth_rate = inputs.get("growth_rate", 0)  # % expected or actual growth
    market_size = inputs.get("market_size", 0)  # optional (future use)

    # ---- SAFETY DEFAULTS ----
    if revenue <= 0:
        return build_response(
            score=0,
            label="Low Opportunity",
            insight="Revenue must be greater than 0 to assess opportunity.",
            metrics={
                "revenue": revenue,
                "growth_rate": growth_rate
            }
        )

    # ---- SCORING: GROWTH RATE (70%) ----
    growth_score = 0
    if growth_rate >= 50:
        growth_score = 70
    elif growth_rate >= 30:
        growth_score = 55
    elif growth_rate >= 15:
        growth_score = 40
    elif growth_rate > 0:
        growth_score = 25
    else:
        growth_score = 10

    # ---- SCORING: MARKET POTENTIAL (30%) ----
    # (Simple placeholder logic for now)
    if market_size >= 1_000_000:
        market_score = 30
    elif market_size >= 100_000:
        market_score = 20
    elif market_size > 0:
        market_score = 10
    else:
        market_score = 5

    # ---- FINAL SCORE ----
    score = growth_score + market_score
    score = max(0, min(100, score))

    # ---- LABEL ----
    if score >= 75:
        label = "High Growth Potential"
    elif score >= 50:
        label = "Moderate Growth"
    else:
        label = "Low Growth"

    # ---- INSIGHT ----
    insight = (
        f"Growth rate is {growth_rate}%. "
        f"Market size indicator is {market_size}."
    )

    # ---- METRICS ----
    metrics = {
        "revenue": revenue,
        "growth_rate_percent": growth_rate,
        "market_size": market_size,
        "growth_score": growth_score,
        "market_score": market_score
    }

    return build_response(score, label, insight, metrics)
