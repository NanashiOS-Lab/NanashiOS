def run(input_data):
    """Sentiment Analysis Agent - NanashiOS"""
    text = input_data.get("text", "").lower()

    positive_words = ["bien", "super", "excellent", "bon", "parfait", "great", "good", "love", "génial", "bravo"]
    negative_words = ["mal", "mauvais", "terrible", "nul", "bad", "hate", "awful", "horrible", "catastrophe", "raté"]

    pos = sum(1 for w in positive_words if w in text)
    neg = sum(1 for w in negative_words if w in text)

    if pos > neg:
        sentiment, score = "positif", round(min(0.6 + 0.08 * pos, 0.99), 2)
    elif neg > pos:
        sentiment, score = "négatif", round(min(0.6 + 0.08 * neg, 0.99), 2)
    else:
        sentiment, score = "neutre", 0.55

    return {"sentiment": sentiment, "score": score, "status": "success"}
