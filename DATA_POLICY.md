# Politique de donnees (DATA_POLICY)

## Objectif

Definir les principes de gestion des donnees clients dans `ia-devis` pour rester conforme et limiter les risques.

## 1) Minimisation

- Collecter uniquement les donnees necessaires au devis.
- Eviter de stocker des informations non utiles (notes medicales, infos RH, etc.).
- Limiter la granularite des donnees dans les historiques.

## 2) Retention

- Devis et historiques: retention par defaut de 24 mois (a ajuster selon contexte legal).
- Purge trimestrielle des donnees obsoletees.
- Archivage separe si conservation legale obligatoire.

## 3) Anonymisation

- Pour les demos et formations, remplacer :
  - noms de personnes,
  - emails,
  - telephones,
  - adresses exactes.
- Ne jamais publier de donnees reelles dans un depot public.

## 4) Securite

- Variables d'environnement pour les cles API.
- Acces limite aux personnes autorisees.
- Sauvegardes chiffrees recommandees.
- Journaliser les acces et modifications critiques.

## 5) Droits des personnes (RGPD)

- Droit d'acces/correction/suppression sur demande.
- Tracer les demandes et delais de traitement.
- Informer clairement les clients de l'usage d'outils IA dans la preparation des devis.

## 6) Sous-traitants IA

- Verifier les conditions contractuelles (DPA).
- Verifier la localisation des donnees et garanties de securite.
- Eviter d'envoyer des donnees sensibles non necessaires au modele.
