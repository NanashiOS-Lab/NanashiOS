"""
Tests — Exécution des agent.py NanashiOS (sans dépendances ML)
"""
import importlib.util
import os
import sys
import pytest


def load_agent(agent_dir):
    path = os.path.join(agent_dir, "agent.py")
    spec = importlib.util.spec_from_file_location("agent", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


ROOT = os.path.dirname(os.path.dirname(__file__))
MKT_DIR = os.path.join(ROOT, "marketplace", "agents")

AGENT_INPUTS = {
    "résumé-texte-v1":            {"text": "NanashiOS est un système souverain. Il fonctionne localement. Zéro cloud."},
    "sentiment-v1":               {"text": "Ce produit est excellent, je le recommande vivement."},
    "traduction-v1":              {"text": "Bonjour le monde", "target_lang": "en"},
    "keyword-extractor-v1":       {"text": "Intelligence artificielle souveraine locale NanashiOS agents autonomes"},
    "ethical-reasoner-v1":        {"query": "Aider les personnes âgées à utiliser la technologie"},
    "fake-news-detector-v1":      {"text": "Un scandale incroyable révélé par des sources exclusives."},
    "human-auth-v1":              {"text": "Salut ! J'espère que tu vas bien... c'est un peu compliqué là."},
    "code-writer-v1":             {"task": "calculer la somme de deux nombres", "language": "python"},
    "prompt-optimizer-v1":        {"prompt": "chien", "mode": "image"},
    "semantic-search-v1":         {"query": "intelligence artificielle", "corpus": ["L'IA est partout", "Le chat dort", "NanashiOS utilise l'IA locale"]},
    "local-malware-detector-v1":  {"file_path": os.path.join(ROOT, "main.py")},
    "contract-auditor-v1":        {"contract_code": "function withdraw() { msg.sender.call.value(balance)(); }"},
    "patent-drafter-v1":          {"idea": "Système d'authentification biométrique local sans cloud", "inventor": "NanashiOS-Lab"},
    "self-healing-v1":            {"error_log": "AttributeError: 'NoneType' object has no attribute 'process'"},
    "energy-optimizer-v1":        {"workload": {"cpu_usage": 0.9, "memory_usage": 0.5, "gpu_usage": 0.3}},
    "dream-analyzer-v1":          {"dream_log": "Je volais au-dessus d'une forêt et tombais dans l'eau."},
    "watermark-detector-v1":      {"image": os.path.join(ROOT, "favicon.ico")},
    "behavioral-auth-v1":         {"behavior_data": {"typing_speed": 55, "consistency": 0.82, "error_rate": 0.05}},
    "quantum-safe-encryptor-v1":  {"action": "generate_key"},
    "self-learning-v1":           {"observation": "NanashiOS fonctionne en local", "feedback": "correct"},
    "collaborative-learning-v1":  {"local_knowledge": ["item1", "item2"], "shared_knowledge": ["item2", "item3"]},
    "personal-knowledge-graph-v1":{"action": "add", "entity": "NanashiOS", "relation": "utilise", "target": "agents"},
    "pulse-logic-v1":             {"premises": ["NanashiOS est local", "local contient des données"], "question": "est-il souverain ?"},
    "topologique-v1":             {"data": {"nodes": ["A","B","C"], "edges": [{"from":"A","to":"B"},{"from":"B","to":"C"}]}},
    "coordinateur-multi-agents-v1":{"task": "analyser et résumer ce document", "available_agents": ["résumé-texte-v1","sentiment-v1"]},
    "pdf-extracteur-v1":          {"pdf_path": "/tmp/nonexistent.pdf"},
    "blur-detection-v1":          {"image": os.path.join(ROOT, "favicon.ico")},
    "agent-1-blur-detection-v1":  {"image": os.path.join(ROOT, "favicon.ico")},
    "agent-2-real-time-ocr":      {"image": os.path.join(ROOT, "favicon.ico")},
    "image-deepfake-detector-v1": {"image": os.path.join(ROOT, "favicon.ico")},
    "audio-deepfake-detector-v1": {"audio": "/tmp/nonexistent.wav"},
}


def agent_test_cases():
    cases = []
    if not os.path.isdir(MKT_DIR):
        return cases
    for agent_id, input_data in AGENT_INPUTS.items():
        agent_dir = os.path.join(MKT_DIR, agent_id)
        agent_py = os.path.join(agent_dir, "agent.py")
        if os.path.exists(agent_py):
            cases.append((agent_id, agent_dir, input_data))
    return cases


@pytest.mark.parametrize("agent_id,agent_dir,input_data", agent_test_cases())
def test_agent_runs_and_returns_dict(agent_id, agent_dir, input_data):
    """Chaque agent doit s'exécuter sans exception et retourner un dict."""
    mod = load_agent(agent_dir)
    result = mod.run(input_data)
    assert isinstance(result, dict), f"{agent_id} doit retourner un dict"


@pytest.mark.parametrize("agent_id,agent_dir,input_data", agent_test_cases())
def test_agent_has_status_field(agent_id, agent_dir, input_data):
    """Chaque agent doit retourner un champ 'status'."""
    mod = load_agent(agent_dir)
    result = mod.run(input_data)
    assert "status" in result, f"{agent_id} : champ 'status' manquant dans la réponse"
