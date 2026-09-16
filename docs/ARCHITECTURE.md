# ARCHITECTURE CIBLE

## 1. Vue générale

```text
DONNÉES SOURCES
      |
      v
GLOBAL MAPPER
collecte / préparation / nettoyage / reprojection / découpage / contrôle
      |
      v
DONNÉES SIG PROPRES
      |
      v
POSTGRESQL + POSTGIS
      |
      +----------------------+
      |                      |
      v                      v
MODÈLE TERRAIN          MODÈLE SCÉNARIO
grille hexagonale       situation initiale
cellules                règles / objectifs
      |                      |
      +----------+-----------+
                 v
         MOTEUR DE SIMULATION
         C++20
                 |
      +----------+----------+
      |          |          |
      v          v          v
   TEMPS     CAPTEURS    ÉVÉNEMENTS
      |          |          |
      +----------+----------+
                 v
          ÉTAT RÉEL / ÉTAT PERÇU
                 |
                 v
          DÉCISIONS / ACTIONS
                 |
                 v
           JOURNALISATION
                 |
        +--------+--------+
        v                 v
      REJEU             DÉBRIEFING
                 |
                 v
        REST / WEBSOCKET
                 |
                 v
       REACT + CARTE
       BLUE / RED / UMPIRE
```

## 2. Responsabilités

### Global Mapper
Collecte et préparation des données géographiques avant ingestion dans le système.

### PostGIS
Source persistante de vérité pour :
- terrain ;
- grille ;
- géométries ;
- métadonnées ;
- scénarios et sessions selon le modèle final.

### Domaine
Objets métier indépendants de la base et de l'IHM.

### Moteur de simulation
Temps, règles, déplacements, événements, transitions d'état, observations et production des traces.

### Services
REST/OpenAPI et WebSocket via Drogon.

### IHM
React/TypeScript et moteur cartographique choisi.

### Journalisation
Traces structurées des actions, observations, décisions, événements et transitions.

## 3. Principe de séparation
Aucun composant ne doit absorber les responsabilités d'un autre.
