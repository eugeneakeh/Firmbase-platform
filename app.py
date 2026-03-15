import streamlit as st
from engines.financial_engine import run_financial_engine

st.title("Firmbase Autonomous Strategy Platform")

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
