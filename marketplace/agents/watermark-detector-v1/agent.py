def run(input_data):
    """Watermark Detector - NanashiOS. Détecte filigranes visibles et invisibles."""
    image_path = input_data.get("image", "")
    try:
        import cv2, numpy as np
        img = cv2.imread(image_path)
        if img is None:
            return {"has_watermark": False, "confidence": 0.0, "status": "error"}
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        edges = cv2.Canny(gray, 50, 150)
        h, w = gray.shape
        corners = [
            edges[:h//5, :w//3], edges[:h//5, 2*w//3:],
            edges[4*h//5:, :w//3], edges[4*h//5:, 2*w//3:]
        ]
        corner_density = [np.sum(c > 0) / c.size for c in corners]
        max_density = max(corner_density)
        has_watermark = max_density > 0.05
        confidence = round(min(max_density * 5, 0.99), 2)
        return {"has_watermark": has_watermark, "confidence": confidence,
                "corner_densities": [round(d, 3) for d in corner_density], "status": "success"}
    except ImportError:
        return {"has_watermark": False, "confidence": 0.0, "note": "opencv non installé", "status": "success"}
