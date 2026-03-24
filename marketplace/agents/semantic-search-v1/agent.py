def run(input_data):
    """Semantic Search - NanashiOS. Utilise sentence-transformers si dispo."""
    query = input_data.get("query", "")
    corpus = input_data.get("corpus", [])
    top_k = int(input_data.get("top_k", 5))
    if not corpus or not query:
        return {"results": [], "top_result": "", "status": "success"}
    try:
        from sentence_transformers import SentenceTransformer, util
        model = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")
        q_emb = model.encode(query, convert_to_tensor=True)
        c_emb = model.encode(corpus, convert_to_tensor=True)
        scores = util.cos_sim(q_emb, c_emb)[0].tolist()
        ranked = sorted(zip(corpus, scores), key=lambda x: x[1], reverse=True)[:top_k]
        results = [{"document": d, "score": round(s, 3)} for d, s in ranked]
        return {"results": results, "top_result": results[0]["document"] if results else "", "status": "success"}
    except ImportError:
        q_words = set(query.lower().split())
        scored = [{"document": d, "score": round(len(q_words & set(d.lower().split())) / max(len(q_words),1), 3)} for d in corpus]
        scored.sort(key=lambda x: x["score"], reverse=True)
        return {"results": scored[:top_k], "top_result": scored[0]["document"] if scored else "", "status": "success"}
