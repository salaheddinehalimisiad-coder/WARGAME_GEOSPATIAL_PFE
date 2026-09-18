# PROJECT MEMORY

## État actuel du projet
L'**ÉTAPE 00 — Initialisation du projet** est officiellement validée (**`PASS`**) :
- **Arborescence normalisée matérialisée** :
  - Racines créées : `src/`, `tests/`, `docker/`, `data/` (avec `docs/` et `scripts/` déjà existants).
  - Sous-dossiers de données créés : `data/raw/`, `data/processed/`, `data/vector/`, `data/raster/`.
  - Fichiers `.gitkeep` pour versionner la structure sans stocker de données volumineuses.
  - Aucun code métier ni donnée SIG importée prématurément.
- **Roadmap officielle source unique de vérité** : [`docs/ROADMAP.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ROADMAP.md) avec 31 étapes et 247 sous-tâches uniques (`PXX-TYY-SZZ`).
- **Suivi d'avancement consolidé** :
  - **Avancement global calculé** : **3,24 %** (8 sous-tâches cochées sur 247 au total).
  - **Étapes terminées (PASS)** : **1 / 31** (ÉTAPE 00 validée à 100,00 %).
  - **Étape active** : **ÉTAPE 01 — Analyse détaillée du cahier des charges** (Statut : `PLANNED`, 0 / 7 sous-tâches — 0,00 %).
  - **Sous-tâches validées de l'ÉTAPE 00 (8/8)** :
    - `P00-T01-S01` [x] (Dépôt distant GitHub avec branche `main`).
    - `P00-T01-S02` [x] (Fichier `.gitignore` excluant caches, binaires et rasters volumineux).
    - `P00-T01-S03` [x] (Guide de gestion des branches dans `docs/GIT_WORKFLOW_AND_CICD.md`).
    - `P00-T01-S04` [x] (Convention de commits sémantiques dans `AGENT_RULES.md`).
    - `P00-T02-S01` [x] (Arborescence `src/`, `tests/`, `data/`, `docs/`, `scripts/`, `docker/`).
    - `P00-T02-S02` [x] (Sous-dossiers `data/raw/`, `data/processed/`, `data/vector/`, `data/raster/`).
    - `P00-T02-S03` [x] (Pipeline CI `.github/workflows/ci.yml` opérationnel).
    - `P00-T02-S04` [x] (Validation locale des scripts d'intégrité réussie).
- **Tableau de bord synchronisé** : [`docs/ETAT_AVANCEMENT.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ETAT_AVANCEMENT.md) généré automatiquement avec donut vectoriel [`docs/assets/progress/progress_donut.svg`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/assets/progress/progress_donut.svg) et application interactive [`docs/dashboard.html`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/dashboard.html).
- **Architecture visuelle validée** : 6 diagrammes vectoriels SVG sur fond blanc (#ffffff) dans [`docs/ARCHITECTURE.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ARCHITECTURE.md) et leurs sources éditables dans `docs/assets/architecture/source/`.

## Référence officielle
`Cahier_des_charges_PFE_Wargame_geospatial.docx` — Version 1.0 (PFE 2026–2027).

## Règles maîtresses
- **SIG & ETL** : Global Mapper est l'unique outil SIG du workflow courant (aucun SIG concurrent actif).
- **Principe d'intégration** : « Autonomous First — CommandView Ready » (PFE 100% autonome, architecture et APIs préparées pour une intégration ultérieure dans le C4ISR CommandView).
- **Unités** : Niveau minimal d'agrégation fixé au bataillon.
- **Équipements** : Capacités abstraites uniquement (aucune arme réelle détaillée).
- **Incertitude** : Séparation stricte État Réel (Umpire) vs État Perçu (Blue/Red).
- **Suivi d'avancement** : Ne jamais modifier manuellement le pourcentage d'avancement ; toujours cocher les sous-tâches réelles dans `docs/ROADMAP.md` puis exécuter `python scripts/update_progress.py`.
- **Développement** : Progression séquentielle stricte, une seule étape active à la fois, validation par preuves, zéro développement prématuré d'étapes aval.

## Prochaine étape
**ÉTAPE 01 — Analyse détaillée du cahier des charges** (Statut : `PLANNED`. En attente de validation et d'instruction formelle de démarrage).

## Historique récent
- **Validation PASS ÉTAPE 00** : Matérialisation de l'arborescence normalisée (`src/`, `tests/`, `docker/`, `data/raw/`, `data/processed/`, `data/vector/`, `data/raster/`) avec fichiers `.gitkeep` ; validation des 8 sous-tâches de l'étape 00 ; passage du statut Étape 00 à PASS (100 %) ; avancement global à 3,24 %.
- **Audit & correction documentaire** : Épuration des exigences arbitraires dans `docs/ROADMAP.md`, `docs/ARCHITECTURE.md` et les SVG ; harmonisation NoData ; recalibration stricte sur les faits vérifiés.
- **Mise à niveau documentaire initiale** : Création de la roadmap 31 étapes avec 247 sous-tâches, script autonome de calcul et donut SVG, dashboard d'avancement, 6 diagrammes d'architecture SVG sur fond blanc avec sources éditables.
