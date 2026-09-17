# CHANGELOG

## [INIT / GIT & CI/CD] — Initialisation Dépôt Git & Pipeline CI/CD
- Initialisation du dépôt local Git avec branche principale `main`.
- Configuration du dépôt distant officiel : `https://github.com/salaheddinehalimisiad-coder/WARGAME_GEOSPATIAL_PFE.git`.
- Création du `.gitignore` pour protéger les données SIG brutes, caches et fichiers temporaires.
- Ajout de la Section 8 dans [MASTER_PROMPT.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/MASTER_PROMPT.md) détaillant la gouvernance Git, branches par phases et la CI/CD.
- Mise à jour de [AGENT_RULES.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/AGENT_RULES.md) avec les règles de commits conventionnels et de push systématique.
- Rédaction du guide [docs/GIT_WORKFLOW_AND_CICD.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/GIT_WORKFLOW_AND_CICD.md).
- Mise en place du workflow GitHub Actions [.github/workflows/ci.yml](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/.github/workflows/ci.yml) (vérifications d'intégrité, conformité SIG exclusive Global Mapper, linter).

## [UPDATE] — Intégration du Master Prompt v1.0
- Remplacement intégral de [MASTER_PROMPT.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/MASTER_PROMPT.md) par la version officielle complète issue du cahier des charges Version 1.0.
- Mise à niveau de [AGENT_RULES.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/AGENT_RULES.md) pour aligner les règles absolues : Global Mapper seul outil SIG, niveau bataillon, abstraction des équipements, incertitude (réel vs perçu), progression par preuves.
- Mise à jour de [REFERENCE_CHECKLIST.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/REFERENCE_CHECKLIST.md) avec les critères de contrôle préalables et les conditions PASS.
- Mise à jour de [PROJECT_MEMORY.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/PROJECT_MEMORY.md) pour refléter l'état d'alignement du projet.

## [ALIGN] — Alignement CommandView Ready & Flexibilité Pipeline SIG
- Intégration explicite du principe directeur **« Autonomous First — CommandView Ready »** (Section 33 du Cahier des charges) dans [MASTER_PROMPT.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/MASTER_PROMPT.md), [AGENT_RULES.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/AGENT_RULES.md), [PROJECT_PROMPT.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/PROJECT_PROMPT.md) et [docs/ARCHITECTURE.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ARCHITECTURE.md).
- Clarification du pipeline SIG / ETL : **Global Mapper** est l'unique outil SIG du workflow courant.

## Documentation — Roadmap détaillée et suivi d’avancement
- **Roadmap détaillée** : Refonte exhaustive de [`docs/ROADMAP.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ROADMAP.md) couvrant l'intégralité des 31 étapes officielles (ÉTAPE 00 à ÉTAPE 30), structurées avec objectifs, entrées, sorties, livrables, critères d'acceptation et bancs de tests.
- **Système de cases à cocher & identifiants uniques** : Définition de 247 sous-tâches terminales concrètes et vérifiables (zéro formule vague), portant chacune un identifiant unique normalisé `PXX-TYY-SZZ`.
- **Calcul automatique de l'avancement** : Création du script autonome [`scripts/update_progress.py`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/scripts/update_progress.py) sans dépendance externe, appliquant la formule officielle $Avancement = \frac{\text{Sous-tâches cochées}}{\text{Sous-tâches totales}} \times 100$.
- **Graphique circulaire (Donut SVG)** : Génération automatique du diagramme vectoriel [`docs/assets/progress/progress_donut.svg`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/assets/progress/progress_donut.svg) sur fond blanc avec affichage centré du pourcentage, statistiques et étape active.
- **Tableau de bord officiel** : Création de [`docs/ETAT_AVANCEMENT.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ETAT_AVANCEMENT.md) comme vue calculée officielle (synthèse globale, étape active, tâches bloquées, tableau d'avancement par étape avec statuts normalisés).
- **Tableau de bord web réactif et interactif** : Création de [`docs/dashboard.html`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/dashboard.html) (application web standalone sans dépendance avec recherche instantanée, filtres dynamiques, accordéons dépliables, animation fluide de l'avancement et synchronisation automatique avec les données JSON).
- **Architecture visuelle professionnelle** : Refonte de [`docs/ARCHITECTURE.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ARCHITECTURE.md) avec 6 diagrammes vectoriels SVG sur fond blanc (architecture globale, pipeline SIG, données, flux de simulation, cloisonnement Blue/Red/Umpire, architecture technique) et conservation des sources éditables dans `docs/assets/architecture/source/`.
- **Banc de test d'avancement** : Création du script de validation [`scripts/test_progress_calculation.py`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/scripts/test_progress_calculation.py) validant mathématiquement le calcul d'avancement (test 5/20 = 25.00%), la détection d'étape active et le rejet strict des identifiants dupliqués.
- **Check-list de référence** : Mise à jour de [`docs/REFERENCE_CHECKLIST.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/REFERENCE_CHECKLIST.md) avec l'ensemble des critères de conformité documentaire, roadmap, suivi et architecture.


