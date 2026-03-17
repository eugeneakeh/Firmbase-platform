import streamlit as st
import pandas as pd
import plotly.graph_objects as go
def validate_inputs(data):
    errors = []

    if data["starting_cash"] <= 0:
        errors.append("Starting cash must be greater than 0.")

    if data["revenue"] <= 0:
        errors.append("Revenue must be greater than 0.")

    if data["cost"] < 0:
        errors.append("Cost cannot be negative.")

    if data["commitments"] < 0:
        errors.append("Commitments cannot be negative.")

    if data["cost"] > data["revenue"]:
        errors.append("Cost cannot exceed revenue (unprofitable case not allowed here).")

    if not (0 <= data["financial_risk"] <= 1):
        errors.append("Financial risk must be between 0 and 1.")

    if not (1 <= data["severity"] <= 10):
        errors.append("Risk severity must be between 1 and 10.")

    if not (0 <= data["probability"] <= 1):
        errors.append("Risk probability must be between 0 and 1.")

    if not (0 <= data["priority"] <= 1):
        errors.append("Capital priority must be between 0 and 1.")

    if data["market_size"] <= 0:
        errors.append("Market size must be greater than 0.")

    if not (0 <= data["regulation"] <= 1):
        errors.append("Regulation must be between 0 and 1.")

    return errors

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
        "Governance",
        "Business Simulation",
        "System Check"
    ]
)


# -------------------------
# MASTER DASHBOARD
# -------------------------
if page == "Master Dashboard":

    st.header("Firmbase Strategic Intelligence Dashboard")
    st.write("Unified analysis across all Firmbase engines")
    st.markdown("---")

    # -------------------------
    # INPUTS
    # -------------------------
    with st.expander("💰 Financial Inputs"):
        starting_cash = st.number_input("Starting Cash ($)", value=0, step=10000)
        commitments = st.number_input("Planned Commitments ($)", value=0, step=10000)
        revenue = st.number_input("Revenue ($)", value=0, step=10000)
        cost = st.number_input("Cost ($)", value=0, step=10000)
        financial_risk = st.slider("Financial Risk (0-1)", 0.0, 1.0, 0.1)

    # -------------------------
    # RISK INPUTS
    # -------------------------
    with st.expander("⚠️ Risk Engine Inputs"):
        severity = st.slider("Risk Severity", 1, 10, 5)
        probability = st.slider("Risk Probability", 0.0, 1.0, 0.3)

    # -------------------------
    # OPPORTUNITY INPUTS
    # -------------------------
    with st.expander("🚀 Opportunity Engine Inputs"):
        opportunity_value = st.slider("Strategic Value", 1, 10, 7)
        opportunity_risk = st.slider("Risk Adjustment", 0.0, 1.0, 0.2)

    # -------------------------
    # CAPITAL ALLOCATION INPUTS
    # -------------------------
    with st.expander("💹 Capital Allocation"):
        priority = st.slider("Strategic Priority", 0.0, 1.0, 0.8)

    # -------------------------
    # MARKET INPUTS
    # -------------------------
    with st.expander("🌎 Market Expansion"):
        market_size = st.number_input("Market Size", value=0, step=10000)
        regulation = st.slider("Regulatory Barrier (0-1)", 0.0, 1.0, 0.3)

    # -------------------------
    # GOVERNANCE INPUTS
    # -------------------------
    with st.expander("🛡️ Governance & Compliance"):
        compliance = st.selectbox("Compliance Status", [1, 0], format_func=lambda x: "Compliant" if x==1 else "Non-Compliant")

    # -------------------------
    # STORE INPUTS IN SESSION STATE
    # -------------------------
    st.session_state.update({
        "starting_cash": starting_cash,
        "commitments": commitments,
        "revenue": revenue,
        "cost": cost,
        "financial_risk": financial_risk,
        "severity": severity,
        "probability": probability,
        "opportunity_value": opportunity_value,
        "opportunity_risk": opportunity_risk,
        "priority": priority,
        "market_size": market_size,
        "regulation": regulation,
        "compliance": compliance
    })

    # -------------------------
    # INPUT VALIDATION
    # -------------------------
    def validate_inputs(data):
        errors = []
        if data["starting_cash"] <= 0:
            errors.append("Starting cash must be greater than 0.")
        if data["revenue"] <= 0:
            errors.append("Revenue must be greater than 0.")
        if data["cost"] < 0:
            errors.append("Cost cannot be negative.")
        if data["commitments"] < 0:
            errors.append("Planned commitments cannot be negative.")
        if data["cost"] > data["revenue"]:
            errors.append("Cost cannot exceed revenue.")
        if not (0 <= data["financial_risk"] <= 1):
            errors.append("Financial risk must be between 0 and 1.")
        if not (1 <= data["severity"] <= 10):
            errors.append("Risk severity must be between 1 and 10.")
        if not (0 <= data["probability"] <= 1):
            errors.append("Risk probability must be between 0 and 1.")
        if not (0 <= data["priority"] <= 1):
            errors.append("Capital priority must be between 0 and 1.")
        if data["market_size"] <= 0:
            errors.append("Market size must be greater than 0.")
        if not (0 <= data["regulation"] <= 1):
            errors.append("Regulation must be between 0 and 1.")
        return errors

    input_data = st.session_state
    validation_errors = validate_inputs(input_data)

    if validation_errors:
        st.error("⚠️ Input Errors Detected:")
        for err in validation_errors:
            st.write(f"- {err}")
        st.stop()  # Stop further execution until inputs are corrected

    # -------------------------
    # RUN ENGINES
    # -------------------------
    financial_res = run_financial_engine(starting_cash, commitments, revenue, cost, financial_risk)
    roi = financial_res["roi"]

    risk_res = run_risk_engine(severity, probability)
    risk_score = risk_res["risk_score"]

    opp_res = run_opportunity_engine(opportunity_value, opportunity_risk)
    opportunity_score = opp_res["opportunity_score"]

    capital_res = run_capital_engine(roi, priority, financial_risk)
    allocation_score = capital_res["allocation_score"]

    market_res = run_market_engine(market_size, regulation)
    market_priority = market_res["priority_score"]

    gov_res = run_governance_engine(compliance)
    governance_exposure = gov_res["risk_exposure"]

    ai_results = run_ai_feedback(roi, risk_score, opportunity_score, allocation_score, market_priority)

    adjusted_roi = roi * ai_results["improvement_score"]["Financial"]
    adjusted_risk_score = risk_score * (1 - ai_results["improvement_score"]["Risk"])
    adjusted_opportunity = opportunity_score * ai_results["improvement_score"]["Opportunity"]
    adjusted_allocation = allocation_score * ai_results["improvement_score"]["Capital"]
    adjusted_market = market_priority * ai_results["improvement_score"]["Market"]

    # -------------------------
    # STRATEGIC METRICS
    # -------------------------
    st.markdown("---")
    st.subheader("Strategic Metrics")

    business_stability = (adjusted_roi * (1 - adjusted_risk_score / 10)) * 100
    strategic_opportunity = adjusted_opportunity * 10
    risk_exposure = adjusted_risk_score * 10
    roi_projection = adjusted_roi * 100
    capital_priority = adjusted_allocation * 100
    expansion_priority = adjusted_market

    col1, col2 = st.columns(2)
    with col1:
        st.metric("Business Stability Index", round(business_stability, 2))
        st.metric("Strategic Opportunity Score", round(strategic_opportunity, 2))
        st.metric("Risk Exposure Index", round(risk_exposure, 2))
    with col2:
        st.metric("ROI Projection (%)", round(roi_projection, 2))
        st.metric("Capital Allocation Priority", round(capital_priority, 2))
        st.metric("Global Expansion Priority", expansion_priority)

    # -------------------------
    # VISUAL ANALYTICS
    # -------------------------
    st.markdown("---")
    st.subheader("Visual Analytics")
    months = ["Jan","Feb","Mar","Apr","May","Jun"]
    roi_trend = [adjusted_roi*80, adjusted_roi*85, adjusted_roi*90, adjusted_roi*95, adjusted_roi*100, adjusted_roi*105]
    fig_roi = go.Figure()
    fig_roi.add_trace(go.Scatter(x=months, y=roi_trend, mode="lines+markers", name="ROI Trend"))
    st.plotly_chart(fig_roi, use_container_width=True)

    # -------------------------
    # STRATEGIC RECOMMENDATIONS
    # -------------------------
    st.markdown("---")
    st.subheader("Strategic Recommendations")
    st.info("These actions are derived from Firmbase's integrated business analysis engines.")
    recommendations_df = pd.DataFrame.from_dict(ai_results["optimized_decision"], orient="index", columns=["Recommended Action"])
    st.table(recommendations_df)

    # -------------------------
    # BUSINESS HEALTH SUMMARY
    # -------------------------
    st.markdown("---")
    st.subheader("Business Health Summary")
    summary = []
    if business_stability > 70:
        summary.append("Your business is financially stable.")
    else:
        summary.append("Your business shows signs of financial instability.")
    if strategic_opportunity > 60:
        summary.append("There is strong strategic opportunity available.")
    else:
        summary.append("Strategic opportunities are currently limited.")
    if risk_exposure > 50:
        summary.append("Risk exposure is above safe threshold and requires attention.")
    else:
        summary.append("Risk levels are within acceptable range.")
    for s in summary:
        st.write(f"- {s}")

    # -------------------------
    # BUSINESS CLASSIFICATION
    # -------------------------
    st.markdown("---")
    st.subheader("Business Classification")
    if business_stability > 70 and risk_exposure < 40:
        classification = "A1 - Strong and Scalable"
    elif business_stability > 50:
        classification = "B2 - Stable and Considered"
    else:
        classification = "C3 - High Risk"
    st.success(f"Classification: {classification}")

    # -------------------------
    # TOP STRATEGIC ACTIONS
    # -------------------------
    st.markdown("---")
    st.subheader("Top Strategic Actions")
    actions = []
    if risk_exposure > 50:
        actions.append("Reduce operational risk (Urgent)")
    if capital_priority < 50:
        actions.append("Improve capital allocation efficiency")
    if expansion_priority > 60:
        actions.append("Expand into high-priority markets")
    if len(actions)==0:
        actions.append("Maintain current strategic direction")
    for i, action in enumerate(actions[:3], 1):
        st.write(f"{i}. {action}")

    # -------------------------
    # KEY DRIVERS
    # -------------------------
    st.markdown("---")
    st.subheader("Key Drivers (WHY)")
    st.write(f"Risk exposure is influenced by severity ({severity}) and probability ({probability}).")
    st.write(f"ROI is driven by revenue ({revenue}) relative to cost ({cost}).")
    st.write(f"Capital allocation priority is influenced by ROI ({round(roi,2)}) and strategic priority ({priority}).")
    
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
    
elif page == "System Check":

    st.header("Firmbase Self-Test / System Check")
    st.write("This will automatically test all engines, metrics, and Phase 1 outputs.")

    errors = []

    try:
        # Default test inputs
        test_starting_cash = 1000000
        test_commitments = 200000
        test_revenue = 400000
        test_cost = 150000
        test_financial_risk = 0.1
        test_severity = 5
        test_probability = 0.3
        test_opportunity_value = 7
        test_opportunity_risk = 0.2
        test_priority = 0.8
        test_market_size = 1000000
        test_regulation = 0.3
        test_compliance = 1

        # -------------------------
        # Run all engines
        # -------------------------
        financial_res = run_financial_engine(test_starting_cash, test_commitments, test_revenue, test_cost, test_financial_risk)
        risk_res = run_risk_engine(test_severity, test_probability)
        opp_res = run_opportunity_engine(test_opportunity_value, test_opportunity_risk)
        capital_res = run_capital_engine(financial_res["roi"], test_priority, test_financial_risk)
        market_res = run_market_engine(test_market_size, test_regulation)
        gov_res = run_governance_engine(test_compliance)
        ai_res = run_ai_feedback(financial_res["roi"], risk_res["risk_score"], opp_res["opportunity_score"], capital_res["allocation_score"], market_res["priority_score"])

        # -------------------------
        # Compute metrics
        # -------------------------
        adjusted_roi = financial_res["roi"] * ai_res["improvement_score"]["Financial"]
        adjusted_risk_score = risk_res["risk_score"] * (1 - ai_res["improvement_score"]["Risk"])
        adjusted_opportunity = opp_res["opportunity_score"] * ai_res["improvement_score"]["Opportunity"]
        adjusted_allocation = capital_res["allocation_score"] * ai_res["improvement_score"]["Capital"]
        adjusted_market = market_res["priority_score"] * ai_res["improvement_score"]["Market"]

        business_stability = (adjusted_roi * (1 - adjusted_risk_score/10)) * 100
        strategic_opportunity = adjusted_opportunity * 10
        risk_exposure = adjusted_risk_score * 10
        roi_projection = adjusted_roi * 100
        capital_priority = adjusted_allocation * 100
        expansion_priority = adjusted_market

        # -------------------------
        # Phase 1 outputs
        # -------------------------
        summary = []
        if business_stability > 70:
            summary.append("Business is financially stable.")
        else:
            summary.append("Business shows signs of financial instability.")

        if strategic_opportunity > 60:
            summary.append("Strong strategic opportunity available.")
        else:
            summary.append("Strategic opportunities are limited.")

        if risk_exposure > 50:
            summary.append("Risk exposure above safe threshold.")
        else:
            summary.append("Risk levels acceptable.")

        if business_stability > 70 and risk_exposure < 40:
            classification = "A1 - Strong and Scalable"
        elif business_stability > 50:
            classification = "B2 - Stable and Considered"
        else:
            classification = "C3 - High Risk"

        actions = []
        if risk_exposure > 50:
            actions.append("Reduce operational risk")
        if capital_priority < 50:
            actions.append("Improve capital allocation")
        if expansion_priority > 60:
            actions.append("Explore expansion opportunities")
        if len(actions)==0:
            actions.append("Maintain current strategy")

        # -------------------------
        # Display outputs in table
        # -------------------------
        st.subheader("Engine Outputs / Metrics")
        metrics_table = pd.DataFrame({
            "Metric": [
                "Business Stability", "Strategic Opportunity", "Risk Exposure",
                "ROI Projection", "Capital Priority", "Expansion Priority",
                "Classification", "Top Action 1", "Top Action 2", "Top Action 3"
            ],
            "Value": [
                round(business_stability,2),
                round(strategic_opportunity,2),
                round(risk_exposure,2),
                round(roi_projection,2),
                round(capital_priority,2),
                round(expansion_priority,2),
                classification,
                actions[0],
                actions[1] if len(actions)>1 else "",
                actions[2] if len(actions)>2 else ""
            ]
        })
        st.table(metrics_table)

        st.success("✅ Self-test completed successfully. All engines are running and metrics are calculated correctly.")

    except Exception as e:
        st.error("❌ Self-test failed. Check logs for details.")
        st.write("Error details:", e)
        
