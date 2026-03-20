from core.schema import build_response


def run_capital_engine(inputs: dict):
    """
    تقييم كفاءة رأس المال:
    - العائد على الاستثمار (ROI)
    - كفاءة استخدام رأس المال
    """

    revenue = inputs.get("revenue", 0)
    cost = inputs.get("cost", 0)
    capital = inputs.get("capital", 0)  # total invested capital

    # ---- SAFETY CHECK ----
    if capital <= 0:
        return build_response(
            score=0,
            label="Unknown Efficiency",
            insight="Capital must be greater than 0 to evaluate efficiency.",
            metrics={
                "revenue": revenue,
                "cost": cost,
                "capital": capital
            }
        )

    # ---- CORE METRICS ----
    profit = revenue - cost
    roi = (profit / capital) * 100

    # Capital efficiency: how much revenue per capital unit
    efficiency = (revenue / capital) * 100

    # ---- SCORING LOGIC ----

    # ROI Score (60%)
    if roi >= 50:
        roi_score = 60
    elif roi >= 30:
        roi_score = 45
    elif roi >= 15:
        roi_score = 30
    elif roi > 0:
        roi_score = 15
    else:
        roi_score = 5

    # Efficiency Score (40%)
    if efficiency >= 200:
        eff_score = 40
    elif efficiency >= 150:
        eff_score = 30
    elif efficiency >= 100:
        eff_score = 20
    elif efficiency > 0:
        eff_score = 10
    else:
        eff_score = 5

    # ---- FINAL SCORE ----
    score = roi_score + eff_score
    score = max(0, min(100, score))

    # ---- LABEL ----
    if score >= 75:
        label = "Efficient Capital Use"
    elif score >= 50:
        label = "Moderate Efficiency"
    else:
        label = "Inefficient Capital Use"

    # ---- INSIGHT ----
    insight = (
        f"ROI is {round(roi, 2)}%. "
        f"Capital efficiency is {round(efficiency, 2)}%."
    )

    # ---- METRICS ----
    metrics = {
        "revenue": revenue,
        "cost": cost,
        "capital": capital,
        "profit": profit,
        "roi_percent": round(roi, 2),
        "efficiency_percent": round(efficiency, 2)
    }

    return build_response(score, label, insight, metrics)
