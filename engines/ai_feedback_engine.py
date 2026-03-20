def run_ai_feedback_engine(central_result: dict):
    """
    AI explanation layer:
    Turns analytics into human understanding.
    """

    score = central_result["overall_score"]
    breakdown = central_result["breakdown"]

    insights = []

    # Financial insight
    fin = breakdown["financial"]
    insights.append(f"Financial: {fin['insight']}")

    # Risk insight
    risk = breakdown["risk"]
    insights.append(f"Risk: {risk['insight']}")

    # Opportunity insight
    opp = breakdown["opportunity"]
    insights.append(f"Opportunity: {opp['insight']}")

    # Capital insight
    cap = breakdown["capital"]
    insights.append(f"Capital: {cap['insight']}")

    # Final interpretation
    if score >= 75:
        conclusion = "Overall, this is a strong business with scalable potential."
    elif score >= 50:
        conclusion = "Business is stable but requires optimization."
    else:
        conclusion = "Business is under pressure and needs restructuring."

    return {
        "insights": insights,
        "conclusion": conclusion
    }
