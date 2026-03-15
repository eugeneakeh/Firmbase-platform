import streamlit as st

st.title("Firmbase Autonomous Strategy Platform")

st.header("Financial Engine")

starting_cash = st.number_input("Starting Cash",1000000)
commitments = st.number_input("Planned Commitments",200000)
revenue = st.number_input("Revenue",400000)
cost = st.number_input("Cost",150000)
risk = st.slider("Risk Factor",0.0,1.0,0.1)

cash_available = starting_cash - commitments
roi = (revenue - cost) / cost
risk_adjusted_roi = roi * (1 - risk)
projected_cashflow = cash_available + revenue - cost

st.write("Cash Available:", cash_available)
st.write("ROI:", roi)
st.write("Risk Adjusted ROI:", risk_adjusted_roi)
st.write("Projected Cash Flow:", projected_cashflow)
