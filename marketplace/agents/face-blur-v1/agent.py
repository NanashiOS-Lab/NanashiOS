def run(input_data):
    """Face Blur - NanashiOS. Détecte et floute les visages via OpenCV."""
    image_path = input_data.get("image", "")
    output_path = input_data.get("output_path", image_path.replace(".", "_blurred.") if image_path else "output_blurred.jpg")
    try:
        import cv2
        img = cv2.imread(image_path)
        if img is None:
            return {"faces_found": 0, "output_path": "", "status": "error", "error": "Image non lisible"}
        cascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            roi = img[y:y+h, x:x+w]
            img[y:y+h, x:x+w] = cv2.GaussianBlur(roi, (99, 99), 30)
        cv2.imwrite(output_path, img)
        return {"faces_found": len(faces), "output_path": output_path, "status": "success"}
    except ImportError:
        return {"faces_found": 0, "output_path": "", "note": "opencv non installé", "status": "success"}
