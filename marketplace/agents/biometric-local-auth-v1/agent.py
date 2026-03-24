def run(input_data):
    """Biometric Auth - NanashiOS. Empreinte via face_recognition ou hashlib."""
    biometric_data = input_data.get("biometric_data", {})
    stored_hash = input_data.get("stored_hash", "")
    try:
        import face_recognition, numpy as np
        encoding = biometric_data.get("face_encoding")
        stored_encoding = biometric_data.get("stored_encoding")
        if encoding and stored_encoding:
            dist = face_recognition.face_distance([np.array(stored_encoding)], np.array(encoding))[0]
            authenticated = bool(dist < 0.6)
            confidence = round(float(1.0 - dist), 3)
            return {"authenticated": authenticated, "confidence": confidence, "status": "success"}
    except ImportError:
        pass
    import hashlib
    data_str = str(sorted(biometric_data.items())).encode()
    h = hashlib.sha256(data_str).hexdigest()
    authenticated = (stored_hash == h) if stored_hash else False
    return {"authenticated": authenticated, "confidence": 0.95 if authenticated else 0.05, "hash": h, "status": "success"}
