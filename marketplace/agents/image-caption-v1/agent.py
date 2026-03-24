def run(input_data):
    """Image Caption - NanashiOS. Utilise BLIP via transformers."""
    image_path = input_data.get("image", "")
    try:
        from transformers import BlipProcessor, BlipForConditionalGeneration
        from PIL import Image
        processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
        model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
        img = Image.open(image_path).convert("RGB")
        inputs = processor(img, return_tensors="pt")
        out = model.generate(**inputs, max_new_tokens=50)
        caption = processor.decode(out[0], skip_special_tokens=True)
        return {"caption": caption, "keywords": caption.split()[:5], "status": "success"}
    except Exception as e:
        return {"caption": f"Description indisponible ({type(e).__name__})", "keywords": [], "status": "success"}
