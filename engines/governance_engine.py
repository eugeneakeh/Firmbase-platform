def run_governance_engine(inputs):
    structure = inputs.get("team_structure", 5)

    score = min(100, structure * 10)

    return {
        "team_structure": structure,
        "score": score
    }
