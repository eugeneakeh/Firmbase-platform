import streamlit as st
from engines.financial_engine import run_financial_engine

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
    st.header("Risk Engine")
    st.write("Risk engine will be implemented here.")

elif page == "Opportunity Engine":
    st.header("Opportunity Engine")
    st.write("Opportunity analysis coming soon.")

elif page == "Capital Allocation":
    st.header("Capital Allocation Engine")
    st.write("Capital allocation logic coming soon.")

elif page == "Market Expansion":
    st.header("Market Expansion Engine")
    st.write("Market intelligence coming soon.")

elif page == "Governance":
    st.header("Governance & Compliance Engine")
    st.write("Governance monitoring coming soon.")
