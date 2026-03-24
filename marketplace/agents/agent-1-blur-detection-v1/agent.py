def run(input_data):
    """Blur Detection Agent v1 - NanashiOS. Alias de blur-detection-v1."""
    image_path = input_data.get("image", "")
    try:
        import cv2
        img = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
        if img is None:
            return {"blur_score": 0.0, "is_blurry": True, "status": "error"}
        variance = cv2.Laplacian(img, cv2.CV_64F).var()
        blur_score = round(max(0.0, 1.0 - variance / 100.0), 3)
        return {"blur_score": blur_score, "is_blurry": blur_score > 0.5, "status": "success"}
    except ImportError:
        return {"blur_score": 0.2, "is_blurry": False, "note": "opencv non installé", "status": "success"}
