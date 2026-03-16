import streamlit as st
from engines.financial_engine import run_financial_engine
from engines.risk_engine import run_risk_engine
from engines.opportunity_engine import run_opportunity_engine
from engines.capital_engine import run_capital_engine
from engines.market_engine import run_market_engine
from engines.governance_engine import run_governance_engine
import plotly.graph_objects as go
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

    st.write("Unified strategic intelligence across all Firmbase engines")

    # --- Sample Inputs for Global Metrics ---
    
    roi = 0.35
    risk_score = 1.5
    opportunity_score = 6.5
    allocation_score = 0.4
    market_priority = 600000
    governance_exposure = 0

    # --- Strategic Indicators ---

    business_stability = (roi * (1 - risk_score/10)) * 100
    strategic_opportunity = opportunity_score * 10
    risk_exposure = risk_score * 10
    roi_projection = roi * 100
    capital_priority = allocation_score * 100
    expansion_priority = market_priority

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Business Stability Index", round(business_stability,2))
        st.metric("Strategic Opportunity Score", round(strategic_opportunity,2))
        st.metric("Risk Exposure Index", round(risk_exposure,2))

    with col2:
        st.metric("ROI Projection (%)", round(roi_projection,2))
        st.metric("Capital Allocation Priority", round(capital_priority,2))
        st.metric("Global Expansion Priority", expansion_priority)

st.subheader("Visual Strategic Analytics")

# ROI Trend (Sample Data)
roi_trend = [25, 28, 32, 35, 37, 40]
months = ["Jan","Feb","Mar","Apr","May","Jun"]
fig_roi = go.Figure()
fig_roi.add_trace(go.Scatter(x=months, y=roi_trend, mode='lines+markers', name='ROI %'))
fig_roi.update_layout(title="ROI Trend", xaxis_title="Month", yaxis_title="ROI (%)")
st.plotly_chart(fig_roi)

# Risk Exposure Bar Chart
risk_levels = ['Financial','Risk','Opportunity','Capital','Market','Governance']
risk_values = [20, 15, 10, 12, 18, 5]  # Sample scores
fig_risk = go.Figure([go.Bar(x=risk_levels, y=risk_values, marker_color='red')])
fig_risk.update_layout(title="Risk Exposure by Engine", yaxis_title="Risk Score")
st.plotly_chart(fig_risk)

# Opportunity Scores
opportunity_scores = [7, 6, 8, 5]
opportunity_names = ['New Product','Partnership','Expansion','M&A']
fig_op = go.Figure([go.Bar(x=opportunity_names, y=opportunity_scores, marker_color='green')])
fig_op.update_layout(title="Opportunity Scores", yaxis_title="Score")
st.plotly_chart(fig_op)

# Market Expansion Priority
markets = ['USA','Nigeria','Germany','India']
market_priority = [1000000, 500000, 800000, 650000]
fig_market = go.Figure([go.Bar(x=markets, y=market_priority, marker_color='blue')])
fig_market.update_layout(title="Market Expansion Priority", yaxis_title="Priority Score")
st.plotly_chart(fig_market)

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
