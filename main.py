"""
MAWS Entry Point
Usage: python main.py "Votre requête"
"""
import sys
import argparse
from core.waka_engine import waka

def main():
    parser = argparse.ArgumentParser(description="MAWS: Multimodal Agentic Waka System")
    parser.add_argument("query", nargs="?", help="La tâche à exécuter", default=None)
    parser.add_argument("--interactive", "-i", action="store_true", help="Mode conversationnel")

    args = parser.parse_args()

    if args.interactive or not args.query:
        print(f"\n👻 MAWS v{waka.version} (Nanashi Protocol Active)")
        print("Tapez 'exit' pour quitter.\n")

        while True:
            try:
                user_input = input("Nanashi@maws:~$ ")
                if user_input.lower() in ['exit', 'quit']:
                    break
                result = waka.process_query(user_input)
                print(f" > {result['response']}\n")
            except KeyboardInterrupt:
                break
    else:
        result = waka.process_query(args.query)
        print(result['response'])

if __name__ == "__main__":
    main()
