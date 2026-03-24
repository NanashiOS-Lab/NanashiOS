"""
Tests — Validité des manifests NanashiOS
"""
import json
import glob
import os
import pytest


def all_manifests():
    root = os.path.dirname(os.path.dirname(__file__))
    paths = (
        glob.glob(os.path.join(root, "agents", "*/manifest.json")) +
        glob.glob(os.path.join(root, "marketplace", "agents", "*/manifest.json")) +
        [os.path.join(root, "manifest.json"),
         os.path.join(root, "index.json"),
         os.path.join(root, "marketplace", "index.json")]
    )
    return [p for p in paths if os.path.exists(p)]


@pytest.mark.parametrize("path", all_manifests())
def test_manifest_valid_json(path):
    """Chaque manifest doit être du JSON valide."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    assert isinstance(data, dict)


@pytest.mark.parametrize("path", [
    p for p in all_manifests()
    if "agents" in p and "index" not in p
])
def test_manifest_required_fields(path):
    """Chaque manifest d'agent doit avoir id, name, description, license."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    for field in ("id", "name", "description", "license"):
        assert field in data, f"Champ '{field}' manquant dans {path}"
    assert data["license"].startswith("BSL"), f"Licence inattendue dans {path}"


@pytest.mark.parametrize("path", [
    p for p in all_manifests()
    if "agents" in p and "index" not in p
])
def test_manifest_has_name_fr(path):
    """Chaque manifest d'agent doit avoir un champ name_fr (support français)."""
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    assert "name_fr" in data, f"name_fr manquant dans {path}"
    assert data["name_fr"].strip(), f"name_fr vide dans {path}"


def index_agents():
    root = os.path.dirname(os.path.dirname(__file__))
    result = []
    for idx_path in [
        os.path.join(root, "index.json"),
        os.path.join(root, "marketplace", "index.json"),
    ]:
        if not os.path.exists(idx_path): continue
        with open(idx_path, encoding="utf-8") as f:
            data = json.load(f)
        base = os.path.dirname(idx_path)
        for agent in data.get("agents", []):
            full_path = os.path.join(base, agent["path"])
            result.append((agent["id"], full_path))
    return result


@pytest.mark.parametrize("agent_id,manifest_path", index_agents())
def test_index_references_exist(agent_id, manifest_path):
    """Chaque agent référencé dans index.json doit avoir un manifest existant."""
    assert os.path.exists(manifest_path), (
        f"Agent '{agent_id}' référencé mais manifest introuvable : {manifest_path}"
    )
