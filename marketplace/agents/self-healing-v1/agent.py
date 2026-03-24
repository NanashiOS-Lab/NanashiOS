def run(input_data):
    """Self Healing - NanashiOS. Analyse les logs d'erreurs et propose des corrections."""
    import re
    error_log = input_data.get("error_log", "")
    current_state = input_data.get("current_state", "unknown")
    if not error_log.strip():
        return {"diagnosis": "Aucune erreur détectée.", "fix_applied": False, "new_state": current_state, "status": "success"}
    ERROR_PATTERNS = {
        r"ImportError|ModuleNotFoundError": ("Module manquant", "pip install {module}"),
        r"NameError": ("Variable non définie", "Vérifier les imports et déclarations"),
        r"AttributeError": ("Attribut manquant sur objet", "Vérifier la classe et ses méthodes"),
        r"KeyError": ("Clé manquante dans dictionnaire", "Utiliser .get() avec valeur par défaut"),
        r"FileNotFoundError": ("Fichier introuvable", "Vérifier le chemin et les permissions"),
        r"PermissionError": ("Permission refusée", "Vérifier les droits d'accès"),
        r"ConnectionError|TimeoutError": ("Erreur réseau", "Vérifier la connexion ou utiliser le mode hors-ligne"),
        r"MemoryError": ("Mémoire insuffisante", "Réduire la taille des données ou libérer de la mémoire"),
        r"JSONDecodeError": ("JSON invalide", "Valider le JSON avec un linter"),
    }
    diagnosis = []
    fixes = []
    for pattern, (diag, fix) in ERROR_PATTERNS.items():
        if re.search(pattern, error_log, re.IGNORECASE):
            diagnosis.append(diag)
            fixes.append(fix)
    if not diagnosis:
        diagnosis = ["Erreur inconnue - analyse manuelle requise"]
        fixes = ["Consulter les logs complets"]
    return {
        "diagnosis": " | ".join(diagnosis),
        "proposed_fixes": fixes,
        "fix_applied": False,
        "new_state": "diagnosed",
        "status": "success"
    }
