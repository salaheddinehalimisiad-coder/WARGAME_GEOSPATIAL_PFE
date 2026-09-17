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
- Clarification du pipeline SIG / ETL : **Global Mapper** est l'outil principal d'appui et de référence, complété par la suite open source recommandée par le cahier des charges (**QGIS, GDAL, PROJ**) selon les besoins techniques (automatisation, reprojection, batch).
- Suppression du contrôle CI restrictif anti-QGIS dans [.github/workflows/ci.yml](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/.github/workflows/ci.yml).

