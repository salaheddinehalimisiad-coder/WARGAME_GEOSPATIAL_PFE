# ROADMAP — PROJET REPARTI DE ZERO

## Phase 0 — Initialisation
Références, règles agent, structure projet, Git, documentation.

## Phase 1 — Analyse et architecture
Exigences, acteurs, scénarios fonctionnels, architecture, modèle de données.

## Phase 2 — SIG / ETL avec Global Mapper
Collecte des données, MNT/DEM, routes, hydrographie, végétation/occupation du sol, zones urbaines/infrastructures, limites et emprises.
Objectif : produire des couches propres et documentées.

## Phase 3 — QA des données SIG
Contrôle géométrique, CRS, emprises, attributs, cohérence topologique, métadonnées et reproductibilité.

## Phase 4 — Grille hexagonale
Choix H3 ou équivalent, génération/chargement de la grille, règles d'identification et voisinage.

## Phase 5 — PostGIS
Schéma, contraintes, index spatiaux, ingestion des données propres et de la grille.

## Phase 6 — Unités et équipements
Unit, Side, Equipment, Sensor, capacités abstraites.

## Phase 7 — Moteur de simulation
État du monde, déplacements, règles, transitions et reproductibilité.

## Phase 8 — Capteurs et incertitude
Observations, confiance, précision, état réel vs état perçu.

## Phase 9 — Temps, événements et décisions
Horloge, événements planifiés/conditionnels, délais, décisions, contraintes.

## Phase 10 — Services
Drogon, REST, WebSocket, gestion de session.

## Phase 11 — Interfaces
Blue, Red, Umpire, carte et COP.

## Phase 12 — Journalisation et rejeu
Log structuré, reconstruction d'une session.

## Phase 13 — Débriefing
Chronologie, décisions majeures, indicateurs, comparaison réel/perçu.

## Phase 14 — Validation
Tests, démonstration de bout en bout, documentation finale.

Règle : une phase ne passe à la suivante qu'après validation.
