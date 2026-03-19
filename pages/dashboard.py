import streamlit as st
import plotly.graph_objects as go
from engines.core_engine import run_all_engines

def show():
    st.header("Strategic Intelligence Dashboard")

    # -------------------------
    # INPUTS
    # -------------------------
    starting_cash = st.number_input("Starting Cash", 10000)
    commitments = st.number_input("Commitments", 0)
    revenue = st.number_input("Revenue", 10000)
    cost = st.number_input("Cost", 5000)
    financial_risk = st.slider("Financial Risk", 0.0, 1.0, 0.1)

    severity = st.slider("Risk Severity", 1, 10, 5)
    probability = st.slider("Risk Probability", 0.0, 1.0, 0.3)

    opportunity_value = st.slider("Opportunity Value", 1, 10, 7)
    opportunity_risk = st.slider("Opportunity Risk", 0.0, 1.0, 0.2)

    priority = st.slider("Capital Priority", 0.0, 1.0, 0.8)

    market_size = st.number_input("Market Size", 10000)
    regulation = st.slider("Regulation", 0.0, 1.0, 0.3)

    compliance = st.selectbox("Compliance", [1, 0])

    # -------------------------
    # DATA
    # -------------------------
    data = {
        "starting_cash": starting_cash,
        "commitments": commitments,
        "revenue": revenue,
        "cost": cost,
        "financial_risk": financial_risk,
        "severity": severity,
        "probability": probability,
        "opportunity_value": opportunity_value,
        "opportunity_risk": opportunity_risk,
        "priority": priority,
        "market_size": market_size,
        "regulation": regulation,
        "compliance": compliance
    }

    results = run_all_engines(data)

    # -------------------------
    # METRICS
    # -------------------------
    st.metric("Business Stability", round(results["business_stability"], 2))
    st.metric("Risk Exposure", round(results["risk_exposure"], 2))
    st.metric("Opportunity", round(results["strategic_opportunity"], 2))

    # -------------------------
    # CHART
    # -------------------------
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=["Now"],
        y=[results["roi_projection"]],
        mode="markers"
    ))
    st.plotly_chart(fig)

    # -------------------------
    # AI
    # -------------------------
    st.subheader("Insights")
    for i in results["ai"]["insights"]:
        st.write("-", i)
