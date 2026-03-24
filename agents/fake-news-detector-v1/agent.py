def run(input_data):
    """
    Fake-News-Detector-v1 - NanashiOS
    Détecte les fake news et désinformation dans un texte
    """
    text = input_data.get("text", "").lower()

    # Simulation simple (à remplacer par un vrai modèle plus tard)
    if any(word in text for word in ["fake", "mensonge", "rumeur", "complot", "hoax"]):
        is_fake = True
        reliability_score = 0.25
        reasons = ["Mots suspects de désinformation détectés", "Ton sensationnaliste"]
    elif len(text) < 30:
        is_fake = False
        reliability_score = 0.6
        reasons = ["Texte trop court pour analyse fiable"]
    else:
        is_fake = False
        reliability_score = 0.78
        reasons = ["Aucun indicateur majeur de fake news"]

    return {
        "is_fake": is_fake,
        "reliability_score": reliability_score,
        "reasons": reasons,
        "status": "success"
    }
