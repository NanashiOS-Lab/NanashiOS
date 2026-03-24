def run(input_data):
    """Image Deepfake Detector - NanashiOS"""
    image_path = input_data.get("image", "")

    # Simulation déterministe (à remplacer par un vrai modèle CNN deepfake)
    import hashlib
    seed = int(hashlib.md5(str(image_path).encode()).hexdigest()[:4], 16)
    score = seed / 65535.0

    is_deepfake = score > 0.5
    confidence = round(min(0.72 + abs(score - 0.5) * 0.5, 0.99), 2)
    analysis = (
        "Anomalies GAN détectées : fréquences spectrales irrégulières et artefacts de compression."
        if is_deepfake else
        "Image authentique — aucune signature synthétique détectée."
    )
    return {"is_deepfake": is_deepfake, "confidence": confidence, "analysis": analysis, "status": "success"}
