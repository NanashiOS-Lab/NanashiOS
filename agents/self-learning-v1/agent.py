def run(input_data):
    """
    Self-Learning-v1 - NanashiOS
    Apprend de nouvelles tâches à partir d’exemples
    """
    task_example = input_data.get("task_example", "")
    user_feedback = input_data.get("user_feedback", "positif")

    # Simulation simple (à remplacer par vrai apprentissage plus tard)
    if "positif" in user_feedback.lower():
        learned_behavior = f"Tâche apprise avec succès : {task_example}"
        confidence = 0.85
    else:
        learned_behavior = f"Tâche révisée suite à feedback négatif : {task_example}"
        confidence = 0.65

    return {
        "learned_behavior": learned_behavior,
        "confidence": confidence,
        "status": "success"
    }
