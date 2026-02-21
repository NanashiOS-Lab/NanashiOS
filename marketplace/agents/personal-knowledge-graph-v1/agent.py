def run(input_data):
    """
    Personal-Knowledge-Graph-v1 - NanashiOS
    Gère un graphe de connaissances personnel local
    """
    query = input_data.get("query", "")
    action = input_data.get("action", "query")

    if action == "add":
        response = f"Information ajoutée au graphe : {query}"
    elif action == "update":
        response = f"Information mise à jour dans le graphe : {query}"
    else:
        response = f"Réponse à la requête : {query} (simulation de recherche dans le graphe personnel)"

    related_nodes = ["NanashiOS", "Souveraineté", "Privacy"]

    return {
        "response": response,
        "related_nodes": related_nodes,
        "status": "success"
    }
