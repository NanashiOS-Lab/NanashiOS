def run(input_data):
    """
    Human-Auth-v1 - NanashiOS
    Détecte si un texte est humain ou généré par IA
    """
    text = input_data.get("text", "")

    # Simulation simple (à remplacer par un vrai modèle plus tard)
    if len(text) < 50:
        authenticity = "Incertain"
        score = 0.5
    elif "IA" in text or "GPT" in text or "ChatGPT" in text:
        authenticity = "IA"
        score = 0.2
    else:
        authenticity = "Humain"
        score = 0.85

    return {
        "authenticity": authenticity,
        "score": score,
        "status": "success"
    }
