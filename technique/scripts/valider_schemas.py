import json
from pathlib import Path

from jsonschema import validate


ROOT_DIR = Path(__file__).resolve().parent.parent.parent
SCHEMAS_DIR = ROOT_DIR / "technique" / "schemas"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def main():
    services_schema = load_json(SCHEMAS_DIR / "services.schema.json")
    devis_schema = load_json(SCHEMAS_DIR / "devis.schema.json")

    services_data = load_json(ROOT_DIR / "metier" / "catalogue" / "services.json")
    sample_devis_data = load_json(ROOT_DIR / "technique" / "tests" / "sample_devis.json")

    validate(instance=services_data, schema=services_schema)
    validate(instance=sample_devis_data, schema=devis_schema)

    print("Schemas valides.")


if __name__ == "__main__":
    main()
