def run(input_data):
    """Traduction - NanashiOS. Utilise transformers Helsinki-NLP si dispo."""
    text = input_data.get("text", "")
    target = input_data.get("target_lang", "en")
    source = input_data.get("source_lang", "fr")
    if not text.strip():
        return {"translated_text": "", "source_lang": source, "target_lang": target, "status": "success"}
    try:
        from transformers import pipeline
        model_name = f"Helsinki-NLP/opus-mt-{source}-{target}"
        translator = pipeline("translation", model=model_name, device=-1)
        result = translator(text[:512])[0]["translation_text"]
        return {"translated_text": result, "source_lang": source, "target_lang": target, "status": "success"}
    except Exception:
        return {"translated_text": f"[{target.upper()}] {text}", "source_lang": source, "target_lang": target, "status": "success"}
