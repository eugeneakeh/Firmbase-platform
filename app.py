import streamlit as st
from engines.financial_engine import run_financial_engine
from engines.risk_engine import run_risk_engine
from engines.opportunity_engine import run_opportunity_engine
from engines.capital_engine import run_capital_engine
from engines.market_engine import run_market_engine

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

    st.header("Master Strategic Dashboard")

    st.write("This dashboard aggregates outputs from all Firmbase engines.")

    st.metric("Business Stability Index", "Pending")
    st.metric("Strategic Opportunity Score", "Pending")
    st.metric("Risk Exposure Index", "Pending")
    st.metric("ROI Projection", "Pending")

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
