# SPÉCIFICATIONS FONCTIONNELLES DU SYSTÈME

**Document de référence pour l'ÉTAPE 01 du projet PFE 2026–2027**  
**Titre du projet :** Développement d’un wargame géospatial pour l’entraînement à la prise de décision  
**Référence contractuelle :** `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0) & [`MASTER_PROMPT.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/MASTER_PROMPT.md)  
**Classification :** PFE Académique / Recherche appliquée — Abstraction totale des capacités militaires  

---

## 1. Introduction et Objet du Document

Le présent document formalise les spécifications fonctionnelles détaillées du wargame géospatial destiné à l'entraînement à la prise de décision tactique et opérationnelle.

Conformément au cahier des charges officiel Version 1.0, ce système logiciel a pour vocation :
1. D'intégrer un environnement géographique réaliste préparé via une chaîne SIG rigoureuse.
2. De discrétiser l'espace au moyen d'une grille hexagonale régulière supportant les calculs de franchissement, d'observation et de mouvement.
3. De simuler des confrontations tactiques au niveau d'agrégation minimal du **bataillon**, en maintenant une abstraction stricte des matériels et armements.
4. De séparer de manière hermétique l'**État Réel** (Ground Truth) de la simulation et les **États Perçus** respectifs des camps **Blue** et **Red**.
5. D'outiller l'**Arbitre (Umpire)** pour l'animation du scénario, le contrôle du temps et la conduite de débriefings objectifs grâce à la journalisation et au rejeu chronologique.
6. De respecter le principe architectural **« Autonomous First — CommandView Ready »** (Section 33 du CdC), assurant un fonctionnement 100% autonome pour le PFE tout en exposant des interfaces standardisées (REST, WebSocket, schémas relationnels ouverts).

---

## 2. Terrain, Modèle Géospatial et Grille Hexagonale (P01-T01-S01)

### 2.1 Modèle Numérique de Terrain (MNT / DEM) et Altimétrie
- **Rôle fonctionnel** : Fournir l'altitude continue et la matrice de déclivité nécessaires au calcul de la mobilité terrestre et des lignes de vue optiques.
- **Altitude** : Valeur altimétrique z (en mètres) rattachée à chaque cellule ou nœud du maillage géographique.
- **Pente (Déclivité)** : Dérivée spatiale locale calculée à partir des gradients d'altitude, intervenant directement comme coefficient multiplicateur du coût de déplacement des bataillons.
- **Exposition et crêtes** : Identification géométrique des lignes de crête et des zones d'ombre topographique pour le calcul de l'intervisibilité et du masquage des capteurs.
- **Traitement des NoData** : Application d'un traitement documenté et validé lors de la phase de préparation SIG, garantissant l'absence de valeurs aberrantes ou manquantes sur l'aire d'opération (AOI).

### 2.2 Couches Thématiques Vectorielles
- **Réseau routier et franchissements** : Classification normalisée des voiries (voies rapides, routes principales, chemins carrossables, ponts, passages à gué). Le réseau routier procure un bonus de vitesse de franchissement et canalise les axes logistiques.
- **Hydrographie** : Rivières, canaux, lacs et zones marécageuses. Définition des degrés d'infranchissabilité ou de ralentissement sévère pour les bataillons mécanisés et motorisés.
- **Occupation du sol et couvert végétal** : Forêts denses, bois clairs, cultures, zones ouvertes. Détermination des coefficients de dissimulation (camouflage) et de friction au déplacement.
- **Zones urbaines et bâti** : Agglomérations, villages, zones industrielles. Procurent une protection accrue aux unités en posture défensive tout en limitant les vitesses d'évolution et les portées d'observation directe.

### 2.3 Grille Hexagonale Régulière
- **Topologie** : Pavage régulier du plan en hexagones orientés (orientation pointe en haut ou côté plat en haut, homogène sur tout le système). L'hexagone est retenu pour l'équidistance parfaite entre les 6 cellules voisines, éliminant les biais diagonaux des grilles carrées.
- **Système de coordonnées** : Adopter un système formel de coordonnées hexagonales (coordonnées axiales `(q, r)` ou cubiques `(x, y, z)` avec $x + y + z = 0$) assurant des calculs de distance euclidienne en $O(1)$ et une indexation matricielle directe.
- **Agrégation géographique par cellule** : Chaque cellule hexagonale hérite des propriétés spatiales de son emprise :
  - Altitude moyenne et écart altimétrique.
  - Pente moyenne et maximale.
  - Type de surface dominant (route, terrain découvert, forêt, urbain, eau).
  - Indice de mobilité (coût de franchissement en points de mouvement).
  - Indice de masquage / couvert défensif (pourcentage de protection).
- **Indexation spatiale** : Intégration dans la base de données spatiale via géométrie polygonale PostGIS munie d'un index spatial GiST (`ST_Intersects`, `ST_Contains`).

### 2.4 Chaîne SIG et Global Mapper
- **Outil SIG unique du workflow courant** : Global Mapper est l'unique logiciel SIG de traitement, de contrôle et d'harmonisation des données géospatiales du projet.
- **Projection officielle** : Reprojection impérative de l'intégralité des couches dans un Système de Coordonnées de Référence métrique officiel (UTM / CRS projeté adapté à la zone d'intérêt), éliminant toute distorsion d'échelle angulaire WGS84.
- **Génération du livrable propre** : Exportation des couches d'élévation (GeoTIFF) et des vecteurs nettoyés (Shapefiles / GeoPackage) dans `data/processed/` avant chargement dans PostGIS.

---

## 3. Unités, Équipements Abstraits et Capteurs (P01-T01-S02)

### 3.1 Modèle des Unités Tactiques
- **Échelon minimal obligatoire : BATAILLON** :
  - Aucune entité individuelle (soldat, véhicule isolé, escouade, compagnie) n'est représentée.
  - L'unité de base manipulée par les joueurs et le moteur est le **bataillon** (force organisée de 300 à 800 personnels équivalents).
- **Attributs obligatoires de l'unité** :
  - `id` : Identifiant immuable unique (ex: `UNIT-BLUE-01`).
  - `nom` : Désignation tactique (ex: `1er Bataillon Mécanisé`).
  - `affiliation` : Camp d'appartenance (`BLUE`, `RED`, ou `NEUTRAL`).
  - `type` : Rôle opérationnel abstrait (`INFANTERIE_MOTORISEE`, `INFANTERIE_MECANISEE`, `BLINDE_CHEVRON`, `ARTILLERIE_APPUI`, `RECONNAISSANCE_ECLAIREURS`, `LOGISTIQUE_SOUTIEN`).
  - `cellule_courante` : Coordonnée hexagonale actuelle sur la grille.
  - `points_de_force` : Valeur numérique synthétique (ex: 100/100) représentant l'effectif et la valeur opérationnelle résiduelle.
  - `moral` : Indice d'endurance psychologique et de cohésion collective (0 à 100%).
  - `ravitaillement` : État des stocks logistiques (munitions, carburant, vivres).
  - `posture` : État opérationnel courant (`MOUVEMENT`, `ATTENTE`, `RETRANCHE_DEFENSIF`, `EN_COMBAT`, `DESORGANISE`, `NEUTRALISE`).
  - `vitesse_base` : Capacité de mouvement nominale par tour (en points de déplacement).

### 3.2 Abstraction Totale des Capacités et Équipements
- **Règle d'or de non-prolifération technique** : Conformément à la Section 4.3 et à la Règle 29 du Master Prompt, aucune caractéristique technique réelle d'arme (calibre millimétrique, désignation commerciale de missile, blindage en millimètres RHA, portée réelle classifiée) ne doit être introduite.
- **Paramètres capacitaires autorisés** :
  - `puissance_feu_relative` : Coefficient d'efficacité offensive à distance.
  - `portee_engagement_relative` : Distance maximale d'action exprimée en nombre de cellules hexagonales.
  - `protection_relative` : Coefficient de réduction des dommages subis selon le type d'attaque et le couvert du terrain.
  - `mobilite_relative` : Facteur de franchissement des terrains difficiles et du relief.
  - `autonomie_endurance` : Nombre de tours continus en manœuvre avant pénalité de ravitaillement.
  - `taux_disponibilite` : Pourcentage de fiabilité opérationnelle des moyens du bataillon.

### 3.3 Modèle des Capteurs, Lignes de Vue et Détections
- **Types de capteurs abstraits** :
  - `OBSERVATION_VISUELLE_DIRECTE` : Observation optique depuis les cellules occupées par le bataillon. Portée courte à moyenne, très dépendante de la pente, de la météo et de la végétation.
  - `RADAR_SURVEILLANCE_SOL` : Détection tout-temps des mouvements. Portée longue, mais bloqué par le relief et incapable d'identifier finement l'adversaire.
  - `OBSERVATION_AERIENNE_DRONE` : Capteur déporté offrant une vue plongeante réduisant considérablement le masquage topographique.
  - `RECONNAISSANCE_HUMAINE_PATROUILLE` : Détection discrète infiltrée à haute fidélité d'identification.
- **Lignes de vue (LOS - Line of Sight)** :
  - Algorithme de tracé de rayon altimétrique entre le centre de la cellule observatrice et le centre de la cellule cible.
  - Masquage par crête : si une cellule intermédiaire présente une altitude supérieure à la droite reliant observateur et cible, la ligne de vue est coupée.
  - Masquage par couvert végétal ou bâti : atténuation progressive de la détection.
- **Incertitude et détection bruitée** :
  - Toute détection ne produit pas une certitude absolue. L'observation génère une entité `Observation` caractérisée par :
    - `position_estimee` : Coordonnées de la cellule observée (pouvant comporter une dérive d'une ou deux cellules).
    - `precision_localisation` : Rayon d'incertitude géographique (en nombre de cellules).
    - `niveau_identification` : Degré de connaissance (`DETECTION_ANONYME` -> `TYPE_GENERIQUE` -> `BATAILLON_IDENTIFIE`).
    - `indice_confiance` : Pourcentage d'assurance évalué par le capteur (0 à 100%).
    - `horodatage` : Tour ou seconde simulée de l'observation.
    - `persistance` : Observation ponctuelle (s'estompe rapidement si non rafraîchie) vs observation entretenue par contact suivi.

---

## 4. Règles d'Arbitrage et Séparation Réel vs Perçu (P01-T01-S03)

### 4.1 Étanchéité Absolue : Ground Truth (Réel) vs Perceived State (Perçu)
- **Le monde réel (Ground Truth)** :
  - Contient l'état physique exact de toutes les cellules, unités, positions, mouvements, niveaux logistiques et événements du scénario.
  - Calculé et stocké exclusivement par le moteur de simulation au sein de la base de données.
  - **Inviolabilité** : Aucun client joueur (Blue ou Red) ne doit pouvoir interroger ou recevoir directement la table de l'état réel.
- **L'état perçu Blue (Blue COP)** :
  - Vue opérationnelle construite dynamiquement pour le camp Blue.
  - Contient :
    - La connaissance exacte et exhaustive de l'ensemble des forces Blue.
    - Les données géographiques du terrain (carte, relief, voirie).
    - Les observations courantes et historiques portant sur les forces adverses Red, après application du filtre des capteurs et de l'incertitude.
    - Les zones d'ombre (brouillard de guerre / Fog of War) masquant totalement les zones non couvertes par un capteur amical actif.
- **L'état perçu Red (Red COP)** :
  - Vue opérationnelle symétrique construite dynamiquement pour le camp Red, strictement imperméable aux informations Blue.

### 4.2 Rôle et Prérogatives de l'Arbitre (Umpire)
- **Omniscience** : L'Arbitre a accès en temps réel à l'État Réel complet, ainsi qu'à la superposition des États Perçus Blue et Red (permettant d'évaluer immédiatement les asymétries d'information).
- **Gestionnaire du temps** : L'Arbitre contrôle le flux temporel de l'exercice :
  - Démarrage, mise en pause, reprise.
  - Défilement tour par tour ou écoulement continu accéléré.
  - Clôture de phase d'ordres et validation de la résolution de tour.
- **Injection d'événements et aléas** :
  - Injection manuelle ou programmée d'incidents opérationnels : coupure de communications, brouillage radar, météo dégradée (brouillard réduisant la portée des capteurs visuels), destructions d'ouvrages d'art (pont détruit bloquant une route).
- **Arbitrage des situations limites** :
  - Possibilité pour l'arbitre de forcer un résultat de combat, de réassigner une unité ou de modifier une règle en direct si l'objectif pédagogique l'exige.
- **Conduite du débriefing** :
  - Accès aux tableaux de bord analytiques, aux chronologies de prise de décision et aux journaux d'événements.

---

## 5. Spécification des Rôles et Interfaces Utilisateurs (P01-T01-S04)

### 5.1 Rôle BLUE — Commandant de Force Amie
- **Responsabilités** :
  - Analyser la situation tactique sur sa COP (Common Operational Picture).
  - Évaluer le terrain, les axes praticables et les zones clés.
  - Définir les ordres de déplacement pour ses bataillons (chemins planifiés).
  - Assigner les postures d'engagement et les zones de surveillance des capteurs.
  - Émettre des décisions formelles validées dans le temps imparti.
- **IHM dédiée (Interface Blue)** :
  - Carte interactive OpenLayers/Leaflet affichant le fond de carte SIG, le MNT ombré et la grille hexagonale.
  - Symboles normalisés des bataillons Blue (affichant posture, état de santé, rayon d'action).
  - Traces des observations sur l'ennemi (fantômes bruités, cercles d'incertitude, niveau d'identification).
  - Panneau contextuel de sélection d'unité avec actions : Déplacer, Changer de posture, Activer capteur.
  - Panneau de saisie et de validation des décisions tactiques.
  - Horloge de la session et alertes opérationnelles (contacts détectés, tirs subis).

### 5.2 Rôle RED — Commandant de Force Opposée
- **Responsabilités** :
  - Conduire le camp Red selon la doctrine définie par le scénario ou par un joueur humain indépendant.
  - Manœuvrer ses bataillons sous le couvert du relief et de la végétation pour surprendre le dispositif Blue.
- **IHM dédiée (Interface Red)** :
  - Strictement similaire dans ses capacités fonctionnelles à l'interface Blue, mais isolée sur le plan des flux de données WebSocket et des contrôleurs API Drogon.
  - Affichage exclusif des forces Red et des contacts bruités sur les forces Blue.

### 5.3 Rôle UMPIRE — Arbitre et Directeur d'Exercice
- **Responsabilités** :
  - Initialiser la session de wargame et charger le scénario retenu.
  - Paramétrer la durée maximale en tours et les conditions de victoire.
  - Superviser les actions simultanées ou alternées de Blue et Red.
  - Contrôler le respect des règles et injecter des événements perturbateurs.
  - Piloter la phase d'After Action Review (AAR) et d'analyse des décisions.
- **IHM dédiée (Interface Umpire)** :
  - **Master COP** : Affichage simultané des trois calques (État Réel en surbrillance, calque de perception Blue, calque de perception Red).
  - **Pupitre de contrôle du moteur** : Boutons Start, Pause, Step Next Turn, Fast Forward.
  - **Console d'événements** : Générateur d'événements impromptus (météo, coupures, renforts).
  - **Tableau de bord de débriefing** : Graphiques d'évolution des potentiels, chronologie des ordres, matrice de charge décisionnelle et écarts réel/perçu.

---

## 6. Processus Décisionnel et Charge Décisionnelle Abstraite

### 6.1 Modélisation de la Décision Humaine
- Le système s'appuie sur une formalisation objective et observable du cycle de décision (Boucle OODA : Observer, Orienter, Décider, Agir) sans prétendre modéliser la psychologie interne du joueur :
  - **Phase 1 : Observation** : Réception des contacts et rafraîchissement de la COP à l'instant $t$.
  - **Phase 2 : Orientation** : Consultation des propriétés du terrain, de l'état des unités et des rapports de forces estimés.
  - **Phase 3 : Décision** : Choix explicite formulé par le joueur parmi plusieurs options tactiques (ex: Attaque frontale, Contournement flanc droit, Repli défensif sur ligne d'arrêt).
  - **Phase 4 : Action** : Enregistrement de la décision, émission des ordres de mouvement et transmission au moteur de simulation.
- **Structure d'un enregistrement de décision** :
  - Identifiant unique `decision_id`.
  - Camp émetteur (`BLUE` / `RED`).
  - Tour et horodatage de formulation (`timestamp_creation`).
  - Horodatage de validation par le joueur (`timestamp_validation`).
  - Temps de réflexion calculé ($\Delta t = \text{validation} - \text{création}$).
  - Situation perçue au moment du choix (instantané des unités visibles).
  - Option retenue et ordres associés.

### 6.2 Indicateur de Charge Décisionnelle Abstraite
- Afin de fournir un support pédagogique lors du débriefing, le système calcule un indice synthétique de **charge décisionnelle** normalisé entre 0 et 100 :
  $$\text{Charge Décisionnelle} = f(\text{Événements concurrents}, \text{Incertitude}, \text{Alternatives}, \text{Pression temporelle})$$
- **Composantes de la formule** :
  1. *Densité événementielle* : Nombre d'alertes, de nouveaux contacts et d'incidents survenus lors du tour courant.
  2. *Indice d'incertitude* : Ratio entre les unités ennemies détectées sous forme bruitée/imprécise et le nombre total de cellules actives.
  3. *Complexité du choix* : Nombre d'unités amies nécessitant un ordre simultané.
  4. *Contrainte temporelle* : Rapprochement de l'échéance de fin de tour impartie par l'arbitre.
- Cette formule est entièrement documentée, transparente, paramétrable dans le scénario et testable unitairement.

---

## 7. Traçabilité, Rejeu et Débriefing Après Action (AAR)

### 7.1 Journalisation Continue (Logging Événementiel)
- Chaque interaction, transition d'état, mouvement, tir abstrait, émission d'ordre et événement injecté est consigné dans une table de journalisation immuable (`simulation_logs`).
- Chaque entrée contient :
  - Numéro de tour et temps simulé.
  - Horodatage réel d'enregistrement.
  - Type d'événement (`MOUVEMENT`, `OBSERVATION`, `COMBAT`, `DECISION`, `ARBITRAGE`, `SYSTEME`).
  - Payload structuré en JSON détaillant l'état avant / état après.

### 7.2 Moteur de Rejeu Chronologique (Replay Engine)
- Capacité de rejouer intégralement une session enregistrée de bout en bout de façon déterministe.
- Modes de lecture : Play (1x, 2x, 4x), Pause, Step-by-Step (tour par tour), Saut direct à un tour spécifique grâce à des instantanés d'état périodiques (keyframes).
- Bascule de point de vue pendant le rejeu : l'instructeur peut visionner le déroulement selon la perspective Réelle, la perspective Blue ou la perspective Red.

### 7.3 Module de Débriefing et Métriques
- Comparaison automatique entre l'état réel et l'état perçu au moment exact d'une décision clé (mise en évidence des biais d'appréciation dus au brouillard de guerre).
- Courbes d'évolution temporelle :
  - Évolution des points de force Blue vs Red.
  - Évolution de la charge décisionnelle au fil des tours.
  - Taux d'occupation des objectifs du scénario.
- Production d'un rapport de synthèse exportable en fin d'exercice.

---

## 8. Conclusion et Conformité

Le présent document constitue la référence fonctionnelle exhaustive pour la conception de l'architecture technique (ÉTAPE 02) et du modèle relationnel (ÉTAPE 03). Il respecte à 100% les exigences du Cahier des charges Version 1.0, garantit l'abstraction capacitaire absolue au niveau bataillon, et sanctuarise le rôle unique de Global Mapper dans le workflow SIG.
