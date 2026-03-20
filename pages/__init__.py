import streamlit as st
from core_engine import run_all_engines


def show():
    st.header("Risk Intelligence Engine")

    severity = st.slider("Severity", 1, 10, 5)
    probability = st.slider("Probability", 0.0, 1.0, 0.3)

    data = {
        "starting_cash": 10000,
        "commitments": 0,
        "revenue": 10000,
        "cost": 5000,
        "financial_risk": 0.1,
        "severity": severity,
        "probability": probability,
        "opportunity_value": 5,
        "opportunity_risk": 0.2,
        "priority": 0.5,
        "market_size": 10000,
        "regulation": 0.3,
        "compliance": 1
    }

    results = run_all_engines(data)

    st.metric("Risk Score", round(results["risk_exposure"], 2))
