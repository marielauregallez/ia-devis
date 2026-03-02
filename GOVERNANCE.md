# Gouvernance du systeme `ia-devis`

## Objectif

Ce document definit les regles de gouvernance pour utiliser `ia-devis` de maniere fiable, responsable et conforme.

## Validation humaine obligatoire

- Aucun devis ne doit etre envoye automatiquement au client.
- Un humain valide explicitement les elements critiques avant generation finale :
  - prestations selectionnees,
  - prix unitaires,
  - remises appliquees,
  - total HT/TTC,
  - hypotheses emises.
- La validation humaine est une etape de controle qualite et de responsabilite legale.

## Gestion des erreurs IA

- Si la sortie IA est invalide (format, calcul, incoherence), la generation est interrompue.
- En cas d'ambiguite dans la demande client, le systeme doit :
  1. signaler l'incertitude,
  2. formuler des hypotheses explicites,
  3. demander confirmation avant finalisation.
- Les erreurs doivent etre traitees en mode "fail safe" : pas de devis final sans correction ou validation.

## Journalisation

- Les operations importantes doivent etre tracables :
  - date/heure de generation,
  - source de la demande client,
  - version des regles de tarification,
  - utilisateur ayant valide le devis.
- Les journaux doivent permettre un audit posteriori (qui a valide quoi, quand).
- Les journaux ne doivent pas exposer de donnees sensibles inutilement.

## Controle de derive

- Revue periodique des devis generes pour detecter :
  - surestimation/sous-estimation recurrente,
  - usage incoherent des remises,
  - biais de selection de prestations.
- Comparaison echantillonnee entre devis produits et decisions metier attendues.
- Mise a jour des regles metier (`2-catalogue/`) lorsque des ecarts repetes sont observes.

## Securite des donnees

- Principe de minimisation : ne stocker que les informations necessaires au devis.
- Protection des fichiers contenant des donnees clients (`3-clients/`, `5-devis-genere/`).
- Acces limite aux personnes autorisees (controle d'acces du poste/depot).
- Ne jamais publier de donnees clients reelles dans un depot public.
- Rotation et protection des cles API si utilisation d'un service LLM externe.

## Conformite (RGPD et reglementations applicables)

- Base legale et finalite explicite : utilisation des donnees uniquement pour produire des devis.
- Droit des personnes : correction/suppression des donnees clients sur demande.
- Limitation de conservation : definir une duree de retention et purger les donnees obsoletees.
- Transparence : informer les clients qu'un systeme assiste par IA peut etre utilise dans la preparation.
- Encadrement contractuel des sous-traitants IA (DPA, localisation des donnees, garanties de securite).
- Verification reguliere de conformite selon le pays cible (RGPD, nLPD, etc.).

## Cadence de revue recommandee

- Revue operationnelle : mensuelle
- Revue securite/conformite : trimestrielle
- Revue complete du dispositif de gouvernance : semestrielle
