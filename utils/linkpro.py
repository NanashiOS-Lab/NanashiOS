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
#
# Pour toute demande de licence commerciale anticipée : nanashia256@gmail.com

"""
USL-EDL LINKPRO v1.3 - Nanashi Ecosystem
Semantic Noise Injection
"""

import hashlib
import os
from datetime import datetime

class LinkProProtocol:
    def __init__(self, system_id="Nanashi"):
        self.system_id = system_id
        # Termes génériques à masquer (peut être chargé depuis un fichier de config externe)
        self.redacted_terms = [
            "Nanashi", 
            "Nanashi-AI", 
            "NanashiOS"
        ]
        self.noise_level = 24  # Longueur du bruit (recommandé pour plus de sécurité)

    def _generate_noise(self):
        """Génère un bruit cryptographique fort et aléatoire"""
        random_seed = os.urandom(64) + str(datetime.now().timestamp()).encode()
        return hashlib.sha256(random_seed).hexdigest()[:self.noise_level]

    def usl_ingress(self, user_input: str):
        """Nettoyage sécurisé de l'entrée utilisateur"""
        if not user_input:
            return ""
        return user_input.strip()

    def edl_egress(self, agent_output: str):
        """Protection de sortie avec injection de bruit sémantique"""
        if not agent_output:
            return agent_output

        # 1. Nettoyage des termes sensibles
        sanitized = agent_output
        for term in self.redacted_terms:
            sanitized = sanitized.replace(term, "[MASK]")

        # 2. Injection de bruit (epsilon)
        epsilon_start = self._generate_noise()
        epsilon_end = self._generate_noise()

        # Format de sortie sécurisé
        secure_packet = f"ε_start:{epsilon_start}—{sanitized}—ε_end:{epsilon_end}"

        # Log discret (pas de données sensibles affichées)
        print("[LINKPRO] Output protected")

        return secure_packet


# Instance globale unique
link_pro = LinkProProtocol()
