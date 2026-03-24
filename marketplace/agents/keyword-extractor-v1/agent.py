def run(input_data):
    """Keyword Extractor - NanashiOS. Utilise RAKE ou TF-IDF."""
    text = input_data.get("text", "")
    max_kw = int(input_data.get("max_keywords", 8))
    if not text.strip():
        return {"keywords": [], "status": "success"}
    try:
        from rake_nltk import Rake
        import nltk; nltk.download("stopwords", quiet=True); nltk.download("punkt", quiet=True)
        r = Rake()
        r.extract_keywords_from_text(text)
        keywords = r.get_ranked_phrases()[:max_kw]
        return {"keywords": keywords, "status": "success"}
    except ImportError:
        import re
        stopwords = {"le","la","les","de","du","des","un","une","en","et","à","au","aux","ce","qui","que","se"}
        words = [w.lower() for w in re.findall(r"\b[a-zA-ZÀ-ÿ]{4,}\b", text)]
        freq = {}
        for w in words:
            if w not in stopwords: freq[w] = freq.get(w, 0) + 1
        keywords = sorted(freq, key=freq.get, reverse=True)[:max_kw]
        return {"keywords": keywords, "status": "success"}
