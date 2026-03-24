def run(input_data):
    """Behavioral Auth - NanashiOS. Authentification par comportement."""
    import math
    behavior_data = input_data.get("behavior_data", {})
    profile = input_data.get("stored_profile", {})
    typing_speed = float(behavior_data.get("typing_speed", 0))
    consistency = float(behavior_data.get("consistency", 0.5))
    error_rate = float(behavior_data.get("error_rate", 0.1))
    session_duration = float(behavior_data.get("session_duration_s", 0))
    score = 0.0
    if profile:
        ref_speed = float(profile.get("avg_typing_speed", 50))
        speed_diff = abs(typing_speed - ref_speed) / max(ref_speed, 1)
        score += max(0, 0.4 * (1 - speed_diff))
        score += 0.3 * consistency
        score += 0.2 * (1 - error_rate)
        if session_duration > 5: score += 0.1
    else:
        score = 0.88 if (typing_speed > 40 and consistency > 0.75) else 0.45
    confidence = round(min(max(score, 0.0), 0.99), 2)
    return {"authenticated": confidence > 0.65, "confidence": confidence,
            "behavior_score": confidence, "status": "success"}
