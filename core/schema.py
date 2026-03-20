from typing import Dict, Any


def build_response(
    score: float,
    label: str,
    insight: str,
    metrics: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Standard response format for all engines in Firmbase.
    Ensures consistency across the system.
    """

    return {
        "score": round(score, 2),
        "label": label,
        "insight": insight,
        "metrics": metrics
    }
