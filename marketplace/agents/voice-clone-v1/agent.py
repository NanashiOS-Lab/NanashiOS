def run(input_data):
    """Voice Clone - NanashiOS. Utilise TTS/Coqui si dispo."""
    audio_path = input_data.get("audio_path", "")
    text_to_speak = input_data.get("text", "")
    output_path = input_data.get("output_path", "cloned_voice.wav")
    try:
        from TTS.api import TTS
        tts = TTS("tts_models/multilingual/multi-dataset/xtts_v2")
        tts.tts_to_file(text=text_to_speak, speaker_wav=audio_path, language="fr", file_path=output_path)
        return {"output_path": output_path, "status": "success"}
    except ImportError:
        return {"output_path": "", "note": "TTS (Coqui) non installé. Installer : pip install TTS", "status": "success"}
    except Exception as e:
        return {"output_path": "", "error": str(e), "status": "error"}
