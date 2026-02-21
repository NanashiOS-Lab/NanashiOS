def run(input_data):
    """
    Contract-Auditor-v1 - NanashiOS
    Audite un contrat pour détecter risques et incohérences
    """
    contract = input_data.get("contract_text", "")

    # Simulation simple (à remplacer par analyse réelle plus tard)
    if "confidential" in contract.lower() or "secret" in contract.lower():
        risk_score = 0.75
        problematic_clauses = ["Clause de confidentialité trop large", "Manque de durée"]
    else:
        risk_score = 0.35
        problematic_clauses = ["Aucune clause majeure détectée"]

    risk_report = f"Rapport d'audit : Score de risque {risk_score}. Clauses problématiques : {', '.join(problematic_clauses)}"

    return {
        "risk_report": risk_report,
        "risk_score": risk_score,
        "problematic_clauses": problematic_clauses,
        "status": "success"
    }
