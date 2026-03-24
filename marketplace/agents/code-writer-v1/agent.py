def run(input_data):
    """Code Writer - NanashiOS. Génère du code structuré dans le langage demandé."""
    task = input_data.get("task", "Aucune tâche spécifiée.")
    language = input_data.get("language", "python").lower()
    templates = {
        "python": f'''# NanashiOS Code-Writer-v1
# Tâche : {task}

def main():
    """
    {task}
    """
    # TODO: Implémentation de : {task}
    result = None
    return result

if __name__ == "__main__":
    main()
''',
        "javascript": f'''// NanashiOS Code-Writer-v1
// Tâche : {task}

async function main() {{
    // TODO: Implémenter : {task}
    const result = null;
    return result;
}}

main().catch(console.error);
''',
        "rust": f'''// NanashiOS Code-Writer-v1
// Tâche : {task}

fn main() {{
    // TODO: Implémenter : {task}
    println!("NanashiOS - {{:?}}", "{task}");
}}
''',
        "typescript": f'''// NanashiOS Code-Writer-v1
// Tâche : {task}

async function main(): Promise<void> {{
    // TODO: Implémenter : {task}
    const result: unknown = null;
    console.log(result);
}}

main();
''',
    }
    code = templates.get(language, f"# Langage {language} non supporté\n# Tâche : {task}")
    return {"code": code, "explanation": f"Code généré pour : {task} ({language})", "language": language, "status": "success"}
