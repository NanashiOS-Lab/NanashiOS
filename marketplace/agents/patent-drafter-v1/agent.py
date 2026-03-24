def run(input_data):
    """Patent Drafter - NanashiOS. Génère un squelette de brevet."""
    idea = input_data.get("idea", "")
    inventor = input_data.get("inventor", "NanashiOS-Lab")
    domain = input_data.get("domain", "Intelligence Artificielle")
    if not idea.strip():
        return {"patent_draft": "", "status": "success"}
    draft = f"""DEMANDE DE BREVET - NanashiOS Patent Drafter v1
═══════════════════════════════════════════════════

TITRE : {idea.upper()[:80]}

INVENTEUR(S) : {inventor}
DOMAINE TECHNIQUE : {domain}
DATE : 2026

1. CHAMP DE L'INVENTION
   La présente invention concerne {idea.lower()}.

2. ART ANTÉRIEUR
   Les solutions existantes présentent des limitations en termes de performance,
   souveraineté des données et adaptabilité locale.

3. RÉSUMÉ DE L'INVENTION
   L'invention propose une méthode et un système permettant {idea.lower()}
   de manière souveraine, locale et sans recours au cloud.

4. DESCRIPTION DÉTAILLÉE
   [À compléter par l'inventeur avec les étapes techniques précises]

5. REVENDICATIONS
   1. Système permettant {idea.lower()} caractérisé en ce qu'il opère localement.
   2. Procédé selon la revendication 1, caractérisé par l'absence de transfert de données.

6. ABRÉGÉ
   {idea}. Application locale souveraine. Inventeur : {inventor}.
"""
    return {"patent_draft": draft, "title": idea[:80], "inventor": inventor, "status": "success"}
