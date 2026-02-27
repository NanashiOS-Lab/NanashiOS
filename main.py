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
MAWS - Multimodal Agentic Waka System
Point d'entrée principal de NanashiOS
Usage: python main.py "Votre requête" [--interactive]
"""

import sys
import argparse
import logging
from core.waka_engine import waka
from core.link_pro import link_pro   # Protection de sortie

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="MAWS: Multimodal Agentic Waka System - NanashiOS")
    parser.add_argument("query", nargs="?", help="La tâche à exécuter")
    parser.add_argument("-i", "--interactive", action="store_true", help="Mode conversationnel interactif")
    parser.add_argument("--version", action="version", version=f"MAWS v{waka.version} (NanashiOS)")

    args = parser.parse_args()

    if args.interactive or not args.query:
        print(f"\nNanashiOS - MAWS v{waka.version}")
        print("Mode interactif activé. Tapez 'exit' pour quitter.\n")

        while True:
            try:
                user_input = input("Nanashi@maws:~$ ").strip()
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("Fermeture de NanashiOS.")
                    break
                if user_input:
                    # Traitement de la requête
                    raw_result = waka.process_query(user_input)
                    # Protection de la sortie avec LinkPro
                    protected_result = link_pro.edl_egress(raw_result.get('response', ''))
                    print(f" → {protected_result}\n")
            except KeyboardInterrupt:
                print("\nArrêt par l'utilisateur.")
                break
            except Exception as e:
                logging.error(f"Erreur : {e}")
    else:
        try:
            raw_result = waka.process_query(args.query)
            protected_result = link_pro.edl_egress(raw_result.get('response', ''))
            print(protected_result)
        except Exception as e:
            logging.error(f"Erreur : {e}")

if __name__ == "__main__":
    main()
