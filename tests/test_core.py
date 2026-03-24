"""
Tests — Core NanashiOS (LinkPro, Ghosts, WakaEngine)
"""
import sys
import os
import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))


def test_link_pro_is_active():
    from core.link_pro import link_pro
    assert link_pro.is_active is True


def test_link_pro_ingress_strips():
    from core.link_pro import link_pro
    assert link_pro.usl_ingress("  bonjour  ") == "bonjour"


def test_link_pro_egress_returns_string():
    from core.link_pro import link_pro
    result = link_pro.edl_egress("test output")
    assert isinstance(result, str)
    assert "test output" in result


def test_link_pro_egress_masks_brand():
    from core.link_pro import link_pro
    result = link_pro.edl_egress("NanashiOS est souverain")
    assert "NanashiOS" not in result
    assert "[MASK]" in result


def test_ghost_blinky_analyze_task():
    from core.ghosts import blinky
    result = blinky.analyze_task("résume ce texte")
    assert isinstance(result, str)
    assert len(result) > 0


def test_shadow_critique_short_response():
    from core.ghosts import shadow
    result = shadow.critique("TestAgent", "Ok.", "une question")
    assert result["status"] == "critique"
    assert "Réponse trop courte" in result["points"]


def test_shadow_critique_valid_response():
    from core.ghosts import shadow
    result = shadow.critique("TestAgent", "Voici une analyse complète et détaillée du sujet demandé, avec les éléments nécessaires à la compréhension.", "une question")
    assert result["status"] == "validé"


def test_waka_engine_routing_resume():
    from core.waka_engine import waka
    result = waka.process_query("résume ce texte long")
    assert result["status"] == "success"
    assert result["agent"] == "ResumeTexte"


def test_waka_engine_routing_code():
    from core.waka_engine import waka
    result = waka.process_query("écris du code python pour trier une liste")
    assert result["status"] == "success"
    assert result["agent"] == "CodeWriter"


def test_waka_engine_routing_translation():
    from core.waka_engine import waka
    result = waka.process_query("traduis en anglais : bonjour")
    assert result["status"] == "success"
    assert result["agent"] == "Traduction"


def test_waka_engine_response_is_protected():
    from core.waka_engine import waka
    result = waka.process_query("test")
    assert "ε_start:" in result["response"]
    assert "ε_end:" in result["response"]


def test_config_language():
    from config.settings import settings
    assert settings.LANGUAGE == "fr"
    assert "fr" in settings.SUPPORTED_LANGUAGES
