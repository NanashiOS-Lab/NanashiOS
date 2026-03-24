# NanashiOS — Documentation API & Agents

**Version** : 1.1.0 | **Licence** : BSL-1.1 | **Langue** : Français

---

## Architecture

```
NanashiOS
├── main.py                  # Point d'entrée CLI
├── core/
│   ├── waka_engine.py       # Orchestrateur central (routage, critique)
│   ├── ghosts.py            # 30 agents + hiérarchie (Blinky/Inky/Pinky/Shadow)
│   └── link_pro.py          # Protection I/O (USL-ingress, EDL-egress, ε-Noise)
├── config/settings.py       # Configuration (langue, seuils, clés)
├── marketplace/agents/      # Implémentations complètes des 30 agents
├── agents/                  # Copies des agents (registre racine)
└── tests/                   # Tests pytest (349 tests)
```

---

## Utilisation CLI

```bash
# Requête directe
python main.py "résume ce texte : ..."

# Mode interactif
python main.py --interactive
python main.py -i

# Version
python main.py --version
```

---

## API Python

### WakaEngine

```python
from core.waka_engine import waka

result = waka.process_query("résume ce document")
# {
#   "status": "success",
#   "agent": "ResumeTexte",
#   "response": "ε_start:...—résumé—ε_end:...",
#   "critique_status": "validé"
# }
```

### Appel direct d'un agent

```python
import importlib.util, os

def load_agent(agent_id):
    path = f"marketplace/agents/{agent_id}/agent.py"
    spec = importlib.util.spec_from_file_location("agent", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod

agent = load_agent("résumé-texte-v1")
result = agent.run({"text": "Votre texte long ici...", "max_sentences": 3})
# {"summary": "...", "key_points": [...], "status": "success"}
```

---

## Référence des 30 agents

### 📝 Texte & Langage

| ID | Nom FR | Entrée | Sortie |
|---|---|---|---|
| `résumé-texte-v1` | Agent de Résumé de Texte | `text`, `max_sentences` | `summary`, `key_points` |
| `sentiment-v1` | Agent d'Analyse des Sentiments | `text` | `sentiment`, `score` |
| `traduction-v1` | Agent de Traduction | `text`, `target_lang`, `source_lang` | `translated_text` |
| `keyword-extractor-v1` | Agent Extracteur de Mots-Clés | `text`, `max_keywords` | `keywords[]` |
| `ethical-reasoner-v1` | Agent de Raisonnement Éthique | `query` | `verdict`, `ethics_score`, `reasoning` |
| `fake-news-detector-v1` | Agent Détecteur de Fausses Nouvelles | `text` | `is_fake`, `confidence` |
| `human-auth-v1` | Agent d'Authenticité Humaine | `text` | `is_human`, `confidence` |
| `prompt-optimizer-v1` | Agent Optimiseur de Prompts | `prompt`, `mode` | `optimized_prompt`, `improvements[]` |
| `semantic-search-v1` | Agent de Recherche Sémantique | `query`, `corpus[]`, `top_k` | `results[]`, `top_result` |

### 🖼️ Vision

| ID | Nom FR | Entrée | Sortie |
|---|---|---|---|
| `blur-detection-v1` | Agent de Détection de Flou | `image` (chemin) | `blur_score`, `is_blurry` |
| `image-caption-v1` | Agent de Description d'Images | `image` (chemin) | `caption`, `keywords[]` |
| `face-blur-v1` | Agent de Floutage de Visages | `image`, `output_path` | `faces_found`, `output_path` |
| `image-deepfake-detector-v1` | Agent Détecteur de Deepfake d'Images | `image` (chemin) | `is_deepfake`, `confidence`, `analysis` |
| `watermark-detector-v1` | Agent Détecteur de Filigranes | `image` (chemin) | `has_watermark`, `confidence` |

### 🎙️ Audio

| ID | Nom FR | Entrée | Sortie |
|---|---|---|---|
| `voice-clone-v1` | Agent de Clonage de Voix | `audio_path`, `text`, `output_path` | `output_path` |
| `audio-deepfake-detector-v1` | Agent Détecteur de Deepfake Audio | `audio` (chemin) | `is_deepfake`, `confidence`, `analysis` |
| `agent-2-real-time-ocr` | Agent OCR en Temps Réel | `image`, `lang` | `text`, `word_count` |

### 🔒 Sécurité & Privacy

| ID | Nom FR | Entrée | Sortie |
|---|---|---|---|
| `local-malware-detector-v1` | Agent Détecteur de Malwares Local | `file_path` | `is_malware`, `confidence`, `sha256` |
| `biometric-local-auth-v1` | Agent d'Authentification Biométrique Locale | `biometric_data`, `stored_hash` | `authenticated`, `confidence` |
| `behavioral-auth-v1` | Agent d'Authentification Comportementale | `behavior_data`, `stored_profile` | `authenticated`, `confidence` |
| `contract-auditor-v1` | Agent Auditeur de Contrats | `contract_code` | `vulnerabilities[]`, `risk_score` |
| `quantum-safe-encryptor-v1` | Agent Chiffreur Quantique Sécurisé | `action`, `data`, `key` | `ciphertext`/`plaintext`/`key` |
| `patent-drafter-v1` | Agent Rédacteur de Brevets | `idea`, `inventor`, `domain` | `patent_draft` |
| `self-healing-v1` | Agent d'Auto-Réparation | `error_log`, `current_state` | `diagnosis`, `proposed_fixes[]` |

### 🤝 Coordination & Avancé

| ID | Nom FR | Entrée | Sortie |
|---|---|---|---|
| `coordinateur-multi-agents-v1` | Coordinateur Multi-Agents | `task`, `available_agents[]`, `constraints` | `coordination_plan`, `task_assignment` |
| `pulse-logic-v1` | Agent Pulse Logic | `premises[]`, `question` | `conclusions[]`, `answer` |
| `personal-knowledge-graph-v1` | Agent de Graphe de Connaissances Personnel | `action`, `entity`, `relation`, `target` | `nodes`, `edges` |
| `collaborative-learning-v1` | Agent d'Apprentissage Collaboratif | `local_knowledge[]`, `shared_knowledge[]` | `merged_knowledge[]` |
| `self-learning-v1` | Agent d'Auto-Apprentissage | `observation`, `feedback`, `knowledge_path` | `entries_learned` |
| `dream-analyzer-v1` | Agent Analyseur de Rêves | `dream_log` | `interpretation`, `sleep_quality` |
| `energy-optimizer-v1` | Agent Optimiseur d'Énergie | `workload{}`, `constraints{}` | `estimated_power_watts`, `recommendations[]` |

### 🛠️ Outils Techniques

| ID | Nom FR | Entrée | Sortie |
|---|---|---|---|
| `code-writer-v1` | Agent Rédacteur de Code | `task`, `language` | `code`, `explanation` |
| `pdf-extracteur-v1` | Agent Extracteur PDF | `pdf_path`, `max_pages` | `text`, `pages` |
| `topologique-v1` | Agent Analyseur de Topologie | `data{nodes[], edges[]}` | `analysis{}` |

---

## Configuration

```python
# config/settings.py
LANGUAGE = "fr"               # Langue par défaut (env: NANASHI_LANG)
SUPPORTED_LANGUAGES = ["fr", "en"]
ANONYMITY_LEVEL = "High"
BLOCKCHAIN_AUDIT = True
SIMILARITY_THRESHOLD = 0.85
```

---

## Tests

```bash
pip install pytest
python -m pytest tests/ -v

# Tests disponibles :
# tests/test_manifests.py  — validité JSON, champs requis, name_fr, index
# tests/test_agents.py     — exécution des 30 agents, champ status
# tests/test_core.py       — LinkPro, Shadow, routage WakaEngine, config
```

---

## Routage automatique

Le moteur `WakaEngine` route automatiquement chaque requête vers l'agent approprié
selon les mots-clés détectés :

| Mots-clés | Agent sélectionné |
|---|---|
| `résumé`, `synthèse`, `résume` | `ResumeTexte` |
| `code`, `python`, `programme` | `CodeWriter` |
| `traduis`, `traduction` | `Traduction` |
| `sentiment`, `émotion` | `Sentiment` |
| `cherche`, `recherche` | `SemanticSearch` |
| `malware`, `virus`, `scan` | `LocalMalwareDetector` |
| `deepfake audio` | `AudioDeepfakeDetector` |
| `deepfake image` | `ImageDeepfakeDetector` |
| *(aucun match)* | `Blinky` (orchestrateur) |

---

*NanashiOS — Pas de nom. Pas de trace. Contrôle total.* 👻
