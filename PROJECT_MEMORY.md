# PROJECT MEMORY

## État actuel du projet
Mise à niveau structurelle de la gouvernance et de la documentation terminée :
- **Roadmap ultra-détaillée** : 31 étapes officielles (ÉTAPE 00 à ÉTAPE 30), découpées en tâches et sous-tâches concrètes avec identifiants uniques normalisés (`PXX-TYY-SZZ`) dans [`docs/ROADMAP.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ROADMAP.md).
- **Source de vérité des tâches** : `docs/ROADMAP.md` constitue l'unique source de vérité des cases à cocher (`- [ ]` / `- [x]`).
- **Tableau de bord d'avancement** : [`docs/ETAT_AVANCEMENT.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ETAT_AVANCEMENT.md) est une vue calculée automatiquement, intégrant le pourcentage d'avancement exact, le tableau des statuts par étape, l'étape active et les tâches restantes.
- **Outil de calcul automatique** : [`scripts/update_progress.py`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/scripts/update_progress.py) calcule automatiquement le taux de complétion basé sur les sous-tâches feuilles terminales et génère le graphique circulaire vectoriel [`docs/assets/progress/progress_donut.svg`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/assets/progress/progress_donut.svg).
- **Architecture visuelle refondue** : Refonte intégrale de [`docs/ARCHITECTURE.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ARCHITECTURE.md) avec 6 diagrammes vectoriels professionnels SVG sur fond blanc (sources conservées dans `docs/assets/architecture/source/`), bannissant tout schéma ASCII.
- **Gouvernance Git & CI/CD** : Dépôt distant configuré, pipeline GitHub Actions (`.github/workflows/ci.yml`), branches isolées par phase.

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
**ÉTAPE 00 — Initialisation du projet** (dépôt, structure, documentation initiale, environnement, CI/CD).

## Historique récent
- **Mise à niveau documentaire et gouvernance** : Création de la roadmap 31 étapes avec 247 sous-tâches uniques, script de calcul automatique et donut SVG, dashboard d'avancement, 6 diagrammes d'architecture SVG sur fond blanc avec sources éditables, check-list de référence mise à jour.
- **Alignement CommandView Ready** : Intégration du principe directeur « Autonomous First — CommandView Ready » (Section 33 du CdC).
- **Master Prompt v1.0** : Intégration des 62 sections officielles de référence.
- **Initialisation Git & CI/CD** : Dépôt configuré avec GitHub, pipeline de base `.github/workflows/ci.yml`.
