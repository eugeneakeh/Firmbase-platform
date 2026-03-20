from core.central_engine import run_central_engine


def run_firmbase(inputs: dict):
    """
    Orchestrator layer:
    - Validates inputs
    - Cleans data
    - Runs central engine
    - Enhances output (future AI layer ready)
    """

    # ---- INPUT VALIDATION ----
    validated_inputs = validate_inputs(inputs)

    # ---- RUN CORE SYSTEM ----
    result = run_central_engine(validated_inputs)

    # ---- POST PROCESSING ----
    enhanced_result = enhance_output(result)

    return enhanced_result


def validate_inputs(inputs: dict):
    """
    Ensures safe numeric inputs for all engines
    """

    safe_inputs = {}

    # Required numeric fields with fallback defaults
    safe_inputs["revenue"] = max(float(inputs.get("revenue", 0)), 0)
    safe_inputs["cost"] = max(float(inputs.get("cost", 0)), 0)
    safe_inputs["debt"] = max(float(inputs.get("debt", 0)), 0)
    safe_inputs["capital"] = max(float(inputs.get("capital", 0)), 0)

    # Optional advanced fields
    safe_inputs["growth_rate"] = float(inputs.get("growth_rate", 0))
    safe_inputs["market_size"] = float(inputs.get("market_size", 0))

    return safe_inputs


def enhance_output(result: dict):
    """
    Future AI layer hook (recommendations, insights, feedback)
    """

    score = result["overall_score"]

    if score >= 75:
        recommendation = "Business is strong. Focus on scaling and expansion."
    elif score >= 50:
        recommendation = "Business is stable. Optimize weak areas before scaling."
    else:
        recommendation = "High risk detected. Prioritize financial stabilization."

    result["recommendation"] = recommendation

    return result
