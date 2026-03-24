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
NanashiOS - Point d'entrée principal
Usage: python main.py "Votre requête" [--interactive]
"""

import sys
import argparse
import logging
from core.waka_engine import waka

# Configuration du logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    parser = argparse.ArgumentParser(description="NanashiOS - Système d'IA Souveraine Locale")
    parser.add_argument("query", nargs="?", help="La tâche à exécuter")
    parser.add_argument("-i", "--interactive", action="store_true", help="Mode conversationnel interactif")
    parser.add_argument("--version", action="version", version="NanashiOS v1.0 (2026)")

    args = parser.parse_args()

    if args.interactive or not args.query:
        print(f"\nNanashiOS v1.0")
        print("Mode interactif activé. Tapez 'exit' pour quitter.\n")

        while True:
            try:
                user_input = input("Nanashi@nanashios:~$ ").strip()
                if user_input.lower() in ['exit', 'quit', 'q']:
                    print("Fermeture de NanashiOS.")
                    break
                if user_input:
                    # Traitement de la requête
                    raw_result = waka.process_query(user_input)
                    print(f" → {raw_result.get('response', '')}\n")
            except KeyboardInterrupt:
                print("\nArrêt par l'utilisateur.")
                break
            except Exception as e:
                logging.error(f"Erreur : {e}")
    else:
        try:
            raw_result = waka.process_query(args.query)
            print(raw_result.get('response', ''))
        except Exception as e:
            logging.error(f"Erreur : {e}")

if __name__ == "__main__":
    main()
