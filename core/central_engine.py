from engines.financial_engine import run_financial_engine
from engines.risk_engine import run_risk_engine
from engines.opportunity_engine import run_opportunity_engine
from engines.capital_engine import run_capital_engine


def run_central_engine(inputs: dict):
    """
    Central intelligence layer of Firmbase.
    Combines all engine outputs into a unified business score.
    """

    # ---- RUN ALL ENGINES ----
    financial = run_financial_engine(inputs)
    risk = run_risk_engine(inputs)
    opportunity = run_opportunity_engine(inputs)
    capital = run_capital_engine(inputs)

    # ---- EXTRACT SCORES ----
    financial_score = financial["score"]
    risk_score = risk["score"]
    opportunity_score = opportunity["score"]
    capital_score = capital["score"]

    # ---- INTELLIGENCE WEIGHTING MODEL ----
    # You can tune these later based on strategy
    overall_score = (
        0.30 * financial_score +
        0.25 * risk_score +
        0.25 * opportunity_score +
        0.20 * capital_score
    )

    # ---- FINAL CLAMP ----
    overall_score = max(0, min(100, overall_score))

    # ---- SYSTEM STATUS ----
    if overall_score >= 75:
        status = "Strong Business"
    elif overall_score >= 50:
        status = "Stable Business"
    else:
        status = "At Risk"

    # ---- INSIGHT SUMMARY ----
    summary = generate_summary(financial, risk, opportunity, capital)

    return {
        "overall_score": round(overall_score, 2),
        "status": status,
        "summary": summary,
        "breakdown": {
            "financial": financial,
            "risk": risk,
            "opportunity": opportunity,
            "capital": capital
        }
    }


def generate_summary(financial, risk, opportunity, capital):
    """
    Human-readable explanation layer
    """

    return (
        f"Financial performance is rated {financial['label']}. "
        f"Risk level is {risk['label']}. "
        f"Growth potential is {opportunity['label']}. "
        f"Capital efficiency is {capital['label']}."
    )
