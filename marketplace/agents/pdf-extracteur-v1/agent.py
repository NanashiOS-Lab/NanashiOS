def run(input_data):
    """PDF Extracteur - NanashiOS. Extrait le texte d'un PDF via PyMuPDF ou pdfminer."""
    import os
    pdf_path = input_data.get("pdf_path", "")
    max_pages = int(input_data.get("max_pages", 0))
    if not pdf_path or not os.path.exists(pdf_path):
        return {"text": "", "pages": 0, "status": "error", "error": "Fichier PDF introuvable"}
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf_path)
        pages = len(doc)
        limit = max_pages if max_pages else pages
        text = "\n\n".join(doc[i].get_text() for i in range(min(limit, pages)))
        doc.close()
        return {"text": text.strip(), "pages": pages, "chars": len(text), "status": "success"}
    except ImportError:
        pass
    try:
        from pdfminer.high_level import extract_text
        text = extract_text(pdf_path)
        return {"text": text.strip(), "pages": 0, "chars": len(text), "status": "success"}
    except ImportError:
        return {"text": "", "pages": 0, "status": "error", "error": "PyMuPDF ou pdfminer.six requis"}
