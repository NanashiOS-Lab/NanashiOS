def run(input_data):
    """
    Détection-Émotion-v1 - NanashiOS
    Détecte les émotions dans un texte ou audio
    """
    text = input_data.get("input", "").lower()

    # Simulation simple (à remplacer par un vrai modèle plus tard)
    if any(word in text for word in ["joie", "heureux", "content", "happy"]):
        emotion = "Joie"
        confidence = 0.85
    elif any(word in text for word in ["colère", "énervé", "fâché", "angry"]):
        emotion = "Colère"
        confidence = 0.80
    elif any(word in text for word in ["tristesse", "triste", "déprimé", "sad"]):
        emotion = "Tristesse"
        confidence = 0.82
    elif any(word in text for word in ["peur", "effrayé", "anxieux", "fear"]):
        emotion = "Peur"
        confidence = 0.78
    else:
        emotion = "Neutre"
        confidence = 0.65

    return {
        "emotion": emotion,
        "confidence": confidence,
        "status": "success"
    }
