def run(input_data):
    """Self Learning - NanashiOS. Apprentissage incrémental local."""
    import json, os, hashlib
    observation = input_data.get("observation", "")
    feedback = input_data.get("feedback", "")
    knowledge_path = input_data.get("knowledge_path", "/tmp/nanashi_knowledge.json")
    knowledge = {}
    if os.path.exists(knowledge_path):
        try:
            with open(knowledge_path) as f: knowledge = json.load(f)
        except Exception: knowledge = {}
    if observation:
        key = hashlib.md5(observation.encode()).hexdigest()[:8]
        knowledge[key] = {"observation": observation, "feedback": feedback, "count": knowledge.get(key, {}).get("count", 0) + 1}
    try:
        with open(knowledge_path, "w") as f: json.dump(knowledge, f)
        persisted = True
    except Exception: persisted = False
    return {"entries_learned": len(knowledge), "last_entry": observation[:100],
            "persisted": persisted, "status": "success"}
