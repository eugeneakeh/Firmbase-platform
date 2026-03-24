class InputSchema:
    REQUIRED_FIELDS = ["revenue", "cost"]


def validate_inputs(inputs: dict):
    if not isinstance(inputs, dict):
        raise TypeError("Inputs must be a dictionary")

    for field in InputSchema.REQUIRED_FIELDS:
        if field not in inputs:
            raise ValueError(f"Missing required input: {field}")

    if inputs["revenue"] < 0 or inputs["cost"] < 0:
        raise ValueError("Revenue and cost must be non-negative")

    return True
