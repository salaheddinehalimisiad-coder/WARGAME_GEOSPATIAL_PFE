# SOURCES DES DIAGRAMMES D'ARCHITECTURE

Ce dossier contient les fichiers sources vectoriels modifiables des 6 diagrammes d'architecture du projet **WARGAME GÉOSPATIAL PFE** :

1. `architecture_globale.svg` : Architecture globale de bout en bout (SIG amont → PostGIS → Moteur C++20 → Drogon → React/TS → CommandView Ready).
2. `architecture_pipeline_sig.svg` : Pipeline SIG exclusif Global Mapper (Collecte → Préparation → Nettoyage → Contrôle QA → Données Propres → PostGIS).
3. `architecture_donnees.svg` : Modèle de données relationnel et entités métier (Scenario, Session, Unit, Equipment, Sensor, Cell, Event, LogEntry, DebriefMetric).
4. `architecture_flux_simulation.svg` : Cycle complet et boucle OODA de simulation pas-à-pas avec déterminisme bit-à-bit.
5. `architecture_blue_red_umpire.svg` : Cloisonnement strict des vues, brouillard de guerre et rôle d'arbitrage omniscient Umpire.
6. `architecture_technique.svg` : Stack logicielle, protocoles de communication (REST/OpenAPI, WebSocket), conteneurisation Docker et CI/CD.

## Outils d'édition recommandés

Les fichiers sources sont rédigés en format SVG vectoriel standardisé (W3C XML) et peuvent être ouverts et édités avec :
- **Draw.io** (desktop ou web sur draw.io) : Glisser-déposer le fichier SVG pour le modifier graphiquement.
- **Inkscape** : Éditeur vectoriel open-source de référence.
- **Adobe Illustrator** ou **Figma** : Support complet des calques et styles SVG.
- **Éditeur de code (VS Code / Antigravity)** : Modification textuelle directe des coordonnées et labels.

## Règles graphiques
- Fond blanc obligatoire (`#ffffff`).
- Typographie système lisible (-apple-system, Segoe UI, Roboto, Helvetica, Arial).
- Aucune régression vers des schémas ASCII textuels.
- Alignement strict avec les décisions architecturales officielles du Master Prompt v1.0.
