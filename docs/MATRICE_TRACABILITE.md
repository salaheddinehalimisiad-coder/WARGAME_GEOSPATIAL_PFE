# MATRICE DE TRAÇABILITÉ DES EXIGENCES & CRITÈRES D'ACCEPTATION

**Document de référence pour l'ÉTAPE 01 du projet PFE 2026–2027**  
**Titre du projet :** Développement d’un wargame géospatial pour l’entraînement à la prise de décision  
**Référence contractuelle :** `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0) & [`MASTER_PROMPT.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/MASTER_PROMPT.md)  
**Livrable officiel associé :** `docs/MATRICE_TRACABILITE.md`  

---

## 1. Objet et Méthodologie de Traçabilité

La matrice de traçabilité établit le lien bidirectionnel strict et vérifiable entre chaque article du cahier des charges officiel Version 1.0 et son implémentation logicielle, son étape de réalisation dans la roadmap, ainsi que son moyen de test et de validation.

Conformément à la Section 35 du Master Prompt, chaque exigence obéit au cycle de traçabilité formel :
$$\text{EXIGENCE (CdC)} \longrightarrow \text{FONCTIONNALITÉ} \longrightarrow \text{COMPOSANT} \longrightarrow \text{SOUS-TÂCHE ROADMAP} \longrightarrow \text{TEST} \longrightarrow \text{PREUVE}$$

Ce document permet de répondre sans ambiguïté à la question centrale d'assurance qualité :
> **« Où cette exigence du cahier des charges est-elle implémentée dans le système et comment est-elle formellement validée ? »**

---

## 2. Tableau de Correspondance Exhaustif (CdC v1.0 $\longleftrightarrow$ Système) (P01-T02-S01)

L'intégralité des 35 sections du Cahier des charges officiel Version 1.0 est couverte ci-dessous sans aucune omission :

| Section CdC | Intitulé de l'exigence du CdC | Composant Logiciel / Module | Étape Roadmap | Identifiant Sous-Tâche | Méthode de Validation & Test |
|:---|:---|:---|:---:|:---:|:---|
| **1** | **Présentation générale** : Prototype de wargame géospatial d'aide à la décision | Système complet / Socle | ÉTAPE 00 / 01 | `P00-T01-S01`, `P01-T01-S01` | Revue de cadrage et audit de structure |
| **2** | **Contexte et justification** : Entraînement opérationnel, formalisation de l'analyse | Moteur décisionnel & Débriefing | ÉTAPE 20 / 27 | `P20-T01-S01`, `P27-T01-S01` | Banc de test des métriques décisionnelles |
| **3** | **Problématique scientifique** : Couplage SIG, simulation OODA et incertitude perçue | Core Engine & Module SIG | ÉTAPE 08 / 15 / 18 | `P08-T01-S01`, `P15-T01-S01`, `P18-T01-S01` | Tests unitaires C++20 sur boucle d'état |
| **4.1** | **Objectif général** : Wargame complet combinant terrain réel, unités et arbitre | Architecture Globale | ÉTAPE 02 / 28 | `P02-T01-S01`, `P28-T01-S01` | Démonstration sur scénario complet |
| **4.2** | **Objectifs spécifiques** : Modélisation, moteur déterministe, COP, rejeu | Tous modules | ÉTAPE 02 à 29 | `P02-T02-S01` à `P29-T02-S04` | Suite globale GoogleTest et Cypress/Vitest |
| **5.1** | **Système d'information géographique** : Importation, gestion de couches, CRS métrique | Pipeline SIG / PostGIS | ÉTAPE 05 / 06 / 11 | `P05-T01-S01`, `P06-T01-S02`, `P11-T01-S01` | Outil de contrôle Global Mapper, index GiST |
| **5.2** | **Modélisation du terrain** : MNT, pentes, voirie, hydrographie, occupation du sol | `src/terrain/` | ÉTAPE 08 / 09 / 10 | `P08-T01-S01`, `P09-T01-S01`, `P10-T01-S01` | Tests unitaires profils de pente artificiels |
| **5.3** | **Modèle des unités** : Échelon bataillon minimum, moral, force, ravitaillement | `src/units/` | ÉTAPE 12 | `P12-T01-S01` à `P12-T02-S04` | Tests unitaires des états et transitions |
| **5.4** | **Modèle des équipements** : Abstraction totale, capacités sans armes réelles | `src/equipment/` | ÉTAPE 13 | `P13-T01-S01` à `P13-T02-S04` | Vérification de conformité de l'ontologie |
| **6** | **Capteurs, observations et incertitude** : LOS, masquage relief, brouillard de guerre | `src/sensors/`, `src/fov/` | ÉTAPE 14 / 17 / 18 | `P14-T01-S01`, `P17-T01-S01`, `P18-T01-S01` | Tests géométriques de ligne de vue et dérive |
| **7** | **Moteur de simulation** : Boucle d'exécution, isolation, transitions d'état | `src/sim/engine/` | ÉTAPE 15 | `P15-T01-S01` à `P15-T02-S04` | Banc de reproductibilité sur scénario test |
| **8** | **Gestion du temps et des événements** : Horloge simulée, pas-à-pas, événements | `src/sim/timeline/` | ÉTAPE 19 | `P19-T01-S01` à `P19-T02-S04` | Tests de progression et d'injection temporelle |
| **9** | **Modèle de décision** : Capture du processus OODA, situation perçue, alternatives | `src/decision/` | ÉTAPE 20 | `P20-T01-S01` à `P20-T02-S04` | Validation des traces d'ordres horodatées |
| **9.1** | **Charge décisionnelle abstraite** : Indice synthétique paramétrable (0-100) | `src/decision/workload/`| ÉTAPE 20 | `P20-T02-S01` à `P20-T02-S03` | Tests unitaires mathématiques de la formule |
| **10** | **Rapport des potentiels et indicateurs** : Ratios de force, disponibilité | `src/analytics/` | ÉTAPE 27 | `P27-T01-S01` à `P27-T01-S04` | Comparaison avec calcul analytique théorique |
| **11** | **Rôles** : Cloisonnement strict Blue / Red / Umpire (arbitre omniscient) | `src/security/`, `src/api/` | ÉTAPE 22 / 23 / 24 | `P22-T01-S01`, `P23-T01-S01`, `P24-T01-S01` | Tests d'étanchéité des sessions WebSocket |
| **12** | **Interface cartographique et COP** : Carte web, hexagones, symbolisation | `frontend/src/map/` | ÉTAPE 22 / 23 / 24 | `P22-T02-S01`, `P23-T02-S01`, `P24-T02-S01` | Tests d'intégration IHM et fluidité de rendu |
| **13** | **Journalisation et traçabilité** : Enregistrement immuable des événements et ordres | `src/logging/` | ÉTAPE 25 | `P25-T01-S01` à `P25-T02-S04` | Test de non-altération des logs SQL |
| **14** | **Rejeu et débriefing** : Reconstitution exacte, navigation temporelle, AAR | `src/replay/` | ÉTAPE 26 / 27 | `P26-T01-S01`, `P27-T01-S01` | Test d'identité d'état simulé vs rejoué |
| **15** | **Conception des scénarios** : Fichiers scénarios configurables (JSON/YAML) | `data/scenarios/` | ÉTAPE 28 | `P28-T01-S01` à `P28-T01-S04` | Validation du parseur et schéma de validation |
| **16** | **Architecture logicielle cible** : Découplage Moteur / API Drogon / IHM React | Architecture / C++20 | ÉTAPE 02 / 21 | `P02-T01-S01`, `P21-T01-S01` | Revue d'architecture et conformité OpenAPI |
| **17** | **Technologies open source recommandées** : C++20, PostGIS, Drogon, React | Stack technique | ÉTAPE 04 / 21 | `P04-T01-S01`, `P21-T01-S01` | Compilation conteneurisée sans bibliothèque proprio |
| **18** | **Modèle de données minimal** : Tables Scenario, Session, Unit, Cell, etc. | `src/db/migrations/` | ÉTAPE 03 / 11 | `P03-T01-S01`, `P11-T01-S01` | Exécution des migrations SQL PostgreSQL 16 |
| **19** | **Données géographiques** : MNT et vecteurs sur zone d'étude définie | `data/processed/` | ÉTAPE 05 / 06 / 07 | `P05-T01-S01`, `P06-T01-S01`, `P07-T01-S01` | Rapport formel de contrôle qualité SIG |
| **20** | **Sécurité et maîtrise des données** : 100% local, aucune fuite, données ouvertes | Infrastructure | ÉTAPE 00 / 04 | `P00-T01-S02`, `P04-T02-S01` | Audit réseau (zéro requête externe en simu) |
| **21** | **Fonctionnalités minimales** : MVP opérationnel couvrant le cycle complet | Prototype intégré | ÉTAPE 28 / 29 | `P28-T02-S01`, `P29-T01-S01` | Test de bout en bout de la chaîne |
| **22** | **Livrables** : Rapports, codes sources, documentations, scripts | Documentation / Git | ÉTAPE 00 à 30 | `P00-T01-S03`, `P30-T01-S01` | Audit d'exhaustivité des livrables |
| **23** | **Planning indicatif** : Respect des jalons de réalisation du PFE | Suivi d'avancement | ÉTAPE 00 à 30 | `P00-T02-S04`, `P30-T02-S04` | Synchronisation automatique `update_progress.py` |
| **24** | **Critères d'acceptation** : Conditions de recette formelle du prototype | Assurance Qualité | ÉTAPE 01 / 29 | `P01-T02-S03`, `P29-T02-S01` | Procès-verbal de recette contradictoire |
| **25** | **Critères d'évaluation du PFE** : Rigueur d'ingénierie, démarche scientifique | Documentation globale | ÉTAPE 30 | `P30-T01-S01` à `P30-T02-S04` | Revue paritaire et rapport de soutenance |
| **26** | **Positionnement scientifique** : Simulation à événements discrets, OODA, incertitude | `docs/` | ÉTAPE 01 / 30 | `P01-T01-S03`, `P30-T01-S02` | Revue de la documentation méthodologique |
| **27** | **Schéma conceptuel global** : Modélisation des flux et interactions | `docs/ARCHITECTURE.md` | ÉTAPE 02 | `P02-T01-S01` à `P02-T02-S04` | Validation des 6 diagrammes SVG vectoriels |
| **28** | **Perspectives** : CommandView Ready, multi-scénarios, IA adverse future | `docs/`, OpenAPI | ÉTAPE 02 / 21 / 29 | `P02-T02-S03`, `P21-T02-S04`, `P29-T02-S03` | Conformité de la spécification OpenAPI |
| **29** | **Compétences requises** : SIG (Global Mapper), C++20, PostGIS, React | Environnement | ÉTAPE 04 | `P04-T01-S01` à `P04-T02-S04` | Validation du build pipeline et des dépendances |
| **30** | **Compétences acquises** : Ingénierie logicielle, architecture, validation | Rapports de projet | ÉTAPE 30 | `P30-T02-S01` à `P30-T02-S04` | Rédaction du mémoire de fin d'études |
| **31** | **Limites** : Aucune prétention psychiatrique, niveau bataillon strict | Règles de conception | ÉTAPE 01 / 12 / 20 | `P01-T01-S02`, `P12-T01-S02`, `P20-T02-S04` | Audit de non-dépassement de périmètre |
| **32** | **Conditions de réalisation** : Matériel standard, outils libres, pas de cloud requis | Déploiement local | ÉTAPE 00 / 04 | `P00-T02-S01`, `P04-T02-S03` | Validation sur machine de développement locale |
| **33** | **Intégration future dans CommandView** : « Autonomous First — CommandView Ready » | Points d'ancrage / Bus | ÉTAPE 02 / 21 / 29 | `P02-T02-S03`, `P21-T02-S04`, `P29-T02-S03` | Revue d'interopérabilité des interfaces REST |
| **34** | **Conclusion** : Bilan opérationnel du prototype | Rapport final | ÉTAPE 30 | `P30-T02-S03` | Validation globale du livrable académique |
| **35** | **Liste des acronymes** : Définition des termes (COP, LOS, MNT, OODA, etc.) | Glossaire officiel | ÉTAPE 01 / 30 | `P01-T02-S01`, `P30-T01-S03` | Contrôle d'homogénéité terminologique |

---

## 3. Contraintes Non-Fonctionnelles & Reproductibilité Temporelle (P01-T02-S02)

### 3.1 Déterminisme et Reproductibilité Algorithmique
- **Moteur pseudo-aléatoire contrôlé** : Utilisation exclusive du générateur standard C++20 `std::mt19937_64` initialisé par une graine (seed) entière explicitement renseignée dans le fichier de scénario.
- **Reproductibilité parfaite** : L'exécution successive de deux sessions utilisant le même scénario, la même graine et la même suite ordonnée d'ordres joueurs doit produire des états du monde (positions, moral, observations) **strictement identiques au bit près**.
- **Isolation du moteur de simulation (Core Isolation)** :
  - Le moteur de calcul métier (`src/sim/`) ne doit comporter aucun appel direct d'entrée-sortie bloquante, aucun appel socket réseau, ni aucune requête asynchrone dépendante de l'horloge système physique (`std::chrono::system_clock`).
  - Le temps physique est découplé du temps logique simulé (`SimulatedTime`).

### 3.2 Protocole de Mesure de Performance (Zéro Seuil Arbitraire)
- Conformément aux règles de correction validées, aucun seuil arbitraire non justifié n'est imposé a priori. Les exigences de performance reposent sur un protocole objectif :
  1. **Scénario de référence étalon** : Définition d'un scénario de charge nominale (ex: terrain de 100 x 100 hexagones, 20 bataillons Blue, 20 bataillons Red, 50 capteurs actifs).
  2. **Mesures instrumentées** : Mesure du temps de résolution d'un tour complet, de la latence de calcul A* d'un chemin, du temps de traitement des requêtes spatiales PostGIS et de la fréquence de rafraîchissement d'IHM.
  3. **Documentation des métriques** : Les temps mesurés sont consignés dans `docs/RAPPORT_BENCHMARKS_PERFORMANCE.md` et analysés au regard de la fluidité utilisateur.

### 3.3 Sécurité, Étanchéité et Souveraineté des Données
- **Fonctionnement 100% hors-ligne (Air-Gap Ready)** : Le prototype doit pouvoir être déployé et opéré intégralement sur un réseau local ou une machine isolée sans aucun accès à Internet.
- **Étanchéité des perspectives** : L'API Drogon et le gestionnaire de WebSocket doivent garantir qu'un client connecté sous le rôle Blue ne puisse, sous aucun prétexte ou requête forgée, recevoir les coordonnées de l'état réel ou les données privées du camp Red.

---

## 4. Critères d'Acceptation de Recette Finale (P01-T02-S03)

La recette finale du prototype (prévue lors de l'ÉTAPE 29) sera déclarée `PASS` uniquement si les 15 critères majeurs suivants sont validés avec preuves matérielles :

1. **[REC-01] Préparation SIG exclusive Global Mapper** : Preuve que toutes les couches du terrain ont été importées, harmonisées, reprojetées en métrique et nettoyées exclusivement dans Global Mapper (`docs/CATALOGUE_SIG.md` et `.gmw` validés).
2. **[REC-02] Discrétisation hexagonale régulière** : Preuve de la génération d'une grille hexagonale cohérente recouvrant l'emprise avec coordonnées axiales et propriétés de terrain agrégées sans décalage géométrique.
3. **[REC-03] Échelon bataillon strict** : Preuve de l'absence totale d'entités subordonnées (soldats, armes individuelles) et respect de l'échelle d'agrégation tactique.
4. **[REC-04] Abstraction totale des équipements** : Preuve qu'aucun nom commercial d'armement réel ni paramètre balistique classifié n'est employé dans le modèle de données.
5. **[REC-05] Séparation étanche Réel vs Perçu** : Preuve par audit des flux réseau que le client Blue ne reçoit que ses propres unités et des contacts bruités, et que l'arbitre dispose de l'état réel complet.
6. **[REC-06] Calcul d'intervisibilité (LOS)** : Preuve de fonctionnement de l'algorithme de masquage par le relief (crêtes) et les surfaces boisées/urbaines.
7. **[REC-07] Détection et observation bruitée** : Preuve que les observations comportent des dérives d'incertitude réalistes et des niveaux d'identification gradués.
8. **[REC-08] Déplacements et coûts de franchissement** : Preuve que les trajets calculés par le moteur privilégient les réseaux routiers et évitent les zones infranchissables selon la pente et la surface.
9. **[REC-09] Moteur déterministe et reproductible** : Preuve de réplication identique à 100% sur un banc d'essai multi-tours avec graine figée.
10. **[REC-10] Traçabilité et journalisation immuable** : Preuve de l'enregistrement de l'intégralité des événements, ordres et transitions dans la table `simulation_logs`.
11. **[REC-11] Rejeu chronologique bidirectionnel** : Preuve de la capacité à rejouer une session enregistrée avec bascule dynamique de point de vue (Réel, Blue, Red).
12. **[REC-12] Débriefing et After Action Review (AAR)** : Preuve de restitution de la chronologie des décisions, de la courbe de charge décisionnelle et de la confrontation entre état perçu et réalité.
13. **[REC-13] Interfaces dédiées opérationnelles** : Preuve de l'existence des trois interfaces fonctionnelles distinctes (COP Blue, COP Red, Master Umpire).
14. **[REC-14] Architecture découplée et conteneurisée** : Preuve de l'exécution intégrale via Docker Compose (PostGIS + Serveur Drogon C++20 + Frontend web).
15. **[REC-15] Compatibilité « Autonomous First — CommandView Ready »** : Preuve de la conformité de l'API REST via spécification OpenAPI documentée, prête pour une interconnexion C4ISR future.

---

## 5. Glossaire et Liste des Acronymes (Section 35 CdC)

- **AAR** : After Action Review (Débriefing après action).
- **AOI** : Area of Interest (Zone ou emprise d'intérêt géographique).
- **C4ISR** : Command, Control, Communications, Computers, Intelligence, Surveillance, and Reconnaissance.
- **COP** : Common Operational Picture (Situation tactique commune partagée).
- **CRS** : Coordinate Reference System (Système de coordonnées de référence géodésique).
- **DEM / MNT** : Digital Elevation Model / Modèle Numérique de Terrain.
- **ETL** : Extract, Transform, Load (Processus d'extraction, transformation et chargement de données).
- **FOV** : Field of View (Champ de vision ou secteur angulaire d'un capteur).
- **GIS / SIG** : Système d'Information Géographique.
- **GiST** : Generalized Search Tree (Index spatial PostgreSQL/PostGIS).
- **LOS** : Line of Sight (Ligne de vue directe / calcul d'intervisibilité).
- **MVP** : Minimum Viable Product (Produit minimum viable).
- **OODA** : Observe, Orient, Decide, Act (Boucle décisionnelle de Boyd).
- **REST** : Representational State Transfer (Architecture d'API web standard).
- **UTM** : Universal Transverse Mercator (Système de projection cartographique conforme métrique).
- **WebSocket** : Protocole réseau bidirectionnel temps réel sur socket TCP.
