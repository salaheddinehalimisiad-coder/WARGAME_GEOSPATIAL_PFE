# ARCHITECTURE CIBLE

## 1. Vue générale

```text
DONNÉES SOURCES
      |
      v
PIPELINE SIG & ETL
Global Mapper (principal) + QGIS / GDAL / PROJ (compléments)
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
      +----------+----------+
      |                     |
      v                     v
REACT + CARTE         COMMANDVIEW READY
BLUE / RED / UMPIRE   (Interopérabilité C4ISR future)
```

## 2. Responsabilités

### Pipeline SIG / ETL (Global Mapper, QGIS, GDAL, PROJ)
Collecte, traitement de MNT, conversions, reprojections et préparation des couches géospatiales avant ingestion dans le système. Global Mapper sert de base principale, épaulé par QGIS/GDAL/PROJ pour l'automatisation et les traitements complémentaires.

### PostGIS
Source persistante de vérité pour :
- terrain ;
- grille hexagonale ;
- géométries et index spatiaux ;
- métadonnées ;
- scénarios et sessions.

### Domaine
Objets métier purs (Terrain, Cell, Unit, Equipment, Sensor, Observation, Decision, Event...) indépendants de la base et de l'IHM.

### Moteur de simulation
Temps, règles, déplacements, événements, transitions d'état, incertitude (état réel vs perçu) et production des traces.

### Services
REST/OpenAPI et WebSocket via Drogon.

### IHM
React/TypeScript et moteur cartographique choisi (OpenLayers / Leaflet). Vues Blue, Red et Arbitre.

### Journalisation
Traces structurées des actions, observations, décisions, événements et transitions (reproductibilité, rejeu, débriefing).

## 3. Principe de séparation
Aucun composant ne doit absorber les responsabilités d'un autre.

## 4. Principe « Autonomous First — CommandView Ready » (Section 33 du Cahier des charges)

Le wargame est développé comme un système autonome pour l'expérimentation de la prise de décision, tout en garantissant dès sa conception la compatibilité avec une intégration ultérieure dans l'architecture C4ISR **CommandView** :

1. **Connexion à une base opérationnelle distribuée** : Modèle de données spatiales et entités compatibles avec les schémas C4ISR.
2. **Publication et consommation d'événements** : Événements de jeu et décisions exposés sous forme d'événements standardisés.
3. **Intégration au COP (Common Operational Picture)** : Couches cartographiques, symbolisation et statuts des forces exploitables directement par le COP de CommandView.
4. **Interopérabilité des alertes et de la journalisation** : Logs structurés auditables, compatibles avec les outils de traçabilité opérationnels.
5. **Aide à la décision et planification** : Points d'extension pour brancher des modules d'analyse tactique ou de planification d'ordres.
6. **Sécurité et rôles (IAM / RBAC)** : Gestion des profils Blue, Red, Umpire articulée sur des rôles extensibles.
7. **Supervision et observabilité** : Métriques du moteur et état des sessions exposables via des standards d'observabilité.

