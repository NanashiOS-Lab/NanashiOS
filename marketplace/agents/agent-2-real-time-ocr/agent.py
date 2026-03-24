def run(input_data):
    """Real-Time OCR - NanashiOS. Utilise pytesseract si dispo."""
    image_path = input_data.get("image", "")
    lang = input_data.get("lang", "fra+eng")
    try:
        import pytesseract
        from PIL import Image
        img = Image.open(image_path)
        text = pytesseract.image_to_string(img, lang=lang).strip()
        return {"text": text, "word_count": len(text.split()), "status": "success"}
    except ImportError:
        return {"text": "(pytesseract non installé)", "word_count": 0, "status": "success"}
    except Exception as e:
        return {"text": "", "word_count": 0, "error": str(e), "status": "error"}
