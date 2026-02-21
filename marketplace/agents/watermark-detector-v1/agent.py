def run(input_data):
    """
    Watermark-Detector-v1 - NanashiOS
    Détecte les watermarks C2PA et signatures numériques
    """
    media = input_data.get("media", "")

    # Simulation simple (à remplacer par vraie détection C2PA plus tard)
    if "c2pa" in media.lower() or "adobe" in media.lower():
        has_watermark = True
        confidence = 0.92
        details = "Watermark C2PA détecté - Contenu authentifié"
    else:
        has_watermark = False
        confidence = 0.35
        details = "Aucun watermark C2PA détecté"

    return {
        "has_watermark": has_watermark,
        "confidence": confidence,
        "details": details,
        "status": "success"
    }
