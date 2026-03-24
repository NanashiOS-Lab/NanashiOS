def run(input_data):
    """Coordinateur Multi-Agents - NanashiOS"""
    task = input_data.get("task", "")
    available_agents = input_data.get("available_agents", [])

    plan = f"Plan de coordination pour : {task}\n"
    assignment = {}
    for i, agent in enumerate(available_agents):
        assignment[agent] = f"Sous-tâche {i + 1} : {task}"
        plan += f"  → {agent} : {assignment[agent]}\n"

    return {
        "coordination_plan": plan,
        "task_assignment": assignment,
        "status": "en cours",
        "status_code": "success"
    }
