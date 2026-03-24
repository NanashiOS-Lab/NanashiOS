def run(input_data):
    """Knowledge Graph - NanashiOS. Graphe de connaissances local."""
    action = input_data.get("action", "add")
    graph_path = input_data.get("graph_path", "/tmp/nanashi_kg.json")
    import json, os
    graph = {"nodes": {}, "edges": []}
    if os.path.exists(graph_path):
        try:
            with open(graph_path) as f: graph = json.load(f)
        except Exception: pass
    if action == "add":
        entity = input_data.get("entity", "")
        relation = input_data.get("relation", "")
        target = input_data.get("target", "")
        if entity: graph["nodes"][entity] = graph["nodes"].get(entity, {"mentions": 0})
        if target: graph["nodes"][target] = graph["nodes"].get(target, {"mentions": 0})
        if entity and relation and target:
            graph["edges"].append({"from": entity, "relation": relation, "to": target})
            graph["nodes"][entity]["mentions"] = graph["nodes"][entity].get("mentions", 0) + 1
    elif action == "query":
        query = input_data.get("query_entity", "")
        related = [e for e in graph["edges"] if e["from"] == query or e["to"] == query]
        try:
            with open(graph_path, "w") as f: json.dump(graph, f)
        except Exception: pass
        return {"entity": query, "relations": related, "status": "success"}
    try:
        with open(graph_path, "w") as f: json.dump(graph, f)
    except Exception: pass
    return {"nodes": len(graph["nodes"]), "edges": len(graph["edges"]), "status": "success"}
