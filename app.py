import streamlit as st
from engines.financial_engine import run_financial_engine
from engines.risk_engine import run_risk_engine
from engines.opportunity_engine import run_opportunity_engine
from engines.capital_engine import run_capital_engine
from engines.market_engine import run_market_engine
from engines.governance_engine import run_governance_engine
import plotly.graph_objects as go
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

    st.header("Firmbase Dynamic Strategic Intelligence Dashboard")
    st.write("Aggregates real-time outputs from all Firmbase engines with AI-driven recommendations")

    # --- ENGINE INPUTS ---
    # Financial Engine
    starting_cash = st.number_input("Financial: Starting Cash", 1000000)
    commitments = st.number_input("Financial: Planned Commitments", 200000)
    revenue = st.number_input("Financial: Revenue", 400000)
    cost = st.number_input("Financial: Cost", 150000)
    financial_risk = st.slider("Financial: Risk Factor", 0.0, 1.0, 0.1)
    financial_results = run_financial_engine(starting_cash, commitments, revenue, cost, financial_risk)
    roi = financial_results["roi"]

    # Risk Engine
    severity = st.slider("Risk: Severity", 1, 10, 5)
    probability = st.slider("Risk: Probability", 0.0, 1.0, 0.3)
    risk_results = run_risk_engine(severity, probability)
    risk_score = risk_results["risk_score"]

    # Opportunity Engine
    opportunity_value = st.slider("Opportunity: Strategic Value", 1, 10, 7)
    opportunity_risk = st.slider("Opportunity: Risk", 0.0, 1.0, 0.2)
    opp_results = run_opportunity_engine(opportunity_value, opportunity_risk)
    opportunity_score = opp_results["opportunity_score"]

    # Capital Allocation Engine
    priority = st.slider("Capital: Strategic Priority", 0.0, 1.0, 0.8)
    capital_results = run_capital_engine(roi, priority, financial_risk)
    allocation_score = capital_results["allocation_score"]

    # Market Expansion Engine
    market_size = st.number_input("Market: Market Size", 1000000)
    regulation = st.slider("Market: Regulatory Barrier", 0.0, 1.0, 0.3)
    market_results = run_market_engine(market_size, regulation)
    market_priority = market_results["priority_score"]

    # Governance Engine
    compliance = st.selectbox("Governance: Compliance Status", [1,0], format_func=lambda x: "Compliant" if x==1 else "Non-Compliant")
    gov_results = run_governance_engine(compliance)
    governance_exposure = gov_results["risk_exposure"]

    # --- STRATEGIC METRICS ---
    business_stability = (roi * (1 - risk_score/10)) * 100
    strategic_opportunity = opportunity_score * 10
    risk_exposure = risk_score * 10
    roi_projection = roi * 100
    capital_priority = allocation_score * 100
    expansion_priority = market_priority

    # Display Metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Business Stability Index", round(business_stability,2))
        st.metric("Strategic Opportunity Score", round(strategic_opportunity,2))
        st.metric("Risk Exposure Index", round(risk_exposure,2))
    with col2:
        st.metric("ROI Projection (%)", round(roi_projection,2))
        st.metric("Capital Allocation Priority", round(capital_priority,2))
        st.metric("Global Expansion Priority", expansion_priority)

    # --- VISUAL STRATEGIC ANALYTICS ---
    st.subheader("Dynamic Visual Analytics")

    # ROI Trend
    roi_trend = [roi*80, roi*85, roi*90, roi*95, roi*100, roi*105]  # dynamically scaled
    months = ["Jan","Feb","Mar","Apr","May","Jun"]
    fig_roi = go.Figure()
    fig_roi.add_trace(go.Scatter(x=months, y=roi_trend, mode='lines+markers', name='ROI %'))
    fig_roi.update_layout(title="ROI Trend", xaxis_title="Month", yaxis_title="ROI (%)")
    st.plotly_chart(fig_roi)

    # Risk Exposure by Engine
    risk_levels = ['Financial','Risk','Opportunity','Capital','Market','Governance']
    risk_values = [
        financial_risk*20,
        risk_score,
        opportunity_risk*10,
        financial_risk*15,
        regulation*20,
        governance_exposure*10
    ]
    fig_risk = go.Figure([go.Bar(x=risk_levels, y=risk_values, marker_color='red')])
    fig_risk.update_layout(title="Risk Exposure by Engine", yaxis_title="Risk Score")
    st.plotly_chart(fig_risk)

    # Opportunity Score
    opportunity_names = ['Current Opportunity']
    fig_op = go.Figure([go.Bar(x=opportunity_names, y=[opportunity_score], marker_color='green')])
    fig_op.update_layout(title="Opportunity Score", yaxis_title="Score")
    st.plotly_chart(fig_op)

    # Market Expansion Priority
    markets = ['Selected Market']
    fig_market = go.Figure([go.Bar(x=markets, y=[market_priority], marker_color='blue')])
    fig_market.update_layout(title="Market Expansion Priority", yaxis_title="Priority Score")
    st.plotly_chart(fig_market)

    # --- AI FEEDBACK & OPTIMIZATION LOOP ---
    ai_results = run_ai_feedback(roi, risk_score, opportunity_score, allocation_score, market_priority)

    st.subheader("AI Optimization Recommendations")
    for engine, decision in ai_results["optimized_decision"].items():
        st.write(f"{engine} Engine: {decision}")
    
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
