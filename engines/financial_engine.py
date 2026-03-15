def run_financial_engine(starting_cash, commitments, revenue, cost, risk):

    cash_available = starting_cash - commitments

    roi = (revenue - cost) / cost

    risk_adjusted_roi = roi * (1 - risk)

    projected_cashflow = cash_available + revenue - cost

    return {
        "cash_available": cash_available,
        "roi": roi,
        "risk_adjusted_roi": risk_adjusted_roi,
        "projected_cashflow": projected_cashflow
    }
