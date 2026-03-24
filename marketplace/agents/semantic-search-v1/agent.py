def run(input_data):
    """Semantic Search Agent - NanashiOS"""
    query = input_data.get("query", "").lower()
    corpus = input_data.get("corpus", [])
    top_k = input_data.get("top_k", 5)

    if not corpus:
        return {"results": [], "top_result": "", "status": "success"}

    query_words = set(query.split())
    scored = []
    for doc in corpus:
        doc_words = set(doc.lower().split())
        overlap = len(query_words & doc_words)
        score = overlap / max(len(query_words | doc_words), 1)
        scored.append({"document": doc, "score": round(score, 3)})

    scored.sort(key=lambda x: x["score"], reverse=True)
    results = scored[:top_k]
    return {"results": results, "top_result": results[0]["document"] if results else "", "status": "success"}
