# CHANGELOG
## [IN_PROGRESS / ÉTAPE 02] — Ouverture de la phase d'architecture (2026-09-21)
- Validation formelle de la sous-tâche `P02-T01-S02` : spécification des interfaces REST (12 opérations, 9 familles) et WebSocket (6 flux asynchrones) sous Drogon, distinction dépendance statique vs flux runtime, isolation étanche des traces brutes réservées à l'Arbitre dans `docs/ARCHITECTURE.md`.
- Validation formelle de la sous-tâche `P02-T01-S01` : formalisation du découpage modulaire C++20 (`core`, `terrain`, `units`, `sim`, `api`), dépendances acycliques (DAG), propriété univoque des données et isolation Réel/Perçu dans `docs/ARCHITECTURE.md`.
- Ouverture officielle de l'ÉTAPE 02 (Architecture fonctionnelle et technique) au statut `IN_PROGRESS`.
- Création et bascule sur la branche dédiée `phase/02-architecture`.
- Réutilisation des 6 diagrammes d'architecture SVG existants comme base de référence validée (sans recréation).

## [PASS / ÉTAPE 01] — Clôture de l'analyse du CdC et validation de la recette (2026-09-21)
- Validation formelle contradictoire de la sous-tâche `P01-T02-S03` et des 9 critères d'acceptation contractuels `CRIT-01` à `CRIT-09` (CdC Section 24).
- Complétion intégrale des 7 sous-tâches de l'ÉTAPE 01 (7/7, 100,00 %).
- Statut officiel de l'ÉTAPE 01 déclaré `PASS`.
- Avancement global du projet porté à 6,07 % (15 / 247 sous-tâches).
- Alignement préalable des 6 diagrammes d'architecture SVG (commit `c04fcdd`) et synchronisation stricte avec `docs/ARCHITECTURE.md`.

## [POLICY] — Normalisation de la politique documentaire (2026-09-19)
- Adoption d'une documentation progressive légère : notes courtes par étape dans `docs/etapes/ETAPE_XX.md`.
- Suppression de la génération automatique de gros rapports JSON à chaque étape.
- `PROJECT_MEMORY.md` devient la mémoire durable et structurée du projet.
- `CHANGELOG.md` conservé pour les changements et commits significatifs uniquement.
- Création de `docs/etapes/ETAPE_00.md` et `docs/etapes/ETAPE_01.md`.
- Identification de doublons documentaires : `docs/rapport_mise_a_niveau_documentation.json` est identique à `docs/rapports/rapport_mise_a_niveau_documentation.json` (conservation temporaire des deux en attente de décision).
- Vérification des 6 diagrammes SVG (`docs/assets/architecture/`) : présents et intacts.


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

## [FIX / AUDIT] — Audit formel et correction de la mise à niveau documentaire
- **Épuration des exigences arbitraires dans docs/ROADMAP.md** : Remplacement de l'ensemble des seuils de latence arbitraires (< 2 ms, < 10 ms, < 15 ms, < 1 µs) et seuils imposés (>= 85%) par des mesures objectives sur scénarios de référence avec métriques documentées.
- **Suppression des nombres de tours arbitraires** : Remplacement des mentions 100, 200 et 500 tours par des bancs d'essai multi-tours et sessions d'endurance de référence.
- **Suppression des sources de données prématurées** : Remplacement des mentions SRTM, Copernicus, OpenStreetMap et BD TOPO dans la feuille de route, l'architecture et les diagrammes SVG par une formulation de sélection et validation en phase de collecte (CHOIX À VALIDER).
- **Harmonisation du traitement NoData** : Remplacement de l'interpolation systématique par un traitement selon méthode documentée et validée dans ROADMAP.md, ARCHITECTURE.md et architecture_pipeline_sig.svg.
- **Suppression des FPS imposés** : Remplacement de « 60 FPS sans latence » par une exigence de fluidité de rendu et navigation dans architecture_technique.svg.
- **Audit rigoureux des sous-tâches ÉTAPE 00** : Seules les 6 sous-tâches réellement prouvées sont cochées [x] (P00-T01-S01 à S04, P00-T02-S03 et S04) ; les sous-tâches P00-T02-S01 et P00-T02-S02 sont maintenues à [ ] (TODO).
- **Distinction avancement et statut de validation** : ÉTAPE 00 passe au statut `IN_PROGRESS` (6 / 8 sous-tâches, 75,00 %) et avancement global à 2,43 % (6 / 247 sous-tâches), sans validation PASS prématurée.
- **Synchronisation complète des diagrammes SVG** : Diagrammes dans `docs/assets/architecture/` et sources dans `docs/assets/architecture/source/` rigoureusement identiques et validés.
- **Mise à jour du rapport JSON de conformité** : `docs/rapport_mise_a_niveau_documentation.json` consolidé avec tous les indicateurs et preuves exigés.

## [PASS / ÉTAPE 00] — Finalisation de l'arborescence et validation de l'Étape 00
- **Création des répertoires racines (`P00-T02-S01`)** : Matérialisation de `src/`, `tests/`, `docker/` et `data/` (préservation stricte de `docs/` et `scripts/` existants sans altération des fichiers).
- **Création des répertoires de données (`P00-T02-S02`)** : Matérialisation sous `data/` des conteneurs `data/raw/`, `data/processed/`, `data/vector/`, `data/raster/` avec conservation de l'interdiction de données SIG brutes.
- **Ajout des fichiers `.gitkeep`** : Suivi de la structure de répertoires vides dans Git via `.gitkeep` sans inclure de code ni de données volumineuses.
- **Validation formelle de l'ÉTAPE 00** : Complétion des 8 sous-tâches de l'étape 00 (8/8, 100,00 %), statut de l'ÉTAPE 00 déclaré `PASS`.
- **Mise à jour de l'avancement global** : Avancement global porté à **3,24 %** (8 / 247 sous-tâches).
- **Étape active suivante** : ÉTAPE 01 — Analyse détaillée du cahier des charges (statut : `PLANNED`).

## [CLEANUP / ARBORESCENCE] — Suppression du dossier dupliqué imbriqué et consolidation de la racine unique
- **Audit exhaustif du sous-dossier imbriqué `WARGAME_GEOSPATIAL_PFE/`** : Comparaison récursive complète (45 fichiers analysés : 22 identiques, 17 versions obsolètes de documents maîtres, 6 fichiers de cache Git).
- **Confirmation de zéro perte de données** : Vérification qu'aucune donnée SIG ni aucun code source métier n'étaient présents dans le dossier imbriqué.
- **Suppression de la duplication accidentelle** : Élimination sécurisée du sous-dossier imbriqué `WARGAME_GEOSPATIAL_PFE/`.
- **Création du répertoire centralisé de rapports** : Création de `docs/rapports/` et génération du rapport formel [`docs/rapports/rapport_audit_arborescence.json`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/rapports/rapport_audit_arborescence.json).
- **Validation de la racine unique** : Structure normalisée strictement conforme aux exigences (racine unique, 7 dossiers, 8 fichiers maîtres).

## [AUDIT / ÉTAPE 01] — Audit critique des sources et révision des spécifications selon le CdC v1.0
- **Audit des sources contractuelles** : Dénombrement et vérification directe des 35 sections du fichier officiel `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0).
- **Révision des spécifications fonctionnelles (`docs/SPECIFICATIONS_FONCTIONNELLES.md`)** :
  - Classification explicite de chaque exigence en [A] Présente au CdC, [B] Déduite raisonnablement, [C] Proposition technique à valider, [D] Purgée de l'ancien cadrage.
  - Purge intégrale de la boucle rigide en 4 phases, des classes rigides de contact (Inconnu/Catégorie/Identifié), des probabilités numériques de détection hardcodées (85%, 60%), des décotes temporelles arbitraires, des tables d'atténuation LOS ad-hoc, des attributs psychologiques de moral subjectif, et du terme VPC.
  - Sanctuarisation de l'échelon bataillon minimal, de l'abstraction capacitaire des armements, de la séparation hermétique État Réel vs État Perçu, et du modèle de décision observable sans psychologie clinique.
- **Révision de la matrice de traçabilité (`docs/MATRICE_TRACABILITE.md`)** :
  - Couverture à 100% des 35 sections officielles avec typologie explicite (Exigence, Interprétation, Décision d'architecture, Choix technologique, Proposition future).
  - Clarification du statut de Global Mapper : choix d'ingénierie et d'architecture interne du projet (distinct des technologies recommandées à titre indicatif dans la Section 17 du CdC).
  - Remplacement de la nomenclature inventée REC-01..REC-15 par les 9 critères d'acceptation textuels contractuels de la Section 24 du CdC (`CRIT-01` à `CRIT-09`).
- **Suivi d'avancement et statut** : ÉTAPE 01 maintenue au statut `IN_PROGRESS` (6 / 7 sous-tâches, 85,71 %) et avancement global à **5,67 %** (14 / 247 sous-tâches) dans l'attente de la validation contradictoire du rapport d'audit.
- **Rapports d'audit générés** : [`docs/rapports/rapport_audit_source_etape_01.md`](docs/rapports/rapport_audit_source_etape_01.md) et [`docs/rapports/rapport_audit_source_etape_01.json`](docs/rapports/rapport_audit_source_etape_01.json).







