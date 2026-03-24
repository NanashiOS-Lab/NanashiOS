def run(input_data):
    """Prompt Optimizer - NanashiOS. Améliore un prompt pour LLM ou génération image."""
    prompt = input_data.get("prompt", "")
    mode = input_data.get("mode", "llm")
    if not prompt.strip():
        return {"optimized_prompt": "", "improvements": [], "status": "success"}
    improvements = []
    optimized = prompt.strip()
    if len(optimized) < 20:
        optimized = f"Décris en détail et de manière précise : {optimized}"
        improvements.append("Ajout d'une directive de détail")
    if mode == "image" and not any(w in optimized.lower() for w in ["style","qualité","résolution","réaliste","4k","hd"]):
        optimized += ", style photographique réaliste, haute résolution, éclairage cinématographique"
        improvements.append("Ajout de qualificateurs visuels pour image")
    if mode == "llm" and not any(w in optimized for w in ["Réponds","Explique","Liste","Génère","Décris"]):
        optimized = "Réponds de manière structurée et détaillée. " + optimized
        improvements.append("Ajout d'une directive de format de réponse")
    return {"optimized_prompt": optimized, "original_prompt": prompt, "improvements": improvements, "status": "success"}
