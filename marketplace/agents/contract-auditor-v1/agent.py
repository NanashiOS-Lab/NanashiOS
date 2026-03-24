def run(input_data):
    """Contract Auditor - NanashiOS. Analyse de vulnérabilités de smart contracts."""
    contract_code = input_data.get("contract_code", "")
    if not contract_code.strip():
        return {"vulnerabilities": [], "risk_score": 0.0, "status": "success"}
    PATTERNS = {
        "Reentrancy": ["call.value","transfer","send"],
        "Integer Overflow": ["+=","-=","*=","++","--"],
        "tx.origin": ["tx.origin"],
        "Unchecked return": ["call(","delegatecall(","staticcall("],
        "Self-destruct": ["selfdestruct","suicide"],
        "Timestamp dependence": ["block.timestamp","now"],
    }
    found = []
    for vuln, patterns in PATTERNS.items():
        if any(p in contract_code for p in patterns):
            found.append(vuln)
    risk = round(min(len(found) * 0.15, 0.95), 2)
    return {"vulnerabilities": found, "vuln_count": len(found), "risk_score": risk,
            "summary": f"{len(found)} vulnérabilité(s) détectée(s).", "status": "success"}
