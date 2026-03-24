def run(input_data):
    """Collaborative Learning - NanashiOS. Fusion locale de connaissances."""
    local_knowledge = input_data.get("local_knowledge", [])
    shared_knowledge = input_data.get("shared_knowledge", [])
    merged = list({str(k): k for k in (local_knowledge + shared_knowledge)}.values())
    new_knowledge = [k for k in shared_knowledge if k not in local_knowledge]
    return {"merged_knowledge": merged, "new_entries": new_knowledge,
            "total_entries": len(merged), "status": "success"}
