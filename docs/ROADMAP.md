# ROADMAP OFFICIELLE DU PROJET

Référence : Section 15 du `MASTER_PROMPT.md` (Version 1.0 — PFE 2026–2027).

---

## ÉTAPE 00 — Initialisation du projet
- Création du dépôt
- Structure des dossiers
- Documentation initiale
- Règles de travail
- Environnement
- Git
- CI/CD de base

## ÉTAPE 01 — Analyse détaillée du cahier des charges
- Exigences
- Objectifs
- Acteurs
- Fonctionnalités
- Contraintes
- Critères d’acceptation
- Livrables

## ÉTAPE 02 — Architecture fonctionnelle et technique
- Architecture globale
- Responsabilités
- Flux
- Dépendances
- Interfaces entre composants

## ÉTAPE 03 — Modèle de données
- Modèle conceptuel
- Modèle logique
- Entités
- Relations
- Données géospatiales
- Données de simulation

## ÉTAPE 04 — Préparation de l’environnement
- C++20
- Drogon
- PostgreSQL
- PostGIS
- React
- TypeScript
- GoogleTest
- Docker
- GitHub Actions

## ÉTAPE 05 — Collecte des données SIG
Traitement exclusivement avec Global Mapper.
Collecter selon le périmètre :
- MNT/DEM
- Routes/pistes
- Hydrographie
- Zones urbaines
- Occupation du sol / végétation
- Infrastructures
- Limites
- Emprises

## ÉTAPE 06 — Préparation et nettoyage SIG
Global Mapper exclusivement.
- Nettoyage
- Correction
- Harmonisation
- Reprojection
- Mosaïquage
- Découpage
- Préparation des attributs
- Export

## ÉTAPE 07 — Contrôle qualité SIG
Vérifier :
- CRS
- Emprise
- Géométrie
- Attributs
- Unités
- Cohérence spatiale
- Cohérence thématique
- Métadonnées
- Validité des sorties
Aucune donnée ne passe à l’étape suivante sans validation.

## ÉTAPE 08 — Modèle du terrain
Construire progressivement les modèles nécessaires :
- Altitude
- Pente
- Hydrographie
- Occupation du sol
- Zones urbaines
- Infrastructures
- Propriétés utiles au mouvement et à l’observation

## ÉTAPE 09 — Conception de la grille hexagonale
- Étude H3 / équivalent
- Comparaison
- Choix
- Identifiants
- Voisinage
- Relation terrain/cellule

## ÉTAPE 10 — Validation de la grille
- Géométrie
- Couverture
- Voisinage
- Cohérence
- Tests

## ÉTAPE 11 — Intégration PostgreSQL / PostGIS
- Schéma
- Contraintes
- Index
- Terrain
- Grille
- Vérification

## ÉTAPE 12 — Modèle des unités
- Unit
- Side
- Positions
- États
- Capacités abstraites

## ÉTAPE 13 — Modèle des équipements
- Equipment
- Capacité
- Disponibilité
- Mobilité relative
- Protection
- Observation
- Endurance
- Portée relative

## ÉTAPE 14 — Modèle des capteurs
- Sensor
- Portée
- Précision
- Disponibilité
- Conditions d’observation

## ÉTAPE 15 — Moteur de simulation
- État initial
- État courant
- Transitions
- Règles
- Reproductibilité

## ÉTAPE 16 — Déplacements
- Déplacement sur grille
- Contraintes terrain
- Règles
- Tests

## ÉTAPE 17 — Observations et incertitude
- Observations
- Positions estimées
- Précision
- Confiance
- Horodatage
- Source

## ÉTAPE 18 — État réel / état perçu
- Séparation des informations
- Visibilité Blue
- Visibilité Red
- Accès Umpire
- Règles de diffusion

## ÉTAPE 19 — Temps et événements
- Horloge
- Mode pas-à-pas
- Accélération
- Événements
- Délais
- Échéances

## ÉTAPE 20 — Modèle de décision
- Situation perçue
- Informations
- Options
- Choix
- Validation
- Résultat

## ÉTAPE 21 — Services Drogon
- REST
- OpenAPI
- WebSocket
- Scénarios
- Sessions
- Commandes

## ÉTAPE 22 — Interface Blue
- Carte interactive & COP Blue
- Symbolisation des unités
- Commandes et décisions
- Visualisation perçue

## ÉTAPE 23 — Interface Red
- Carte interactive & COP Red
- Symbolisation des unités
- Commandes et décisions
- Visualisation perçue

## ÉTAPE 24 — Interface Umpire
- Vue globale Arbitre (état réel)
- Contrôle de la simulation
- Injection d'événements
- Supervision

## ÉTAPE 25 — Journalisation
- Traces structurées (joueur, observation, événement, décision, système, simulation)
- Persistance et reproductibilité

## ÉTAPE 26 — Rejeu
- Lecture, pause, vitesse variable
- Navigation temporelle
- Visualisation des décisions
- Comparaison réel / perçu

## ÉTAPE 27 — Débriefing et indicateurs
- Chronologie
- Évolution des indicateurs et charge décisionnelle
- Analyse des écarts réel vs perçu
- Rapport de session

## ÉTAPE 28 — Scénario de démonstration complet
- Déroulement complet de bout en bout
- Terrain → Grille → Déploiement → Incertitude → Décision → Simulation → Rejeu → Débriefing

## ÉTAPE 29 — Validation globale
- Tests de non-régression et d'intégration
- Critères d'acceptation du cahier des charges

## ÉTAPE 30 — Documentation finale et soutenance
- Documentation technique et utilisateur
- Rapport final de PFE
- Support de soutenance
