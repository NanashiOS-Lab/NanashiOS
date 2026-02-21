def run(input_data):
    """
    Dream-Analyzer-v1 - NanashiOS
    Analyse les rêves et la qualité du sommeil
    """
    dream_log = input_data.get("dream_log", "").lower()

    # Simulation simple (à remplacer par analyse réelle plus tard)
    if any(word in dream_log for word in ["voler", "fly", "chute", "fall"]):
        interpretation = "Rêve de liberté ou d’anxiété liée à la perte de contrôle."
        sleep_quality = 0.65
    elif "poursuite" in dream_log or "chase" in dream_log:
        interpretation = "Sentiment de pression ou de fuite dans la vie quotidienne."
        sleep_quality = 0.45
    else:
        interpretation = "Rêve neutre ou positif. Pas d’anomalie majeure détectée."
        sleep_quality = 0.80

    return {
        "interpretation": interpretation,
        "sleep_quality": sleep_quality,
        "status": "success"
    }
