# PROJECT PROMPT — WARGAME GÉOSPATIAL PFE

Construire un démonstrateur autonome de wargame géospatial pour l'entraînement à la prise de décision, conformément au cahier des charges officiel.

Objectif fonctionnel :
Terrain SIG → grille hexagonale → situation initiale → Blue/Red → capteurs et observations → état réel/perçu → décisions → moteur de simulation → temps/événements → journalisation → rejeu → débriefing.

Choix techniques du projet :
- C++20 / Drogon
- PostgreSQL/PostGIS
- Global Mapper pour la chaîne SIG/ETL
- H3 ou équivalent après validation
- React/TypeScript
- OpenLayers ou Leaflet
- spdlog
- GoogleTest
- Docker/Compose
- Git/CI

Priorité :
1. exactitude du modèle ;
2. traçabilité ;
3. testabilité ;
4. simplicité ;
5. interface.
