# core_engine.py

import math

# -------------------------
# HELPER
# -------------------------
def clamp(value, min_val=0, max_val=100):
    return max(min_val, min(value, max_val))


# -------------------------
# FINANCIAL ENGINE
# -------------------------
def run_financial_engine(starting_cash, commitments, revenue, cost, financial_risk):
    profit = revenue - cost
    roi = profit / (cost + 1e-6)

    roi_score = clamp(roi * 100)

    liquidity = (starting_cash - commitments) / (starting_cash + 1e-6)
    liquidity_score = clamp(liquidity * 100)

    financial_score = (roi_score * 0.6 + liquidity_score * 0.4) * (1 - financial_risk)

    return {
        "profit": profit,
        "roi": roi,
        "roi_score": roi_score,
        "liquidity_score": liquidity_score,
        "financial_score": financial_score
    }


# -------------------------
# RISK ENGINE
# -------------------------
def run_risk_engine(severity, probability):
    risk_raw = severity * probability
    risk_score = clamp(risk_raw * 10)

    return {
        "risk_raw": risk_raw,
        "risk_score": risk_score
    }


# -------------------------
# OPPORTUNITY ENGINE
# -------------------------
def run_opportunity_engine(opportunity_value, opportunity_risk):
    opportunity_raw = opportunity_value * (1 - opportunity_risk)
    opportunity_score = clamp(opportunity_raw * 10)

    return {
        "opportunity_raw": opportunity_raw,
        "opportunity_score": opportunity_score
    }


# -------------------------
# CAPITAL ENGINE
# -------------------------
def run_capital_engine(roi_score, priority, risk_score):
    capital_score = (
        roi_score * 0.5 +
        (priority * 100) * 0.3 +
        (100 - risk_score) * 0.2
    )

    return {
        "capital_score": clamp(capital_score)
    }


# -------------------------
# MARKET ENGINE
# -------------------------
def run_market_engine(market_size, regulation):
    market_factor = math.log1p(market_size)
    market_score = clamp((market_factor / 10) * 100)

    expansion_score = market_score * (1 - regulation)

    return {
        "market_score": market_score,
        "expansion_score": clamp(expansion_score)
    }


# -------------------------
# GOVERNANCE ENGINE
# -------------------------
def run_governance_engine(compliance):
    governance_score = 100 if compliance == 1 else 30

    return {
        "governance_score": governance_score
    }


# -------------------------
# AI FEEDBACK (LIGHT)
# -------------------------
def run_ai_feedback(financial_score, risk_score, opportunity_score):
    insights = []

    if financial_score < 50:
        insights.append("Improve profitability or liquidity")

    if risk_score > 60:
        insights.append("Risk exposure is high — mitigation required")

    if opportunity_score > 70:
        insights.append("Strong opportunity — consider expansion")

    return {
        "insights": insights
    }


# -------------------------
# CENTRAL ENGINE
# -------------------------
def run_all_engines(data):

    fin = run_financial_engine(
        data["starting_cash"],
        data["commitments"],
        data["revenue"],
        data["cost"],
        data["financial_risk"]
    )

    risk = run_risk_engine(
        data["severity"],
        data["probability"]
    )

    opp = run_opportunity_engine(
        data["opportunity_value"],
        data["opportunity_risk"]
    )

    cap = run_capital_engine(
        fin["roi_score"],
        data["priority"],
        risk["risk_score"]
    )

    market = run_market_engine(
        data["market_size"],
        data["regulation"]
    )

    gov = run_governance_engine(
        data["compliance"]
    )

    ai = run_ai_feedback(
        fin["financial_score"],
        risk["risk_score"],
        opp["opportunity_score"]
    )

    # -------------------------
    # MASTER METRICS
    # -------------------------
    business_stability = (
        fin["financial_score"] * 0.4 +
        (100 - risk["risk_score"]) * 0.3 +
        gov["governance_score"] * 0.2 +
        cap["capital_score"] * 0.1
    )

    strategic_opportunity = (
        opp["opportunity_score"] * 0.6 +
        market["expansion_score"] * 0.4
    )

    return {
        "financial": fin,
        "risk": risk,
        "opportunity": opp,
        "capital": cap,
        "market": market,
        "governance": gov,
        "ai": ai,

        "business_stability": clamp(business_stability),
        "strategic_opportunity": clamp(strategic_opportunity),
        "risk_exposure": clamp(risk["risk_score"]),
        "roi_projection": clamp(fin["roi_score"]),
        "capital_priority": clamp(cap["capital_score"]),
        "expansion_priority": clamp(market["expansion_score"])
    }
