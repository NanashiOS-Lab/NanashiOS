# SPDX-License-Identifier: BSL-1.1
# Copyright (c) 2026 NanashiOS-Lab. All rights reserved.
#
# Business Source License 1.1 – Nanashi Edition
#
# Utilisation non commerciale : Libre et gratuite pour tout usage personnel,
# éducatif ou de recherche.
#
# Utilisation commerciale : Interdite jusqu’au 20 février 2030,
# sauf accord écrit préalable avec NanashiOS-Lab.
#
# Exception Acquisition :
# Toute entité qui acquiert plus de 50 % du contrôle du projet ou des tokens $NANA
# obtient immédiatement une licence commerciale illimitée et perpétuelle.
#
# Au 20 février 2030, la licence passe automatiquement en MIT License.

"""
NanashiOS - GhostAgent System
Hiérarchie complète avec les 30 agents
"""

import importlib.util
import os

_MKT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "marketplace", "agents")


def _load_marketplace_agent(agent_id: str):
    """Charge le module agent.py depuis marketplace/agents/<agent_id>/."""
    path = os.path.join(_MKT_DIR, agent_id, "agent.py")
    if not os.path.exists(path):
        return None
    spec = importlib.util.spec_from_file_location(f"mkt_{agent_id}", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


class GhostAgent:
    """Classe de base pour tous les agents autonomes"""
    def __init__(self, name, role, clearance_level=1, supervisor=None):
        self.name = name
        self.role = role
        self.clearance = clearance_level
        self.supervisor = supervisor
        self.active = True

    def log(self, message):
        """Log discret"""
        print(f"[{self.name}] {message}")

    def _delegate(self, agent_id: str, input_data: dict) -> str:
        """Délègue l'exécution à l'implémentation marketplace et formate la réponse."""
        mod = _load_marketplace_agent(agent_id)
        if mod is None:
            return f"[{self.name}] Agent marketplace '{agent_id}' introuvable."
        result = mod.run(input_data)
        # Formate le dict en une réponse lisible
        skip = {"status"}
        parts = [f"{k} : {v}" for k, v in result.items() if k not in skip and v not in (None, "", [], {})]
        return " | ".join(parts) if parts else str(result)

    def process(self, input_data):
        """Méthode à surcharger par chaque agent"""
        raise NotImplementedError("Chaque agent doit implémenter process()")


# ====================== HIÉRARCHIE ======================

class Blinky(GhostAgent):
    """Boss Final - Orchestrateur Suprême"""
    def __init__(self):
        super().__init__("Blinky", "Orchestrator Final", clearance_level=5, supervisor=None)

    def analyze_task(self, user_input: str) -> str:
        self.log(f"Analyse de la tâche : {user_input[:60]}...")
        return f"Tâche analysée par Blinky : {user_input}"

    def process(self, input_data):
        return self.analyze_task(input_data)


class Inky(GhostAgent):
    """Chef du Domaine Développement"""
    def __init__(self):
        super().__init__("Inky", "Lead Developer", clearance_level=4, supervisor=None)


class Pinky(GhostAgent):
    """Chef du Domaine Recherche"""
    def __init__(self):
        super().__init__("Pinky", "Lead Researcher", clearance_level=4, supervisor=None)


class Shadow(GhostAgent):
    """Agent Contradictoire - Devil's Advocate"""
    def __init__(self):
        super().__init__("Shadow", "Critique & Vérification", clearance_level=4, supervisor=None)

    def critique(self, agent_name: str, result: str, user_query: str):
        self.log(f"Critique du résultat de {agent_name}")
        critique_points = []
        
        if len(result) < 50:
            critique_points.append("Réponse trop courte")
        if any(word in result.lower() for word in ["peut-être", "je pense", "probablement"]):
            critique_points.append("Manque de certitude")
        if any(word in result.lower() for word in ["toujours", "jamais", "tous", "aucun"]):
            critique_points.append("Affirmation trop absolue")
        
        if critique_points:
            return {"status": "critique", "points": critique_points}
        else:
            return {"status": "validé", "message": "Aucune faille majeure"}


# ====================== LES 30 AGENTS ======================

# --- Agents Texte & Langage ---
class ResumeTexte(GhostAgent):
    def __init__(self):
        super().__init__("ResumeTexte", "Text Summarization", 2, pinky)

    def process(self, text):
        self.log("Résumé en cours")
        return self._delegate("résumé-texte-v1", {"text": text})

class Sentiment(GhostAgent):
    def __init__(self):
        super().__init__("Sentiment", "Emotion Analysis", 2, pinky)

    def process(self, text):
        self.log("Analyse sentimentale")
        return self._delegate("sentiment-v1", {"text": text})

class Traduction(GhostAgent):
    def __init__(self):
        super().__init__("Traduction", "Translation", 2, pinky)

    def process(self, text):
        self.log("Traduction en cours")
        return self._delegate("traduction-v1", {"text": text})

class KeywordExtractor(GhostAgent):
    def __init__(self):
        super().__init__("KeywordExtractor", "Keyword Analysis", 2, pinky)

    def process(self, text):
        self.log("Extraction mots-clés")
        return self._delegate("keyword-extractor-v1", {"text": text})

class EthicalReasoner(GhostAgent):
    def __init__(self):
        super().__init__("EthicalReasoner", "Ethical Analysis", 3, pinky)

    def process(self, query):
        self.log("Raisonnement éthique")
        return self._delegate("ethical-reasoner-v1", {"query": query})

class FakeNewsDetector(GhostAgent):
    def __init__(self):
        super().__init__("FakeNewsDetector", "Fact Checking", 3, pinky)

    def process(self, text):
        self.log("Vérification fake news")
        return self._delegate("fake-news-detector-v1", {"text": text})

class HumanAuth(GhostAgent):
    def __init__(self):
        super().__init__("HumanAuth", "Humanity Verification", 4, pinky)

    def process(self, text):
        self.log("Vérification authenticité")
        return self._delegate("human-auth-v1", {"text": text})

# --- Agents Vision ---
class BlurDetection(GhostAgent):
    def __init__(self):
        super().__init__("BlurDetection", "Image Quality", 3, inky)

    def process(self, image_path):
        self.log(f"Analyse flou : {image_path}")
        return self._delegate("blur-detection-v1", {"image": image_path})

class ImageCaption(GhostAgent):
    def __init__(self):
        super().__init__("ImageCaption", "Vision Captioning", 3, inky)

    def process(self, image_path):
        self.log(f"Description image : {image_path}")
        return self._delegate("image-caption-v1", {"image": image_path})

class FaceBlur(GhostAgent):
    def __init__(self):
        super().__init__("FaceBlur", "Privacy Protection", 4, inky)

    def process(self, image_path):
        self.log(f"Floutage visages : {image_path}")
        return self._delegate("face-blur-v1", {"image": image_path})

class ImageDeepfakeDetector(GhostAgent):
    def __init__(self):
        super().__init__("ImageDeepfakeDetector", "Deepfake Detection", 4, inky)

    def process(self, image_path):
        self.log(f"Analyse deepfake image : {image_path}")
        return self._delegate("image-deepfake-detector-v1", {"image": image_path})

# --- Agents Audio ---
class RealTimeOCR(GhostAgent):
    def __init__(self):
        super().__init__("RealTimeOCR", "OCR", 3, pinky)

    def process(self, image_path):
        self.log(f"OCR : {image_path}")
        return self._delegate("agent-2-real-time-ocr", {"image": image_path})

class VoiceClone(GhostAgent):
    def __init__(self):
        super().__init__("VoiceClone", "Voice Synthesis", 3, inky)

    def process(self, audio_path):
        self.log(f"Clonage voix : {audio_path}")
        return self._delegate("voice-clone-v1", {"audio_path": audio_path, "text": ""})

class AudioDeepfakeDetector(GhostAgent):
    def __init__(self):
        super().__init__("AudioDeepfakeDetector", "Audio Analysis", 4, pinky)

    def process(self, audio_path):
        self.log(f"Analyse deepfake audio : {audio_path}")
        return self._delegate("audio-deepfake-detector-v1", {"audio": audio_path})

# --- Agents Sécurité ---
class LocalMalwareDetector(GhostAgent):
    def __init__(self):
        super().__init__("LocalMalwareDetector", "Security", 4, inky)

    def process(self, file_path):
        self.log(f"Scan malware : {file_path}")
        return self._delegate("local-malware-detector-v1", {"file_path": file_path})

class BiometricLocalAuth(GhostAgent):
    def __init__(self):
        super().__init__("BiometricLocalAuth", "Authentication", 5, inky)

    def process(self, data):
        self.log("Vérification biométrique")
        return self._delegate("biometric-local-auth-v1", {"biometric_data": data if isinstance(data, dict) else {}})

class ContractAuditor(GhostAgent):
    def __init__(self):
        super().__init__("ContractAuditor", "Smart Contract Audit", 5, inky)

    def process(self, code):
        self.log("Audit contrat")
        return self._delegate("contract-auditor-v1", {"contract_code": code})

class PatentDrafter(GhostAgent):
    def __init__(self):
        super().__init__("PatentDrafter", "Patent Writing", 4, pinky)

    def process(self, idea):
        self.log("Rédaction brevet")
        return self._delegate("patent-drafter-v1", {"idea": idea})

class SelfHealing(GhostAgent):
    def __init__(self):
        super().__init__("SelfHealing", "System Self-Repair", 5, blinky)

    def process(self, error):
        self.log("Auto-réparation")
        return self._delegate("self-healing-v1", {"error_log": str(error)})

# --- Agents Coordination & Avancé ---
class CoordinateurMultiAgents(GhostAgent):
    def __init__(self):
        super().__init__("CoordinateurMultiAgents", "Multi-Agent Coordination", 5, blinky)

    def process(self, task):
        self.log("Coordination multi-agents")
        return self._delegate("coordinateur-multi-agents-v1", {"task": task, "available_agents": []})

class PulseLogic(GhostAgent):
    def __init__(self):
        super().__init__("PulseLogic", "Logical Reasoning", 4, pinky)

    def process(self, query):
        self.log("Raisonnement logique")
        return self._delegate("pulse-logic-v1", {"premises": [], "question": query})

class PersonalKnowledgeGraph(GhostAgent):
    def __init__(self):
        super().__init__("PersonalKnowledgeGraph", "Knowledge Management", 4, pinky)

    def process(self, data):
        self.log("Mise à jour graphe")
        return self._delegate("personal-knowledge-graph-v1", {"action": "add", "entity": str(data)[:50]})

class CollaborativeLearning(GhostAgent):
    def __init__(self):
        super().__init__("CollaborativeLearning", "Collective Learning", 4, blinky)

    def process(self, data):
        self.log("Apprentissage collaboratif")
        return self._delegate("collaborative-learning-v1", {"local_knowledge": [], "shared_knowledge": [str(data)]})

# --- Agents Outils Techniques ---
class CodeWriter(GhostAgent):
    def __init__(self):
        super().__init__("CodeWriter", "Code Generation", 3, inky)

    def process(self, request):
        self.log("Génération code")
        return self._delegate("code-writer-v1", {"task": request, "language": "python"})

class PDFExtracteur(GhostAgent):
    def __init__(self):
        super().__init__("PDFExtracteur", "Document Processing", 3, pinky)

    def process(self, pdf_path):
        self.log(f"Extraction PDF : {pdf_path}")
        return self._delegate("pdf-extracteur-v1", {"pdf_path": pdf_path})

class TopologyAnalyzer(GhostAgent):
    def __init__(self):
        super().__init__("TopologyAnalyzer", "Network Analysis", 4, inky)

    def process(self, data):
        self.log("Analyse topologique")
        return self._delegate("topologique-v1", {"data": data if isinstance(data, dict) else {}})

class SemanticSearch(GhostAgent):
    def __init__(self):
        super().__init__("SemanticSearch", "Semantic Search", 3, pinky)

    def process(self, query):
        self.log("Recherche sémantique")
        return self._delegate("semantic-search-v1", {"query": query, "corpus": []})

class DataVisualizer(GhostAgent):
    def __init__(self):
        super().__init__("DataVisualizer", "Data Visualization", 3, pinky)

    def process(self, data):
        self.log("Visualisation données")
        return f"Visualisation demandée pour : {str(data)[:100]}. Installer matplotlib pour le rendu graphique."

class AutoDebugger(GhostAgent):
    def __init__(self):
        super().__init__("AutoDebugger", "Automated Debugging", 4, inky)

    def process(self, error_log):
        self.log("Débogage automatique")
        return self._delegate("self-healing-v1", {"error_log": str(error_log)})

# --- Agents Orphelins Intégrés ---
class DetectionEmotion(GhostAgent):
    def __init__(self):
        super().__init__("DetectionEmotion", "Emotion Detection", 2, pinky)

    def process(self, text):
        self.log("Détection émotion")
        return self._delegate("détection-émotion-v1", {"text": text})

class BehavioralAuth(GhostAgent):
    def __init__(self):
        super().__init__("BehavioralAuth", "Behavioral Authentication", 4, inky)

    def process(self, data):
        self.log("Authentification comportementale")
        behavior = data if isinstance(data, dict) else {}
        return self._delegate("behavioral-auth-v1", {"behavior_data": behavior})

class DreamAnalyzer(GhostAgent):
    def __init__(self):
        super().__init__("DreamAnalyzer", "Dream Analysis", 2, pinky)

    def process(self, text):
        self.log("Analyse de rêve")
        return self._delegate("dream-analyzer-v1", {"dream_log": text})

class EnergyOptimizer(GhostAgent):
    def __init__(self):
        super().__init__("EnergyOptimizer", "Energy Optimization", 3, inky)

    def process(self, data):
        self.log("Optimisation énergétique")
        workload = data if isinstance(data, dict) else {}
        return self._delegate("energy-optimizer-v1", {"workload": workload, "constraints": {}})

class PromptOptimizer(GhostAgent):
    def __init__(self):
        super().__init__("PromptOptimizer", "Prompt Optimization", 3, pinky)

    def process(self, prompt):
        self.log("Optimisation de prompt")
        return self._delegate("prompt-optimizer-v1", {"prompt": prompt})

class QuantumSafeEncryptor(GhostAgent):
    def __init__(self):
        super().__init__("QuantumSafeEncryptor", "Post-Quantum Encryption", 5, inky)

    def process(self, data):
        self.log("Chiffrement post-quantique")
        text = data if isinstance(data, str) else str(data)
        return self._delegate("quantum-safe-encryptor-v1", {"action": "encrypt", "data": text})

class SelfLearning(GhostAgent):
    def __init__(self):
        super().__init__("SelfLearning", "Self Learning", 4, blinky)

    def process(self, data):
        self.log("Apprentissage automatique")
        obs = data if isinstance(data, str) else str(data)
        return self._delegate("self-learning-v1", {"observation": obs, "feedback": ""})

class TopologyAnalyzerV1(GhostAgent):
    def __init__(self):
        super().__init__("TopologyAnalyzerV1", "Topology Analysis v1", 4, inky)

    def process(self, data):
        self.log("Analyse topologie v1")
        return self._delegate("topology-analyzer-v1", {"data": data if isinstance(data, dict) else {}})

class WatermarkDetector(GhostAgent):
    def __init__(self):
        super().__init__("WatermarkDetector", "Watermark Detection", 3, inky)

    def process(self, image_path):
        self.log(f"Détection watermark : {image_path}")
        return self._delegate("watermark-detector-v1", {"image": image_path})

class RealTimeOCRV1(GhostAgent):
    def __init__(self):
        super().__init__("RealTimeOCRV1", "OCR v1", 3, pinky)

    def process(self, image_path):
        self.log(f"OCR v1 : {image_path}")
        return self._delegate("real-time-ocr-v1", {"image": image_path})

class BlurDetectionV1(GhostAgent):
    def __init__(self):
        super().__init__("BlurDetectionV1", "Blur Detection v1", 3, inky)

    def process(self, image_path):
        self.log(f"Détection flou v1 : {image_path}")
        return self._delegate("agent-1-blur-detection-v1", {"image": image_path})


# ====================== INSTANCES GLOBALES ======================

# Instances de la hiérarchie (doivent être créées avant les 30 agents)
blinky = Blinky()
inky = Inky()
pinky = Pinky()
shadow = Shadow()

# Liaison des superviseurs vers la même instance blinky
inky.supervisor = blinky
pinky.supervisor = blinky
shadow.supervisor = blinky

# Instances des 30 agents
resume_texte = ResumeTexte()
sentiment = Sentiment()
traduction = Traduction()
keyword_extractor = KeywordExtractor()
ethical_reasoner = EthicalReasoner()
fake_news_detector = FakeNewsDetector()
human_auth = HumanAuth()

blur_detection = BlurDetection()
image_caption = ImageCaption()
face_blur = FaceBlur()
image_deepfake = ImageDeepfakeDetector()

real_time_ocr = RealTimeOCR()
voice_clone = VoiceClone()
audio_deepfake = AudioDeepfakeDetector()

local_malware = LocalMalwareDetector()
biometric_auth = BiometricLocalAuth()
contract_auditor = ContractAuditor()
patent_drafter = PatentDrafter()
self_healing = SelfHealing()

coordinateur = CoordinateurMultiAgents()
pulse_logic = PulseLogic()
knowledge_graph = PersonalKnowledgeGraph()
collaborative = CollaborativeLearning()

code_writer = CodeWriter()
pdf_extracteur = PDFExtracteur()
topology_analyzer = TopologyAnalyzer()
semantic_search = SemanticSearch()
data_visualizer = DataVisualizer()
auto_debugger = AutoDebugger()

detection_emotion = DetectionEmotion()
behavioral_auth = BehavioralAuth()
dream_analyzer = DreamAnalyzer()
energy_optimizer = EnergyOptimizer()
prompt_optimizer = PromptOptimizer()
quantum_encryptor = QuantumSafeEncryptor()
self_learning = SelfLearning()
topology_analyzer_v1 = TopologyAnalyzerV1()
watermark_detector = WatermarkDetector()
real_time_ocr_v1 = RealTimeOCRV1()
blur_detection_v1 = BlurDetectionV1()
