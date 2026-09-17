# ROADMAP OFFICIELLE DU PROJET

Référence : `MASTER_PROMPT.md` (Version 1.0 — PFE 2026–2027) & `Cahier_des_charges_PFE_Wargame_geospatial.docx`.  
Gouvernance : Source unique de vérité des cases à cocher. Chaque sous-tâche terminale porte un identifiant unique standardisé au format `PXX-TYY-SZZ`.  
Calcul automatique : `python scripts/update_progress.py`.

---

## ÉTAPE 00 — Initialisation du projet

### Objectif
Mettre en place le socle d'ingénierie, la gouvernance Git, l'arborescence normalisée, la documentation de cadrage et la chaîne d'intégration continue initiale.

### Entrées
- Cahier des charges officiel Version 1.0 (`Cahier_des_charges_PFE_Wargame_geospatial.docx`).
- Dépôt Git initialisé et configuré avec le remote distant officiel.

### Sorties
- Dépôt structuré selon les standards d'ingénierie logicielle.
- Arborescence normalisée (`data/`, `src/`, `tests/`, `docs/`, `scripts/`, `docker/`).
- Pipeline GitHub Actions opérationnel (`.github/workflows/ci.yml`).

### Livrables
- Fichiers maîtres : `MASTER_PROMPT.md`, `AGENT_RULES.md`, `PROJECT_MEMORY.md`, `CHANGELOG.md`.
- Fichier de configuration CI : `.github/workflows/ci.yml`.
- Configuration d'exclusion : `.gitignore`.

### Critères d’acceptation
- Intégrité vérifiée de tous les fichiers maîtres sans corruption.
- Pipeline CI vert sur GitHub Actions sans avertissements bloquants.
- Exclusion effective des données SIG brutes et binaires dans Git.

### Tests
- Test CI de présence et non-vacuité des documents maîtres.
- Test de vérification syntaxique du pipeline YAML.
- Test de non-régression locale sur la structure des dossiers.

### Tâche T00-01 — Configuration du dépôt et gouvernance Git
#### Sous-tâches
- [ ] P00-T01-S01 — Configurer le dépôt distant GitHub avec la branche principale main
- [ ] P00-T01-S02 — Créer le fichier .gitignore interdisant les caches, binaires et données SIG volumineuses
- [ ] P00-T01-S03 — Définir le guide de gestion des branches par phase dans docs/GIT_WORKFLOW_AND_CICD.md
- [ ] P00-T01-S04 — Mettre en place la convention de commits sémantiques dans AGENT_RULES.md

### Tâche T00-02 — Arborescence et environnement de base
#### Sous-tâches
- [ ] P00-T02-S01 — Créer l'arborescence des dossiers src, tests, data, docs, scripts et docker
- [ ] P00-T02-S02 — Définir les sous-dossiers data/raw, data/processed, data/vector et data/raster
- [ ] P00-T02-S03 — Mettre en place le pipeline CI de base dans .github/workflows/ci.yml
- [ ] P00-T02-S04 — Valider l'exécution locale des scripts d'intégrité documentaire

---

## ÉTAPE 01 — Analyse détaillée du cahier des charges

### Objectif
Extraire, analyser et formaliser l'ensemble des exigences fonctionnelles, contraintes techniques, profils d'utilisateurs et critères de recette du cahier des charges officiel.

### Entrées
- `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0).
- `MASTER_PROMPT.md`.

### Sorties
- Spécification formelle des besoins fonctionnels et non-fonctionnels.
- Matrice de traçabilité des exigences du cahier des charges.
- Tableau d'analyse des acteurs (Blue, Red, Umpire).

### Livrables
- Document de spécification des exigences : `docs/SPECIFICATIONS_FONCTIONNELLES.md`.
- Matrice de traçabilité : `docs/MATRICE_TRACABILITE.md`.

### Critères d’acceptation
- 100% des sections du cahier des charges mappées dans la matrice de traçabilité.
- Validation explicite des contraintes d'échelle (niveau bataillon minimum).
- Définition formelle des profils Blue, Red et Umpire.

### Tests
- Vérification croisée des numéros d'articles du cahier des charges dans la matrice.
- Revue de conformité des règles d'engagement et d'arbitrage.

### Tâche T01-01 — Analyse des exigences fonctionnelles
#### Sous-tâches
- [ ] P01-T01-S01 — Extraire toutes les exigences fonctionnelles relatives au terrain et à la grille
- [ ] P01-T01-S02 — Extraire les exigences relatives aux unités, équipements et capteurs
- [ ] P01-T01-S03 — Définir formellement les règles de l'arbitre et la séparation réel versus perçu
- [ ] P01-T01-S04 — Rédiger la spécification des rôles Blue, Red et Umpire dans docs/SPECIFICATIONS_FONCTIONNELLES.md

### Tâche T01-02 — Matrice de traçabilité et critères d'acceptation
#### Sous-tâches
- [ ] P01-T02-S01 — Construire le tableau de correspondance entre articles du CdC et composants logiciels
- [ ] P01-T02-S02 — Identifier les contraintes de performance et de reproductibilité temporelle
- [ ] P01-T02-S03 — Établir la liste des critères d'acceptation de recette finale dans docs/MATRICE_TRACABILITE.md

---

## ÉTAPE 02 — Architecture fonctionnelle et technique

### Objectif
Concevoir l'architecture modulaire globale du système, définir les contrats d'interface, la séparation stricte des responsabilités et les diagrammes structurels visuels.

### Entrées
- Matrice de traçabilité issue de l'ÉTAPE 01.
- Principes d'architecture du `MASTER_PROMPT.md`.

### Sorties
- Schémas d'architecture globale, pipeline SIG, flux de données et composants techniques.
- Spécification des interfaces et protocoles d'échange (REST, WebSocket, IPC).

### Livrables
- Document refondu : `docs/ARCHITECTURE.md`.
- Diagrammes vectoriels SVG dans `docs/assets/architecture/`.
- Fichiers sources éditables dans `docs/assets/architecture/source/`.

### Critères d’acceptation
- Aucun bloc textuel ASCII utilisé pour les diagrammes d'architecture.
- Respect strict du principe Autonomous First - CommandView Ready.
- Séparation physique et logique garantie entre moteur de simulation et IHM.

### Tests
- Validation de la syntaxe vectorielle des fichiers SVG générés.
- Revue d'absence de couplage cyclique entre modules.

### Tâche T02-01 — Conception de l'architecture logicielle
#### Sous-tâches
- [ ] P02-T01-S01 — Définir le découpage en modules C++20 (core, terrain, units, sim, api)
- [ ] P02-T01-S02 — Spécifier les interfaces de communication REST et WebSocket sous Drogon
- [ ] P02-T01-S03 — Définir la frontière d'intégration future avec le système C4ISR CommandView
- [ ] P02-T01-S04 — Rédiger le document descriptif des modules dans docs/ARCHITECTURE.md

### Tâche T02-02 — Production des diagrammes visuels
#### Sous-tâches
- [ ] P02-T02-S01 — Concevoir et exporter le diagramme d'architecture globale en SVG
- [ ] P02-T02-S02 — Concevoir et exporter le diagramme du pipeline SIG en SVG
- [ ] P02-T02-S03 — Concevoir et exporter le diagramme du flux de simulation en SVG
- [ ] P02-T02-S04 — Concevoir et exporter le diagramme d'isolation Blue Red Umpire en SVG
- [ ] P02-T02-S05 — Archiver l'ensemble des fichiers sources des diagrammes dans source/

---

## ÉTAPE 03 — Modèle de données

### Objectif
Élaborer le modèle conceptuel, logique et physique des données pour le terrain, les entités opérationnelles, les événements et les traces.

### Entrées
- Spécifications fonctionnelles (`docs/SPECIFICATIONS_FONCTIONNELLES.md`).
- Diagrammes d'architecture (`docs/ARCHITECTURE.md`).

### Sorties
- Modèle Conceptuel des Données (MCD) et Modèle Logique des Données (MLD).
- Dictionnaire complet des données avec types, contraintes et index.

### Livrables
- Spécification du modèle de données : `docs/MODELE_DONNEES.md`.
- Schéma relationnel SVG : `docs/assets/architecture/architecture_donnees.svg`.

### Critères d’acceptation
- Prise en compte de toutes les entités : Scenario, Session, Unit, Equipment, Sensor, Cell, Event, LogEntry.
- Contraintes d'intégrité référentielle et d'historisation sans perte.
- Absence d'attributs spécifiques aux armes réelles (maintien de l'abstraction).

### Tests
- Vérification de la normalisation en 3ème forme normale (3NF).
- Revue de conformité des types géométriques PostGIS prévus.

### Tâche T03-01 — Modélisation conceptuelle et logique
#### Sous-tâches
- [ ] P03-T01-S01 — Modéliser les entités spatiales TerrainCell, ElevationPoint et RoadSegment
- [ ] P03-T01-S02 — Modéliser les entités tactiques Unit, Side, EquipmentProfile et SensorProfile
- [ ] P03-T01-S03 — Modéliser les entités dynamiques GameSession, TurnEvent, Order et SimulationTrace
- [ ] P03-T01-S04 — Rédiger le dictionnaire de données exhaustif dans docs/MODELE_DONNEES.md

### Tâche T03-02 — Schémas relationnels et validation
#### Sous-tâches
- [ ] P03-T02-S01 — Concevoir le diagramme Entité-Relation vectoriel des données du wargame
- [ ] P03-T02-S02 — Valider l'abstraction stricte des capacités d'équipements sans armes réelles
- [ ] P03-T02-S03 — Intégrer le diagramme architecture_donnees.svg dans la documentation

---

## ÉTAPE 04 — Préparation de l’environnement

### Objectif
Configurer l'environnement de développement complet, la chaîne de compilation C++20, Drogon, PostgreSQL/PostGIS, Node.js/React et conteneurisation Docker.

### Entrées
- Définition de la stack technique officielle du projet.
- Spécifications des dépendances logicielles.

### Sorties
- Fichiers CMakeLists.txt configurés avec support C++20 et GoogleTest.
- Conteneur Docker Compose prêt pour PostgreSQL 16 / PostGIS 3.4.
- Environnement frontend React 18 / TypeScript initialisé.

### Livrables
- Fichiers de build : `CMakeLists.txt`.
- Configuration Docker : `docker/docker-compose.yml`, `docker/Dockerfile.db`.
- Documentation de déploiement : `docs/ENVIRONNEMENT_DEV.md`.

### Critères d’acceptation
- Compilation réussie d'un binaire C++20 minimal avec CMake.
- Démarrage vérifié de l'instance PostgreSQL/PostGIS via Docker Compose.
- Exécution réussie des tests unitaires GoogleTest initiaux.

### Tests
- Test de compilation C++20 sans warning avec `-Wall -Wextra -Wpedantic`.
- Test de connexion TCP et requête spatiale `SELECT PostGIS_Version();`.
- Test de build frontend `npm run build`.

### Tâche T04-01 — Configuration de la chaîne de build C++20
#### Sous-tâches
- [ ] P04-T01-S01 — Rédiger le fichier racine CMakeLists.txt avec standard C++20 exigé
- [ ] P04-T01-S02 — Configurer l'intégration de GoogleTest via FetchContent ou module local
- [ ] P04-T01-S03 — Configurer les dépendances externes spdlog et drogon dans CMake
- [ ] P04-T01-S04 — Créer un test unitaire C++ témoin validant la chaîne de compilation

### Tâche T04-02 — Configuration des conteneurs et bases de données
#### Sous-tâches
- [ ] P04-T02-S01 — Rédiger le fichier docker/docker-compose.yml avec service PostGIS
- [ ] P04-T02-S02 — Écrire le script d'initialisation SQL activant l'extension postgis
- [ ] P04-T02-S03 — Documenter la procédure de démarrage et d'arrêt dans docs/ENVIRONNEMENT_DEV.md
- [ ] P04-T02-S04 — Valider le test de connectivité réseau à la base depuis le runner CI

---

## ÉTAPE 05 — Collecte SIG avec Global Mapper

### Objectif
Acquérir et importer l'ensemble des couches géospatiales nécessaires sur la zone d'étude exclusivement au moyen de Global Mapper.

### Entrées
- Délimitation de la zone d'intérêt géographique (AOI / Bounding Box).
- Sources de données ouvertes (SRTM, Copernicus, OpenStreetMap, BD TOPO).

### Sorties
- Couches brutes importées et cataloguées dans Global Mapper.
- Espaces de travail Global Mapper (`.gmw`) structurés et sauvegardés.

### Livrables
- Catalogue des sources de données SIG : `docs/CATALOGUE_SIG.md`.
- Fichier projet Global Mapper : `data/raw/workspace_collecte.gmw`.

### Critères d’acceptation
- Utilisation exclusive de Global Mapper pour toute opération SIG courante.
- Couverture intégrale de l'emprise géographique par le MNT et les vecteurs.
- Absence d'artefacts d'importation ou de projections corrompues.

### Tests
- Vérification visuelle et métrique de la superposition des couches dans Global Mapper.
- Contrôle de la résolution spatiale du MNT importé (<= 30 mètres).

### Tâche T05-01 — Cadrage géographique et sélection des sources
#### Sous-tâches
- [ ] P05-T01-S01 — Définir précisément les coordonnées de la boîte englobante de la zone d'étude
- [ ] P05-T01-S02 — Sélectionner les sources de MNT adaptées avec métadonnées d'acquisition
- [ ] P05-T01-S03 — Sélectionner les couches vectorielles des routes, pistes et franchissements
- [ ] P05-T01-S04 — Rédiger la fiche de métadonnées des sources dans docs/CATALOGUE_SIG.md

### Tâche T05-02 — Importation et organisation dans Global Mapper
#### Sous-tâches
- [ ] P05-T02-S01 — Importer les dalles raster altimétriques dans un workspace Global Mapper dédié
- [ ] P05-T02-S02 — Importer les couches vectorielles de réseau viaire et hydrographique
- [ ] P05-T02-S03 — Structurer l'arborescence des calques dans Global Mapper par thématique
- [ ] P05-T02-S04 — Sauvegarder le projet de travail data/raw/workspace_collecte.gmw

---

## ÉTAPE 06 — Préparation et nettoyage SIG avec Global Mapper

### Objectif
Nettoyer, harmoniser, reprojeter dans le système de coordonnées de référence officiel, découper et exporter les données SIG prêtes à l'emploi avec Global Mapper.

### Entrées
- Workspace Global Mapper brut issu de l'ÉTAPE 05.
- Spécifications du CRS cible (UTM / projection locale métrique).

### Sorties
- Couches raster et vectorielles nettoyées, corrigées et projetées.
- Exports standardisés (GeoTIFF métrique, Shapefiles / GeoPackage propres).

### Livrables
- Couches nettoyées dans `data/processed/`.
- Journal des opérations et traitements appliqués : `docs/JOURNAL_PREPARATION_SIG.md`.

### Critères d’acceptation
- Reprojection de l'ensemble des couches dans le CRS métrique retenu.
- Traitement complet des valeurs NoData dans le raster altimétrique.
- Correction des géométries vectorielles non valides (nœuds pendants, auto-intersections).

### Tests
- Exécution de l'outil de validation géométrique vectorielle dans Global Mapper.
- Contrôle de cohérence de l'étendue spatiale sur l'ensemble des exports.

### Tâche T06-01 — Traitement du modèle numérique de terrain
#### Sous-tâches
- [ ] P06-T01-S01 — Mosaïquer les dalles altimétriques dans Global Mapper
- [ ] P06-T01-S02 — Reprojeter le MNT dans le système de projection métrique retenu
- [ ] P06-T01-S03 — Combler les zones de NoData par interpolation dans Global Mapper
- [ ] P06-T01-S04 — Exporter le MNT nettoyé au format GeoTIFF dans data/processed/dem_clean.tif

### Tâche T06-02 — Nettoyage et harmonisation vectorielle
#### Sous-tâches
- [ ] P06-T02-S01 — Découper les couches vectorielles strictement sur l'emprise de la zone de jeu
- [ ] P06-T02-S02 — Filtrer et normaliser les attributs de franchissement des routes et ponts
- [ ] P06-T02-S03 — Nettoyer les polygones d'occupation du sol et zones urbaines
- [ ] P06-T02-S04 — Exporter les couches vectorielles prêtes pour l'ingestion dans data/processed/

---

## ÉTAPE 07 — Contrôle qualité SIG

### Objectif
Vérifier méthodiquement la conformité, la précision géométrique, la cohérence topologique et l'exhaustivité des données préparées avant toute intégration logicielle.

### Entrées
- Données SIG préparées dans `data/processed/`.
- Grille des critères de contrôle qualité géospatiale.

### Sorties
- Rapport officiel de contrôle qualité SIG certifiant les couches.
- Dossier de données validées `data/validated/`.

### Livrables
- Rapport de contrôle qualité : `docs/RAPPORT_QA_SIG.md`.
- Check-list de recette des couches géographiques signée.

### Critères d’acceptation
- Taux de validité géométrique vectorielle de 100%.
- Tolérance d'erreur altimétrique vérifiée conforme aux spécifications.
- Accord parfait des limites et emprises entre toutes les couches.

### Tests
- Script de vérification automatisée d'intégrité des fichiers GeoTIFF et GeoPackage.
- Contrôle d'unicité des identifiants et présence des attributs obligatoires.

### Tâche T07-01 — Contrôles géométriques et topologiques
#### Sous-tâches
- [ ] P07-T01-S01 — Vérifier la stricte conformité du CRS métrique sur chaque fichier exporté
- [ ] P07-T01-S02 — Détecter et éliminer les micro-polygones et segments orphelins
- [ ] P07-T01-S03 — Vérifier la connectivité topologique du réseau routier
- [ ] P07-T01-S04 — Consigner les métriques géométriques dans docs/RAPPORT_QA_SIG.md

### Tâche T07-02 — Certification et gel des données géographiques
#### Sous-tâches
- [ ] P07-T02-S01 — Vérifier la plage des valeurs d'élévation par rapport à la réalité terrain
- [ ] P07-T02-S02 — Contrôler la cohérence des zones inondables et franchissements hydrauliques
- [ ] P07-T02-S03 — Transférer les fichiers validés dans le répertoire data/validated/
- [ ] P07-T02-S04 — Formaliser le procès-verbal de validation de l'étape QA SIG

---

## ÉTAPE 08 — Modèle du terrain

### Objectif
Concevoir les structures de données en C++20 pour modéliser le relief, le calcul de pente, la rugosité, les types de surface et leurs coefficients d'impact tactique.

### Entrées
- Données validées issues de l'ÉTAPE 07.
- Spécifications des coûts de franchissement et d'observation selon le terrain.

### Sorties
- Bibliothèque C++20 `terrain_core` modélisant les propriétés physiques du sol.
- Classes de calcul de pente, d'intervisibilité et de rugosité.

### Livrables
- Fichiers d'en-tête et sources : `src/terrain/terrain_model.hpp`, `src/terrain/terrain_model.cpp`.
- Suite de tests unitaires : `tests/terrain_tests.cpp`.

### Critères d’acceptation
- Calcul de pente mathématiquement exact à partir de la matrice d'élévation.
- Détermination déterministe des types de surface (route, forêt, bâti, eau).
- Couverture de code par les tests unitaires >= 85%.

### Tests
- Tests unitaires GoogleTest sur profils de pente artificiels connus (pente nulle, 10%, 45%).
- Tests de performance mesurant le temps d'accès aux propriétés du terrain (< 1 µs par point).

### Tâche T08-01 — Structures de données d'élévation et de pente
#### Sous-tâches
- [ ] P08-T01-S01 — Définir la structure C++20 ElevationGrid avec accès indexé rapide
- [ ] P08-T01-S02 — Implémenter l'algorithme d'estimation de pente par gradients locaux
- [ ] P08-T01-S03 — Développer les tests unitaires pour le calcul d'altitude et de déclivité
- [ ] P08-T01-S04 — Écrire les benchmarks de performance sur le maillage d'élévation

### Tâche T08-02 — Propriétés de surface et coefficients tactiques
#### Sous-tâches
- [ ] P08-T02-S01 — Énumérer les classes de terrain (Route, Plaine, Foret, Urbain, Eau)
- [ ] P08-T02-S02 — Définir la table de correspondance des modificateurs de mobilité
- [ ] P08-T02-S03 — Implémenter le calcul de coefficient de masquage visuel du terrain
- [ ] P08-T02-S04 — Valider l'indépendance de terrain_core vis-à-vis des composants IHM

---

## ÉTAPE 09 — Conception de la grille hexagonale

### Objectif
Concevoir et dimensionner le maillage hexagonal régulier du théâtre d'opérations, établir le système de coordonnées et les relations spatiales de voisinage.

### Entrées
- Boîte englobante de la zone de jeu validée.
- Échelle tactique retenue (rayon d'hexagone adapté au niveau bataillon).

### Sorties
- Spécification mathématique du maillage hexagonal (orientation flat-top ou pointy-top).
- Système de coordonnées axiales/cubiques et algorithmes de distance/voisinage.

### Livrables
- Spécification mathématique de la grille : `docs/GRILLE_HEXAGONALE.md`.
- Implémentation C++20 : `src/grid/hex_grid.hpp`, `src/grid/hex_coordinates.hpp`.

### Critères d’acceptation
- Distance métrique inter-centres constante et documentée.
- Fonctions de voisinage retournant rigoureusement les 6 cellules adjacentes.
- Algorithme de conversion bidirectionnel précis entre coordonnées métriques et coordonnées hexagonales.

### Tests
- Tests unitaires vérifiant les propriétés mathématiques des coordonnées cubiques (x + y + z = 0).
- Tests des 6 directions cardinales hexagonales et de symétrie des distances.

### Tâche T09-01 — Spécification mathématique et géométrie
#### Sous-tâches
- [ ] P09-T01-S01 — Choisir et justifier l'orientation des hexagones (flat-topped vs pointy-topped)
- [ ] P09-T01-S02 — Dimensionner l'apothème de l'hexagone en cohérence avec le niveau bataillon
- [ ] P09-T01-S03 — Formaliser le système de coordonnées cubiques et axiales dans docs/GRILLE_HEXAGONALE.md
- [ ] P09-T01-S04 — Documenter l'étude comparative d'alternatives (H3 vs grille métrique plane)

### Tâche T09-02 — Implémentation du moteur de maillage hexagonal
#### Sous-tâches
- [ ] P09-T02-S01 — Écrire la structure C++20 HexCoord avec opérateurs arithmétiques
- [ ] P09-T02-S02 — Implémenter le calcul de distance hexagonale en norme cubique
- [ ] P09-T02-S03 — Implémenter la fonction d'extraction des 6 voisins immédiats
- [ ] P09-T02-S04 — Implémenter la projection métrique cartésienne vers cellule hexagonale

---

## ÉTAPE 10 — Validation de la grille

### Objectif
Vérifier l'absence de déformation, la complétude de la couverture, l'exactitude des calculs de voisinage et la robustesse géométrique de la grille hexagonale.

### Entrées
- Implémentation `src/grid/` issue de l'ÉTAPE 09.
- Emprise géographique validée.

### Sorties
- Suite de tests unitaires et d'intégration validant 100% des cas géométriques limites.
- Export GeoJSON/Shapefile de la grille pour inspection visuelle dans Global Mapper.

### Livrables
- Rapport de validation de la grille : `docs/VALIDATION_GRILLE.md`.
- Export géométrique de contrôle : `data/processed/grid_validation.geojson`.

### Critères d’acceptation
- Recouvrement continu sans aucun vide ni chevauchement sur la zone de jeu.
- Temps de résolution de l'hexagone englobant un point inférieur à 500 nanosecondes.
- Validation de l'alignement visuel de la grille sur les données SIG dans Global Mapper.

### Tests
- Tests automatisés d'invariance par translation et rotation.
- Test d'échantillonnage de 10 000 points aléatoires projetés dans la grille.

### Tâche T10-01 — Tests automatisés et cas aux limites
#### Sous-tâches
- [ ] P10-T01-S01 — Développer le banc de test des frontières de l'emprise géographique
- [ ] P10-T01-S02 — Valider l'invariance de distance entre deux cellules commutatives
- [ ] P10-T01-S03 — Écrire les tests d'interpolation le long d'une ligne d'hexagones (line drawing)
- [ ] P10-T01-S04 — Mesurer la performance d'exécution sur 1 million de conversions spatiales

### Tâche T10-02 — Inspection visuelle et contrôle SIG
#### Sous-tâches
- [ ] P10-T02-S01 — Générer l'export vectoriel des centroïdes et bordures d'hexagones
- [ ] P10-T02-S02 — Importer la grille générée dans Global Mapper pour vérification d'emprise
- [ ] P10-T02-S03 — Contrôler la concordance entre les frontières naturelles et les cellules
- [ ] P10-T02-S04 — Rédiger le rapport technique de validation dans docs/VALIDATION_GRILLE.md

---

## ÉTAPE 11 — Intégration PostgreSQL/PostGIS

### Objectif
Créer le schéma relationnel spatial, implémenter les tables de cellules, stocker les attributs du terrain et déployer les index spatiaux optimisés.

### Entrées
- Modèle conceptuel de données (`docs/MODELE_DONNEES.md`).
- Données de terrain et géométries de grille validées.

### Sorties
- Scripts de migration DDL PostgreSQL/PostGIS versionnés.
- Base de données initialisée contenant les cellules hexagonales et couches SIG.

### Livrables
- Scripts de migration : `src/db/migrations/V001__init_spatial_schema.sql`.
- Script d'ingestion des données : `scripts/ingest_terrain_grid.py`.

### Critères d’acceptation
- Exécution sans erreur de l'intégralité des scripts SQL de migration.
- Index spatiaux GiST opérationnels sur toutes les colonnes géométriques.
- Requête spatiale de sélection de cellule par coordonnées métriques < 2 millisecondes.

### Tests
- Test automatisé d'exécution de migration sur conteneur Docker vierge.
- Test de performance sur requêtes spatiales `ST_Intersects` et `ST_DWithin`.

### Tâche T11-01 — Création du schéma et des tables spatiales
#### Sous-tâches
- [ ] P11-T01-S01 — Écrire le script DDL créant les tables hex_cell, terrain_feature et elevation_grid
- [ ] P11-T01-S02 — Définir les clés primaires, contraintes d'intégrité et clés étrangères
- [ ] P11-T01-S03 — Créer les index spatiaux GiST sur les colonnes geometry(Polygon, CRS)
- [ ] P11-T01-S04 — Configurer les index composites sur les identifiants de coordonnées hexagonales

### Tâche T11-02 — Ingestion des données et vérification
#### Sous-tâches
- [ ] P11-T02-S01 — Développer le script d'ingestion automatique de la grille dans PostgreSQL
- [ ] P11-T02-S02 — Associer à chaque cellule les propriétés agrégées du terrain
- [ ] P11-T02-S03 — Rédiger les requêtes de test d'intégrité et de comptage des cellules
- [ ] P11-T02-S04 — Valider le plan d'exécution des requêtes spatiales avec EXPLAIN ANALYZE

---

## ÉTAPE 12 — Modèle des unités

### Objectif
Modéliser en C++20 les unités opérationnelles (niveau bataillon), leurs camps (Blue, Red), leurs états dynamiques, leurs capacités et leurs contraintes tactiques.

### Entrées
- Spécification fonctionnelle des unités (`docs/SPECIFICATIONS_FONCTIONNELLES.md`).
- Abstraction des forces imposée par le cahier des charges.

### Sorties
- Module C++20 `unit_core` gérant les unités, factions, effectifs et états opérationnels.
- Gestionnaires d'état d'unité (prêt, en mouvement, engagé, désorganisé, neutralisé).

### Livrables
- Fichiers sources : `src/units/unit.hpp`, `src/units/unit_state.hpp`, `src/units/side.hpp`.
- Tests unitaires : `tests/unit_model_tests.cpp`.

### Critères d’acceptation
- Respect strict de l'échelon minimal au niveau bataillon.
- Représentation abstraite des capacités sans modélisation balistique micro-détaillée.
- Validation des transitions d'états d'unités selon les règles de simulation.

### Tests
- Tests unitaires sur les transitions d'état d'une unité.
- Tests d'immutabilité des identifiants et de cohérence des assignations de faction.

### Tâche T12-01 — Définition de l'entité Unit et des factions
#### Sous-tâches
- [ ] P12-T01-S01 — Définir l'énumération Side (Blue, Red, Neutral, Umpire)
- [ ] P12-T01-S02 — Définir l'énumération UnitType au niveau bataillon (Infanterie, Blinde, Artillerie, Soutien)
- [ ] P12-T01-S03 — Implémenter la classe C++20 Unit avec attributs d'identification et posture
- [ ] P12-T01-S04 — Rédiger la spécification détaillée des états d'unité dans docs/MODELE_UNITES.md

### Tâche T12-02 — Logique des capacités et états d'unité
#### Sous-tâches
- [ ] P12-T02-S01 — Définir la machine à états finis des statuts opérationnels d'une unité
- [ ] P12-T02-S02 — Implémenter le calcul de cohésion et d'attrition abstraite
- [ ] P12-T02-S03 — Écrire la suite de tests unitaires sur les transitions autorisées et interdites
- [ ] P12-T02-S04 — Vérifier l'encapsulation stricte évitant toute fuite d'informations secrètes

---

## ÉTAPE 13 — Modèle des équipements

### Objectif
Modéliser les profils d'équipements génériques, leurs classes de mobilité relative, de protection, d'endurance et de portée abstraite.

### Entrées
- Règles d'abstraction des équipements du `MASTER_PROMPT.md`.
- Spécifications du cahier des charges interdisant les armes réelles détaillées.

### Sorties
- Module C++20 `equipment_core` contenant les classes de profils matériels.
- Associations entre unités et profils d'équipements.

### Livrables
- Fichiers sources : `src/equipment/equipment_profile.hpp`, `src/equipment/equipment_registry.hpp`.
- Tests unitaires : `tests/equipment_tests.cpp`.

### Critères d’acceptation
- Aucune mention de modèles réels classifiés ou détaillés (ex: T-72, Abrams, Rafale).
- Définition en classes fonctionnelles génériques (ex: ChenilleLourde, RoueLegere, Tracte).
- Disponibilité opérationnelle paramétrable par scénario.

### Tests
- Tests unitaires vérifiant la validité des plages de valeurs des attributs d'équipement.
- Tests d'application des modificateurs d'équipement sur les capacités de l'unité hôte.

### Tâche T13-01 — Spécification des profils d'équipements génériques
#### Sous-tâches
- [ ] P13-T01-S01 — Définir les catégories abstraites d'équipements (Mobilite, Protection, PuissanceRelative)
- [ ] P13-T01-S02 — Créer le schéma de profil d'équipement avec coefficients normalisés [0.0 - 1.0]
- [ ] P13-T01-S03 — Rédiger le catalogue des équipements génériques du PFE dans docs/EQUIPEMENTS.md
- [ ] P13-T01-S04 — Valider l'absence totale de données techniques militaires réelles sensibles

### Tâche T13-02 — Implémentation et registre d'équipements
#### Sous-tâches
- [ ] P13-T02-S01 — Coder la classe EquipmentProfile et son registre centralisé en mémoire
- [ ] P13-T02-S02 — Implémenter la méthode d'évaluation de la vitesse maximale relative
- [ ] P13-T02-S03 — Implémenter l'impact de l'usure et des pannes sur la disponibilité matérielle
- [ ] P13-T02-S04 — Écrire les tests d'association unitaire entre bataillon et équipements

---

## ÉTAPE 14 — Modèle des capteurs

### Objectif
Modéliser les capacités de détection, les portées, les cônes de vision, la sensibilité aux conditions environnementales et la précision de localisation.

### Entrées
- Modèle de terrain (élévation et masquage) issu de l'ÉTAPE 08.
- Profils d'équipements issus de l'ÉTAPE 13.

### Sorties
- Module C++20 `sensor_core` modélisant les capteurs optiques, radar et humains.
- Fonctions de calcul de probabilité de détection et ligne de vue (Line of Sight - LOS).

### Livrables
- Fichiers sources : `src/sensors/sensor.hpp`, `src/sensors/los_calculator.hpp`.
- Tests unitaires : `tests/sensor_los_tests.cpp`.

### Critères d’acceptation
- Algorithme de ligne de vue tenant compte de l'altimétrie du terrain et des masques végétaux.
- Dégradation paramétrable de la détection selon la météo et l'heure du jour.
- Production d'estimations bruitées conformes au modèle d'incertitude.

### Tests
- Tests de ligne de vue sur cas géométriques d'école (crête masquante, vallée ouverte).
- Tests statistiques de distribution de l'erreur de localisation estimée.

### Tâche T14-01 — Algorithme de ligne de vue (LOS)
#### Sous-tâches
- [ ] P14-T01-S01 — Implémenter l'algorithme de tracé de rayon altimétrique entre deux cellules
- [ ] P14-T01-S02 — Intégrer les hauteurs de canopée et d'urbanisation dans le calcul de masque
- [ ] P14-T01-S03 — Optimiser le calcul de visibilité avec mise en cache locale des profils
- [ ] P14-T01-S04 — Écrire les tests unitaires GoogleTest pour les profils masqués et dégagés

### Tâche T14-02 — Détection et précision des capteurs
#### Sous-tâches
- [ ] P14-T01-S05 — Modéliser les capteurs OptiqueDirect, RadarSurveillance et RenseignementHumain
- [ ] P14-T02-S01 — Définir la formule de probabilité de détection en fonction de la distance
- [ ] P14-T02-S02 — Implémenter l'introduction d'un biais d'estimation de position gaussien
- [ ] P14-T02-S03 — Valider la génération déterministe d'incertitude via graine pseudo-aléatoire

---

## ÉTAPE 15 — Moteur de simulation

### Objectif
Concevoir et développer le cœur de simulation en C++20, orchestrant l'état du monde, le séquencement des tours, l'application des règles et la reproductibilité absolue.

### Entrées
- Modules `terrain_core`, `unit_core`, `equipment_core` et `sensor_core`.
- Principes de simulation déterministe du `MASTER_PROMPT.md`.

### Sorties
- Moteur de simulation `SimulationEngine` autonome, pur et découplé du réseau.
- Boucle d'exécution pas-à-pas avec gestion des états avant/après transition.

### Livrables
- Fichiers sources : `src/sim/simulation_engine.hpp`, `src/sim/world_state.hpp`.
- Tests d'intégration : `tests/simulation_engine_tests.cpp`.

### Critères d’acceptation
- Reproductibilité bit-à-bit garantie pour une graine pseudo-aléatoire donnée.
- Séparation étanche entre l'état vrai du monde et les vues partielles des joueurs.
- Absence totale d'appels bloquants ou d'attente active dans le moteur.

### Tests
- Test de reproductibilité : deux exécutions avec même graine doivent produire des états finaux identiques.
- Test de rollback ou sauvegarde/restauration d'un instantané (snapshot) du monde.

### Tâche T15-01 — Architecture de l'état du monde et transitions
#### Sous-tâches
- [ ] P15-T01-S01 — Définir la classe WorldState représentant l'état exhaustif de la simulation
- [ ] P15-T01-S02 — Coder le mécanisme de snapshot mémoire pour la sauvegarde d'état
- [ ] P15-T01-S03 — Définir l'interface pure Command et son mécanisme d'application sur le monde
- [ ] P15-T01-S04 — Rédiger la documentation du cycle de vie du moteur dans docs/MOTEUR_SIMULATION.md

### Tâche T15-02 — Orchestration et reproductibilité
#### Sous-tâches
- [ ] P15-T02-S01 — Implémenter la classe SimulationEngine gérant la progression des phases de jeu
- [ ] P15-T02-S02 — Intégrer un générateur de nombres pseudo-aléatoires déterministe (std::mt19937_64)
- [ ] P15-T02-S03 — Développer le banc d'essai de reproductibilité parfaite sur 100 tours
- [ ] P15-T02-S04 — Valider l'isolation totale du moteur vis-à-vis des sockets et de la base de données

---

## ÉTAPE 16 — Déplacements

### Objectif
Implémenter la planification et l'exécution des déplacements sur la grille hexagonale, en intégrant les coûts de franchissement, le réseau routier et la zone de contrôle.

### Entrées
- Grille hexagonale (`src/grid/`) et modèle de terrain (`src/terrain/`).
- Moteur de simulation (`src/sim/`).

### Sorties
- Algorithme de recherche de chemin (A* hexagonal) pondéré par le relief et les routes.
- Gestion des ordres de mouvement et consommation des points de déplacement.

### Livrables
- Fichiers sources : `src/movement/pathfinding.hpp`, `src/movement/movement_resolver.hpp`.
- Tests unitaires : `tests/movement_pathfinding_tests.cpp`.

### Critères d’acceptation
- Trajectoires optimales respectant strictement les coûts de relief et de voirie.
- Blocage strict des mouvements sur cellules infranchissables (ex: plans d'eau majeurs).
- Calcul de chemin entre deux points distants de 50 cellules résolu en moins de 10 ms.

### Tests
- Tests unitaires sur chemins d'école privilégiant la route malgré un détour géométrique.
- Tests d'interdiction de superposition illégale d'unités amies ou ennemies.

### Tâche T16-01 — Algorithme de calcul d'itinéraire A* hexagonal
#### Sous-tâches
- [ ] P16-T01-S01 — Adapter l'heuristique de distance hexagonale pour l'algorithme A*
- [ ] P16-T01-S02 — Intégrer les coûts dynamiques de terrain, déclivité et infrastructure routière
- [ ] P16-T01-S03 — Implémenter l'évitement des obstacles infranchissables et unités ennemies
- [ ] P16-T01-S04 — Développer les tests de performance du pathfinding sur grille complète

### Tâche T16-02 — Résolution des ordres de mouvement
#### Sous-tâches
- [ ] P16-T02-S01 — Définir la structure MoveOrder avec points de passage et vitesse demandée
- [ ] P16-T02-S02 — Implémenter la décrémentation des points de mouvement par tour
- [ ] P16-T02-S03 — Gérer les interruptions de déplacement en cas de contact inattendu
- [ ] P16-T02-S04 — Valider la mise à jour cohérente des coordonnées de l'unité dans WorldState

---

## ÉTAPE 17 — Observations et incertitude

### Objectif
Implémenter la génération des rapports d'observation avec dégradation de la précision, identification incertaine des types d'unités et persistance des contacts obsolètes.

### Entrées
- Modèle des capteurs (`src/sensors/`) et état vrai du monde (`WorldState`).
- Spécifications du brouillard de guerre.

### Sorties
- Générateur d'observations tactiques `ObservationEngine`.
- Structures d'observations partielles avec indices de confiance et horodatage.

### Livrables
- Fichiers sources : `src/perception/observation.hpp`, `src/perception/observation_engine.hpp`.
- Tests unitaires : `tests/observation_uncertainty_tests.cpp`.

### Critères d’acceptation
- Dissimulation totale des unités ennemies situées hors de portée ou masquées.
- Présence d'un niveau de confiance explicite (ex: Détecté, Classifié, Identifié).
- Dégradation progressive de la fraîcheur de l'information au fil des tours écoulés.

### Tests
- Tests vérifiant qu'une unité masquée derrière une crête ne génère aucune observation.
- Tests de variation du rayon d'incertitude de position en fonction de la distance du capteur.

### Tâche T17-01 — Structure et typologie des observations
#### Sous-tâches
- [ ] P17-T01-S01 — Définir la structure Observation (id, position_estimee, confiance, timestamp)
- [ ] P17-T01-S02 — Définir les niveaux de classification (Inconnu, Véhicule, BataillonInfanterie, etc.)
- [ ] P17-T01-S03 — Implémenter le calcul de dérive temporelle de la précision du contact
- [ ] P17-T01-S04 — Rédiger les principes mathématiques d'incertitude dans docs/INCERTITUDE.md

### Tâche T17-02 — Moteur de génération des contacts perçus
#### Sous-tâches
- [ ] P17-T02-S01 — Scanner l'ensemble des capteurs actifs d'une faction pour calculer la visibilité
- [ ] P17-T02-S02 — Générer les observations bruitées sans altérer l'état réel de la cible
- [ ] P17-T02-S03 — Fusionner les observations multiples d'une même cible par plusieurs capteurs
- [ ] P17-T02-S04 — Valider la stricte étanchéité mémoire entre observation générée et unité réelle

---

## ÉTAPE 18 — État réel / état perçu

### Objectif
Concevoir et implémenter la séparation stricte du modèle de connaissances entre l'Arbitre (Omniscient / État Réel) et chaque joueur (Partiel / État Perçu).

### Entrées
- `WorldState` et `ObservationEngine`.
- Règles de filtrage d'informations du `MASTER_PROMPT.md`.

### Sorties
- Structure `PerceivedState` dédiée par camp (Blue et Red).
- Mécanismes d'export sécurisés interdisant toute fuite vers les clients joueurs.

### Livrables
- Fichiers sources : `src/perception/perceived_state.hpp`, `src/perception/state_filter.hpp`.
- Tests d'isolation de sécurité : `tests/state_security_isolation_tests.cpp`.

### Critères d’acceptation
- Impossibilité mathématique et technique pour un client Blue de lire les positions réelles Red.
- Vue Umpire disposant de la superposition de l'état réel et des deux états perçus.
- Zéro fuite de métadonnées dans les payloads JSON destinés aux joueurs.

### Tests
- Tests d'analyse de charge utile (payload audit) garantissant l'absence de coordonnées réelles.
- Tests d'accès non autorisé rejetés par les filtres de sécurité.

### Tâche T18-01 — Filtrage et construction de l'état perçu
#### Sous-tâches
- [ ] P18-T01-S01 — Implémenter la classe PerceivedState contenant unités amies et observations
- [ ] P18-T01-S02 — Coder la fonction de filtrage sélectif StateFilter::buildForSide(WorldState, Side)
- [ ] P18-T01-S03 — Masquer intégralement les pistes non observées dans la vue transmise
- [ ] P18-T01-S04 — Formaliser le contrat d'isolation sécuritaire dans docs/SECURITE_ISOLATION.md

### Tâche T18-02 — Vue globale et contrôle de l'Arbitre
#### Sous-tâches
- [ ] P18-T02-S01 — Implémenter la structure UmpireState consolidant réalité et perceptions
- [ ] P18-T02-S02 — Développer les fonctions de calcul d'écart (écart de position réel vs perçu)
- [ ] P18-T02-S03 — Écrire les tests unitaires de contrôle d'intégrité de la vue Arbitre
- [ ] P18-T02-S04 — Valider les tests d'étanchéité interdisant les lectures croisées entre camps

---

## ÉTAPE 19 — Temps et événements

### Objectif
Gérer la chronologie de simulation, le temps discret (tour par tour) ou continu discrétisé, la planification d'événements différés et les échéances d'ordres.

### Entrées
- Moteur de simulation `SimulationEngine`.
- Spécifications du modèle temporel.

### Sorties
- Gestionnaire d'horloge de jeu `SimulationClock` et file d'événements prioritaire.
- Prise en charge des retards de transmission et délais d'exécution.

### Livrables
- Fichiers sources : `src/sim/time_manager.hpp`, `src/sim/event_queue.hpp`.
- Tests unitaires : `tests/time_events_tests.cpp`.

### Critères d’acceptation
- Ordonnancement strict et déterministe des événements par horodatage croissant.
- Capacité d'accélération, pause et exécution pas-à-pas sans désynchronisation.
- Prise en compte de délais paramétrables pour la réception des ordres de commandement.

### Tests
- Tests d'insertion désordonnée dans la file d'événements vérifiant l'ordre d'exécution réel.
- Test de stabilité de l'horloge sur 1 000 pas de temps successifs.

### Tâche T19-01 — Horloge de simulation et file d'événements
#### Sous-tâches
- [ ] P19-T01-S01 — Définir la classe SimulationClock avec support pas-à-pas et vitesse variable
- [ ] P19-T01-S02 — Implémenter la file d'attente à priorité chronologique EventQueue
- [ ] P19-T01-S03 — Définir les types d'événements standards (Ordre, Mouvement, Contact, FinTour)
- [ ] P19-T01-S04 — Écrire les tests d'ordonnancement temporel déterministe

### Tâche T19-02 — Délais de transmission et planification
#### Sous-tâches
- [ ] P19-T02-S01 — Modéliser les délais de transmission d'ordres selon les liaisons de commandement
- [ ] P19-T02-S02 — Implémenter l'annulation ou la modification d'ordres en cours d'acheminement
- [ ] P19-T02-S03 — Tester le comportement du moteur lors d'une cascade d'événements simultanés
- [ ] P19-T02-S04 — Documenter la politique de résolution temporelle dans docs/MODELE_TEMPOREL.md

---

## ÉTAPE 20 — Modèle de décision

### Objectif
Formaliser le cycle de décision opérationnelle (OODA : Observer, Orienter, Décider, Agir), la capture des intentions, la validation des ordres et l'évaluation de leur impact.

### Entrées
- États perçus Blue et Red (`src/perception/`).
- Catalogue des ordres autorisés.

### Sorties
- Module C++20 `decision_core` formalisant le modèle d'ordres et d'intentions.
- Validateur de cohérence opérationnelle des ordres soumis.

### Livrables
- Fichiers sources : `src/decision/decision_model.hpp`, `src/decision/order_validator.hpp`.
- Tests unitaires : `tests/decision_model_tests.cpp`.

### Critères d’acceptation
- Enregistrement systématique de la justification et de l'intention associée à chaque ordre.
- Rejet immédiat des ordres invalides (ex: unité inexistante, portée excessive, carburant nul).
- Traçabilité complète du décideur et de l'horodatage de soumission de l'ordre.

### Tests
- Tests de validation syntaxique et sémantique sur ordres licites et illicites.
- Tests d'impact décisionnel mesurant le temps de réaction entre perception et ordre.

### Tâche T20-01 — Typologie des ordres et capture des intentions
#### Sous-tâches
- [ ] P20-T01-S01 — Définir la hiérarchie des ordres (Deplacement, PostureDefensive, Reconnaissance, Halte)
- [ ] P20-T01-S02 — Intégrer les champs obligatoires d'intention tactique et de règles d'engagement
- [ ] P20-T01-S03 — Coder la structure DecisionContext capturant l'état perçu lors du choix
- [ ] P20-T01-S04 — Rédiger le manuel des ordres opérationnels dans docs/MODELE_DECISION.md

### Tâche T20-02 — Moteur de validation des décisions
#### Sous-tâches
- [ ] P20-T02-S01 — Implémenter la classe OrderValidator vérifiant la faisabilité physique de l'ordre
- [ ] P20-T02-S02 — Générer des messages d'erreur explicites en cas de refus d'un ordre
- [ ] P20-T02-S03 — Développer les tests unitaires couvrant l'ensemble des cas d'invalidation
- [ ] P20-T02-S04 — Valider l'enregistrement de l'empreinte décisionnelle pour l'analyse ultérieure

---

## ÉTAPE 21 — Services Drogon

### Objectif
Implémenter la couche de services backend avec le framework C++ Drogon, fournissant l'API REST conforme OpenAPI et les canaux WebSocket temps réel.

### Entrées
- Moteur de simulation (`src/sim/`).
- Spécifications des échanges client-serveur.

### Sorties
- Contrôleurs HTTP REST et gestionnaires WebSocket Drogon opérationnels.
- Spécification OpenAPI 3.0 documentant l'ensemble des endpoints.

### Livrables
- Contrôleurs Drogon : `src/api/controllers/`, `src/api/websockets/`.
- Fichier de spécification API : `docs/openapi.yaml`.

### Critères d’acceptation
- Démarrage sans erreur du serveur HTTP/WebSocket Drogon sur port configurable.
- Authentification et assignation stricte des sessions par profil (Blue, Red, Umpire).
- Temps de réponse moyen des requêtes REST sous charge nominale < 15 ms.

### Tests
- Tests d'intégration automatisés des endpoints HTTP via curl / client HTTP Drogon.
- Test de diffusion de messages d'état aux clients connectés via WebSocket.

### Tâche T21-01 — Contrôleurs REST et documentation OpenAPI
#### Sous-tâches
- [ ] P21-T01-S01 — Implémenter le contrôleur de gestion de scénarios et sessions (/api/sessions)
- [ ] P21-T01-S02 — Implémenter le contrôleur de soumission des ordres tactiques (/api/orders)
- [ ] P21-T01-S03 — Générer et valider le contrat d'interface OpenAPI dans docs/openapi.yaml
- [ ] P21-T01-S04 — Coder les tests d'intégration automatisés des endpoints REST

### Tâche T21-02 — Passerelle WebSocket et synchronisation temps réel
#### Sous-tâches
- [ ] P21-T02-S01 — Développer le WebSocketHandler Drogon avec filtrage par rôle d'abonné
- [ ] P21-T02-S02 — Implémenter la sérialisation JSON haute performance des états perçus
- [ ] P21-T02-S03 — Développer le mécanisme de broadcast sélectif pour chaque tour ou événement
- [ ] P21-T02-S04 — Valider la robustesse aux déconnexions et reconnexions intempestives des clients

---

## ÉTAPE 22 — Interface Blue

### Objectif
Développer l'IHM web opérationnelle dédiée au joueur Blue en React/TypeScript, affichant la Common Operational Picture (COP) Blue, la grille et la console d'ordres.

### Entrées
- Contrat d'API REST et flux WebSocket (`docs/openapi.yaml`).
- Bibliothèque de symbolisation cartographique.

### Sorties
- Application web React/TypeScript pour le joueur Blue.
- Composants de carte interactive, panneau d'ordres et flux d'alertes.

### Livrables
- Code source frontend : `src/frontend/blue_app/`.
- Guide utilisateur Blue : `docs/MANUEL_UTILISATEUR_BLUE.md`.

### Critères d’acceptation
- Affichage exclusif des informations autorisées pour le camp Blue.
- Rendu fluide de la carte et de la grille hexagonale à 60 images par seconde.
- Soumission interactive d'ordres de mouvement et de posture validée par le backend.

### Tests
- Tests unitaires des composants React avec Vitest / React Testing Library.
- Test d'intégration de bout en bout simulant la connexion et la prise d'ordre Blue.

### Tâche T22-01 — Composant cartographique et affichage de la grille
#### Sous-tâches
- [ ] P22-T01-S01 — Initialiser l'application React/TypeScript pour l'espace joueur Blue
- [ ] P22-T01-S02 — Intégrer le composant cartographique et afficher la couche de fond SIG
- [ ] P22-T01-S03 — Développer la couche vectorielle de rendu de la grille hexagonale
- [ ] P22-T01-S04 — Implémenter la sélection interactive de cellule avec surbrillance

### Tâche T22-02 — Symbolisation tactique et panneau de commandement
#### Sous-tâches
- [ ] P22-T02-S01 — Implémenter la symbolisation normalisée des unités Blue et des contacts ennemis
- [ ] P22-T02-S02 — Développer le formulaire interactif de saisie d'ordres de déplacement
- [ ] P22-T02-S03 — Connecter le client WebSocket pour la réception des mises à jour en direct
- [ ] P22-T02-S04 — Rédiger le manuel d'utilisation Blue dans docs/MANUEL_UTILISATEUR_BLUE.md

---

## ÉTAPE 23 — Interface Red

### Objectif
Développer l'IHM web opérationnelle dédiée au joueur Red en React/TypeScript, reflétant fidèlement sa perspective opérationnelle, son brouillard de guerre et ses ordres.

### Entrées
- Spécifications des rôles et endpoints d'authentification Red.
- Composants de base développés à l'ÉTAPE 22.

### Sorties
- Application web React/TypeScript pour le joueur Red.
- Interface adaptée à la doctrine et aux capacités tactiques Red.

### Livrables
- Code source frontend : `src/frontend/red_app/`.
- Guide utilisateur Red : `docs/MANUEL_UTILISATEUR_RED.md`.

### Critères d’acceptation
- Étanchéité absolue de l'affichage Red vis-à-vis des positions réelles des unités Blue.
- Cohérence visuelle et ergonomique conforme aux exigences du PFE.
- Fonctionnement autonome sur navigateur web standard sans plugin tiers.

### Tests
- Tests de non-régression visuelle sur l'affichage des contacts perçus.
- Test d'exécution simultanée des interfaces Blue et Red sur deux navigateurs distincts.

### Tâche T23-01 — Déploiement du client Red
#### Sous-tâches
- [ ] P23-T01-S01 — Configurer l'environnement client Red avec profil d'authentification dédié
- [ ] P23-T01-S02 — Adapter la charte graphique et la symbolisation des forces d'opposition Red
- [ ] P23-T01-S03 — Implémenter l'affichage des observations rapportées par les capteurs Red
- [ ] P23-T01-S04 — Valider le blocage de tout accès aux canaux d'informations réservés à Blue

### Tâche T23-02 — Contrôles tactiques et ergonomie Red
#### Sous-tâches
- [ ] P23-T02-S01 — Adapter le panneau de commandement pour les ordres spécifiques Red
- [ ] P23-T02-S02 — Implémenter le retour visuel de validation des ordres soumis par Red
- [ ] P23-T02-S03 — Coder la console d'historique des alertes et contacts pour Red
- [ ] P23-T02-S04 — Rédiger le guide d'utilisation Red dans docs/MANUEL_UTILISATEUR_RED.md

---

## ÉTAPE 24 — Interface Umpire

### Objectif
Développer l'IHM de supervision de l'Arbitre (Umpire) en React/TypeScript, permettant le contrôle complet du scénario, l'affichage de l'état réel et l'injection d'événements.

### Entrées
- Services d'arbitrage Drogon (`/api/umpire/*`).
- Spécifications du rôle de supervision globale.

### Sorties
- Console de supervision Umpire complète avec vue omnisciente.
- Outils d'injection d'incidents météo, pannes ou ordres d'arbitre en temps réel.

### Livrables
- Code source frontend : `src/frontend/umpire_app/`.
- Manuel de l'arbitre : `docs/MANUEL_UMPIRE.md`.

### Critères d’acceptation
- Affichage simultané et différencié : réalité terrain, vision Blue, vision Red.
- Contrôle direct du cycle de simulation : pause, avance pas-à-pas, modification de vitesse.
- Capacité d'injecter des événements exogènes perturbateurs en cours de partie.

### Tests
- Test de basculement de vue (vue réelle, calque Blue, calque Red) sur l'interface Umpire.
- Test d'injection d'un événement arbitre et vérification de sa propagation immédiate.

### Tâche T24-01 — Tableau de bord omniscient Umpire
#### Sous-tâches
- [ ] P24-T01-S01 — Développer l'interface Umpire avec triple affichage (Réel, Perçu Blue, Perçu Red)
- [ ] P24-T01-S02 — Implémenter les commutateurs de couches pour superposer ou isoler les vues
- [ ] P24-T01-S03 — Afficher le panneau de pilotage de l'horloge (Play, Pause, Step, Vitesse)
- [ ] P24-T01-S04 — Rédiger le manuel d'exploitation Arbitre dans docs/MANUEL_UMPIRE.md

### Tâche T24-02 — Outils d'intervention et d'arbitrage
#### Sous-tâches
- [ ] P24-T02-S01 — Développer le formulaire d'injection d'événements (Météo, Brouillage, Pannes)
- [ ] P24-T02-S02 — Implémenter l'ajustement direct des postures ou de l'attrition d'une unité
- [ ] P24-T02-S03 — Coder la console d'affichage en direct des journaux du système
- [ ] P24-T02-S04 — Valider l'auditabilité de toute intervention d'arbitrage dans les traces

---

## ÉTAPE 25 — Journalisation

### Objectif
Concevoir et déployer le système de journalisation structurée et immuable, garantissant l'auditabilité intégrale des ordres, événements, observations et décisions.

### Entrées
- Moteur de simulation et ensemble des couches fonctionnelles.
- Spécifications de traçabilité du cahier des charges.

### Sorties
- Sous-système de logging haute performance avec spdlog et persistance PostGIS.
- Schéma structuré des traces d'audit (JSON structuré avec horodatage haute précision).

### Livrables
- Module de logging : `src/logging/simulation_logger.hpp`, `src/logging/log_entry.hpp`.
- Schéma de base de données de journalisation : `src/db/migrations/V002__logging_schema.sql`.

### Critères d’acceptation
- Zéro perte de trace lors des montées en charge de la simulation.
- Horodatage microseconde et typage strict de chaque événement journalisé.
- Format de log compatible avec les exigences d'auditabilité C4ISR CommandView.

### Tests
- Tests de stress d'écriture de 50 000 événements consécutifs sans blocage du moteur.
- Test de conformité du schéma JSON des traces produites.

### Tâche T25-01 — Architecture du journal d'audit structuré
#### Sous-tâches
- [ ] P25-T01-S01 — Définir la structure LogEntry (timestamp, session_id, type, acteur, payload)
- [ ] P25-T01-S02 — Configurer spdlog pour l'écriture asynchrone sans blocage du thread de calcul
- [ ] P25-T01-S03 — Implémenter le collecteur de traces vers la base de données PostgreSQL
- [ ] P25-T01-S04 — Écrire la spécification du format des traces dans docs/SPECIFICATION_LOGS.md

### Tâche T25-02 — Couverture des événements et intégrité
#### Sous-tâches
- [ ] P25-T02-S01 — Instrumenter le moteur pour tracer chaque transition d'état d'unité
- [ ] P25-T02-S02 — Tracer les soumissions d'ordres avec leur contexte décisionnel complet
- [ ] P25-T02-S03 — Coder la vérification d'intégrité cryptographique des journaux (checksums)
- [ ] P25-T02-S04 — Valider l'exhaustivité des logs par rapport aux exigences du cahier des charges

---

## ÉTAPE 26 — Rejeu

### Objectif
Développer le moteur de rejeu fidèle et la console de restitution temporelle permettant de revivre une session enregistrée avec vitesse modulable et sauts temporels.

### Entrées
- Traces structurées générées à l'ÉTAPE 25.
- Moteur d'état `WorldState`.

### Sorties
- Module C++20 `replay_core` capable de reconstituer l'état du monde à tout instant T.
- Interface de lecture temporelle (Play, Pause, VCR, Slider chronologique).

### Livrables
- Fichiers sources : `src/replay/replay_engine.hpp`, `src/replay/timeline_navigator.hpp`.
- Interface de rejeu : `src/frontend/replay_viewer/`.

### Critères d’acceptation
- Exactitude rigoureuse de la reconstitution de l'état du monde à tout pas de temps.
- Navigation bidirectionnelle fluide (recul, avance rapide, saut direct à un tour).
- Capacité de basculer la perspective de vue pendant le rejeu (Réel, Blue, Red).

### Tests
- Test de conformité : comparaison automatique entre l'état initial simulé et l'état rejoué.
- Test de performance lors du saut chronologique instantané sur une session de 200 tours.

### Tâche T26-01 — Moteur de reconstitution chronologique
#### Sous-tâches
- [ ] P26-T01-S01 — Implémenter le chargeur de session ReplayLoader depuis les logs PostgreSQL
- [ ] P26-T01-S02 — Développer la reconstruction par application séquentielle des deltas d'état
- [ ] P26-T01-S03 — Mettre en place un système d'instantanés périodiques (key-frames) pour les sauts rapides
- [ ] P26-T01-S04 — Valider la stricte identité d'état entre session originale et rejeu

### Tâche T26-02 — Contrôleur et lecteur de rejeu
#### Sous-tâches
- [ ] P26-T02-S01 — Développer les composants d'interface de la barre de navigation temporelle
- [ ] P26-T02-S02 — Implémenter le sélecteur de point de vue dynamique en cours de rejeu
- [ ] P26-T02-S03 — Développer le panneau d'affichage des événements marquants sur la frise
- [ ] P26-T02-S04 — Rédiger le guide d'utilisation du rejeu dans docs/GUIDE_REJEU.md

---

## ÉTAPE 27 — Débriefing et indicateurs

### Objectif
Concevoir et implémenter les outils d'analyse après action (AAR), le calcul des indicateurs de performance tactique, l'analyse des écarts et la génération de rapports.

### Entrées
- Données de rejeu et traces de simulation.
- Métriques d'évaluation décisionnelle définies dans le cahier des charges.

### Sorties
- Module de calcul des indicateurs de débriefing `DebriefMetricsEngine`.
- Générateur automatique de rapports de synthèse de session (PDF / Markdown / JSON).

### Livrables
- Fichiers sources : `src/debrief/metrics_calculator.hpp`, `src/debrief/report_generator.hpp`.
- Tableau de bord de restitution : `src/frontend/debrief_dashboard/`.

### Critères d’acceptation
- Calcul quantitatif des écarts entre perception et réalité (délai de détection, erreur de position).
- Analyse de la réactivité décisionnelle (délai entre détection et émission d'ordre).
- Exportation réussie d'un rapport complet d'analyse après action.

### Tests
- Tests unitaires sur les formules mathématiques de calcul des indicateurs tactiques.
- Test de génération de rapport automatisé sans régression de format.

### Tâche T27-01 — Moteur de calcul des métriques décisionnelles
#### Sous-tâches
- [ ] P27-T01-S01 — Implémenter le calcul du temps moyen de réaction tactique par camp
- [ ] P27-T01-S02 — Calculer l'indicateur d'erreur d'appréciation de la situation ennemie
- [ ] P27-T01-S03 — Implémenter le ratio d'efficacité des ordres (ordres exécutés vs annulés/bloqués)
- [ ] P27-T01-S04 — Coder le calcul des pertes et consommations relatives de ressources

### Tâche T27-02 — Restitution visuelle et rapports de synthèse
#### Sous-tâches
- [ ] P27-T02-S01 — Concevoir les graphiques interactifs d'évolution de la partie (courbes de pertes, détection)
- [ ] P27-T02-S02 — Développer le composant de comparaison visuelle côte-à-côte Réel vs Perçu
- [ ] P27-T02-S03 — Implémenter le générateur de rapport de synthèse de débriefing
- [ ] P27-T02-S04 — Documenter la méthodologie d'analyse tactique dans docs/DEBRIEFING_METHODOLOGIE.md

---

## ÉTAPE 28 — Scénario de démonstration complet

### Objectif
Concevoir, intégrer et tester un scénario tactique de référence complet de bout en bout, illustrant l'ensemble des capacités du wargame géospatial.

### Entrées
- Système intégralement assemblé (SIG, moteur, services, interfaces, débriefing).
- Données géographiques validées sur la zone de démonstration.

### Sorties
- Scénario tactique de référence officiel prêt à être exécuté pour la soutenance.
- Script de déroulement pas-à-pas de la démonstration avec points clés à observer.

### Livrables
- Fichier scénario de référence : `data/scenarios/scenario_reference_demonstration.json`.
- Guide de la démonstration : `docs/SCENARIO_DEMONSTRATION.md`.

### Critères d’acceptation
- Déroulement fluide et sans plantage de l'ensemble de la séquence opérationnelle.
- Mise en valeur explicite du rôle du terrain SIG, du brouillard de guerre et de l'arbitrage.
- Durée de démonstration calibrée (15 à 25 minutes) adaptée au jury de PFE.

### Tests
- Répétition intégrale automatisée et manuelle du scénario de démonstration.
- Validation des points de contrôle d'évaluation tactique durant la session.

### Tâche T28-01 — Scénarisation tactique et paramétrage
#### Sous-tâches
- [ ] P28-T01-S01 — Rédiger l'Ordre Préparatoire d'Opération (OPO) et le narratif tactique du scénario
- [ ] P28-T01-S02 — Définir la composition initiale des forces Blue et Red au niveau bataillon
- [ ] P28-T01-S03 — Placer les unités sur les cellules hexagonales de départ conformément à la doctrine
- [ ] P28-T01-S04 — Configurer les conditions météorologiques, visibilité et paramètres d'incertitude

### Tâche T28-02 — Répétition et validation de la démonstration
#### Sous-tâches
- [ ] P28-T02-S01 — Valider l'enchaînement chronologique des événements planifiés et imprévus
- [ ] P28-T02-S02 — Vérifier la lisibilité des situations tactiques sur les trois écrans en simultané
- [ ] P28-T02-S03 — Éprouver le déclenchement du rejeu et la pertinence du rapport de débriefing
- [ ] P28-T02-S04 — Rédiger le conducteur officiel de soutenance dans docs/SCENARIO_DEMONSTRATION.md

---

## ÉTAPE 29 — Validation globale

### Objectif
Exécuter la campagne formelle de recette globale, de non-régression, d'audit de sécurité et de conformité stricte vis-à-vis du cahier des charges officiel.

### Entrées
- Système finalisé et scénario de référence opérationnel.
- Matrice de traçabilité issue de l'ÉTAPE 01.

### Sorties
- Procès-verbal de recette globale du système.
- Matrice de conformité définitive certifiant 100% des exigences satisfaites.

### Livrables
- Rapport officiel de validation globale : `docs/RAPPORT_VALIDATION_GLOBALE.md`.
- Matrice de traçabilité finale complétée avec références de tests.

### Critères d’acceptation
- Taux de succès des tests automatisés unitaires et d'intégration égal à 100%.
- Absence totale d'anomalie critique ou bloquante répertoriée.
- Conformité intégrale validée avec chaque exigence du cahier des charges.

### Tests
- Exécution de l'ensemble de la suite de tests unitaires, d'intégration et système.
- Test de charge et d'endurance sur session prolongée.

### Tâche T29-01 — Campagne de tests d'intégration et de robustesse
#### Sous-tâches
- [ ] P29-T01-S01 — Exécuter l'intégralité des tests GoogleTest C++20 avec rapport de couverture
- [ ] P29-T01-S02 — Exécuter la suite de tests frontend React et valider l'absence d'erreurs console
- [ ] P29-T01-S03 — Réaliser le test d'endurance sur 500 tours de jeu continus
- [ ] P29-T01-S04 — Auditer la conformité stricte du protocole de communication avec Drogon

### Tâche T29-02 — Recette formelle du cahier des charges
#### Sous-tâches
- [ ] P29-T02-S01 — Passer en revue chaque exigence de la matrice de traçabilité avec son résultat
- [ ] P29-T02-S02 — Vérifier le respect des contraintes d'abstraction et d'isolation sécuritaire
- [ ] P29-T02-S03 — Valider la conformité de l'interface CommandView Ready
- [ ] P29-T02-S04 — Rédiger et signer le procès-verbal de recette dans docs/RAPPORT_VALIDATION_GLOBALE.md

---

## ÉTAPE 30 — Documentation finale et soutenance

### Objectif
Finaliser l'ensemble de la documentation technique, rédiger le mémoire de PFE, préparer le support de présentation multimédia et organiser la soutenance devant le jury.

### Entrées
- Ensemble des livrables techniques, rapports d'essais et code source validé.
- Directives académiques de rédaction du mémoire de PFE.

### Sorties
- Mémoire de fin d'études complet, structuré et relu.
- Diaporama de soutenance officiel avec illustrations vectorielles et démonstrateur.

### Livrables
- Mémoire de PFE : `docs/MEMOIRE_PFE_WARGAME_GEOSPATIAL.pdf`.
- Support de soutenance : `docs/PRESENTATION_SOUTENANCE.pdf`.
- Dossier d'architecture consolidé pour publication.

### Critères d’acceptation
- Qualité rédactionnelle, rigueur scientifique et clarté technique du mémoire.
- Support de soutenance professionnel intégrant les diagrammes d'architecture vectoriels.
- Dossier de projet complet, archivable et reproductible sur tout environnement cible.

### Tests
- Contrôle de cohérence croisée entre le mémoire, le cahier des charges et le logiciel réalisé.
- Répétition générale chronométrée de la présentation orale et de la démonstration live.

### Tâche T30-01 — Finalisation de la documentation technique et utilisateur
#### Sous-tâches
- [ ] P30-T01-S01 — Consolider le manuel d'installation et d'administration dans docs/INSTALLATION.md
- [ ] P30-T01-S02 — Finaliser la documentation des APIs et schémas de base de données
- [ ] P30-T01-S03 — Vérifier et uniformiser l'ensemble des liens et références de la documentation
- [ ] P30-T01-S04 — Générer la documentation du code C++ via Doxygen ou équivalent

### Tâche T30-02 — Rédaction du mémoire et préparation de la soutenance
#### Sous-tâches
- [ ] P30-T02-S01 — Rédiger le mémoire de PFE couvrant contexte, état de l'art, architecture et résultats
- [ ] P30-T02-S02 — Intégrer les diagrammes vectoriels professionnels dans le manuscrit
- [ ] P30-T02-S03 — Élaborer le support de soutenance visuel pour le jury
- [ ] P30-T02-S04 — Réaliser la répétition générale de la soutenance et figer les livrables finaux
