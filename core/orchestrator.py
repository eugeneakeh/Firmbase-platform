from core.schema import validate_inputs
from core.central_engine import aggregate_results

from engines.financial_engine import run_financial_engine
from engines.risk_engine import run_risk_engine
from engines.opportunity_engine import run_opportunity_engine
from engines.capital_engine import run_capital_engine
from engines.market_engine import run_market_engine
from engines.governance_engine import run_governance_engine
from engines.business_case_engine import run_business_case_engine
from engines.ai_feedback_engine import run_ai_feedback_engine


def run_system(inputs: dict):
    validate_inputs(inputs)

    financials = run_financial_engine(inputs)
    risk = run_risk_engine(inputs, financials)
    opportunity = run_opportunity_engine(inputs)
    market = run_market_engine(inputs)
    governance = run_governance_engine(inputs)
    capital = run_capital_engine(inputs, financials, risk)
    business_case = run_business_case_engine(financials, risk)

    aggregated = aggregate_results({
        "financials": financials,
        "risk": risk,
        "opportunity": opportunity,
        "market": market,
        "governance": governance,
        "capital": capital,
        "business_case": business_case
    })

    ai_feedback = run_ai_feedback_engine(aggregated)

    return {**aggregated, "ai_feedback": ai_feedback}
