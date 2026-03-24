def run(input_data):
    """Pulse Logic - NanashiOS. Raisonnement logique formel."""
    premises = input_data.get("premises", [])
    question = input_data.get("question", "")
    RULES = {
        ("est un animal", "a des pattes"): "a la capacité de se déplacer",
        ("est humain", "peut apprendre"): "peut s'améliorer avec l'expérience",
        ("contient des données", "est local"): "est souverain et privé",
    }
    facts = set(p.lower() for p in premises)
    conclusions = []
    for (cond1, cond2), conclusion in RULES.items():
        if any(cond1 in f for f in facts) and any(cond2 in f for f in facts):
            conclusions.append(conclusion)
    if question and conclusions:
        answer = f"Oui, car : {conclusions[0]}" if any(w in question.lower() for w in ["peut","est","a-t-il"]) else conclusions[0]
    elif question:
        answer = "Insuffisamment de prémisses pour conclure."
    else:
        answer = "Aucune question posée."
    return {"conclusions": conclusions, "answer": answer, "premises_count": len(premises), "status": "success"}
