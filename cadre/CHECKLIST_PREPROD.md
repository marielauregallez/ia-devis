# Checklist pre-production

Utiliser cette checklist avant de deployer le projet dans une PME.

## 1) Donnees et regles metier

- [ ] `metier/entreprise/identite.md` complete et valide
- [ ] `metier/entreprise/mentions-legales.md` revu par responsable metier
- [ ] `metier/catalogue/services.json` relu (pas de prix incoherents)
- [ ] `metier/catalogue/regles-tarification.md` valide (remises/supplements)

## 2) Qualite technique

- [ ] Tests passent en local (`pytest -q`)
- [ ] Validation des schemas OK (`python technique/scripts/valider_schemas.py`)
- [ ] CI GitHub verte sur `main`
- [ ] Version des regles (`rule_version`) definie dans l'environnement

## 3) Gouvernance et controle

- [ ] Processus de validation humaine documente
- [ ] RACI confirme (qui valide, qui approuve)
- [ ] Registre des risques initialise (`RISKS.md`)
- [ ] Procedure de gestion incident IA validee

## 4) Conformite et securite

- [ ] Politique donnees validee (`DATA_POLICY.md`)
- [ ] Duree de retention des devis definie
- [ ] Donnees sensibles non committees dans Git
- [ ] Cles API stockees hors repo (variables d'environnement)

## 5) Go-live

- [ ] Cas de test "devis simple" valide de bout en bout
- [ ] Cas de test "devis complexe" valide de bout en bout
- [ ] Equipe metier formee (30-60 min)
- [ ] Responsable interne nomme pour suivi mensuel
