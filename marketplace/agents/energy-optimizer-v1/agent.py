def run(input_data):
    """Energy Optimizer - NanashiOS. Optimise la consommation énergétique."""
    workload = input_data.get("workload", {})
    constraints = input_data.get("constraints", {})
    cpu_usage = float(workload.get("cpu_usage", 0.5))
    memory_usage = float(workload.get("memory_usage", 0.5))
    gpu_usage = float(workload.get("gpu_usage", 0.0))
    max_power = float(constraints.get("max_power_watts", 100.0))
    estimated_power = (cpu_usage * 65 + memory_usage * 10 + gpu_usage * 150)
    recommendations = []
    if cpu_usage > 0.8:
        recommendations.append("Réduire la fréquence CPU ou distribuer la charge")
    if gpu_usage > 0.7:
        recommendations.append("Utiliser la quantification des modèles (INT8/INT4)")
    if memory_usage > 0.85:
        recommendations.append("Activer le streaming des données plutôt que le chargement total")
    if not recommendations:
        recommendations.append("Consommation optimale — aucun ajustement nécessaire")
    savings = max(0.0, estimated_power - max_power)
    return {
        "estimated_power_watts": round(estimated_power, 1),
        "target_power_watts": max_power,
        "potential_savings_watts": round(savings, 1),
        "recommendations": recommendations,
        "status": "success"
    }
