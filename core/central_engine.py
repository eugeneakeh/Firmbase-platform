def aggregate_results(results: dict):
    scores = []

    for engine, output in results.items():
        if isinstance(output, dict) and "score" in output:
            scores.append(output["score"])

    overall_score = sum(scores) / len(scores) if scores else 0

    return {
        "results": results,
        "overall_score": round(overall_score, 2),
        "system_health": "Strong" if overall_score > 70 else "Moderate" if overall_score > 40 else "Weak"
    }
