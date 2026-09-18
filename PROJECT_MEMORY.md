# PROJECT MEMORY

## État actuel du projet
Audit et correction finale de la mise à niveau structurelle et documentaire achevés :
- **Roadmap officielle épurée** : 31 étapes officielles (ÉTAPE 00 à ÉTAPE 30) découpées en 247 sous-tâches concrètes (`PXX-TYY-SZZ`) dans [`docs/ROADMAP.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ROADMAP.md), expurgée de toute exigence technique arbitraire (aucun seuil de latence sans mesure, aucun FPS imposé, aucun nombre de tours arbitraire, aucune source imposée avant collecte).
- **Source de vérité unique** : `docs/ROADMAP.md` constitue l'unique référence des cases à cocher (`- [ ]` / `- [x]`). Seules les sous-tâches ayant une preuve réelle et tangible sont cochées.
- **Suivi d'avancement réel consolidé** :
  - **Avancement global calculé** : **2,43 %** (6 sous-tâches cochées sur 247 au total).
  - **Étape active** : **ÉTAPE 00 — Initialisation du projet**.
  - **Statut étape active** : `IN_PROGRESS` (6 / 8 sous-tâches terminées, soit 75,00 %).
  - **Détail des preuves ÉTAPE 00** :
    - `P00-T01-S01` [x] (Dépôt distant GitHub configuré avec branche `main`).
    - `P00-T01-S02` [x] (Fichier `.gitignore` interdisant caches, binaires et rasters volumineux).
    - `P00-T01-S03` [x] (Guide de gestion des branches dans `docs/GIT_WORKFLOW_AND_CICD.md`).
    - `P00-T01-S04` [x] (Convention de commits sémantiques dans `AGENT_RULES.md`).
    - `P00-T02-S01` [ ] (Arborescence src/tests/data/docker non encore créée sur le disque — statut TODO).
    - `P00-T02-S02` [ ] (Sous-dossiers data/ non encore créés — statut TODO).
    - `P00-T02-S03` [x] (Pipeline CI `.github/workflows/ci.yml` opérationnel).
    - `P00-T02-S04` [x] (Validation locale des scripts d'intégrité réussie).
- **Tableau de bord synchronisé** : [`docs/ETAT_AVANCEMENT.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ETAT_AVANCEMENT.md) généré automatiquement avec donut vectoriel [`docs/assets/progress/progress_donut.svg`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/assets/progress/progress_donut.svg) et application interactive [`docs/dashboard.html`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/dashboard.html).
- **Architecture visuelle validée** : 6 diagrammes vectoriels SVG sur fond blanc (#ffffff) dans [`docs/ARCHITECTURE.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ARCHITECTURE.md) et leurs sources éditables dans `docs/assets/architecture/source/`, sans technologies ni métriques fictives.

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

## Étape en cours
**ÉTAPE 00 — Initialisation du projet** (Statut : `IN_PROGRESS`, 6/8 sous-tâches complétées. Ne pas déclarer PASS tant que les sous-tâches P00-T02-S01 et P00-T02-S02 ne sont pas matérialisées et validées).

## Historique récent
- **Audit & correction finale de la documentation** : Épuration des seuils arbitraires dans `docs/ROADMAP.md`, `docs/ARCHITECTURE.md` et les SVG ; audit strict des 8 sous-tâches de l'ÉTAPE 00 (6 DONE, 2 TODO) ; recalcul automatique de l'avancement (2,43 %, statut IN_PROGRESS) ; mise à jour du rapport JSON `docs/rapport_mise_a_niveau_documentation.json`.
- **Mise à niveau documentaire initiale** : Création de la roadmap 31 étapes avec 247 sous-tâches uniques, script de calcul automatique et donut SVG, dashboard d'avancement, 6 diagrammes d'architecture SVG sur fond blanc avec sources éditables, check-list de référence.
- **Alignement CommandView Ready** : Intégration du principe directeur « Autonomous First — CommandView Ready » (Section 33 du CdC).
- **Master Prompt v1.0** : Intégration des 62 sections officielles de référence.
- **Initialisation Git & CI/CD** : Dépôt configuré avec GitHub, pipeline de base `.github/workflows/ci.yml`.
