def run(input_data):
    """Fake News Detector - NanashiOS. Heuristique + transformers si dispo."""
    text = input_data.get("text", "")
    if not text.strip():
        return {"is_fake": False, "confidence": 0.5, "status": "success"}
    try:
        from transformers import pipeline
        clf = pipeline("text-classification", model="mrm8488/bert-tiny-finetuned-fake-news-detection", device=-1)
        result = clf(text[:512])[0]
        is_fake = result["label"].upper() == "FAKE"
        return {"is_fake": is_fake, "confidence": round(result["score"], 3), "status": "success"}
    except Exception:
        SENSATIONAL = ["choc","incroyable","révélation","secret","scandale","complot","exclusif","urgent"]
        score = sum(1 for w in SENSATIONAL if w in text.lower()) / len(SENSATIONAL)
        return {"is_fake": score > 0.3, "confidence": round(min(score + 0.4, 0.99), 2), "status": "success"}
