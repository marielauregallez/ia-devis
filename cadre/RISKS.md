# Registre de risques IA

Ce registre suit les risques principaux du systeme et les actions de mitigation.

| ID | Risque | Impact | Probabilite | Niveau | Mitigation | Proprietaire |
|---|---|---|---|---|---|---|
| R1 | Mauvaise selection de prestation | Eleve | Moyen | Eleve | Validation humaine obligatoire avant envoi | Responsable metier |
| R2 | Erreur de calcul remise/TVA | Eleve | Faible | Moyen | Tests + schema + revue humaine | IT/IA |
| R3 | Hallucination (service invente) | Eleve | Moyen | Eleve | Prompt strict + schema + controle metier | IT/IA |
| R4 | Exposition de donnees client | Tres eleve | Faible | Eleve | Minimisation + acces restreint + purge periodique | DPO/IT |
| R5 | Derive des performances dans le temps | Moyen | Moyen | Moyen | Revue mensuelle d'echantillons de devis | Responsable metier |
| R6 | Dependance a un fournisseur LLM unique | Moyen | Moyen | Moyen | Couche adapters multi-provider (OpenAI/Azure/Mistral/Ollama) | IT/IA |

## Processus de suivi

- Mise a jour mensuelle du registre.
- Revue trimestrielle des niveaux de risque.
- Incident critique: mise a jour immediate et plan d'action sous 5 jours ouvres.
