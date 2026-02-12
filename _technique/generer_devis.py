import os
import json
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

# -------------------------
# Configuration
# -------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

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

# -------------------------
# Appel LLM
# -------------------------

def appeler_llm(prompt):
    load_dotenv()
    client = OpenAI()

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}],
        temperature=0
    )

    return response.choices[0].message.content

# -------------------------
# Principal
# -------------------------

def main():
    verifier_fichiers()

    entreprise = charger_texte(ENTREPRISE_DIR / "identite.md")
    mentions = charger_texte(ENTREPRISE_DIR / "mentions-legales.md")
    services = charger_json(CATALOGUE_DIR / "services.json")
    tarification = charger_texte(CATALOGUE_DIR / "regles-tarification.md")
    demande = charger_texte(DEMANDE_DIR / "demande-client.txt")

    prompt = construire_prompt(entreprise, mentions, services, tarification, demande)

    reponse_brute = appeler_llm(prompt)

    # Tentative de parsing JSON
    try:
        donnees_devis = json.loads(reponse_brute)
    except json.JSONDecodeError:
        raise ValueError("La reponse du modele n'est pas un JSON valide.")

    RESULTAT_DIR.mkdir(exist_ok=True)

    with open(RESULTAT_DIR / "devis.json", "w", encoding="utf-8") as f:
        json.dump(donnees_devis, f, indent=2, ensure_ascii=False)

    print("Devis genere avec succes.")

if __name__ == "__main__":
    main()
