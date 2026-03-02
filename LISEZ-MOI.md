# Generateur de devis IA

Un assistant intelligent qui vous aide a creer des devis professionnels, sans aucune competence technique.

## Pour qui, pourquoi ?
PME de services (BTP, architecture, IT, conseil, maintenance industrielle).

Contexte:
-environ 30 à 200 devis/mois générés
-Temps moyen de rédaction : 20 à 60 min
-Forte variabilité selon le commercial
-Oublis fréquents de lignes
-Difficulté à harmoniser les formulations
-Marge parfois incohérente
-Temps non facturé élevé
-Risque d’erreurs tarifaires
-Manque de standardisation
-Dépendance à 1 ou 2 personnes “qui savent faire”

## Objectif du système
Accélérer la rédaction des devis
Standardiser la structure des devis
Sécuriser les marges
Maintenir validation humaine

## Comment ca marche ?

Vous repondez a quelques questions dans le chat, l'agent s'occupe du reste :
il remplit vos informations, configure vos tarifs, et genere vos devis.

## Demarrage rapide

### 1. Installer Cursor

Telechargez et installez [Cursor](https://cursor.sh), un editeur de code avec IA integree.

### 2. Recuperer le projet

Cliquez sur **"Use this template"** sur GitHub (ou clonez le depot), puis ouvrez le dossier dans Cursor.

### 3. Lancer la configuration

Ouvrez le chat Cursor (Ctrl+L) et dites simplement :

> Bonjour

L'agent vous guidera a travers la configuration de votre generateur de devis.
Il vous posera des questions sur :

1. **Votre entreprise** - nom, adresse, activite, equipe
2. **Vos conditions** - TVA, acompte, delai de paiement, garantie
3. **Vos services** - ce que vous vendez, a quel prix
4. **Vos tarifs** - remises, supplements, regles de facturation
5. **Votre logo** - pour l'integrer dans les devis

### 4. Generer un devis

Une fois configure, collez simplement la demande d'un client dans le chat.
L'agent :
- identifie les services concernes
- calcule les prix, remises et TVA
- vous montre un recapitulatif pour validation
- genere un document pret a envoyer (HTML/PDF)

## Organisation du projet

```
ia_devis/
|
|-- LISEZ-MOI.md ................. Ce fichier
|
|-- 1-entreprise/ ................ Vos informations
|   |-- identite.md
|   |-- mentions-legales.md
|   +-- (votre logo)
|
|-- 2-catalogue/ ................. Vos services et tarifs
|   |-- services.json
|   +-- regles-tarification.md
|
|-- 3-clients/ ................... Votre base clients
|   |-- fichier-clients.json
|   +-- historique-devis.json
|
|-- 4-nouvelle-demande/ .......... La demande a traiter
|   +-- demande-client.txt
|
|-- 5-devis-genere/ .............. Le resultat
|   |-- devis.json
|   |-- devis.md
|   +-- devis.html
|
|-- _installation/ ............... Suivi de la configuration
|   +-- etat.json
|
|-- _technique/ .................. Scripts (pas besoin d'y toucher)
|   |-- generer_devis.py
|   |-- generer_pdf.py
|   +-- requirements.txt
|
+-- .cursor/rules/ ............... Comportement de l'agent
    +-- agent-devis.mdc
```

## Modifier vos informations

Vous pouvez a tout moment demander a l'agent dans le chat :

- "Modifie le nom de mon entreprise"
- "Ajoute un nouveau service a CHF 2'000"
- "Change la remise pour les associations"

Ou editez directement les fichiers dans les dossiers correspondants.

## Ce que le systeme fait

- Analyse une demande client
- Identifie les services concernes dans votre catalogue
- Applique vos regles de tarification
- Genere un devis structure et un document lisible

## Ce que le systeme ne fait PAS

- Envoyer le devis au client
- Valider juridiquement le contenu
- Negocier avec le client

## Important

**Tout devis genere doit etre relu et valide par un humain avant envoi.**

## KPI

## Lien vers vidéos démo
