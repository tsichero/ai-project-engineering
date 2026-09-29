import json
from pathlib import Path
from app.retrieval import retrieve_scored

def evaluate_cases(path: str = "evaluation/cases.json", top_k: int = 2) -> dict:
    cases = json.loads(Path(path).read_text(encoding="utf-8"))
    hits = 0
    reciprocal_rank_sum = 0.0
    reciprocal_precision_sum = 0.0
    evaluated = 0
    for case in cases:
        expected = set(case["expected_sources"])
        if not expected:
            continue
        evaluated += 1
        ranked = retrieve_scored(case["question"], top_k=top_k)
        ids = [doc.id for _, doc in ranked]
        matches = [i + 1 for i, doc_id in enumerate(ids) if doc_id in expected]
        if matches:
            hits += 1
            reciprocal_rank_sum += 1.0 / matches[0]
        reciprocal_precision_sum += sum(1 for doc_id in ids if doc_id in expected) / max(len(expected), 1)
    return {
        "cases_with_expected_sources": evaluated,
        "hit_rate_at_k": round(hits / evaluated, 4) if evaluated else 0.0,
        "mrr_at_k": round(reciprocal_rank_sum / evaluated, 4) if evaluated else 0.0,
        "mean_recall_at_k": round(reciprocal_precision_sum / evaluated, 4) if evaluated else 0.0,
        "k": top_k,
    }

if __name__ == "__main__":
    result = evaluate_cases()
    Path("evaluation/results.json").write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))
