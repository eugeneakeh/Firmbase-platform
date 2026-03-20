import streamlit as st
from core.orchestrator import run_firmbase


def show():
    st.title("📊 Firmbase Dashboard")
    st.write("Business Intelligence & Decision System")

    # -----------------------------
    # INPUT SECTION
    # -----------------------------
    st.subheader("Enter Business Data")

    revenue = st.number_input("Revenue", value=10000)
    cost = st.number_input("Cost", value=5000)
    debt = st.number_input("Debt", value=2000)
    capital = st.number_input("Capital Invested", value=10000)

    growth_rate = st.number_input("Growth Rate (%)", value=10)
    market_size = st.number_input("Market Size", value=100000)

    inputs = {
        "revenue": revenue,
        "cost": cost,
        "debt": debt,
        "capital": capital,
        "growth_rate": growth_rate,
        "market_size": market_size
    }

    # -----------------------------
    # RUN ANALYSIS BUTTON
    # -----------------------------
    if st.button("Run Analysis"):
        result = run_firmbase(inputs)

        # -------------------------
        # OUTPUT SECTION
        # -------------------------
        st.divider()

        st.subheader("📌 Overall Result")

        st.metric("Business Score", result["overall_score"])
        st.write(f"Status: **{result['status']}**")

        st.info(result["summary"])

        st.success(result["recommendation"])

        # -------------------------
        # BREAKDOWN SECTION
        # -------------------------
        st.divider()
        st.subheader("📊 Engine Breakdown")

        st.json(result["breakdown"])
