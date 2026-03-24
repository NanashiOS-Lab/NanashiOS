def run(input_data):
    """Coordinateur Multi-Agents - NanashiOS."""
    task = input_data.get("task", "")
    available_agents = input_data.get("available_agents", [])
    constraints = input_data.get("constraints", "")
    if not task:
        return {"coordination_plan": "", "task_assignment": {}, "status": "success"}
    words = task.lower().split()
    assignment = {}
    plan_lines = [f"Tâche principale : {task}"]
    if constraints:
        plan_lines.append(f"Contraintes : {constraints}")
    plan_lines.append("")
    for i, agent in enumerate(available_agents):
        subtask = f"Traiter la partie '{words[i % len(words)] if words else str(i)}' de la tâche"
        assignment[agent] = subtask
        plan_lines.append(f"  [{i+1}] {agent} → {subtask}")
    return {"coordination_plan": "\n".join(plan_lines), "task_assignment": assignment,
            "agents_count": len(available_agents), "status": "en cours"}
