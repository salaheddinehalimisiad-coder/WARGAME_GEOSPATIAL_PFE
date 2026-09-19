# RAPPORT D'AUDIT CRITIQUE DES SOURCES — ÉTAPE 01

**Objet de l'audit :** Contrôle de conformité stricte et élimination des risques de contamination par un ancien cadrage  
**Référence contractuelle unique :** `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0 — PFE 2026–2027)  
**Branche Git :** `phase/01-analyse-cdc`  
**Statut de l'ÉTAPE 01 :** `IN_PROGRESS` (en attente de revue contradictoire et validation par le client)  

---

## 1. Dénombrement et Contrôle des 35 Sections du Cahier des Charges

Le dénombrement des sections a été exécuté directement depuis le fichier binaire officiel `Cahier_des_charges_PFE_Wargame_geospatial.docx` par extraction et analyse de son document XML source (`word/document.xml`).

- **Méthode de comptage :** Analyse des nœuds de paragraphe (`w:p`) comportant un style de titre principal (`Titre1` / `Heading1`) et détection des préfixes numériques de premier niveau (`1.` à `35.`).
- **Nombre de sections principales trouvées :** **Exactement 35 sections**.
- **Liste intégrale des sections répertoriées :**
  1. Présentation générale
  2. Contexte et justification
  3. Problématique scientifique
  4. Objectifs (4.1 Objectif général, 4.2 Objectifs spécifiques)
  5. Périmètre fonctionnel (5.1 SIG, 5.2 Terrain, 5.3 Unités, 5.4 Équipements)
  6. Capteurs, observations et incertitude
  7. Moteur de simulation
  8. Gestion du temps et des événements
  9. Modèle de décision (9.1 Charge décisionnelle abstraite)
  10. Rapport des potentiels et indicateurs
  11. Rôles
  12. Interface cartographique et COP
  13. Journalisation et traçabilité
  14. Rejeu et débriefing
  15. Conception des scénarios
  16. Architecture logicielle cible
  17. Technologies open source recommandées
  18. Modèle de données minimal
  19. Données géographiques
  20. Sécurité et maîtrise des données
  21. Fonctionnalités minimales
  22. Livrables
  23. Planning indicatif
  24. Critères d’acceptation
  25. Critères d’évaluation du PFE
  26. Positionnement scientifique
  27. Schéma conceptuel global
  28. Perspectives
  29. Compétences requises
  30. Compétences acquises
  31. Limites
  32. Conditions de réalisation
  33. Intégration future dans CommandView
  34. Conclusion
  35. Liste des acronymes
- **Couverture de traçabilité dans [docs/MATRICE_TRACABILITE.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/MATRICE_TRACABILITE.md) :** **100 % (35/35 sections tracées)**.

---

## 2. Éléments Conformes au Nouveau Cahier des Charges

Les exigences suivantes ont été vérifiées conformes au texte du CdC v1.0 et sont explicitement taguées **[A]** :
1. **Échelon tactique minimal au bataillon** (*CdC Section 5.3*).
2. **Abstraction capacitaire stricte des matériels** (*CdC Section 5.4, 31*).
3. **Séparation hermétique État Réel (Ground Truth) vs Situation Perçue (Blue/Red COP)** (*CdC Section 6, 11, 12, 27*).
4. **Observations incertaines et bruitées** caractérisées par une position estimée, une précision, un niveau de confiance et un horodatage (*CdC Section 6, 18*).
5. **Moteur de simulation** gérant l'état courant, les règles, les mouvements sur la grille, les interactions abstraites, les observations et les traces (*CdC Section 7*).
6. **Gestion du temps** avec horloge configurable, mode pas-à-pas et accélération (*CdC Section 8*).
7. **Modèle de décision observable** (options, choix, heure, résultat) sans prétention clinique ou psychologique (*CdC Section 9, 31*).
8. **Métrique de charge décisionnelle abstraite** combinant événements, incertitude, alternatives et contrainte temporelle (*CdC Section 9.1*).
9. **Rapport des potentiels et indicateurs synthétiques** transparents et paramétrables (*CdC Section 10*).
10. **Trois rôles exclusifs : Blue, Red, Arbitre / Umpire** (*CdC Section 11*).
11. **Interfaces cartographiques interactives et vue réelle arbitre** (*CdC Section 12*).
12. **Journalisation structurée** de toutes les actions significatives pour la reconstruction (*CdC Section 13*).
13. **Rejeu reproductible et débriefing After Action Review (AAR)** (*CdC Section 14*).
14. **9 critères d'acceptation textuels officiels** (*CdC Section 24*).
15. **Principe « Autonomous First — CommandView Ready »** (*CdC Section 16, 33*).

---

## 3. Éléments Corrigés

1. **Clarification du statut de Global Mapper :**
   - Le CdC (*Section 17*) mentionne indicativement « QGIS/GDAL/PROJ pour les traitements SIG... sous réserve de confirmation d'analyse ».
   - Global Mapper est le choix arrêté par l'équipe projet pour l'ingénierie SIG/ETL.
   - Ce choix est désormais formellement documenté comme un **[Choix technologique interne]** et non comme une obligation contractuelle du CdC.
2. **Modèle temporel :**
   - Remplacement de la notion de séquence rigide en 4 phases imposées par le modèle d'horloge configurable du CdC (*Section 8*).
3. **Classification systématique dans les spécifications :**
   - Réécriture de [docs/SPECIFICATIONS_FONCTIONNELLES.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/SPECIFICATIONS_FONCTIONNELLES.md) avec balisage explicite `[A]`, `[B]`, `[C]`, `[D]`.
4. **Matrice de traçabilité restructurée :**
   - Réécriture de [docs/MATRICE_TRACABILITE.md](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/MATRICE_TRACABILITE.md) avec colonne dédiée spécifiant la nature exacte de chaque ligne (*Exigence du cahier, Interprétation, Décision d’architecture, Choix technologique, Proposition future*).

---

## 4. Éléments Supprimés (Purgés du Cadrage)

Tous les éléments suivants, issus d'anciens cadrages ou de propositions non justifiées par le CdC officiel, ont été **définitivement purgés** :
- **Séquence imposée en 4 phases fermées** (Planification, Détection, Résolution, Arbitrage) présentée comme contractuelle.
- **Nomenclature inventée REC-01 à REC-15** : remplacée par les 9 critères textuels contractuels de la Section 24 du CdC.
- **Classes rigides de contacts "Inconnu / Catégorie / Identifié"** : remplacées par les attributs paramétrables du CdC (position estimée, précision, confiance).
- **Probabilités numériques de détection hardcodées (ex: 85%, 60%)** : supprimées.
- **Formules de décroissance temporelle exponentielle (demi-vie) des contacts** : supprimées.
- **Formules spécifiques d'atténuation de ligne de vue ad-hoc** : supprimées.
- **Règles d'arbitrage manuelles invasives** non prévues à la Section 11 du CdC : supprimées.
- **Règles cinématiques et tables de combat spécifiques inventées** : supprimées au profit du « modèle abstrait d'interaction » prescrit par le CdC.
- **Terme et concept de VPC (Victory Points Conditions)** : supprimé, remplacé par « Objectifs pédagogiques et critères de fin » (*CdC Section 15*).
- **Attribut psychologique subjectif de "moral (0-100%)"** : supprimé, remplacé par « effectif ou disponibilité abstraite, endurance ou attribut équivalent » (*CdC Section 5.3, 5.4*).
- **Profils d'échelle imposés à 50 / 300 / 1500 hexagones** : supprimés de la formulation des exigences.
- **Noms de structures internes `UnitGroundTruth` et `PerceivedContact`** : neutralisés au profit des entités officielles du CdC (`Unit`, `Observation`).

---

## 5. Éléments Conservés comme Propositions d'Architecture à Valider [C]

Ces éléments ne sont pas imposés par le CdC mais proposés par l'équipe technique pour sa mise en œuvre, et sont clairement identifiés comme tels :
- **[PROP-TECH-01]** Déterminisme algorithmique renforcé par le PRNG 64 bits `std::mt19937_64` alimenté par une graine (`seed`) déclarée au scénario pour garantir la reproductibilité prescrite par la Section 24.
- **[PROP-TECH-02]** Système de coordonnées axiales `(q, r)` pour le maillage hexagonal, assurant des calculs de distance euclidienne en $O(1)$.
- **[PROP-TECH-03]** Déploiement conteneurisé via Docker Compose pour l'autonomie d'exécution locale (*CdC Section 17*).
- **[PROP-TECH-04]** Retenue de Global Mapper comme outil SIG/ETL du projet pour le traitement MNT et l'export des couches.

---

## 6. Résultat du Contrôle de Traçabilité

- **Total sections CdC officiel :** 35 sections.
- **Sections tracées dans la matrice :** 35 sections.
- **Taux de couverture :** **100 %**.
- **Conformité globale :** **CONFORME AUX EXIGENCES DU CAHIER OFFICIEL v1.0**.
- **Distinction claire :** Aucune proposition interne n'est plus présentée comme une exigence contractuelle.

---

## 7. État Git et Historique

- **Branche active de travail :** `phase/01-analyse-cdc`
- **Branche cible de merge ultérieur :** `develop` (aucun merge prématuré effectué)
- **Modifications apportées sur la branche :**
  - Révision complète de `docs/SPECIFICATIONS_FONCTIONNELLES.md`.
  - Révision complète de `docs/MATRICE_TRACABILITE.md`.
  - Mise à jour de `docs/ROADMAP.md` (ÉTAPE 01 maintenue en statut `IN_PROGRESS`).
  - Synchronisation de `docs/ETAT_AVANCEMENT.md`, `docs/assets/progress/progress_data.json`, `docs/assets/progress/progress_donut.svg`, et `docs/dashboard.html`.
  - Génération de `docs/rapports/rapport_audit_source_etape_01.json` et `docs/rapports/rapport_audit_source_etape_01.md`.

---

## 8. Tests et Vérifications Exécutés

1. **Test unitaire du calcul de progression :**
   - Commande : `python scripts/test_progress_calculation.py`
   - Résultat : `PASS` (10/10 tests réussis, vérification des 31 étapes et 247 sous-tâches, détection des doublons, validation de l'étape active).
2. **Exécution du script de mise à jour de progression :**
   - Commande : `python scripts/update_progress.py`
   - Résultat :
     - Total sous-tâches : 247
     - Sous-tâches terminées : 14
     - Sous-tâches restantes : 233
     - Progression globale : 5.67 %
     - Étape active : `ÉTAPE 01 — Analyse détaillée du cahier des charges`
     - Statut de l'ÉTAPE 01 : `IN_PROGRESS`
