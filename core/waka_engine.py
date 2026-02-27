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
NanashiOS Core Engine - Waka v1.1
Orchestrateur central du système
"""

import sys
import os

# Ajustement du chemin pour les imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

try:
    from config.settings import settings
    from core.link_pro import link_pro
    from core.ghosts import blinky
except ImportError as e:
    print(f"Erreur critique d'importation : {e}")
    sys.exit(1)


class WakaEngine:
    """Moteur central de NanashiOS"""
    def __init__(self):
        self.name = "NanashiOS Core"
        self.version = "1.1.0"
        print(f"[{self.name}] Initialisation...")

        if not link_pro.is_active:
            raise PermissionError("Tunnel de protection inactif. Arrêt du système.")

        print(f"[{self.name}] Protection de sortie : ACTIVÉE")
        print(f"[{self.name}] Orchestrateur principal : EN LIGNE")

    def process_query(self, user_input: str):
        """
        Traite une requête utilisateur de manière sécurisée.
        """
        # 1. Protection entrée (USL)
        try:
            secure_input = link_pro.usl_ingress(user_input)
        except Exception as e:
            return {"status": "error", "message": str(e)}

        # 2. Analyse et routage par l'orchestrateur
        print(f"[{self.name}] Analyse de la requête...")
        agent_decision = blinky.analyze_task(secure_input)

        # 3. Génération de la réponse brute
        raw_response = f"Requête traitée. {agent_decision}"

        # 4. Protection sortie (EDL)
        safe_response = link_pro.edl_egress(raw_response)

        return {
            "status": "success",
            "response": safe_response
        }


# Instance globale du moteur
waka = WakaEngine()
