import streamlit as st
import pandas as pd

from engines.business_case_engine import BusinessCaseEngine
from core.central_engine import run_central_engine
from insights.recommendation_engine import RecommendationEngine


def show():
    st.set_page_config(layout="wide")

    st.title("📊 Firmbase Dashboard")
    st.caption("Business Decision Intelligence System")

    # -----------------------------
    # INPUT SECTION
    # -----------------------------
    st.subheader("🧾 Business Snapshot")

    col1, col2, col3 = st.columns(3)

    with col1:
        revenue = st.number_input("Monthly Revenue", value=10000)

    with col2:
        cost = st.number_input("Monthly Cost", value=5000)

    with col3:
        cash = st.number_input("Available Cash", value=20000)

    st.subheader("📈 Business Direction")

    col4, col5, col6 = st.columns(3)

    with col4:
        trend = st.selectbox("Sales Trend", ["up", "flat", "down"])

    with col5:
        stage = st.selectbox("Business Stage", ["startup", "growing", "mature"])

    with col6:
        market = st.selectbox("Market Condition", ["strong", "stable", "weak"])

    # -----------------------------
    # RUN BUTTON
    # -----------------------------
    if st.button("Run Business Case"):

        # -----------------------------
        # BUILD BUSINESS CASE
        # -----------------------------
        case_engine = BusinessCaseEngine()
        case = case_engine.build_case({
            "revenue": revenue,
            "cost": cost,
            "cash": cash,
            "trend": trend,
            "stage": stage,
            "market": market
        })

        # -----------------------------
        # RUN CORE ENGINES
        # -----------------------------
        results = run_central_engine(case)

        # -----------------------------
        # GENERATE RECOMMENDATIONS
        # -----------------------------
        rec_engine = RecommendationEngine()

        # Convert engine outputs into signals (simple mapping)
        signals = [
            {"type": "financial", "severity": 1 - (results["financial"]["score"] / 100), "impact": 0.8, "context": results["financial"]["insight"]},
            {"type": "risk", "severity": 1 - (results["risk"]["score"] / 100), "impact": 0.9, "context": results["risk"]["insight"]},
            {"type": "opportunity", "severity": 1 - (results["opportunity"]["score"] / 100), "impact": 1.0, "context": results["opportunity"]["insight"]},
            {"type": "capital", "severity": 1 - (results["capital"]["score"] / 100), "impact": 0.7, "context": results["capital"]["insight"]},
        ]

        recommendations = rec_engine.generate_recommendations(signals)

        # -----------------------------
        # OVERALL SUMMARY
        # -----------------------------
        st.divider()
        st.subheader("📌 Overall Business Health")

        colA, colB = st.columns(2)

        with colA:
            st.metric("Business Score", results["score"])

        with colB:
            st.success(results["status"])

        st.markdown("### 🧭 Key Insight")
        st.write(results["summary"])

        # -----------------------------
        # BREAKDOWN
        # -----------------------------
        st.divider()
        st.subheader("📊 Performance Breakdown")

        f, r, o, c = st.columns(4)

        with f:
            st.markdown("### 💰 Financial")
            st.metric("Score", results["financial"]["score"])
            st.write(results["financial"]["label"])

        with r:
            st.markdown("### ⚠️ Risk")
            st.metric("Score", results["risk"]["score"])
            st.write(results["risk"]["label"])

        with o:
            st.markdown("### 📈 Growth")
            st.metric("Score", results["opportunity"]["score"])
            st.write(results["opportunity"]["label"])

        with c:
            st.markdown("### 🏦 Capital")
            st.metric("Score", results["capital"]["score"])
            st.write(results["capital"]["label"])

        # -----------------------------
        # CHARTS
        # -----------------------------
        st.divider()
        st.subheader("📉 Business Projections")

        df = pd.DataFrame(case["projections"])

        fig1, ax1 = plt.subplots()
        ax1.plot(df["month"], df["revenue"], label="Revenue")
        ax1.plot(df["month"], df["cost"], label="Cost")
        ax1.set_title("Revenue vs Cost")
        ax1.legend()
        st.pyplot(fig1)

        fig2, ax2 = plt.subplots()
        ax2.plot(df["month"], df["profit"])
        ax2.set_title("Profit Trend")
        st.pyplot(fig2)

        # -----------------------------
        # DERIVED METRICS
        # -----------------------------
        st.markdown("### 🧮 Derived Metrics")
        st.write(f"Growth Rate: {case['derived_metrics']['growth_rate'] * 100:.1f}%")
        st.write(f"Runway: {case['runway']} months")
        st.write(f"Health: {case['health']}")

        # -----------------------------
        # RECOMMENDATIONS
        # -----------------------------
        st.divider()
        st.subheader("🚀 Strategic Recommendations")

        for rec in recommendations["recommendations"][:5]:
            st.markdown(f"### {rec['category'].capitalize()} — {rec['priority_level']}")
            st.write(f"**Observation:** {rec['observation']}")
            st.write(f"**Action:** {rec['recommended_action']}")
            st.write(f"**Expected Effect:** {rec['expected_effect']}")
            st.write(f"Score: {rec['score']}")
            st.markdown("---")
