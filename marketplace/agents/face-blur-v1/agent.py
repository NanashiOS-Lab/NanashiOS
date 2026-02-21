import cv2
import numpy as np

def run(input_data):
    """
    Face-Blur-v1 - NanashiOS
    Floute les visages dans une image
    """
    # Simulation simple (remplacer par vrai traitement d'image plus tard)
    image_path = input_data.get("image", "image.jpg")
    blur_strength = input_data.get("blur_strength", 5)

    # Simulation : on retourne un message au lieu de traiter l'image réelle
    faces_detected = 2  # simulation

    return {
        "blurred_image": f"Image floutée avec intensité {blur_strength} (simulation)",
        "faces_detected": faces_detected,
        "status": "success"
    }
