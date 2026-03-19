import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------
# CORE ENGINE
# -------------------------
from core_engine import run_all_engines

# -------------------------
# APP CONFIG
# -------------------------
st.set_page_config(page_title="Firmbase", layout="wide")

st.title("Firmbase Autonomous Strategy Platform")

# -------------------------
# SIDEBAR NAVIGATION
# -------------------------
st.sidebar.title("Firmbase Navigation")

page = st.sidebar.selectbox(
    "Select Module",
    [
        "Master Dashboard",
        "Financial Engine",
        "Risk Engine",
        "Opportunity Engine",
        "Capital Allocation",
        "Market Expansion",
        "Governance",
        "Business Simulation",
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

    if not (0 <= data["financial_risk"] <= 1):
        errors.append("Financial risk must be between 0 and 1.")

    if not (1 <= data["severity"] <= 10):
        errors.append("Severity must be between 1 and 10.")

    if not (0 <= data["probability"] <= 1):
        errors.append("Probability must be between 0 and 1.")

    if not (0 <= data["priority"] <= 1):
        errors.append("Priority must be between 0 and 1.")

    if data["market_size"] <= 0:
        errors.append("Market size must be greater than 0.")

    if not (0 <= data["regulation"] <= 1):
        errors.append("Regulation must be between 0 and 1.")

    return errors

# -------------------------
# MASTER DASHBOARD
# -------------------------
if page == "Master Dashboard":

    st.header("Strategic Intelligence Dashboard")
    st.markdown("---")

    # INPUTS
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
        compliance = st.selectbox("Compliance", [1, 0], format_func=lambda x: "Compliant" if x == 1 else "Non-Compliant")

    # DATA OBJECT
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

    # VALIDATION
    errors = validate_inputs(data)
    if errors:
        st.error("Input Errors:")
        for e in errors:
            st.write("-", e)
        st.stop()

    # ENGINE RUN
    results = run_all_engines(data)

    roi = results["roi_projection"]
    risk = results["risk_exposure"]
    opp = results["strategic_opportunity"]
    cap = results["capital_priority"]
    exp = results["expansion_priority"]

    stability = (roi * 0.4 + (100 - risk) * 0.4 + cap * 0.2)

    # METRICS
    st.subheader("Strategic Metrics")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Stability", round(stability, 2))
        st.metric("Opportunity", round(opp, 2))
        st.metric("Risk", round(risk, 2))

    with col2:
        st.metric("ROI", round(roi, 2))
        st.metric("Capital Priority", round(cap, 2))
        st.metric("Expansion", round(exp, 2))

    # VISUAL
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    fig = go.Figure()
    fig.add_trace(go.Scatter(x=months, y=[roi]*6, mode="lines+markers"))
    st.plotly_chart(fig, use_container_width=True)

    # SUMMARY
    st.subheader("Business Summary")

    if stability > 70:
        st.success("Strong business position")
    elif stability > 50:
        st.warning("Moderate stability")
    else:
        st.error("High risk business")

    st.subheader("Classification")

    if stability > 70 and risk < 40:
        st.success("A1 - Strong")
    elif stability > 50:
        st.info("B2 - Stable")
    else:
        st.error("C3 - Risky")

    st.subheader("Actions")

    actions = []

    if risk > 60:
        actions.append("Reduce risk")

    if cap < 50:
        actions.append("Improve capital allocation")

    if exp > 60:
        actions.append("Expand market")

    if not actions:
        actions.append("Maintain strategy")

    for i, a in enumerate(actions, 1):
        st.write(i, a)

    with st.expander("Audit"):
        st.json(results)

# -------------------------
# SYSTEM CHECK
# -------------------------
elif page == "System Check":

    st.header("System Check")

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
    st.success("System OK")

# -------------------------
# PLACEHOLDER MODULES
# -------------------------
elif page == "Risk Engine":
    st.header("Risk Engine (Module View)")

elif page == "Opportunity Engine":
    st.header("Opportunity Engine (Module View)")

elif page == "Capital Allocation":
    st.header("Capital Engine (Module View)")

elif page == "Market Expansion":
    st.header("Market Engine (Module View)")

elif page == "Governance":
    st.header("Governance Engine (Module View)")

elif page == "Business Simulation":
    st.header("Simulation Engine (Coming Soon)")
