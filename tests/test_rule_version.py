import json
from pathlib import Path


def test_devis_template_has_comment_or_rule_version():
    devis_path = Path("5-devis-genere/devis.json")
    assert devis_path.exists()
    data = json.loads(devis_path.read_text(encoding="utf-8"))
    assert "_commentaire" in data or "devis" in data
