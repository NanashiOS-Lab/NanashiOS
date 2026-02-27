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
    data_visualizer, auto_debugger
)
from core.link_pro import link_pro

class WakaEngine:
    def __init__(self):
        self.name = "NanashiOS Core"
        self.version = "1.1.0"
        print(f"[{self.name}] Initialisation du système...")

        if not link_pro.is_active:
            raise PermissionError("Protection de sortie inactif. Arrêt du système.")

        print(f"[{self.name}] Protection de sortie : ACTIVÉE")
        print(f"[{self.name}] Agent contradictoire Shadow : EN LIGNE")
        print(f"[{self.name}] 30 agents chargés avec hiérarchie")

    def process_query(self, user_input: str):
        """Traite une requête avec hiérarchie et vérification contradictoire"""
        # 1. Protection entrée
        secure_input = link_pro.usl_ingress(user_input)

        # 2. Analyse par l'orchestrateur (Blinky)
        print(f"[{self.name}] Transmission à l'orchestrateur...")
        agent_decision = blinky.analyze_task(secure_input)

        # 3. Exécution par l'agent concerné (simulation pour l'instant)
        raw_response = f"Réponse traitée par l'agent : {agent_decision}"

        # 4. Vérification contradictoire par Shadow
        critique = shadow.critique("Agent Principal", raw_response, secure_input)
        
        if critique["status"] == "critique":
            print("Shadow a détecté des faiblesses → ajustement en cours")
            raw_response += " (ajusté après critique)"

        # 5. Protection finale de sortie
        safe_response = link_pro.edl_egress(raw_response)

        return {
            "status": "success",
            "response": safe_response,
            "critique_status": critique["status"]
        }


# Instance globale du moteur central
waka = WakaEngine()
