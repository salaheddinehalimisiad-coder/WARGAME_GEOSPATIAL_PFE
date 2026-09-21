# ARCHITECTURE DU PROJET

Référence : `MASTER_PROMPT.md` (Version 1.0 — PFE 2026–2027) & `Cahier_des_charges_PFE_Wargame_geospatial.docx`.  
Principe directeur : « Autonomous First — CommandView Ready » (système 100% autonome pour le PFE, tout en préparant des interfaces ouvertes compatibles avec une intégration ultérieure dans le C4ISR CommandView).  
Diagrammes : Tous les schémas sont présentés sous forme vectorielle haute fidélité avec fond blanc (sources modifiables dans [`docs/assets/architecture/source/`](assets/architecture/source/)).

---

## Vue globale

![Architecture Globale](assets/architecture/architecture_globale.svg)

### Explication de l'architecture globale

L'architecture du wargame géospatial repose sur un découpage en cinq couches horizontales étanches, garantissant l'indépendance de la simulation vis-à-vis de l'affichage et du réseau :

1. **Préparation SIG amont** : Traitement des données géographiques exclusivement sous Global Mapper, garantissant l'intégrité du Modèle Numérique de Terrain (MNT), du réseau viaire et de l'occupation du sol. Les couches certifiées par le contrôle qualité (QA) sont exportées sans valeurs NoData vers les formats d'ingestion standardisés (GeoTIFF projeté métrique, GeoPackage).
2. **Persistance spatiale PostgreSQL / PostGIS** : Source de vérité persistante du théâtre d'opérations. Elle stocke les polygones géoréférencés des cellules hexagonales, les attributs physiques agrégés du terrain, les scénarios, ainsi que les journaux d'audit immuables. L'indexation spatiale GiST garantit des temps de sélection optimisés.
3. **Moteur de simulation C++20 (`SimulationEngine`)** : Cœur autonome fonctionnant en temps discret ou continu discrétisé. Il détient l'état réel omniscient (`WorldState`), applique les règles d'engagement au niveau bataillon, calcule les déplacements sur la grille hexagonale pondérés par le relief, calcule les lignes de vue altimétriques (LOS) et génère l'état perçu propre à chaque camp grâce à un modèle d'incertitude paramétrable.
4. **Services backend et API Drogon** : Framework C++ haute performance fournissant des contrôleurs REST conformes à OpenAPI 3.0 pour la gestion des sessions et la prise d'ordres, ainsi qu'un serveur WebSocket assurant la diffusion en direct des mises à jour aux clients autorisés.
5. **Applications frontend React / TypeScript** : Trois interfaces dédiées aux rôles tactiques :
   - **Interface Blue** : Common Operational Picture (COP) tactique amie, visualisation des contacts perçus bruités et console d'ordres.
   - **Interface Red** : Vue tactique de l'opposition avec ses propres capteurs, son brouillard de guerre et ses ordres tactiques.
   - **Interface Umpire** : Console omnisciente de l'arbitre, capable de superposer vérité terrain et perceptions, de moduler l'horloge et d'injecter des incidents.
   - **Module de Rejeu & Débriefing (AAR)** : Navigation temporelle pas-à-pas et indicateurs d'aide à la décision.

---

## Pipeline SIG

![Pipeline SIG](assets/architecture/architecture_pipeline_sig.svg)

### Explication du pipeline SIG

Le pipeline SIG assure la transformation rigoureuse des données brutes en un modèle géospatial exploitable par le moteur :

- **Outil unique de référence** : Global Mapper est l'unique outil SIG du workflow courant pour l'ensemble des opérations de traitement géométrique, d'harmonisation altimétrique et de contrôle qualité.
- **Cycle séquentiel** :
  1. *Collecte* : Importation des dalles MNT et couches vectorielles sélectionnées et validées dans un projet de travail `.gmw`.
  2. *Préparation* : Reprojection systématique dans le Système de Coordonnées de Référence (CRS) métrique officiel (UTM) et traitement des valeurs NoData selon une méthode documentée et validée.
  3. *Nettoyage topologique* : Découpage strict sur l'emprise géographique d'exercice (Bounding Box) et élimination des artefacts géométriques (micro-polygones, nœuds pendants).
  4. *Contrôle qualité (QA)* : Validation formelle selon un protocole de contrôle documenté avant gel des données et ingestion dans PostGIS.

---

## Architecture des données

![Architecture des Données](assets/architecture/architecture_donnees.svg)

### Explication du modèle relationnel

Le schéma de données est structuré en troisième forme normale (3NF) et combine entités spatiales et entités de simulation :

- **Entités géospatiales** : `TerrainCell` (cellule hexagonale avec coordonnées axiales cubiques `q, r, s` et géométrie PostGIS polygonale métrique), enrichie par les attributs de pente maximale, rugosité, hydrographie et coût de mobilité.
- **Entités opérationnelles** : `Unit` (bataillon rattaché à une faction `Side`), `Equipment` (profil générique abstrait caractérisé par mobilité, protection et puissance relative, sans mention d'arme réelle) et `Sensor` (portée, précision, sensibilité météo).
- **Entités dynamiques et traçabilité** : `GameSession` (session de jeu et graine pseudo-aléatoire), `Observation` (contact perçu bruité avec indice de confiance), `Decision` (ordre tactique horodaté avec justification opérationnelle), `Event` (événement de jeu) et `LogEntry` (trace d'audit immuable avec horodatage microseconde et empreinte cryptographique).
- **Entité d'analyse après action** : `DebriefMetric` consolidant les temps de réaction, pertes relatives et distorsions d'appréciation pour le débriefing.

---

## Flux de simulation

![Flux de Simulation](assets/architecture/architecture_flux_simulation.svg)

### Explication du flux d'exécution et de simulation

Le moteur C++20 orchestre chaque cycle de simulation selon une boucle fermée déterministe garantissant une reproductibilité contrôlée :

1. **État initial (WorldState $S_0$)** : Chargement de la grille, des unités et initialisation des paramètres de scénario (avec reproductibilité contrôlée [prop.]).
2. **Actions & Ordres** : Réception des ordres des joueurs via l'API Drogon.
3. **Règles & Contraintes** : Filtrage de faisabilité physique (franchissement du relief, points de mouvement restants).
4. **Temps & Événements** : Avancement de la `SimulationClock` et dépilement ordonné de l'`EventQueue`.
5. **Observations & LOS** : Calcul des lignes de vue d'après l'altimétrie du MNT et génération des contacts bruités.
6. **Séparation État Réel / État Perçu** : Mise à jour de l'état vrai pour l'arbitre et construction des vues partielles pour Blue et Red.
7. **Décisions** : Traitement des choix tactiques des commandants face à leur situation perçue.
8. **Nouvel état ($S_{T+1}$)** : Validation des transitions et application atomique sur le monde.
9. **Journalisation** : Écriture asynchrone non-bloquante de la trace complète via spdlog vers PostgreSQL.

---

## Blue / Red / Umpire

![Blue Red Umpire](assets/architecture/architecture_blue_red_umpire.svg)

### Explication du cloisonnement et des rôles

Le système met en œuvre une politique d'isolation stricte de l'information (brouillard de guerre) :

- **Socle d'informations communes** : Relief SIG, grille hexagonale, réseau routier public et météo générale sont partagés par l'ensemble des acteurs.
- **Cloisonnement Blue / Red** : Chaque joueur dispose uniquement de la visibilité sur ses propres unités et sur les contacts ennemis effectivement détectés par ses capteurs. Les coordonnées adverses non observées ne sont jamais transmises au client, prévenant toute tricherie par inspection mémoire ou réseau.
- **Rôle privilégié de l'Arbitre (Umpire)** :
  - *Vision omnisciente* : Superposition en direct de la réalité terrain et des perceptions Blue et Red, avec mise en évidence des erreurs d'appréciation.
  - *Pilotage temporel* : Pause, lecture pas-à-pas et modification de la cadence de simulation.
  - *Injection d'aléas* : Déclenchement impromptu de perturbations météo ou de pannes matérielles.

---

## Architecture technique

![Architecture Technique](assets/architecture/architecture_technique.svg)

### Explication de la pile logicielle et infrastructure

La solution s'articule autour de technologies modernes, standardisées et conteneurisées :

- **Frontend** : React, TypeScript, OpenLayers / Leaflet pour la cartographie interactive, styles soignés et composants réactifs.
- **Backend & Services** : Framework C++ Drogon, offrant des performances d'exécution maximales, des contrôleurs REST documentés par OpenAPI 3.0 et une passerelle WebSocket bidirectionnelle.
- **Cœur de simulation C++20** : Moteur compilé avec les normes C++20 les plus strictes (`-Wall -Wextra -Wpedantic`), testé unitairement par GoogleTest et exempt de toute dépendance graphique.
- **Base de données & SIG** : PostgreSQL associé à PostGIS déployé via Docker Compose, alimenté par les données issues de Global Mapper.
- **Outillage DevOps & CI/CD** : Intégration continue GitHub Actions (`.github/workflows/ci.yml`), scripts de pilotage documentaire déterministes (`scripts/update_progress.py`), et gouvernance Git basée sur des branches isolées par phase.
- **Extension CommandView Ready** : Points d'ancrage prévus pour une intégration future au système C4ISR CommandView (bus d'événements, formats de données standardisés, observabilité).

---

## Découpage modulaire C++20 (`src/`)

### Objectif du découpage
Conformément aux exigences de modularité, de découplage logique et de testabilité indépendante (*CdC Section 16, 21, 24*), le cœur logiciel en C++20 est structuré selon un découpage en cinq modules logiques étanches.

> [!NOTE]
> Le découpage exact en cinq modules `core / terrain / units / sim / api` constitue un **choix d'ingénierie interne du projet [C]** mis au service des exigences fonctionnelles et contractuelles du CdC v1.0.

### Responsabilités des modules

#### 1. Module `core` [C]
Fournit le socle universel transverse partagé par l'ensemble des modules :
- Abstraction des identifiants typés (`UnitId`, `CellId`, `SessionId`, `EventId`).
- Types géométriques et mathématiques élémentaires (vecteurs, distances, angles).
- Abstraction générique des coordonnées spatiales de la grille (sans figer de format concret prématuré).
- Structures communes de retour et de gestion d'erreurs, horodatage et utilitaires transverses.
- *Interdictions* : Aucune logique métier tactique, aucun état de simulation, aucune dépendance réseau, SQL ou IHM.

#### 2. Module `terrain` [A / C]
Responsable exclusif de la représentation en mémoire et de l'interrogation des données géographiques :
- Modélisation de la grille spatiale hexagonale régulière (*CdC Section 5.2 [A]*).
- Attributs physiques et environnementaux agrégés par cellule : altitude MNT, pente maximale calculée, couverture végétale, présence hydrographique, franchissabilité et réseau viaire (*CdC Section 5.2 [A]*).
- Primitives de calcul spatial pur : relations d'adjacence, calculs de distance sur la grille, profils altimétriques et calcul géométrique brut de ligne de vue (LOS altimétrique).
- *Interdictions* : Aucune logique d'adjudication ou d'engagement, aucune connaissance des unités, aucun accès direct SQL (les données sont injectées au chargement).

#### 3. Module `units` [A / C]
Modélise les entités opérationnelles et leurs capacités abstraites :
- Échelon minimal strict fixé au **bataillon** (*CdC Section 5.3 [A]*), sans représentation de sous-entités individuelles.
- Attributs obligatoires de l'unité : identifiant, affiliation (`Blue` / `Red`), type/rôle générique (infanterie, blindé, appui, reconnaissance, logistique), posture opérationnelle et effectif/disponibilité relative (*CdC Section 5.3 [A]*).
- **Abstraction capacitaire totale** des équipements et capteurs sans aucune référence à des armes réelles, calibres ou désignations réelles (*CdC Section 5.4, 31 [A]*).
- *Interdictions* : Zéro caractéristique d'arme réelle, aucune gestion du temps ou de l'ordonnancement de simulation.

#### 4. Module `sim` [A / C]
Cœur autonome du moteur de simulation :
- **Autorité souveraine sur l'État Réel (`WorldState`)** : détient et fait évoluer la situation objective du monde (unités réelles, postures, horloge logique, file d'événements) (*CdC Section 6, 7 [A]*).
- **Gestion temporelle et événementielle** : pilote l'horloge logique et ordonnance la file prioritaire des événements (*CdC Section 8 [A]*).
- **Résolution et transitions d'état** : valide la franchissabilité du relief, applique les règles d'adjudication de façon déterministe et calcule les transitions d'état (*CdC Section 7, 24 [A]*).
- **Génération de l'incertitude et du brouillard de guerre (FOW)** : applique les modèles de détection selon le relief et construit les **États Perçus** distincts pour chaque camp (*CdC Section 6 [A]*).
- **Journalisation structurée** : émet le flux immuable des traces d'audit pour la reconstruction et le rejeu (*CdC Section 13, 14 [A]*).
- *Interdictions* : Totalement indépendant de l'IHM et du serveur d'exposition réseau ; testable de manière autonome en bibliothèque headless (*CdC Section 16, 24 [A]*).

#### 5. Module `api` [A / C]
Façade applicative d'exposition et de médiation :
- Point d'entrée des requêtes et commandes externes.
- Authentification et acheminement des ordres selon le rôle opérationnel (`Blue`, `Red`, `Umpire`) (*CdC Section 11 [A]*).
- **Filtrage étanche des flux d'information** : garantit qu'un camp ne reçoit que sa situation perçue, et réserve la vision omnisciente (état réel + perceptions) à l'Arbitre (*CdC Section 6, 11 [A]*).
- *Interdictions* : Aucun calcul physique ou tactique (ne calcule ni trajectoire, ni visibilité, ni combat).

### Graphe des dépendances autorisées (DAG)

Le graphe des dépendances est strictement orienté et sans cycle :

```text
       [ core ]
       ^      ^
      /        \
 [ terrain ]  [ units ]
      ^        ^
       \      /
        [ sim ]
           ^
           |
         [ api ]
```

- `terrain` → `core` : utilisation des identifiants et primitives communes.
- `units` → `core` : utilisation des identifiants et énumérations génériques.
- `sim` → `core` : utilisation des utilitaires communs, horodatage et types de base.
- `sim` → `terrain` : consultation du terrain comme donnée de référence en lecture seule.
- `sim` → `units` : manipulation des états dynamiques des unités et application des profils capacitaires.
- `api` → `sim` : transmission des ordres et interrogation des états perçus / état réel.
- `api` → `core` : manipulation des types et identifiants partagés.

### Dépendances interdites

- `core` ne dépend d'aucun autre module (socle terminal autonome).
- `terrain` ne dépend pas de `units`, `sim`, ni `api` (la géographie est neutre et indépendante des troupes et règles).
- `units` ne dépend pas de `terrain`, `sim`, ni `api` (les profils capacitaires sont indépendants de la carte géographique).
- `sim` ne dépend pas de `api` (inversion stricte des dépendances : le moteur ignore le protocole d'exposition externe).
- `sim` ne dépend pas de l'IHM (React), ni des serveurs web, ni des outils SIG amont (Global Mapper).
- `units` ne dépend d'aucune donnée ou nomenclature d'arme réelle.

### Propriété des données (Data Ownership)

- **Données géographiques et grille** : `terrain` est le propriétaire exclusif de la représentation du terrain chargée en mémoire. `sim` ne possède pas le terrain mais l'utilise comme donnée d'entrée et de référence de calcul.
- **État de simulation (`WorldState`)** : `sim` est le propriétaire exclusif de l'état dynamique de la session (bataillons déployés, positions effectives, horloge, événements, traces).
- **Profils structurels d'unités** : `units` détient les définitions de profils capacitaires abstraits ; leurs instances vivantes sont managées dans le `WorldState` de `sim`.
- **Perceptions et observations** : `sim` produit les états perçus ; `api` les reçoit et les distribue en respectant le cloisonnement de chaque camp.
- **Sessions et connexions** : `api` est propriétaire du contexte de session externe et de l'association rôle-utilisateur.

### Séparation État Réel / États Perçus et Rôles Blue / Red / Umpire

1. **État Réel (Ground Truth)** : situation objective absolue détenue exclusivement par `sim`. Accessible uniquement par le rôle Arbitre (Umpire) via `api`. Jamais exposée aux joueurs.
2. **États Perçus (Situations Perçues)** : situations subjectives calculées par `sim` pour Blue et Red selon les capteurs, le relief, les masques et les règles d'incertitude.
3. **Cloisonnement des rôles** :
   - `Blue` : dispose uniquement de la vue perçue amie et des contacts adverses détectés.
   - `Red` : dispose uniquement de sa propre vue perçue et de ses détections.
   - `Umpire` : rôle d'arbitrage disposant de la superposition de l'état réel et des deux états perçus, avec contrôle de l'horloge et injection d'événements.

### Classification des éléments `[A] / [B] / [C] / [D]`

- **[A] Exigences contractuelles du CdC** : découplage simulation/présentation (*Sec. 16*), échelon bataillon (*Sec. 5.3*), abstraction capacitaire totale (*Sec. 5.4, 31*), séparation Réel / Perçu (*Sec. 6, 11*), horloge logique et événements (*Sec. 8*), journalisation et rejeu (*Sec. 13, 14*), rôles Blue/Red/Umpire (*Sec. 11*), déterminisme fonctionnel (*Sec. 24*).
- **[B] Contraintes logiquement déduites** : testabilité du moteur indépendamment de l'IHM et de l'exposition (*déduit de Sec. 16, 24*), filtrage d'information au niveau de l'exposition (*déduit de Sec. 6, 11*), graphe de dépendances acyclique (*déduit de Sec. 16*).
- **[C] Choix d'ingénierie et d'architecture interne du projet** : découpage modulaire en cinq modules `core / terrain / units / sim / api`, Global Mapper comme outil SIG/ETL opérationnel du projet, framework Drogon pour les services C++, GoogleTest pour les tests unitaires automatisés, PRNG seedé pour garantir le déterminisme d'adjudication.
- **[D] Éléments encore ouverts / décisions futures** : choix définitif de la représentation géométrique concrète des coordonnées de grille (axiale, cubique, H3), format précis des conteneurs de transfert mémoire entre `sim` et `api`, échelle de normalisation numérique des valeurs relatives de capacités.
