import streamlit as st
import pandas as pd
import plotly.graph_objects as go

from engines.financial_engine import run_financial_engine
from engines.risk_engine import run_risk_engine
from engines.opportunity_engine import run_opportunity_engine
from engines.capital_engine import run_capital_engine
from engines.market_engine import run_market_engine
from engines.governance_engine import run_governance_engine
from engines.ai_feedback_engine import run_ai_feedback
st.title("Firmbase Autonomous Strategy Platform")

st.sidebar.title("Firmbase Navigation")

page = st.sidebar.selectbox(
    "Select Engine",
    [
        "Master Dashboard",
        "Financial Engine",
        "Risk Engine",
        "Opportunity Engine",
        "Capital Allocation",
        "Market Expansion",
        "Governance"
    ]
)

# MASTER DASHBOARD
if page == "Master Dashboard":

    st.header("Firmbase Strategic Intelligence Dashboard")
    st.write("Unified analysis across all Firmbase engines")

    st.markdown("---")

    # -------------------------
    # Financial Engine Inputs
    # -------------------------
    with st.expander("💰 Financial Engine Inputs", expanded=True):

        starting_cash = st.number_input("Starting Cash ($)", value=1000000, step=10000)
        commitments = st.number_input("Planned Commitments ($)", value=200000, step=10000)
        revenue = st.number_input("Revenue ($)", value=400000, step=10000)
        cost = st.number_input("Cost ($)", value=150000, step=10000)
        financial_risk = st.slider("Risk Factor", 0.0, 1.0, 0.1)

        financial_results = run_financial_engine(
            starting_cash,
            commitments,
            revenue,
            cost,
            financial_risk
        )

        roi = financial_results["roi"]

    # -------------------------
    # Risk Engine
    # -------------------------
    with st.expander("⚠️ Risk Engine Inputs"):

        severity = st.slider("Severity", 1, 10, 5)
        probability = st.slider("Probability", 0.0, 1.0, 0.3)

        risk_results = run_risk_engine(severity, probability)

        risk_score = risk_results["risk_score"]

    # -------------------------
    # Opportunity Engine
    # -------------------------
    with st.expander("🚀 Opportunity Engine Inputs"):

        opportunity_value = st.slider("Strategic Value", 1, 10, 7)
        opportunity_risk = st.slider("Risk Adjustment", 0.0, 1.0, 0.2)

        opp_results = run_opportunity_engine(
            opportunity_value,
            opportunity_risk
        )

        opportunity_score = opp_results["opportunity_score"]

    # -------------------------
    # Capital Allocation
    # -------------------------
    with st.expander("💹 Capital Allocation"):

        priority = st.slider("Strategic Priority", 0.0, 1.0, 0.8)

        capital_results = run_capital_engine(
            roi,
            priority,
            financial_risk
        )

        allocation_score = capital_results["allocation_score"]

    # -------------------------
    # Market Expansion
    # -------------------------
    with st.expander("🌎 Market Expansion"):

        market_size = st.number_input("Market Size", value=1000000, step=10000)
        regulation = st.slider("Regulatory Barrier", 0.0, 1.0, 0.3)

        market_results = run_market_engine(
            market_size,
            regulation
        )

        market_priority = market_results["priority_score"]

    # -------------------------
    # Governance
    # -------------------------
    with st.expander("🛡️ Governance & Compliance"):

        compliance = st.selectbox(
            "Compliance Status",
            [1,0],
            format_func=lambda x: "Compliant" if x == 1 else "Non-Compliant"
        )

        gov_results = run_governance_engine(compliance)

        governance_exposure = gov_results["risk_exposure"]

    # -------------------------
    # AI Feedback (internal)
    # -------------------------
    ai_results = run_ai_feedback(
        roi,
        risk_score,
        opportunity_score,
        allocation_score,
        market_priority
    )

    adjusted_roi = roi * ai_results["improvement_score"]["Financial"]
    adjusted_risk_score = risk_score * (1 - ai_results["improvement_score"]["Risk"])
    adjusted_opportunity = opportunity_score * ai_results["improvement_score"]["Opportunity"]
    adjusted_allocation = allocation_score * ai_results["improvement_score"]["Capital"]
    adjusted_market = market_priority * ai_results["improvement_score"]["Market"]

    # -------------------------
    # Strategic Metrics
    # -------------------------
    st.markdown("---")
    st.subheader("Strategic Metrics")

    business_stability = (adjusted_roi * (1 - adjusted_risk_score/10)) * 100
    strategic_opportunity = adjusted_opportunity * 10
    risk_exposure = adjusted_risk_score * 10
    roi_projection = adjusted_roi * 100
    capital_priority = adjusted_allocation * 100
    expansion_priority = adjusted_market

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Business Stability Index", round(business_stability,2))
        st.metric("Strategic Opportunity Score", round(strategic_opportunity,2))
        st.metric("Risk Exposure Index", round(risk_exposure,2))

    with col2:
        st.metric("ROI Projection (%)", round(roi_projection,2))
        st.metric("Capital Allocation Priority", round(capital_priority,2))
        st.metric("Global Expansion Priority", expansion_priority)

    # -------------------------
    # Visual Analytics
    # -------------------------
    st.markdown("---")
    st.subheader("Visual Analytics")

    months = ["Jan","Feb","Mar","Apr","May","Jun"]
    roi_trend = [
        adjusted_roi*80,
        adjusted_roi*85,
        adjusted_roi*90,
        adjusted_roi*95,
        adjusted_roi*100,
        adjusted_roi*105
    ]

    fig_roi = go.Figure()
    fig_roi.add_trace(
        go.Scatter(
            x=months,
            y=roi_trend,
            mode="lines+markers",
            line=dict(color="royalblue", width=3)
        )
    )

    fig_roi.update_layout(
        title="ROI Trend",
        xaxis_title="Month",
        yaxis_title="ROI (%)"
    )

    st.plotly_chart(fig_roi, use_container_width=True)

    # -------------------------
    # Strategic Recommendations
    # -------------------------
    st.markdown("---")
    st.subheader("Strategic Recommendations")

    st.info(
        "These actions are derived from Firmbase's integrated business analysis engines."
    )

    recommendations_df = pd.DataFrame.from_dict(
        ai_results["optimized_decision"],
        orient="index",
        columns=["Recommended Action"]
    )

    st.table(recommendations_df)
    
# FINANCIAL ENGINE
elif page == "Financial Engine":

    st.header("Financial Engine")

    starting_cash = st.number_input("Starting Cash",1000000)
    commitments = st.number_input("Planned Commitments",200000)
    revenue = st.number_input("Revenue",400000)
    cost = st.number_input("Cost",150000)
    risk = st.slider("Risk Factor",0.0,1.0,0.1)

    results = run_financial_engine(starting_cash,commitments,revenue,cost,risk)

    st.write("Cash Available:", results["cash_available"])
    st.write("ROI:", results["roi"])
    st.write("Risk Adjusted ROI:", results["risk_adjusted_roi"])
    st.write("Projected Cash Flow:", results["projected_cashflow"])

# OTHER ENGINES PLACEHOLDER

elif page == "Risk Engine":

    st.header("Risk Intelligence Engine")

    severity = st.slider("Risk Severity",1,10,5)
    probability = st.slider("Risk Probability",0.0,1.0,0.3)

    results = run_risk_engine(severity,probability)

    st.write("Risk Score:", results["risk_score"])
    st.write("Risk Level:", results["risk_level"])

elif page == "Opportunity Engine":

    st.header("Strategic Opportunity Engine")

    value = st.slider("Strategic Value",1,10,7)
    risk = st.slider("Opportunity Risk",0.0,1.0,0.2)

    results = run_opportunity_engine(value,risk)

    st.write("Opportunity Score:", results["opportunity_score"])
    st.write("Recommendation:", results["decision"])
    
elif page == "Capital Allocation":

    st.header("Capital Allocation Engine")

    roi = st.slider("Expected ROI",0.0,1.0,0.3)
    priority = st.slider("Strategic Priority",0.0,1.0,0.8)
    risk = st.slider("Investment Risk",0.0,1.0,0.2)

    results = run_capital_engine(roi,priority,risk)

    st.write("Allocation Score:", results["allocation_score"])
    st.write("Investment Decision:", results["decision"])
    
elif page == "Market Expansion":

    st.header("Global Market Expansion Engine")

    size = st.number_input("Market Size",1000000)
    regulation = st.slider("Regulatory Barrier",0.0,1.0,0.3)

    results = run_market_engine(size,regulation)

    st.write("Expansion Priority Score:", results["priority_score"])
    st.write("Recommended Strategy:", results["decision"])

elif page == "Governance":

    st.header("Governance & Compliance Engine")

    compliance = st.selectbox(
        "Compliance Status",
        [1,0],
        format_func=lambda x: "Compliant" if x == 1 else "Non-Compliant"
    )

    results = run_governance_engine(compliance)

    st.write("Governance Risk Exposure:", results["risk_exposure"])
    st.write("Status:", results["status"])
