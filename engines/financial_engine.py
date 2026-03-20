from core.schema import build_response


def run_financial_engine(inputs: dict):
    """
    تقييم الأداء المالي الأساسي:
    - الربحية (Profitability)
    - هامش الربح (Profit Margin)
    - الكفاءة (Cost Efficiency)
    """

    revenue = inputs.get("revenue", 0)
    cost = inputs.get("cost", 0)

    # ---- SAFETY CHECK ----
    if revenue <= 0:
        return build_response(
            score=0,
            label="Invalid",
            insight="Revenue must be greater than 0.",
            metrics={"revenue": revenue, "cost": cost}
        )

    # ---- CORE METRICS ----
    profit = revenue - cost
    margin = (profit / revenue) * 100
    cost_ratio = (cost / revenue) * 100

    # ---- SCORING LOGIC (REALISTIC) ----
    score = 0

    # Profitability Score (50%)
    if margin >= 30:
        score += 50
    elif margin >= 20:
        score += 40
    elif margin >= 10:
        score += 30
    elif margin > 0:
        score += 20
    else:
        score += 0

    # Cost Efficiency Score (50%)
    if cost_ratio <= 50:
        score += 50
    elif cost_ratio <= 70:
        score += 40
    elif cost_ratio <= 85:
        score += 25
    else:
        score += 10

    # Clamp score
    score = max(0, min(100, score))

    # ---- LABEL ----
    if score >= 75:
        label = "Strong"
    elif score >= 50:
        label = "Moderate"
    else:
        label = "Weak"

    # ---- INSIGHT ----
    insight = (
        f"Profit margin is {round(margin, 2)}%. "
        f"Cost ratio is {round(cost_ratio, 2)}%. "
    )

    # ---- METRICS ----
    metrics = {
        "revenue": revenue,
        "cost": cost,
        "profit": profit,
        "margin_percent": round(margin, 2),
        "cost_ratio_percent": round(cost_ratio, 2)
    }

    return build_response(score, label, insight, metrics)
