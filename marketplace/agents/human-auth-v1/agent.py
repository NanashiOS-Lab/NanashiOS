def run(input_data):
    """Human Authenticity - NanashiOS. Détecte écriture humaine vs IA."""
    text = input_data.get("text", "")
    if not text.strip():
        return {"is_human": True, "confidence": 0.5, "status": "success"}
    words = text.split()
    avg_len = sum(len(w) for w in words) / max(len(words), 1)
    sentences = [s for s in text.split(".") if s.strip()]
    avg_sent_len = sum(len(s.split()) for s in sentences) / max(len(sentences), 1)
    typos = sum(1 for w in words if w != w.lower() and not w[0].isupper())
    human_score = 0.5
    if 4 < avg_len < 7: human_score += 0.15
    if 8 < avg_sent_len < 20: human_score += 0.15
    if typos > 0: human_score += 0.10
    if any(c in text for c in ["...", "!", "?!", ";"]): human_score += 0.10
    human_score = round(min(human_score, 0.98), 2)
    return {"is_human": human_score > 0.55, "confidence": human_score, "status": "success"}
