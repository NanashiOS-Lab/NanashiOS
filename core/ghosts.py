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
MAWS Ghost Protocol v1.0
Système d'agents autonomes pour NanashiOS
"""

import sys
import os

# Ajustement du chemin pour les imports
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class GhostAgent:
    """Classe de base pour tous les agents autonomes"""
    def __init__(self, name, role, clearance_level=1):
        self.name = name
        self.role = role
        self.clearance = clearance_level
        self.active = True

    def log(self, message):
        """Log discret et minimal"""
        print(f"[{self.name}] {message}")


class Blinky(GhostAgent):
    """Agent Orchestrateur - Analyse et distribue les tâches"""
    def __init__(self):
        super().__init__("Blinky", "Orchestrator", clearance_level=5)

    def analyze_task(self, user_query):
        self.log(f"Analyse de la requête : '{user_query[:60]}...'")
        
        # Analyse simple pour routage
        query_lower = user_query.lower()
        if any(word in query_lower for word in ["code", "python", "script", "programmer"]):
            return "task:inky"
        elif any(word in query_lower for word in ["cherche", "info", "recherche", "données"]):
            return "task:pinky"
        else:
            return "task:generic"


class Inky(GhostAgent):
    """Agent Développeur - Spécialisé dans le code sécurisé"""
    def __init__(self):
        super().__init__("Inky", "Developer", clearance_level=2)


class Pinky(GhostAgent):
    """Agent Chercheur - Spécialisé dans l'analyse et la recherche"""
    def __init__(self):
        super().__init__("Pinky", "Researcher", clearance_level=2)


# Instances globales
blinky = Blinky()
inky = Inky()
pinky = Pinky()


def get_active_ghosts():
    """Retourne la liste des agents actifs"""
    return [blinky, inky, pinky]


# Point d'entrée pour test rapide
if __name__ == "__main__":
    print("Ghost Protocol v1.0 - Agents initialisés")
    print(f"Agents actifs : {len(get_active_ghosts())}")
