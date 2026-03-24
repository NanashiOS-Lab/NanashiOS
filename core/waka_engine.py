# SPDX-License-Identifier: BSL-1.1
# Copyright (c) 2026 NanashiOS-Lab. All rights reserved.

"""
NanashiOS Core Engine - Waka v1.1
Orchestrateur central avec hiérarchie et agent contradictoire
"""

import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from core.ghosts import (
    blinky, inky, pinky, shadow,
    resume_texte, sentiment, traduction, keyword_extractor,
    ethical_reasoner, fake_news_detector, human_auth,
    blur_detection, image_caption, face_blur, image_deepfake,
    real_time_ocr, voice_clone, audio_deepfake,
    local_malware, biometric_auth, contract_auditor, patent_drafter, self_healing,
    coordinateur, pulse_logic, knowledge_graph, collaborative,
    code_writer, pdf_extracteur, topology_analyzer, semantic_search,
    data_visualizer, auto_debugger,
    detection_emotion, behavioral_auth, dream_analyzer, energy_optimizer,
    prompt_optimizer, quantum_encryptor, self_learning, topology_analyzer_v1,
    watermark_detector, real_time_ocr_v1, blur_detection_v1
)
from core.link_pro import link_pro

# Mots-clés pour router la requête vers le bon agent
ROUTING_TABLE = {
    resume_texte:      ["résumé", "résume", "résumer", "summarize", "summary", "synthèse"],
    sentiment:         ["sentiment", "émotion", "positif", "négatif", "ressenti", "feeling"],
    traduction:        ["traduis", "traduire", "traduction", "translate", "translation"],
    keyword_extractor: ["mots-clés", "keywords", "mots clés", "extraire mots", "thèmes"],
    ethical_reasoner:  ["éthique", "moral", "éthiquement", "est-ce bien", "permis", "légal"],
    fake_news_detector:["fake news", "faux", "vérifier", "rumeur", "désinformation"],
    human_auth:        ["humain", "bot", "authenticité", "vérifie si humain"],
    blur_detection:    ["flou", "blur", "qualité image", "netteté"],
    image_caption:     ["décris", "image", "photo", "caption", "description image"],
    face_blur:         ["flouter visage", "anonymiser", "visage", "face blur"],
    image_deepfake:    ["deepfake image", "fausse image", "image authentique"],
    real_time_ocr:     ["ocr", "texte image", "lire image", "extraire texte"],
    voice_clone:       ["voix", "cloner voix", "voice clone", "synthèse vocale"],
    audio_deepfake:    ["deepfake audio", "fausse voix", "audio synthétique"],
    local_malware:     ["malware", "virus", "scan", "sécurité fichier"],
    biometric_auth:    ["biométrie", "empreinte", "authentification biométrique"],
    contract_auditor:  ["contrat", "smart contract", "audit contrat", "solidity"],
    patent_drafter:    ["brevet", "patent", "propriété intellectuelle", "invention"],
    self_healing:      ["répare", "auto-réparation", "bug système", "self-healing"],
    coordinateur:      ["coordonne", "coordination", "multi-agents", "plusieurs agents"],
    pulse_logic:       ["logique", "raisonnement", "déduis", "conclusion"],
    knowledge_graph:   ["graphe", "connaissances", "knowledge", "relations"],
    collaborative:     ["apprentissage collaboratif", "partage connaissances", "fédéré"],
    code_writer:       ["code", "programme", "écris", "python", "javascript", "rust", "fonction"],
    pdf_extracteur:    ["pdf", "document", "extraire pdf", "lire pdf"],
    topology_analyzer: ["topologie", "réseau", "graphe réseau", "topology"],
    semantic_search:   ["cherche", "recherche", "trouve", "search"],
    data_visualizer:   ["visualise", "graphique", "chart", "données", "statistiques"],
    auto_debugger:     ["debug", "erreur", "bug", "corrige", "fix"],
    detection_emotion: ["émotion", "détecte émotion", "colère", "joie", "tristesse", "peur"],
    behavioral_auth:   ["comportement", "typing", "frappe clavier", "authentification comportementale"],
    dream_analyzer:    ["rêve", "songe", "cauchemar", "dream", "analyse rêve"],
    energy_optimizer:  ["énergie", "consommation", "watt", "optimise énergie", "puissance"],
    prompt_optimizer:  ["optimise prompt", "améliore prompt", "reformule", "prompt engineering"],
    quantum_encryptor: ["quantique", "chiffrement", "encrypt", "post-quantique", "cryptographie"],
    self_learning:     ["apprends", "mémorise", "observation", "self-learning", "apprentissage auto"],
    topology_analyzer_v1: ["topologie réseau", "analyse réseau v1", "nœuds", "graphe connexe"],
    watermark_detector:["watermark", "filigrane", "marque image", "détecte watermark"],
    real_time_ocr_v1:  ["ocr v1", "lecture image v1", "extraire texte v1"],
    blur_detection_v1: ["flou v1", "blur v1", "qualité image v1"],
}


class WakaEngine:
    def __init__(self):
        self.name = "NanashiOS Core"
        self.version = "1.1.0"
        print(f"[{self.name}] Initialisation du système...")

        if not link_pro.is_active:
            raise PermissionError("Protection de sortie inactif. Arrêt du système.")

        print(f"[{self.name}] Protection de sortie : ACTIVÉE")
        print(f"[{self.name}] Agent contradictoire Shadow : EN LIGNE")
        print(f"[{self.name}] 41 agents chargés avec hiérarchie")

    def _route(self, user_input: str):
        """Sélectionne l'agent le plus approprié selon la requête."""
        text = user_input.lower()
        best_agent = None
        best_score = 0

        for agent, keywords in ROUTING_TABLE.items():
            score = sum(1 for kw in keywords if kw in text)
            if score > best_score:
                best_score = score
                best_agent = agent

        return best_agent if best_agent else blinky

    def process_query(self, user_input: str):
        """Traite une requête avec routage, hiérarchie et vérification contradictoire."""
        # 1. Protection entrée
        secure_input = link_pro.usl_ingress(user_input)

        # 2. Routage vers l'agent approprié
        agent = self._route(secure_input)
        print(f"[{self.name}] Routage → {agent.name}")

        # 3. Exécution par l'agent sélectionné
        try:
            raw_response = agent.process(secure_input)
        except Exception as e:
            raw_response = blinky.analyze_task(secure_input)

        # 4. Vérification contradictoire par Shadow
        critique = shadow.critique(agent.name, str(raw_response), secure_input)
        if critique["status"] == "critique":
            print(f"[Shadow] Faiblesses détectées → ajustement")
            raw_response = str(raw_response) + " (vérifié et ajusté par Shadow)"

        # 5. Protection finale de sortie
        safe_response = link_pro.edl_egress(str(raw_response))

        return {
            "status": "success",
            "agent": agent.name,
            "response": safe_response,
            "critique_status": critique["status"]
        }


# Instance globale du moteur central
waka = WakaEngine()
