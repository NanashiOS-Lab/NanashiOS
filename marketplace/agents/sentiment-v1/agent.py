def run(input_data):
    """Sentiment Analysis - NanashiOS. Utilise transformers si dispo."""
    text = input_data.get("text", "")
    if not text.strip():
        return {"sentiment": "neutre", "score": 0.5, "status": "success"}
    try:
        from transformers import pipeline
        clf = pipeline("sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment", device=-1)
        result = clf(text[:512])[0]
        label = result["label"]
        score = round(result["score"], 3)
        stars = int(label.split()[0])
        sentiment = "positif" if stars >= 4 else ("négatif" if stars <= 2 else "neutre")
        return {"sentiment": sentiment, "score": score, "status": "success"}
    except ImportError:
        pos = sum(1 for w in ["bien","super","bon","excellent","parfait","great","good"] if w in text.lower())
        neg = sum(1 for w in ["mal","mauvais","terrible","nul","bad","hate","awful"] if w in text.lower())
        if pos > neg: return {"sentiment": "positif", "score": round(min(0.6+0.08*pos,0.99),2), "status": "success"}
        elif neg > pos: return {"sentiment": "négatif", "score": round(min(0.6+0.08*neg,0.99),2), "status": "success"}
        return {"sentiment": "neutre", "score": 0.55, "status": "success"}
