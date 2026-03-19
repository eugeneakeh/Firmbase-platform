import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------
# IMPORT CORE ENGINE
# -------------------------
from engines.core_engine import run_all_engines
# -------------------------
# APP CONFIG
# -------------------------
st.set_page_config(page_title="Firmbase Platform", layout="wide")

st.title("Firmbase Autonomous Strategy Platform")

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
st.sidebar.title("Navigation")

page = st.sidebar.selectbox(
    "Select Module",
    [
        "Master Dashboard",
        "System Check"
    ]
)

# -------------------------
# INPUT VALIDATION
# -------------------------
def validate_inputs(data):
    errors = []

    if data["starting_cash"] <= 0:
        errors.append("Starting cash must be greater than 0.")

    if data["revenue"] <= 0:
        errors.append("Revenue must be greater than 0.")

    if data["cost"] < 0:
        errors.append("Cost cannot be negative.")

    if data["commitments"] < 0:
        errors.append("Commitments cannot be negative.")

    if data["cost"] > data["revenue"]:
        errors.append("Cost cannot exceed revenue.")

    if data["market_size"] <= 0:
        errors.append("Market size must be greater than 0.")

    return errors


# =========================================================
# MASTER DASHBOARD
# =========================================================
if page == "Master Dashboard":

    st.header("Strategic Intelligence Dashboard")
    st.markdown("---")

    # -------------------------
    # INPUTS
    # -------------------------
    with st.expander("💰 Financial Inputs"):
        starting_cash = st.number_input("Starting Cash", value=10000, step=1000)
        commitments = st.number_input("Commitments", value=0, step=1000)
        revenue = st.number_input("Revenue", value=10000, step=1000)
        cost = st.number_input("Cost", value=5000, step=1000)
        financial_risk = st.slider("Financial Risk", 0.0, 1.0, 0.1)

    with st.expander("⚠️ Risk Inputs"):
        severity = st.slider("Severity", 1, 10, 5)
        probability = st.slider("Probability", 0.0, 1.0, 0.3)

    with st.expander("🚀 Opportunity Inputs"):
        opportunity_value = st.slider("Opportunity Value", 1, 10, 7)
        opportunity_risk = st.slider("Opportunity Risk", 0.0, 1.0, 0.2)

    with st.expander("💹 Capital Inputs"):
        priority = st.slider("Capital Priority", 0.0, 1.0, 0.8)

    with st.expander("🌎 Market Inputs"):
        market_size = st.number_input("Market Size", value=10000, step=1000)
        regulation = st.slider("Regulation", 0.0, 1.0, 0.3)

    with st.expander("🛡️ Governance"):
        compliance = st.selectbox(
            "Compliance",
            [1, 0],
            format_func=lambda x: "Compliant" if x == 1 else "Non-Compliant"
        )

    # -------------------------
    # DATA OBJECT
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

    # -------------------------
    # VALIDATION
    # -------------------------
    errors = validate_inputs(data)

    if errors:
        st.error("⚠️ Input Errors Detected")
        for e in errors:
            st.write(f"- {e}")
        st.stop()

    # -------------------------
    # RUN CORE ENGINE
    # -------------------------
    results = run_all_engines(data)

    # -------------------------
    # METRICS
    # -------------------------
    st.markdown("---")
    st.subheader("Strategic Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Business Stability", round(results["business_stability"], 2))
        st.metric("Strategic Opportunity", round(results["strategic_opportunity"], 2))
        st.metric("Risk Exposure", round(results["risk_exposure"], 2))

    with col2:
        st.metric("ROI Projection", round(results["roi_projection"], 2))
        st.metric("Capital Priority", round(results["capital_priority"], 2))
        st.metric("Expansion Priority", round(results["expansion_priority"], 2))

    # -------------------------
    # VISUAL
    # -------------------------
    st.markdown("---")
    st.subheader("Visual Analytics")

    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    roi_trend = [results["roi_projection"]] * 6

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=roi_trend, mode="lines+markers"))
    st.plotly_chart(fig, use_container_width=True)

    # -------------------------
    # AI INSIGHTS
    # -------------------------
    st.markdown("---")
    st.subheader("AI Insights")

    for insight in results["ai"]["insights"]:
        st.write(f"- {insight}")

    # -------------------------
    # SUMMARY
    # -------------------------
    st.markdown("---")
    st.subheader("Business Summary")

    if results["business_stability"] > 70:
        st.success("Strong business position")
    elif results["business_stability"] > 50:
        st.warning("Moderate stability")
    else:
        st.error("Weak business condition")

    # -------------------------
    # CLASSIFICATION
    # -------------------------
    st.subheader("Classification")

    if results["business_stability"] > 70 and results["risk_exposure"] < 40:
        classification = "A1 - Strong & Scalable"
    elif results["business_stability"] > 50:
        classification = "B2 - Stable"
    else:
        classification = "C3 - High Risk"

    st.info(classification)

    # -------------------------
    # ACTIONS
    # -------------------------
    st.subheader("Top Actions")

    actions = []

    if results["risk_exposure"] > 60:
        actions.append("Reduce risk exposure")

    if results["capital_priority"] < 50:
        actions.append("Improve capital allocation")

    if results["expansion_priority"] > 60:
        actions.append("Expand into new markets")

    if not actions:
        actions.append("Maintain current strategy")

    for i, act in enumerate(actions, 1):
        st.write(f"{i}. {act}")

    # -------------------------
    # AUDIT VIEW
    # -------------------------
    st.markdown("---")
    with st.expander("🔍 Audit View"):
        st.json(results)


# =========================================================
# SYSTEM CHECK
# =========================================================
elif page == "System Check":

    st.header("System Validation")

    test_data = {
        "starting_cash": 100000,
        "commitments": 20000,
        "revenue": 50000,
        "cost": 20000,
        "financial_risk": 0.2,
        "severity": 5,
        "probability": 0.3,
        "opportunity_value": 7,
        "opportunity_risk": 0.2,
        "priority": 0.8,
        "market_size": 1000000,
        "regulation": 0.3,
        "compliance": 1
    }

    results = run_all_engines(test_data)

    st.json(results)
    st.success("System running correctly")
