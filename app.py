import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# -------------------------
# Engine Imports
# -------------------------
from engines.financial_engine import run_financial_engine
from engines.risk_engine import run_risk_engine
from engines.opportunity_engine import run_opportunity_engine
from engines.capital_engine import run_capital_engine
from engines.market_engine import run_market_engine
from engines.governance_engine import run_governance_engine
from engines.ai_feedback_engine import run_ai_feedback

# -------------------------
# Sidebar
# -------------------------
st.sidebar.title("📊 Firmbase Navigation")
st.sidebar.markdown("---")
page = st.sidebar.selectbox(
    "Select Dashboard Section",
    [
        "Master Dashboard",
        "Financial Engine",
        "Risk Engine",
        "Opportunity Engine",
        "Capital Allocation",
        "Market Expansion",
        "Governance",
        "Business Simulation"
    ]
)
st.sidebar.markdown("---")
st.sidebar.write("Firmbase © 2026 — Strategic Business Intelligence Platform")

# -------------------------
# Helper Functions
# -------------------------
def display_metrics(metrics_dict):
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Business Stability Index", metrics_dict["business_stability"], help="Adjusted by all engine outputs")
        st.metric("Strategic Opportunity Score", metrics_dict["strategic_opportunity"], help="Based on Opportunity Engine")
        st.metric("Risk Exposure Index", metrics_dict["risk_exposure"], help="Based on Risk Engine")
    with col2:
        st.metric("ROI Projection (%)", metrics_dict["roi_projection"], help="Adjusted ROI from Financial Engine")
        st.metric("Capital Allocation Priority", metrics_dict["capital_priority"], help="Based on Capital Allocation Engine")
        st.metric("Global Expansion Priority", metrics_dict["expansion_priority"], help="Based on Market Expansion Engine")

# -------------------------
# Master Dashboard
# -------------------------
if page == "Master Dashboard":

    st.header("Firmbase Strategic Intelligence Dashboard")
    st.write("Unified analysis across all Firmbase engines")
    st.markdown("---")

    # -------------------------
    # Engine Inputs
    # -------------------------
    with st.expander("💰 Financial Engine Inputs", expanded=True):
        starting_cash = st.number_input("Starting Cash ($)", value=1000000, step=10000)
        commitments = st.number_input("Planned Commitments ($)", value=200000, step=10000)
        revenue = st.number_input("Revenue ($)", value=400000, step=10000)
        cost = st.number_input("Cost ($)", value=150000, step=10000)
        financial_risk = st.slider("Risk Factor", 0.0, 1.0, 0.1)
        financial_results = run_financial_engine(starting_cash, commitments, revenue, cost, financial_risk)
        roi = financial_results["roi"]

    with st.expander("⚠️ Risk Engine Inputs"):
        severity = st.slider("Severity", 1, 10, 5)
        probability = st.slider("Probability", 0.0, 1.0, 0.3)
        risk_results = run_risk_engine(severity, probability)
        risk_score = risk_results["risk_score"]

    with st.expander("🚀 Opportunity Engine Inputs"):
        opportunity_value = st.slider("Strategic Value", 1, 10, 7)
        opportunity_risk = st.slider("Risk Adjustment", 0.0, 1.0, 0.2)
        opp_results = run_opportunity_engine(opportunity_value, opportunity_risk)
        opportunity_score = opp_results["opportunity_score"]

    with st.expander("💹 Capital Allocation"):
        priority = st.slider("Strategic Priority", 0.0, 1.0, 0.8)
        capital_results = run_capital_engine(roi, priority, financial_risk)
        allocation_score = capital_results["allocation_score"]

    with st.expander("🌎 Market Expansion"):
        market_size = st.number_input("Market Size", value=1000000, step=10000)
        regulation = st.slider("Regulatory Barrier", 0.0, 1.0, 0.3)
        market_results = run_market_engine(market_size, regulation)
        market_priority = market_results["priority_score"]

    with st.expander("🛡️ Governance & Compliance"):
        compliance = st.selectbox("Compliance Status", [1, 0], format_func=lambda x: "Compliant" if x==1 else "Non-Compliant")
        gov_results = run_governance_engine(compliance)
        governance_exposure = gov_results["risk_exposure"]

    # -------------------------
    # AI Feedback
    # -------------------------
    ai_results = run_ai_feedback(roi, risk_score, opportunity_score, allocation_score, market_priority)
    adjusted_roi = roi * ai_results["improvement_score"]["Financial"]
    adjusted_risk_score = risk_score * (1 - ai_results["improvement_score"]["Risk"])
    adjusted_opportunity = opportunity_score * ai_results["improvement_score"]["Opportunity"]
    adjusted_allocation = allocation_score * ai_results["improvement_score"]["Capital"]
    adjusted_market = market_priority * ai_results["improvement_score"]["Market"]

    # -------------------------
    # Metrics
    # -------------------------
    st.markdown("---")
    st.subheader("Strategic Metrics")
    metrics_dict = {
        "business_stability": round((adjusted_roi * (1 - adjusted_risk_score/10)) * 100,2),
        "strategic_opportunity": round(adjusted_opportunity*10,2),
        "risk_exposure": round(adjusted_risk_score*10,2),
        "roi_projection": round(adjusted_roi*100,2),
        "capital_priority": round(adjusted_allocation*100,2),
        "expansion_priority": round(adjusted_market,2)
    }
    display_metrics(metrics_dict)

    # -------------------------
    # Visual Analytics
    # -------------------------
    st.markdown("---")
    st.subheader("Visual Analytics")
    months = ["Jan","Feb","Mar","Apr","May","Jun"]
    roi_trend = [adjusted_roi*80, adjusted_roi*85, adjusted_roi*90, adjusted_roi*95, adjusted_roi*100, adjusted_roi*105]
    fig_roi = go.Figure()
    fig_roi.add_trace(go.Scatter(x=months, y=roi_trend, mode="lines+markers", name="ROI Trend"))
    st.plotly_chart(fig_roi, use_container_width=True)

    # -------------------------
    # Strategic Recommendations
    # -------------------------
    st.markdown("---")
    st.subheader("Strategic Recommendations")
    st.info("These actions are derived from Firmbase's integrated business analysis engines.")
    recommendations_df = pd.DataFrame.from_dict(ai_results["optimized_decision"], orient="index", columns=["Recommended Action"])
    st.table(recommendations_df)

    # -------------------------
    # Phase 1 Features
    # -------------------------
    st.markdown("---")
    st.subheader("Business Health Summary")
    summary = []
    if metrics_dict["business_stability"] > 70:
        summary.append("Your business is financially stable.")
    else:
        summary.append("Your business shows signs of financial instability.")
    if metrics_dict["strategic_opportunity"] > 60:
        summary.append("There is strong strategic opportunity available.")
    else:
        summary.append("Strategic opportunities are currently limited.")
    if metrics_dict["risk_exposure"] > 50:
        summary.append("Risk exposure is above safe threshold and requires attention.")
    else:
        summary.append("Risk levels are within acceptable range.")
    for s in summary:
        st.write(f"- {s}")

    st.markdown("---")
    st.subheader("Business Classification")
    if metrics_dict["business_stability"] > 70 and metrics_dict["risk_exposure"] < 40:
        classification = "A1 - Strong and Scalable"
    elif metrics_dict["business_stability"] > 50:
        classification = "B2 - Stable and Considered"
    else:
        classification = "C3 - High Risk"
    st.success(f"Classification: {classification}")

    st.markdown("---")
    st.subheader("Top Strategic Actions")
    actions = []
    if metrics_dict["risk_exposure"] > 50:
        actions.append("Reduce operational risk (Urgent)")
    if metrics_dict["capital_priority"] < 50:
        actions.append("Improve capital allocation efficiency")
    if metrics_dict["expansion_priority"] > 60:
        actions.append("Expand into high-priority markets")
    if len(actions)==0:
        actions.append("Maintain current strategic direction")
    for i, action in enumerate(actions[:3], 1):
        st.write(f"{i}. {action}")

    st.markdown("---")
    st.subheader("Key Drivers (WHY)")
    st.write(f"Risk exposure is influenced by severity ({severity}) and probability ({probability}).")
    st.write(f"ROI is driven by revenue ({revenue}) relative to cost ({cost}).")
    st.write(f"Capital allocation priority is influenced by ROI ({round(roi,2)}) and strategic priority ({priority}).")


# -------------------------
# BUSINESS SIMULATION
# -------------------------
elif page == "Business Simulation":

    st.header("Business Scenario Simulation")
    st.write("Experiment with changes to see projected outcomes and trade-offs.")

    st.subheader("Adjustable Parameters")
    sim_revenue = st.number_input("Simulated Revenue ($)", value=revenue, step=10000)
    sim_cost = st.number_input("Simulated Cost ($)", value=cost, step=10000)
    sim_severity = st.slider("Simulated Risk Severity", 1, 10, severity)
    sim_probability = st.slider("Simulated Risk Probability", 0.0, 1.0, probability)
    sim_priority = st.slider("Simulated Capital Allocation Priority", 0.0, 1.0, priority)
    sim_market = st.slider("Simulated Market Expansion Level", 0.0, 1.0, metrics_dict["expansion_priority"]/100)

    sim_financial = run_financial_engine(starting_cash, commitments, sim_revenue, sim_cost, financial_risk)
    sim_roi = sim_financial["roi"]
    sim_risk = run_risk_engine(sim_severity, sim_probability)
    sim_risk_score = sim_risk["risk_score"]
    sim_capital = run_capital_engine(sim_roi, sim_priority, financial_risk)
    sim_allocation_score = sim_capital["allocation_score"]
    sim_market_res = run_market_engine(market_size, regulation)
    sim_market_priority = sim_market_res["priority_score"] * sim_market

    sim_business_stability = (sim_roi * (1 - sim_risk_score/10)) * 100
    sim_strategic_opportunity = opportunity_score * 10
    sim_risk_exposure = sim_risk_score * 10
    sim_roi_projection = sim_roi * 100
    sim_capital_priority = sim_allocation_score * 100
    sim_expansion_priority = sim_market_priority

    st.subheader("Simulation Results")
    sim_col1, sim_col2 = st.columns(2)
    with sim_col1:
        st.metric("Business Stability Index", round(sim_business_stability,2))
        st.metric("Strategic Opportunity Score", round(sim_strategic_opportunity,2))
        st.metric("Risk Exposure Index", round(sim_risk_exposure,2))
    with sim_col2:
        st.metric("ROI Projection (%)", round(sim_roi_projection,2))
        st.metric("Capital Allocation Priority", round(sim_capital_priority,2))
        st.metric("Global Expansion Priority", round(sim_expansion_priority,2))

    st.markdown("---")
    st.subheader("Trade-off Analysis")
    st.write(f"- Increasing market expansion to {sim_market*100:.0f}% increases expansion priority but may increase risk exposure by {sim_risk_score*10:.1f}")
    st.write(f"- Adjusting capital allocation affects ROI projection: new ROI = {round(sim_roi_projection,2)}")
