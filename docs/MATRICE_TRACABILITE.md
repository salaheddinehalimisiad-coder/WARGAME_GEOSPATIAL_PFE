# MATRICE DE TRAÇABILITÉ DES EXIGENCES & CRITÈRES D'ACCEPTATION

**Document de référence issu de l'audit critique de l'ÉTAPE 01 — PFE 2026–2027**  
**Titre du projet :** Développement d’un wargame géospatial pour l’entraînement à la prise de décision  
**Source contractuelle unique :** `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0)  
**Livrable officiel associé :** `docs/MATRICE_TRACABILITE.md`  

---

## 1. Méthodologie et Typologie de Traçabilité

Afin d'éviter toute confusion entre le texte contractuel et les choix techniques du projet, chaque élément tracé est catégorisé selon sa nature exacte :
- **[Exigence du cahier]** : Dispositif textuel explicite extrait de `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0).
- **[Interprétation]** : Déduction opérationnelle rigoureuse nécessaire à la déclinaison logicielle, sans ajout de contrainte arbitraire.
- **[Décision d’architecture]** : Choix structurel d'ingénierie opéré pour répondre à une exigence (ex: modularité C++, schéma relationnel PostGIS).
- **[Choix technologique]** : Sélection d'un outil ou bibliothèque (ex: Global Mapper pour l'ETL, Drogon C++20, React/TypeScript).
- **[Proposition future]** : Fonctionnalité ou perspective d'extension documentée mais non obligatoire pour le MVP de fin d'études.

---

## 2. Vérification et Dénombrement des Sections du Cahier des Charges

### 2.1 Méthode de Comptage
Le dénombrement a été réalisé directement sur le fichier binaire officiel `Cahier_des_charges_PFE_Wargame_geospatial.docx` par extraction du document XML principal (`word/document.xml`). Les nœuds de paragraphes (`w:p`) comportant un style de titre principal (`Titre1` / `Heading1`) ou un préfixe numéroté de niveau 1 (`1.` à `35.`) ont été répertoriés.

- **Nombre de sections principales trouvées** : **Exactement 35 sections** (numérotées de 1 à 35).
- **Sous-sections formelles identifiées** : 4.1, 4.2, 5.1, 5.2, 5.3, 5.4, 9.1.
- **Taux de couverture de la matrice** : **100 %** (35/35 sections tracées).

---

## 3. Tableau de Traçabilité Exhaustif (35 Sections du CdC v1.0)

| N° | Section CdC Officielle | Nature de l'élément | Synthèse du Contenu CdC | Implémentation Logicielle / Composant | Étape Roadmap | Méthode de Validation & Preuve |
|:---|:---|:---|:---|:---|:---:|:---|
| **1** | **Présentation générale** | [Exigence du cahier] | Prototype de wargame géospatial d'aide à la décision | Socle global du projet | ÉTAPE 00 / 01 | Audit de conformité documentaire et structure |
| **2** | **Contexte et justification** | [Exigence du cahier] | Entraînement opérationnel, formalisation de l'analyse | Moteur décisionnel & Débriefing | ÉTAPE 20 / 27 | Scénario d'évaluation pédagogique |
| **3** | **Problématique scientifique** | [Interprétation] | Couplage SIG, boucle OODA et incertitude perçue | Moteur C++ & Pipeline spatial | ÉTAPE 08 / 15 / 18 | Tests unitaires de la boucle spatio-temporelle |
| **4.1** | **Objectif général** | [Exigence du cahier] | Démonstrateur combinant terrain, unités et arbitre | Intégration globale | ÉTAPE 28 / 29 | Démonstration complète de bout en bout |
| **4.2** | **Objectifs spécifiques** | [Exigence du cahier] | Modélisation, moteur reproductible, COP, rejeu | Tous modules applicatifs | ÉTAPE 02 à 29 | Suites de tests automatisés |
| **5.1** | **Système d'information géographique** | [Exigence du cahier] | Affichage cartographique interactif, couches raster/vecteur, zoom, coordonnées | PostGIS, Frontend Web Leaflet/OpenLayers | ÉTAPE 05 / 06 / 11 / 22 | Tests de rendu cartographique et projections |
| **5.2** | **Modélisation du terrain** | [Exigence du cahier] | Import MNT/DEM, altitude, pente, hydro, voirie, bâti, grille hexagonale | `src/terrain/`, PostGIS raster/vector | ÉTAPE 08 / 09 / 10 | Contrôle altimétrique et calcul des pentes |
| **5.3** | **Modèle des unités** | [Exigence du cahier] | Échelon bataillon minimum, effectif/disponibilité, capacités synthétiques | `src/units/` (C++20) | ÉTAPE 12 | Tests unitaires des attributs et postures |
| **5.4** | **Modèle des équipements** | [Exigence du cahier] | Abstraction totale, portée relative, mobilité, sans armes réelles | `src/equipment/` (C++20) | ÉTAPE 13 | Audit d'absence de caractéristiques réelles |
| **6** | **Capteurs, observations et incertitude** | [Exigence du cahier] | État réel vs état perçu, observations bruitées, confiance, horodatage | `src/sensors/`, `src/fov/` | ÉTAPE 14 / 17 / 18 | Tests de calcul de ligne de vue et d'incertitude |
| **7** | **Moteur de simulation** | [Exigence du cahier] | Évolution d'état, déplacements, interactions abstraites, traces, rejeu | `src/sim/engine/` (C++20) | ÉTAPE 15 | Banc de tests de transitions d'état |
| **8** | **Gestion du temps et des événements** | [Exigence du cahier] | Horloge configurable, pas-à-pas, accélération, événements planifiés | `src/sim/timeline/` | ÉTAPE 19 | Tests de défilement temporel et d'échéances |
| **9** | **Modèle de décision** | [Exigence du cahier] | Processus observable (options, choix, heure, résultat) sans psychologie | `src/decision/` | ÉTAPE 20 | Validation des structures de données de décision |
| **9.1** | **Charge décisionnelle abstraite** | [Exigence du cahier] | Métrique expérimentale paramétrable (événements, incertitude, temps) | `src/decision/workload/` | ÉTAPE 20 | Tests de calcul de la formule synthétique |
| **10** | **Rapport des potentiels et indicateurs** | [Exigence du cahier] | Indicateurs transparents (potentiel agrégé, mobilité, rapport forces) | `src/analytics/` | ÉTAPE 27 | Validation des formules d'agrégation |
| **11** | **Rôles** | [Exigence du cahier] | Blue (conduite), Red (opposant), Arbitre/Umpire (contrôle, état réel) | `src/security/`, `src/api/` | ÉTAPE 22 / 23 / 24 | Tests d'étanchéité des perspectives |
| **12** | **Interface cartographique et COP** | [Exigence du cahier] | Carte interactive, grille hexagone, symboles, vue arbitre | Frontend Web React / Carto | ÉTAPE 22 / 23 / 24 | Tests d'interface et d'affichage des COP |
| **13** | **Journalisation et traçabilité** | [Exigence du cahier] | Enregistrement structuré des actions, détections, événements, décisions | `src/logging/`, table SQL | ÉTAPE 25 | Vérification de l'immuabilité des traces |
| **14** | **Rejeu et débriefing** | [Exigence du cahier] | Rejeu session, avance/recul, comparaison réel vs perçu, AAR | `src/replay/`, `src/debrief/` | ÉTAPE 26 / 27 | Test de fidélité du rejeu depuis les traces |
| **15** | **Conception des scénarios** | [Exigence du cahier] | Emprise, situation initiale, objectifs pédagogiques, critères de fin | `data/scenarios/` (JSON/YAML) | ÉTAPE 28 | Validation du schéma de scénario |
| **16** | **Architecture logicielle cible** | [Décision d’architecture] | « Autonomous First — CommandView Ready », découplage Présentation/API/Moteur | Architecture modulaire C++20 | ÉTAPE 02 / 21 | Revue d'architecture logicielle |
| **17** | **Technologies recommandées** | [Choix technologique] | CdC recommande C++20, PostGIS, Drogon, React. *Pour le SIG, le projet choisit Global Mapper* | Stack Docker / C++20 / GM | ÉTAPE 04 / 21 | Vérification des builds et conteneurs |
| **18** | **Modèle de données minimal** | [Exigence du cahier] | Entités Scenario, Session, Unit, Equipment, Sensor, Observation, Decision, Event, LogEntry | Schéma PostGIS / SQL | ÉTAPE 03 / 11 | Exécution des scripts de schéma relationnel |
| **19** | **Données géographiques** | [Exigence du cahier] | MNT, réseau routier, hydro, bâti, occupation du sol (données publiques) | `data/raw/`, `data/processed/` | ÉTAPE 05 / 06 / 07 | Rapport de contrôle de qualité des données |
| **20** | **Sécurité et maîtrise des données** | [Exigence du cahier] | Cloisonnement rôles, fonctionnement local autonome, aucune donnée classifiée | Déploiement local / RBAC | ÉTAPE 00 / 04 | Audit d'isolation réseau |
| **21** | **Fonctionnalités minimales** | [Exigence du cahier] | 14 fonctionnalités MVP (terrain, hexagones, unités, tours, débriefing) | Prototype intégré | ÉTAPE 28 / 29 | Test de validation fonctionnelle de bout en bout |
| **22** | **Livrables** | [Exigence du cahier] | CdC détaillé, état de l'art, spécifications, prototype, documentation | Livrables documentaires & code | ÉTAPE 00 à 30 | Audit de la liste des livrables |
| **23** | **Planning indicatif** | [Interprétation] | 12 phases indicatives sur ~28 semaines, déclinées en 31 étapes | `docs/ROADMAP.md` | ÉTAPE 00 à 30 | Suivi d'avancement automatique |
| **24** | **Critères d’acceptation** | [Exigence du cahier] | 9 critères textuels contractuels (Fonctionnalité, Simulation, SIG...) | Grille d'acceptation officielle | ÉTAPE 01 / 29 | Procès-verbal de recette finale |
| **25** | **Critères d’évaluation du PFE** | [Exigence du cahier] | Démarche scientifique, qualité de l'architecture, rejeu, ergonomie | Ensemble du projet | ÉTAPE 30 | Rapport de soutenance et mémoire |
| **26** | **Positionnement scientifique** | [Interprétation] | Intersection SIG, simulation, incertitude, traces et décision | `docs/` | ÉTAPE 01 / 30 | Note méthodologique |
| **27** | **Schéma conceptuel global** | [Exigence du cahier] | Flux continu : Terrain → Grille → Unités → Capteurs → Décision → Moteur → Traces → Rejeu | `docs/ARCHITECTURE.md` | ÉTAPE 02 | Diagrammes de flux conceptuels |
| **28** | **Perspectives** | [Proposition future] | CommandView, simulation distribuée, IA adverse, multi-échelons | Spécifications d'interopérabilité | ÉTAPE 02 / 29 | Documentation d'extension future |
| **29** | **Compétences requises** | [Exigence du cahier] | C++, SIG, SQL spatial, architecture, web carto, algorithmic | Équipe projet | ÉTAPE 04 | Validation de l'environnement de développement |
| **30** | **Compétences acquises** | [Exigence du cahier] | Conception système complexe, géospatial, temps réel, industrialisation | Synthèse académique | ÉTAPE 30 | Dossier d'évaluation PFE |
| **31** | **Limites** | [Exigence du cahier] | Outil pédagogique/expérimental, abstraction totale, non-doctrine | Spécifications et scénarios | ÉTAPE 01 / 12 / 13 | Audit des paramètres de simulation |
| **32** | **Conditions de réalisation** | [Exigence du cahier] | Données représentatives, environnement local, annexe technique | Environnement de travail | ÉTAPE 00 / 04 | Configuration du banc local |
| **33** | **Intégration CommandView** | [Proposition future] | Compatibilité C4ISR (REST/OpenAPI, WebSocket, événements) | Points d'interopérabilité | ÉTAPE 02 / 21 / 29 | Spécification d'API ouverte |
| **34** | **Conclusion** | [Exigence du cahier] | Synthèse des objectifs et périmètre du démonstrateur | Rapport de fin d'études | ÉTAPE 30 | Conclusion du rapport de projet |
| **35** | **Liste des acronymes** | [Exigence du cahier] | 20 acronymes officiels (API, C2, C4ISR, COP, MNT, SIG, H3, OODA...) | Glossaire du projet | ÉTAPE 01 / 30 | Contrôle de cohérence terminologique |

---

## 4. Précision sur le Choix de l'Outil SIG (Global Mapper vs Section 17)

- **Mention textuelle du CdC (Section 17)** : « QGIS/GDAL/PROJ pour les traitements SIG. Le choix définitif devra être confirmé après analyse des performances attendues, de la maintenabilité, des compétences disponibles et des contraintes de déploiement. »
- **Décision d'ingénierie du projet** : L'équipe projet a retenu et validé **Global Mapper** comme unique outil SIG/ETL pour le traitement des MNT, la reprojection métrique et la préparation des données géospatiales.
- **Statut de traçabilité** : Cette décision constitue un **[Choix technologique interne]** d'ingénierie et non une obligation contractuelle directe du CdC. Elle garantit l'homogénéité des chaînes de traitement sans altérer les exigences de sortie (MNT exploitable, couches vectorielles nettoyées, coordonnées métriques conformes).

---

## 5. Critères d'Acceptation Officiels du Cahier des Charges (Section 24)

Les critères de recette finale contractuels sont **strictement les 9 critères textuels** définis dans la Section 24 du cahier des charges officiel :

| Réf. CdC | Critère Officiel | Exigence Contractuelle Associée | Mode de Vérification Prévu |
|:---:|:---|:---|:---|
| **CRIT-01** | **Fonctionnalité** | Scénario de démonstration exécutable de bout en bout. | Exécution complète d'une session sans interruption ni plantage. |
| **CRIT-02** | **Simulation** | Transitions cohérentes et reproductibles avec paramètres identiques. | Test de réplication à l'identique de deux exécutions avec paramètres initiaux identiques. |
| **CRIT-03** | **SIG** | Terrain et grille correctement affichés et manipulables. | Contrôle de l'affichage cartographique, du relief et de la navigation sur la grille. |
| **CRIT-04** | **Temps** | Événements et décisions horodatés et conformes aux règles. | Vérification de la chronologie des événements et du respect des contraintes temporelles. |
| **CRIT-05** | **Information** | Visibilité conforme aux règles d’incertitude. | Contrôle du brouillard de guerre et de l'imperméabilité des vues Blue et Red. |
| **CRIT-06** | **Traçabilité** | Actions importantes enregistrées. | Audit du journal des traces (déplacements, détections, décisions, événements). |
| **CRIT-07** | **Rejeu** | Session reconstruisible. | Rejeu complet d'une session passée à partir de ses traces. |
| **CRIT-08** | **Débriefing** | Décisions et événements consultables. | Restitution de la chronologie des décisions et confrontation état perçu / état réel. |
| **CRIT-09** | **Qualité** | Code versionné, documenté et testé. | Audit des dépôts Git, documentation technique et taux de passage des tests. |

---

## 6. Critères Internes de Validation Proposés par le Projet (Non Imposés par le CdC)

En complément des 9 critères contractuels du CdC, l'équipe d'ingénierie propose les critères techniques internes suivants pour outiller les revues d'étape :
- **[PROP-TECH-01]** Déterminisme algorithmique renforcé : utilisation d'un PRNG seedé (`std::mt19937_64`) pour garantir la reproductibilité au bit près.
- **[PROP-TECH-02]** Évaluation métrologique sur scénarios étalons : mesure instrumentée des temps de calcul sans seuils arbitraires prématurés.
- **[PROP-TECH-03]** Conteneurisation de bout en bout via Docker Compose pour simplifier le déploiement local autonome.
