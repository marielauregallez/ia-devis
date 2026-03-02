import json
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
if str(BASE_DIR) not in sys.path:
    sys.path.insert(0, str(BASE_DIR))

from adapters.factory import build_provider  # noqa: E402

# -------------------------
# Configuration
# -------------------------

ENTREPRISE_DIR = BASE_DIR / "1-entreprise"
CATALOGUE_DIR = BASE_DIR / "2-catalogue"
DEMANDE_DIR = BASE_DIR / "4-nouvelle-demande"
RESULTAT_DIR = BASE_DIR / "5-devis-genere"

FICHIERS_REQUIS = [
    ENTREPRISE_DIR / "identite.md",
    ENTREPRISE_DIR / "mentions-legales.md",
    CATALOGUE_DIR / "services.json",
    CATALOGUE_DIR / "regles-tarification.md",
    DEMANDE_DIR / "demande-client.txt"
]

# -------------------------
# Utilitaires
# -------------------------

def verifier_fichiers():
    for fichier in FICHIERS_REQUIS:
        if not fichier.exists():
            raise FileNotFoundError(f"Fichier manquant : {fichier}")

def charger_texte(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return f.read()

def charger_json(chemin):
    with open(chemin, "r", encoding="utf-8") as f:
        return json.load(f)

# -------------------------
# Construction du prompt
# -------------------------

def construire_prompt(entreprise, mentions, services, tarification, demande):
    return f"""
Tu es un assistant chargé de préparer un devis.

CONTEXTE ENTREPRISE :
{entreprise}

CONTRAINTES LÉGALES :
{mentions}

SERVICES DISPONIBLES :
{json.dumps(services, indent=2)}

RÈGLES DE TARIFICATION :
{tarification}

DEMANDE CLIENT :
{demande}

Instructions :
- N'invente aucun service non listé.
- N'invente aucun prix.
- Si une information manque, fais une hypothèse explicite.
- Réponds uniquement en JSON strict selon le format défini.
"""

def extraire_json_strict(texte):
    texte = texte.strip()
    if texte.startswith("```"):
        lignes = texte.splitlines()
        lignes = [line for line in lignes if not line.strip().startswith("```")]
        texte = "\n".join(lignes).strip()
    return json.loads(texte)

# -------------------------
# Principal
# -------------------------

def main():
    load_dotenv()
    verifier_fichiers()

    entreprise = charger_texte(ENTREPRISE_DIR / "identite.md")
    mentions = charger_texte(ENTREPRISE_DIR / "mentions-legales.md")
    services = charger_json(CATALOGUE_DIR / "services.json")
    tarification = charger_texte(CATALOGUE_DIR / "regles-tarification.md")
    demande = charger_texte(DEMANDE_DIR / "demande-client.txt")

    prompt = construire_prompt(entreprise, mentions, services, tarification, demande)

    provider_name = os.getenv("LLM_PROVIDER", "openai")
    model = os.getenv("LLM_MODEL", "gpt-4o-mini")
    rule_version = os.getenv("RULE_VERSION", "2026.03")

    provider = build_provider(provider_name)
    reponse_brute = provider.generate_quote(
        prompt=prompt,
        config={
            "model": model,
            "temperature": 0,
            "api_key": os.getenv("OPENAI_API_KEY"),
            "azure_api_key": os.getenv("AZURE_OPENAI_API_KEY"),
            "azure_endpoint": os.getenv("AZURE_OPENAI_ENDPOINT"),
            "azure_api_version": os.getenv("AZURE_OPENAI_API_VERSION", "2024-10-21"),
            "mistral_api_key": os.getenv("MISTRAL_API_KEY"),
            "ollama_base_url": os.getenv("OLLAMA_BASE_URL", "http://localhost:11434"),
        },
    )

    # Tentative de parsing JSON
    try:
        donnees_devis = extraire_json_strict(reponse_brute)
    except json.JSONDecodeError:
        raise ValueError("La reponse du modele n'est pas un JSON valide.")

    if isinstance(donnees_devis, dict):
        devis = donnees_devis.setdefault("devis", {})
        if isinstance(devis, dict):
            devis["rule_version"] = rule_version

    RESULTAT_DIR.mkdir(exist_ok=True)

    with open(RESULTAT_DIR / "devis.json", "w", encoding="utf-8") as f:
        json.dump(donnees_devis, f, indent=2, ensure_ascii=False)

    print("Devis genere avec succes.")

if __name__ == "__main__":
    main()
