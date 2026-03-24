def run(input_data):
    """Résumé-Texte-v1 - NanashiOS. Utilise sumy+NLTK si dispo, sinon heuristique."""
    text = input_data.get("text", "")
    max_sentences = int(input_data.get("max_sentences", 5))
    if not text.strip():
        return {"summary": "", "key_points": [], "status": "success"}
    try:
        from sumy.parsers.plaintext import PlaintextParser
        from sumy.nlp.tokenizers import Tokenizer
        from sumy.summarizers.lsa import LsaSummarizer
        import nltk; nltk.download("punkt", quiet=True); nltk.download("punkt_tab", quiet=True)
        parser = PlaintextParser.from_string(text, Tokenizer("french"))
        sents = [str(s) for s in LsaSummarizer()(parser.document, max_sentences)]
        return {"summary": " ".join(sents), "key_points": sents[:3], "status": "success"}
    except ImportError:
        raw = [s.strip() for s in text.replace("\n", " ").split(".") if s.strip()]
        sents = raw[:max_sentences]
        return {"summary": ". ".join(sents) + ".", "key_points": raw[:3], "status": "success"}
