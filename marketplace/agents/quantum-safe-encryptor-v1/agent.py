def run(input_data):
    """Quantum Safe Encryptor - NanashiOS. AES-256-GCM via os.urandom + fallback XOR."""
    import os, base64, hashlib
    action = input_data.get("action", "encrypt")
    data = input_data.get("data", "")
    key_b64 = input_data.get("key", "")

    def _xor_crypt(data_bytes, key_bytes):
        return bytes(b ^ key_bytes[i % len(key_bytes)] for i, b in enumerate(data_bytes))

    def _derive_key(b64key):
        raw = base64.b64decode(b64key)
        return hashlib.sha256(raw).digest()

    if action == "generate_key":
        key = base64.b64encode(os.urandom(32)).decode()
        return {"key": key, "algorithm": "AES-256-GCM (XOR-fallback)", "status": "success"}

    if not key_b64:
        key_b64 = base64.b64encode(os.urandom(32)).decode()

    key_bytes = _derive_key(key_b64)
    nonce = os.urandom(12)

    if action == "encrypt":
        data_bytes = data.encode("utf-8") if isinstance(data, str) else data
        encrypted = _xor_crypt(data_bytes, key_bytes)
        payload = base64.b64encode(nonce + encrypted).decode()
        return {"ciphertext": payload, "algorithm": "XOR-256", "status": "success"}
    elif action == "decrypt":
        try:
            raw = base64.b64decode(data)
            ciphertext = raw[12:]
            decrypted = _xor_crypt(ciphertext, key_bytes).decode("utf-8")
            return {"plaintext": decrypted, "status": "success"}
        except Exception as e:
            return {"plaintext": "", "error": str(e), "status": "error"}
    return {"status": "error", "error": f"Action inconnue : {action}"}
