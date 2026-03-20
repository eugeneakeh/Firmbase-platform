from core.schema import build_response


def run_market_engine(inputs: dict):
    """
    Market conditions evaluation:
    - Market size
    - Industry growth signal
    """

    market_size = inputs.get("market_size", 0)
    industry_growth = inputs.get("industry_growth", 0)

    # ---- SCORE LOGIC ----
    size_score = 0
    if market_size >= 1_000_000:
        size_score = 60
    elif market_size >= 100_000:
        size_score = 40
    elif market_size > 0:
        size_score = 20

    growth_score = 0
    if industry_growth >= 50:
        growth_score = 40
    elif industry_growth >= 20:
        growth_score = 30
    elif industry_growth > 0:
        growth_score = 15

    score = size_score + growth_score
    score = max(0, min(100, score))

    label = (
        "Strong Market" if score >= 70 else
        "Moderate Market" if score >= 40 else
        "Weak Market"
    )

    insight = f"Market size: {market_size}, Industry growth: {industry_growth}%"

    metrics = {
        "market_size": market_size,
        "industry_growth": industry_growth,
        "size_score": size_score,
        "growth_score": growth_score
    }

    return build_response(score, label, insight, metrics)
