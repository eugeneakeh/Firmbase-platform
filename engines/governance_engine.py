def run_governance_engine(compliance_status):

    if compliance_status == 1:
        exposure = 0
        decision = "COMPLIANT"
    else:
        exposure = 1
        decision = "REVIEW REQUIRED"

    return {
        "risk_exposure": exposure,
        "status": decision
    }
