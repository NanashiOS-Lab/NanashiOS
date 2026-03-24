def run(input_data):
    """Dream Analyzer - NanashiOS. Analyse les rêves par NLP."""
    dream_log = input_data.get("dream_log", "").lower()
    SYMBOLS = {
        "eau": ("Émotions, inconscient, purification", 0.75),
        "voler": ("Liberté, désir d'évasion ou d'élévation", 0.70),
        "chute": ("Anxiété, perte de contrôle", 0.45),
        "poursuite": ("Stress, fuite d'un problème", 0.40),
        "maison": ("Soi, famille, sécurité intérieure", 0.80),
        "mort": ("Transformation, fin d'un cycle", 0.65),
        "enfant": ("Innocence, créativité, nouveau projet", 0.78),
        "serpent": ("Peur, trahison ou sagesse selon contexte", 0.60),
        "feu": ("Passion, colère ou purification", 0.65),
        "forêt": ("Inconnu, exploration intérieure", 0.70),
    }
    found = [(sym, interp, q) for sym, (interp, q) in SYMBOLS.items() if sym in dream_log]
    if found:
        main_symbol, interp, quality = found[0]
        interpretation = f"Symbole principal '{main_symbol}' : {interp}."
        if len(found) > 1:
            others = ", ".join(f"'{s}'" for s, _, _ in found[1:])
            interpretation += f" Symboles secondaires : {others}."
        sleep_quality = round(sum(q for _, _, q in found) / len(found), 2)
    else:
        interpretation = "Rêve neutre ou positif. Aucun symbole archétypal majeur détecté."
        sleep_quality = 0.78
    return {"interpretation": interpretation, "symbols_found": [s for s, _, _ in found],
            "sleep_quality": sleep_quality, "status": "success"}
