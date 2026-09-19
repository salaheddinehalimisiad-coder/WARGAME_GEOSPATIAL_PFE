# SPÉCIFICATIONS FONCTIONNELLES DU SYSTÈME

**Document de référence issu de l'audit critique de l'ÉTAPE 01 — PFE 2026–2027**  
**Titre du projet :** Développement d’un wargame géospatial pour l’entraînement à la prise de décision  
**Source contractuelle unique :** `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0)  
**Classification des exigences appliquée dans ce document :**
- **[A] DIRECTEMENT PRÉSENTE DANS LE NOUVEAU CAHIER** : Exigence textuelle explicite du CdC v1.0.
- **[B] DÉDUITE DE FAÇON RAISONNABLE MAIS NON EXPLICITE** : Déduction logique directe nécessaire à la mise en œuvre, sans extrapolation technique arbitraire.
- **[C] PROPOSITION D’ARCHITECTURE À VALIDER** : Choix de conception ou d'implémentation proposé par l'équipe d'ingénierie, soumis à validation client.
- **[D] ÉLÉMENT PURGÉ / ANCIEN CADRAGE** : Mention des concepts de l'ancien cadrage formellement identifiés et supprimés du périmètre.

---

## 1. Introduction et Périmètre du Projet

### 1.1 Objet et Finalité [A]
Le système logiciel est un démonstrateur de wargame géospatial centré sur la prise de décision tactique et opérationnelle dans un environnement simulé, dynamique et incertain (*CdC Sections 1, 4.1, 34*). Il combine :
- Un système d'information géographique (SIG) et une modélisation fine du terrain.
- Une discrétisation de l'espace par grille hexagonale.
- Un modèle abstrait d'unités et d'équipements au niveau minimum du **bataillon**.
- La gestion des capteurs, de l'incertitude et la séparation étanche entre **état réel** et **état perçu**.
- Un moteur de simulation pilotant le temps, les événements et les interactions.
- Une traçabilité intégrale, un rejeu chronologique et un module de débriefing pédagogique avec indicateurs synthétiques.
- Une compatibilité avec le principe architectural **« Autonomous First — CommandView Ready »** (*CdC Section 16, 33*).

### 1.2 Limites et Non-Objectifs [A]
- Le wargame est un outil pédagogique et expérimental (*CdC Section 31*).
- Les capacités des équipements sont abstraites : le projet ne vise pas à reproduire les caractéristiques techniques détaillées d'armes réelles (*CdC Section 5.4, 31*).
- Les modèles de décision décrivent le processus observable sans prétendre représenter la psychologie ou la clinique réelle du décideur (*CdC Section 9, 31*).
- Le projet ne constitue ni une doctrine opérationnelle ni une prédiction d'une situation réelle (*CdC Section 31*).

---

## 2. Terrain, Modélisation Géospatiale et Grille Hexagonale

### 2.1 Système d'Information Géographique (SIG) [A]
- **Affichage cartographique interactif** : Zoom, déplacement, sélection, interrogation de couches raster et vectorielles (*CdC Section 5.1*).
- **Gestion des coordonnées et projections** : Prise en compte rigoureuse des projections géodésiques et des coordonnées géoréférencées (*CdC Section 5.1*).
- **Superposition de couches thématiques** : Relief, réseaux, végétation, hydrographie, infrastructures (*CdC Section 5.1, 19*).

### 2.2 Modélisation du Terrain [A]
- **Modèle Numérique de Terrain (MNT / DEM)** : Importation et exploitation de l'altitude continue et de la pente dérivée (*CdC Section 5.2, 19*).
- **Couches d'environnement** : Prise en compte de l'hydrographie, du réseau routier et pistes, de la végétation / occupation du sol, des zones urbaines et des infrastructures pertinentes (*CdC Section 5.2, 19*).
- **Propriétés calculées** : Calcul de propriétés spatiales utiles au mouvement et à l'observation (*CdC Section 5.2*).
- **Données géographiques** : Utilisation de données publiques, représentatives ou synthétiques, sans dépendance à des données classifiées (*CdC Section 19, 20*).

### 2.3 Découpage en Cellules Hexagonales
- **Pavage hexagonal** [A] : Découpage de l'espace géographique en cellules hexagonales régulières (*CdC Section 5.2, 12, 18, 21*).
- **Système de coordonnées axiales/cubiques** [C] : Proposition technique d'adopter des coordonnées axiales `(q, r)` pour l'adressage et le calcul de distance en $O(1)$, compatible avec les géométries PostGIS et H3.
- **Agrégation des attributs par cellule** [B] : Chaque hexagone hérite des caractéristiques du terrain sous-jacent (altitude, pente, type de sol, indice de franchissement, masquage).

### 2.4 Chaîne SIG et Choix des Outils
- **Technologies recommandées par le CdC** [A] : Le CdC mentionne à titre indicatif « QGIS/GDAL/PROJ pour les traitements SIG » sous réserve de confirmation d'analyse (*CdC Section 17*).
- **Choix d'architecture du projet : Global Mapper** [C] : Conformément aux décisions validées du projet, Global Mapper a été retenu comme l'outil SIG/ETL privilégié pour le prétraitement, le reconditionnement MNT et l'export des couches vers la base spatiale. Ce choix relève d'une décision d'ingénierie interne et non d'une obligation textuelle du cahier des charges.

---

## 3. Modèle des Unités et des Équipements Abstraits

### 3.1 Échelon Minimal et Attributs des Unités [A]
- **Échelon tactique** : L'unité opérationnelle minimale est le **bataillon** (*CdC Section 5.3, Master Prompt*). Aucune entité subordonnée (compagnie, section, soldat individuel) n'est représentée comme pion indépendant sur la carte.
- **Attributs obligatoires de l'unité** (*CdC Section 5.3, 18*) :
  - `id` : Identifiant unique.
  - `camp` : Affiliation (Blue / Red).
  - `type` : Rôle ou spécialité générique (ex: infanterie, blindé, appui, reconnaissance, logistique).
  - `niveau_organisation` : Échelon (bataillon).
  - `position` : Cellule hexagonale courante et zone d'action.
  - `effectif_ou_disponibilite` : Effectif ou disponibilité abstraite.
  - `capacites_operationnelles` : Capacités synthétiques agrégées.
  - `capteurs_disponibles` : Liste des capteurs associés à l'unité.
  - `niveau_information` : Connaissance disponible au camp.
  - `etat_courant` : Posture opérationnelle ou disponibilité.
  - `regles_contraintes` : Règles d'engagement ou contraintes de déplacement applicables.

### 3.2 Abstraction Stricte des Équipements [A]
- **Principe d'abstraction totale** : Les équipements sont représentés par des paramètres abstraits sans référence à des armes réelles (*CdC Section 5.4, 31*) :
  - `capacite` : Puissance ou potentiel d'action relatif.
  - `portee_relative` : Distance d'engagement exprimée en unités relatives / hexagones.
  - `mobilite` : Facteur de franchissement et vitesse relative.
  - `protection` : Résistance aux effets adverses et interaction avec le couvert.
  - `observation` : Capacités optiques/électroniques d'acquisition.
  - `disponibilite_endurance` : Disponibilité opérationnelle et autonomie relative.
- *Éléments purgés [D]* : Suppression de tout calibre réel, modèle commercial d'armement, blindage RHA, ainsi que des attributs psychologiques subjectifs ("moral 0-100%") non prescrits par le CdC.

---

## 4. Capteurs, Observations, Incertitude et Séparation Réel / Perçu

### 4.1 Séparation Hermétique : État Réel vs État Perçu [A]
- **État réel (Ground Truth)** : Situation objective globale du théâtre (positions exactes de toutes les unités amies et ennemies, états réels, terrain complet), connue exclusivement du moteur de simulation et accessible à l'Arbitre (*CdC Section 6, 11, 12, 27*).
- **État perçu (Situation Perçue / COP)** : Situation subjective construite pour chaque camp (Blue et Red) à partir de ses propres unités et des observations remontées par ses capteurs (*CdC Section 6, 11, 12*).
- **Brouillard de guerre et visibilité** : Un joueur ne voit de l'adversaire que ce que ses capteurs lui permettent d'observer conformément aux règles d'incertitude du scénario (*CdC Section 6, 24*).

### 4.2 Capteurs et Modèle d'Observation [A]
- **Types de capteurs** : Capteurs coopératifs (remontée amie) et non coopératifs (surveillance adverse), représentés de façon abstraite (*CdC Section 6*).
- **Portée et conditions** : Portée et conditions d'observation paramétrables selon le terrain, l'altitude, la pente et les masques (*CdC Section 5.2, 6*).
- **Observations ponctuelles ou persistantes** : Une observation peut être fugace ou entretenue dans le temps (*CdC Section 6*).
- **Structure d'une Observation** (*CdC Section 6, 18*) :
  - `id` : Identifiant de l'observation.
  - `source` : Capteur ou unité ayant produit l'observation.
  - `position_estimee` : Localisation approximée sur la grille hexagonale.
  - `precision` : Marge d'incertitude spatiale.
  - `confiance` : Niveau de confiance qualitatif ou quantitatif (paramétrable).
  - `horodatage` : Instant d'acquisition dans le temps simulé.
- **Mise à jour progressive** : L'état perçu est mis à jour progressivement selon les flux d'observations successifs (*CdC Section 6*).
- *Éléments purgés [D]* : Suppression des classes rigides imposées « Inconnu / Catégorie / Identifié », des probabilités de détection hardcodées (ex: 85%, 60%) et des formules de décroissance exponentielle arbitraires.

---

## 5. Moteur de Simulation, Gestion du Temps et des Événements

### 5.1 Moteur de Simulation [A]
- **Rôle central** : Assurer l'évolution de l'état du monde à partir des actions des joueurs, des règles du scénario, du terrain et des événements (*CdC Section 7*).
- **Responsabilités élémentaires** (*CdC Section 7*) :
  - Gestion de l'état courant de la simulation.
  - Exécution des actions des joueurs selon les règles.
  - Calcul des déplacements sur la grille hexagonale en tenant compte des coûts de terrain.
  - Calcul des interactions entre unités selon un modèle abstrait.
  - Gestion et diffusion des observations incertaines.
  - Déclenchement des événements programmés ou conditionnels.
  - Production continue des traces et journaux d'exécution.
  - Rejeu reproductible à partir d'un état initial.

### 5.2 Gestion du Temps et des Événements [A]
- **Horloge de simulation** : Horloge logique configurable et indépendante du temps système physique (*CdC Section 8*).
- **Modes temporels** : Mode pas-à-pas et mode avec accélération du temps (*CdC Section 8*).
- **Événements** : Événements planifiés (liés à une échéance temporelle) ou conditionnels (déclenchés par un franchissement de seuil ou une règle) (*CdC Section 8, 18*).
- **Contraintes temporelles** : Délais de décision configurables et échéances de validation pour les joueurs (*CdC Section 8*).
- **Historisation** : Enregistrement chronologique de tous les événements survenus (*CdC Section 8*).

### 5.3 Reproductibilité et Déterminisme
- **Exigence du CdC** [A] : « Transitions cohérentes et reproductibles avec paramètres identiques » (*CdC Section 24*) et « Rejeu reproductible à partir d'un état initial » (*CdC Section 7*).
- **Proposition technique d'implémentation** [C] : Utilisation d'un générateur pseudo-aléatoire 64 bits C++20 (`std::mt19937_64`) contrôlé par une graine (`seed`) déclarée dans le scénario pour assurer la répétabilité stricte au bit près des calculs stochastiques d'adjudication.
- *Éléments purgés [D]* : Suppression de la notion de séquence rigide imposée en 4 phases fermées (Planification/Détection/Résolution/Adjudication) comme exigence contractuelle. Le moteur supporte une horloge configurable pas-à-pas ou continue.

---

## 6. Modèle de Décision et Charge Décisionnelle Abstraite

### 6.1 Modélisation du Processus Décisionnel [A]
- **Description observable** : Le modèle décrit le processus de décision observable sans prétendre représenter la psychologie réelle du décideur (*CdC Section 9, 31*).
- **Structure d'une décision** (*CdC Section 9, 18*) :
  - `id` : Identifiant unique de la décision.
  - `acteur` : Camp ou joueur émetteur (Blue / Red).
  - `situation_percue` : État de la connaissance disponible au moment de la décision.
  - `informations_disponibles` : Éléments cartographiques et rapports de capteurs consultés.
  - `options_envisagees` : Ensemble des alternatives considérées.
  - `option_selectionnee` : Action ou plan d'action retenu.
  - `heure_debut` : Moment d'ouverture de la phase de réflexion.
  - `heure_validation` : Moment de soumission ou validation de l'ordre.
  - `resultat_observe` : Conséquence de l'action après exécution par le moteur.

### 6.2 Charge Décisionnelle Abstraite [A]
- **Définition** : Métrique expérimentale synthétique d'aide à l'évaluation pédagogique (*CdC Section 9.1*).
- **Facteurs constitutifs** : Combine selon une formule documentée, transparente et paramétrable :
  - Le nombre d'événements simultanés à traiter.
  - Le volume d'informations reçues.
  - Le niveau d'incertitude ambiant.
  - Le nombre d'options tactiques ouvertes.
  - La contrainte temporelle (urgence de l'échéance).
- **Avertissement méthodologique explicite** [A] : Il s'agit d'un indicateur de simulation et en aucun cas d'une mesure clinique, physiologique ou psychologique (*CdC Section 9.1, 31*).

---

## 7. Rapport des Potentiels et Indicateurs Synthétiques

### 7.1 Indicateurs de Situation [A]
Le système calcule et met à disposition des joueurs et de l'arbitre des indicateurs transparents et paramétrables (*CdC Section 10*) :
- Potentiel agrégé d'une force.
- Disponibilité relative des moyens.
- Capacité d'observation globale du dispositif.
- Mobilité relative globale.
- État synthétique des unités.
- Rapport de forces synthétique calculé selon les règles du scénario.
- Évolution temporelle de ces indicateurs au cours de l'exercice.

---

## 8. Rôles et Interfaces Utilisateurs

### 8.1 Définition des Rôles [A]
Conformément à la Section 11 du CdC, le système distingue trois rôles opérationnels :
- **Blue** : Conduire son dispositif, observer, analyser la situation, décider et exécuter des actions (*CdC Section 11*).
- **Red** : Conduire le camp opposé selon les règles et objectifs du scénario (*CdC Section 11*).
- **Arbitre / Umpire** : Conserver la situation réelle, paramétrer le scénario, contrôler la simulation, déclencher des événements et conduire le débriefing (*CdC Section 11*).

### 8.2 Interfaces Cartographiques et COP [A]
- **Carte interactive** : Rendu cartographique vectoriel et raster sur fond hexagonal (*CdC Section 12*).
- **Symbolisation adaptée** : Représentation des unités amies, de leurs états et des observations acquises (*CdC Section 12*).
- **Outils d'interaction** : Sélection d'unité, interrogation des propriétés du terrain, émission d'ordres, alertes et panneaux contextuels (*CdC Section 12*).
- **Chronologie et horloge** : Affichage du temps de simulation et des échéances (*CdC Section 12*).
- **Vue Arbitre** : Accès sans restriction à l'état réel et comparaison avec les vues perçues Blue et Red (*CdC Section 12*).

---

## 9. Journalisation, Rejeu et Débriefing

### 9.1 Journalisation Structurée des Traces [A]
- Enregistrement de toutes les actions significatives dans un journal structuré pour garantir la reconstruction intégrale de la session (*CdC Section 13*).
- **Typologie des traces** (*CdC Section 13, 18*) :
  - Actions joueurs (ordres, déplacements, validations de décisions).
  - Observations (détections, localisations estimées, indices de confiance).
  - Événements (déclenchements temporels, conditions satisfaites, événements externes).
  - Décisions (options, choix retenu, délais, résultats).
  - Système (connexion, configuration, erreurs).
  - Simulation (transitions d'état et résultats calculés).

### 9.2 Rejeu Reproductible [A]
- Reconstruction fidèle d'une session passée à partir du journal des traces et de l'état initial (*CdC Section 14*).
- Fonctionnalités de lecture : Avance accélérée, ralenti, pause, navigation temporelle par pas ou saut d'étape (*CdC Section 14*).
- Comparaison dynamique situation réelle vs situation perçue pour analyser les biais (*CdC Section 14*).

### 9.3 Débriefing Pédagogique (After Action Review) [A]
- Chronologie des décisions majeures prises au cours de la partie (*CdC Section 14*).
- Restitution des informations exactes dont disposait le joueur à l'instant précis de sa décision (*CdC Section 14*).
- Analyse des écarts par rapport aux objectifs pédagogiques fixés dans le scénario (*CdC Section 14*).
- Export d'un rapport de session formalisé (*CdC Section 14*).

---

## 10. Conception des Scénarios

### 10.1 Paramètres du Scénario [A]
Conformément à la Section 15 du CdC, un scénario configurable comprend :
- Zone géographique et emprise spatiale (AOI).
- Situation initiale du terrain et du contexte.
- Dispositifs initiaux des forces Blue et Red.
- Objectifs pédagogiques de la séance.
- Informations initiales accessibles à chaque camp.
- Événements temporels préprogrammés.
- Règles de simulation applicables.
- Contraintes de temps pour la prise de décision.
- Critères de fin de session.
- Indicateurs retenus pour le débriefing.
- *Éléments purgés [D]* : Suppression du concept de "VPC" (Victory Points Conditions) issu d'anciens jeux de plateau commerciaux. Seules les notions d'objectifs pédagogiques et de critères de fin du CdC sont retenues.

---

## 11. Architecture Logicielle et Choix Techniques

### 11.1 Principe « Autonomous First — CommandView Ready » [A]
- Le prototype fonctionne de manière totalement autonome pour le cadre académique du PFE tout en préparant des interfaces standardisées compatibles avec une future intégration C4ISR (API REST/OpenAPI, WebSocket, flux géospatiaux standardisés, journalisation structurée) (*CdC Section 16, 33*).

### 11.2 Composants Cibles et Technologies [A / C]
- **Présentation** [A] : IHM web, carte interactive (React, TypeScript, OpenLayers ou Leaflet recommandés).
- **Services applicatifs & Moteur** [A] : Services REST/WebSocket et moteur de simulation en C++20 (Drogon recommandé par le CdC).
- **Données géospatiales** [A] : Base relationnelle spatiale PostgreSQL / PostGIS.
- **Préparation SIG** [C] : Global Mapper pour la chaîne ETL du projet (en lieu et place de l'indication QGIS du CdC, conformément aux choix validés).
- **Journalisation & Tests** [A] : Journalisation structurée (spdlog recommandé) et tests unitaires / intégration (GoogleTest).
- **Déploiement & CI/CD** [A] : Conteneurisation Docker / Docker Compose et pipelines d'intégration continue (GitHub Actions / GitLab CI).

---

## 12. Synthèse de l'Audit Critique des Exigences

| Domaine Fonctionnel | Éléments Conformes CdC v1.0 [A] | Déductions Logiques [B] | Propositions d'Architecture [C] | Éléments Purgés de l'Ancien Cadrage [D] |
|:---|:---|:---|:---|:---|
| **Terrain & SIG** | MNT, pente, hydro, voirie, bâti, grille hexagone (*Sec. 5, 19*) | Agrégation spatiale des propriétés par cellule | Utilisation de Global Mapper comme outil ETL projet | Formules d'atténuation de ligne de vue ad-hoc non vérifiées |
| **Unités & Matériels** | Bataillon minimum, attributs Section 5.3, abstraction totale (*Sec. 5.4*) | Rôles tactiques génériques (infanterie, blindé, appui) | Structure C++ de données `Unit` alignée sur Section 18 | Données réelles d'armes, calibres, blindage RHA, attribut subjectif moral (0-100%) |
| **Capteurs & FOW** | Séparation Réel / Perçu, observations bruitées (*Sec. 6*) | Filtrage spatial des observations par portée | Modèle d'indexation géométrique des portées | Classes rigides Inconnu/Catégorie/Identifié, probabilités hardcodées (85%, 60%) |
| **Simulation & Temps** | Moteur de simulation, horloge configurable, pas-à-pas (*Sec. 7, 8*) | File d'attente d'événements ordonnée chronologiquement | Déterminisme via `std::mt19937_64` et seed de scénario | Découpage obligatoire en 4 phases de tour fermées, tables de combat arbitraires |
| **Décision & Charge** | Processus observable, charge décisionnelle abstraite (*Sec. 9, 9.1*) | Horodatage automatique création / validation d'ordres | Formule transparente documentée dans le scénario | Mesures psychologiques / cliniques, seuils d'effort arbitraires |
| **Rôles & Interfaces** | Rôles Blue / Red / Umpire, COP dédiée, vue réelle arbitre (*Sec. 11, 12*) | Contrôleurs API filtrant les réponses par jeton de rôle | Rendu OpenLayers/Leaflet avec hexagones vectoriels | Rôles supplémentaires non prévus par le cahier |
| **Traces & Rejeu** | Journal structuré, rejeu reproductible, AAR (*Sec. 13, 14*) | Stockage SQL structuré des événements avec payload JSON | Lecteur pas-à-pas avec mode défilement temporel | Terme "VPC", critères de victoire de plateau commercial |
| **Recette & NFR** | 9 critères d'acceptation textuels (*Sec. 24*) | Protocoles de tests automatisés couvrant les 9 critères | Profils de test étalons sans seuils arbitraires | Nomenclature inventée REC-01 à REC-15 présentée comme contractuelle |
