# ÉTAPE 00 — Initialisation du projet

**Statut :** `PASS` (8 / 8 sous-tâches)  
**Branche Git :** `phase/00-init`  
**Commit associé :** Validé et fusionné dans `main` / `develop`

---

## Objectif
Établir les fondations du projet : dépôt Git, gouvernance documentaire, structure d'arborescence, CI/CD, et tableau de bord de suivi d'avancement.

## Travail réalisé
- Dépôt GitHub configuré avec branche `main` et remote `origin`.
- `.gitignore` rédigé (données SIG brutes, caches, binaires).
- Convention de commits sémantiques définie dans `AGENT_RULES.md`.
- Guide `docs/GIT_WORKFLOW_AND_CICD.md` rédigé.
- Pipeline CI/CD GitHub Actions `.github/workflows/ci.yml` mis en place.
- Arborescence racine matérialisée : `src/`, `tests/`, `docker/`, `data/raw/`, `data/processed/`, `data/vector/`, `data/raster/` (avec `.gitkeep`).
- Scripts de suivi : `scripts/update_progress.py` et `scripts/test_progress_calculation.py`.
- Documents maîtres créés : `MASTER_PROMPT.md`, `PROJECT_MEMORY.md`, `AGENT_RULES.md`, `docs/ROADMAP.md`, `docs/ETAT_AVANCEMENT.md`, `docs/ARCHITECTURE.md` (6 diagrammes SVG), `docs/dashboard.html`.

## Fichiers créés / modifiés
- `MASTER_PROMPT.md`, `PROJECT_MEMORY.md`, `AGENT_RULES.md`, `PROJECT_PROMPT.md`
- `.gitignore`, `.github/workflows/ci.yml`
- `docs/ROADMAP.md`, `docs/ETAT_AVANCEMENT.md`, `docs/ARCHITECTURE.md`, `docs/GIT_WORKFLOW_AND_CICD.md`, `docs/REFERENCE_CHECKLIST.md`, `docs/dashboard.html`
- `docs/assets/architecture/` (6 SVG + sources)
- `docs/assets/progress/progress_donut.svg`, `docs/assets/progress/progress_data.json`
- `scripts/update_progress.py`, `scripts/test_progress_calculation.py`
- `src/`, `tests/`, `docker/`, `data/raw/`, `data/processed/`, `data/vector/`, `data/raster/` (`.gitkeep`)

## Décisions validées
- **Global Mapper** = unique outil SIG/ETL du projet.
- **Échelon bataillon** = niveau minimal tactique.
- **Principe « Autonomous First — CommandView Ready »**.
- Séparation stricte données brutes (hors Git) / données transformées (sous Git via `.gitkeep`).
- Suivi d'avancement automatique uniquement via script (`update_progress.py` + `ROADMAP.md`).

## Points importants pour la suite
- Ne jamais modifier manuellement le pourcentage dans `ETAT_AVANCEMENT.md`.
- Toujours cocher dans `ROADMAP.md` puis exécuter `python scripts/update_progress.py`.
- Chaque phase = branche dédiée `phase/XX-nom`.
