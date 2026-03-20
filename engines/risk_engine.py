from core.schema import build_response


def run_risk_engine(inputs: dict):
    """
    تقييم المخاطر المالية:
    - نسبة الدين إلى الإيرادات (Debt Ratio)
    - الضغط المالي (Financial Pressure)
    """

    revenue = inputs.get("revenue", 0)
    debt = inputs.get("debt", 0)

    # ---- SAFETY CHECK ----
    if revenue <= 0:
        return build_response(
            score=0,
            label="High Risk",
            insight="Revenue must be greater than 0 to assess risk.",
            metrics={"revenue": revenue, "debt": debt}
        )

    # ---- CORE METRICS ----
    debt_ratio = (debt / revenue) * 100

    # ---- SCORING LOGIC ----
    # Lower debt ratio = lower risk = higher score
    if debt_ratio <= 20:
        score = 90
    elif debt_ratio <= 40:
        score = 75
    elif debt_ratio <= 60:
        score = 55
    elif debt_ratio <= 80:
        score = 35
    else:
        score = 15

    # Clamp score
    score = max(0, min(100, score))

    # ---- LABEL ----
    if score >= 75:
        label = "Low Risk"
    elif score >= 50:
        label = "Moderate Risk"
    else:
        label = "High Risk"

    # ---- INSIGHT ----
    insight = f"Debt-to-revenue ratio is {round(debt_ratio, 2)}%."

    # ---- METRICS ----
    metrics = {
        "revenue": revenue,
        "debt": debt,
        "debt_ratio_percent": round(debt_ratio, 2)
    }

    return build_response(score, label, insight, metrics)
