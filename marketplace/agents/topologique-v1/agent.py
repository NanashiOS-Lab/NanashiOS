def run(input_data):
    """Topology Analyzer - NanashiOS. Analyse de graphes via networkx."""
    data = input_data.get("data", {})
    nodes = data.get("nodes", [])
    edges = data.get("edges", [])
    try:
        import networkx as nx
        G = nx.DiGraph() if data.get("directed") else nx.Graph()
        G.add_nodes_from(nodes)
        G.add_edges_from([(e["from"], e["to"]) for e in edges if "from" in e and "to" in e])
        analysis = {
            "num_nodes": G.number_of_nodes(),
            "num_edges": G.number_of_edges(),
            "density": round(nx.density(G), 4),
            "is_connected": nx.is_connected(G.to_undirected()) if G.number_of_nodes() > 0 else False,
            "avg_degree": round(sum(d for _, d in G.degree()) / max(G.number_of_nodes(), 1), 2),
        }
        if G.number_of_nodes() > 0:
            centrality = nx.degree_centrality(G)
            analysis["most_central_node"] = max(centrality, key=centrality.get)
        return {"analysis": analysis, "status": "success"}
    except ImportError:
        return {"analysis": {"num_nodes": len(nodes), "num_edges": len(edges)}, "note": "networkx non installé", "status": "success"}
