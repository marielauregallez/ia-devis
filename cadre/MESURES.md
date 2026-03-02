# Mesures de performance et valeur business

## Objectif

Ce document propose un cadre simple pour mesurer l'impact du systeme `ia-devis` :
- gain de temps,
- cout d'utilisation IA,
- ROI potentiel,
- methode de mesure reproductible.

## Temps avant / apres

## Indicateurs a suivre

- **Temps moyen de preparation d'un devis** (de la demande client a la version prete a envoi)
- **Temps de relecture/validation humaine**
- **Temps total de cycle devis**

## Exemple de baseline (a adapter)

- **Avant (manuel)** : 90 min / devis
- **Apres (avec ia-devis)** : 30 min / devis
- **Gain net** : 60 min / devis

## Formule

`Gain de temps par devis = Temps avant - Temps apres`

`Gain de temps mensuel = Gain par devis x Nombre de devis/mois`

## Coût API estime

Le cout depend du modele choisi, du volume de tokens et du nombre de devis.

## Variables

- `C_prompt` : cout moyen du prompt par devis
- `C_sortie` : cout moyen de la reponse par devis
- `N` : nombre de devis par mois

## Formule

`Cout API mensuel = (C_prompt + C_sortie) x N`

## Ordre de grandeur (illustratif)

- Prompt + sortie : ~CHF 0.05 a CHF 0.40 / devis (selon modele et longueur)
- Pour 100 devis/mois : ~CHF 5 a CHF 40 / mois

> Important : utiliser les tarifs officiels du fournisseur LLM au moment du calcul.

## ROI potentiel

## Hypotheses

- `T_gain` : gain de temps moyen par devis (heures)
- `C_horaire` : cout horaire charge de la personne qui produit le devis
- `N` : volume mensuel de devis
- `C_API` : cout API mensuel
- `C_exploit` : autres couts mensuels (maintenance, supervision)

## Formules

`Valeur temps economisee/mois = T_gain x C_horaire x N`

`ROI mensuel brut = Valeur temps economisee/mois - (C_API + C_exploit)`

`ROI % = ROI mensuel brut / (C_API + C_exploit) x 100`

## Exemple (illustratif)

- Gain : 1h/devis
- Cout horaire : CHF 80
- Volume : 60 devis/mois
- Cout API + exploitation : CHF 300/mois

`Valeur = 1 x 80 x 60 = CHF 4'800/mois`

`ROI brut = 4'800 - 300 = CHF 4'500/mois`

## Methode de mesure (recommandee)

## 1) Periode de reference (avant)

- Mesurer sur 2 a 4 semaines en mode actuel.
- Relever pour chaque devis :
  - date/heure debut,
  - date/heure fin,
  - personne chargee,
  - niveau de complexite (simple/moyen/complexe).

## 2) Periode pilote (apres)

- Mesurer sur 2 a 4 semaines avec `ia-devis`.
- Conserver les memes indicateurs + :
  - nombre d'allers-retours de correction,
  - cout API estime par devis,
  - incidents ou erreurs de sortie.

## 3) Comparaison

- Comparer par niveau de complexite (pas seulement moyenne globale).
- Exclure les cas atypiques (outliers) et documenter pourquoi.
- Produire un tableau de synthese mensuel :
  - temps avant/apres,
  - gain total,
  - cout API,
  - ROI.

## 4) Gouvernance de la mesure

- Revue mensuelle avec un responsable metier.
- Recalibrage trimestriel des hypothese de cout/temps.
- Archivage des mesures pour suivre les tendances dans le temps.
