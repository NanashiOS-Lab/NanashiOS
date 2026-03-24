def run(input_data):
    """Ethical Reasoner - NanashiOS. Analyse éthique par règles + LLM optionnel."""
    query = input_data.get("query", "")
    RED_FLAGS = ["tuer","tromper","voler","hacker","exploiter","nuire","espionner","manipuler"]
    GREEN_FLAGS = ["aider","soigner","éduquer","protéger","partager","créer","améliorer"]
    text = query.lower()
    red = sum(1 for w in RED_FLAGS if w in text)
    green = sum(1 for w in GREEN_FLAGS if w in text)
    if red > green:
        verdict = "Refusé"
        score = round(max(0.1, 0.4 - 0.1*red), 2)
        reasoning = f"L'action contient {red} indicateur(s) éthiquement problématique(s)."
    elif green > 0:
        verdict = "Accepté"
        score = round(min(0.99, 0.7 + 0.05*green), 2)
        reasoning = "Action à vocation positive sous réserve de consentement éclairé."
    else:
        verdict = "Neutre"
        score = 0.60
        reasoning = "Aucun indicateur négatif ni positif clair. Contexte à préciser."
    return {"verdict": verdict, "ethics_score": score, "reasoning": reasoning, "status": "success"}
