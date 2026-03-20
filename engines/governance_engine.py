from core.schema import build_response


def run_governance_engine(inputs: dict):
    """
    Governance quality:
    - Debt discipline
    - Capital structure health
    """

    debt = inputs.get("debt", 0)
    capital = inputs.get("capital", 1)

    debt_ratio = (debt / capital) * 100 if capital else 100

    # ---- SCORE ----
    if debt_ratio <= 20:
        score = 90
    elif debt_ratio <= 40:
        score = 70
    elif debt_ratio <= 70:
        score = 50
    else:
        score = 20

    label = (
        "Strong Governance" if score >= 70 else
        "Moderate Governance" if score >= 40 else
        "Weak Governance"
    )

    insight = f"Debt-to-capital ratio is {round(debt_ratio, 2)}%"

    metrics = {
        "debt": debt,
        "capital": capital,
        "debt_ratio": debt_ratio
    }

    return build_response(score, label, insight, metrics)
