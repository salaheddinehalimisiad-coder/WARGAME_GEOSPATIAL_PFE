# ÉTAPE 01 — Analyse détaillée du cahier des charges

**Statut :** `PASS` (7 / 7 sous-tâches terminées)  
**Branche Git :** `phase/01-analyse-cdc`  
**Commits associés :**
- `d0756e6` — `feat(analysis): formalize functional specs and requirements traceability matrix (ETAPE 01)`
- `d61e216` — `refactor(specs): perform critical source audit against official CdC v1.0, purge legacy artifacts and classify requirements [A-D]`
- `c04fcdd` — `docs(architecture): align diagrams with official CdC`

---

## Objectif
Analyser exhaustivement le cahier des charges officiel `Cahier_des_charges_PFE_Wargame_geospatial.docx` (Version 1.0) pour en extraire toutes les exigences fonctionnelles et non-fonctionnelles, et produire la matrice de traçabilité.

## Travail réalisé
- Dénombrement et vérification directe des **35 sections** du fichier XML officiel du CdC v1.0.
- Rédaction et audit de `docs/SPECIFICATIONS_FONCTIONNELLES.md` avec classification systématique :
  - `[A]` Exigence directement présente dans le CdC.
  - `[B]` Déduction logique raisonnable, non arbitraire.
  - `[C]` Proposition d'architecture technique à valider.
  - `[D]` Élément purgé appartenant à un ancien cadrage.
- Rédaction et audit de `docs/MATRICE_TRACABILITE.md` avec 100 % de couverture des 35 sections et typage de chaque ligne (Exigence, Interprétation, Décision d'architecture, Choix technologique, Proposition future).
- Purge complète des éléments non justifiés par le CdC officiel (voir "Décisions validées").

## Fichiers créés / modifiés
- `docs/SPECIFICATIONS_FONCTIONNELLES.md` (créé puis audité et réécrit)
- `docs/MATRICE_TRACABILITE.md` (créé puis audité et réécrit)
- `docs/ROADMAP.md` (6 sous-tâches P01 cochées, P01-T02-S03 maintenue `[ ]` pendant l'audit)
- `docs/ETAT_AVANCEMENT.md`, `docs/assets/progress/progress_data.json`, `docs/assets/progress/progress_donut.svg`, `docs/dashboard.html` (synchronisés)
- `PROJECT_MEMORY.md`, `CHANGELOG.md`
- `scripts/test_progress_calculation.py` (ajustement détection étape active dynamique)
- `docs/rapports/rapport_etape_01.md`, `docs/rapports/rapport_etape_01.json` (archivés, ne plus enrichir)
- `docs/rapports/rapport_audit_source_etape_01.md`, `docs/rapports/rapport_audit_source_etape_01.json` (archivés, ne plus enrichir)

## Décisions validées
1. **Global Mapper** est un **choix d'ingénierie interne** du projet, pas une obligation contractuelle (le CdC Section 17 recommande QGIS/GDAL à titre indicatif).
2. **Échelon bataillon minimal** : aucune entité subordonnée représentée comme pion autonome.
3. **Abstraction capacitaire totale** : paramètres relatifs uniquement, zéro caractéristique d'arme réelle.
4. **Séparation hermétique** État Réel (Ground Truth, Umpire uniquement) vs États Perçus (Blue COP, Red COP).
5. **Déterminisme** via PRNG `std::mt19937_64` avec `seed` de scénario — proposition `[C]` à confirmer en ÉTAPE 02.
6. **Critères d'acceptation officiels** : exactement 9 critères textuels contractuels de la Section 24 du CdC (`CRIT-01` à `CRIT-09`). La nomenclature inventée `REC-01..REC-15` est purgée.
7. **Séquence temporelle** : le CdC prescrit une horloge configurable pas-à-pas ou continue — aucune séquence rigide en 4 phases n'est contractuelle.

## Éléments purgés (anciens cadrages)
- Boucle rigide en 4 phases fermées (Planification/Détection/Résolution/Arbitrage)
- Classes de contacts Inconnu / Catégorie / Identifié
- Probabilités numériques hardcodées (85%, 60%)
- Décotes temporelles exponentielles des observations
- Formules LOS ad-hoc non sourcées
- Attribut psychologique `moral (0-100%)`
- Concept de VPC (Victory Points Conditions)
- Profils d'échelle imposés (50 / 300 / 1500 hexagones)
- Nomenclature REC-01..REC-15

## Points importants pour la suite (ÉTAPE 02)
- Les propositions `[C]` (PRNG seedé, coordonnées axiales `(q,r)`, Docker) devront être confirmées formellement en ÉTAPE 02 lors de la conception de l'architecture.
- La matrice de traçabilité devra être mise à jour avec les composants architecturaux réels définis en ÉTAPE 02.
- La sous-tâche `P01-T02-S03` a été validée formellement après revue contradictoire des 9 critères d'acceptation de la Section 24 du CdC.

## État de l'étape
`PASS` — 7 / 7 sous-tâches validées avec traçabilité intégrale du CdC v1.0.

### Clôture et validation finale (2026-09-21)
- **Validation P01-T02-S03** : Revue contradictoire rigoureuse effectuée avec le client sur les 9 critères contractuels `CRIT-01` à `CRIT-09` issus de la Section 24 du CdC (concordance textuelle exacte à 100 %, zéro exigence inventée, zéro terme obsolète).
- **Matrice de traçabilité** : 35/35 sections du CdC v1.0 couvertes, typologie rigoureuse, critères contractuels isolés des propositions techniques.
- **Clôture de l'ÉTAPE 01** : Étape officiellement validée `PASS`.

### Correction architecture après revue (2026-09-20)
- **6 diagrammes SVG revus et synchronisés** (versions publiées et `docs/assets/architecture/source/`) : formulations trop spécifiques ou prescriptives neutralisées.
- **Purge des termes non contractuels** : `A*`, `OODA`, `mt19937_64`, `React 18`, `PostgreSQL 16` / `PostGIS 3.4`, `score_actuel`, métriques arbitraires ("2 millisecondes").
- **Rôle Umpire repositionné** : clarifié comme rôle de supervision/arbitrage distinct des factions de jeu Blue/Red.
- **Assainissement des références** : suppression de la référence à `docs/RAPPORT_QA_SIG.md` (inexistant), remplacée par un protocole de contrôle qualité documenté.
- **`docs/ARCHITECTURE.md` aligné** : texte rigoureusement synchronisé avec les diagrammes corrigés et le CdC officiel.
- **Aucun développement fonctionnel** : architecture clarifiée et prête pour l'ÉTAPE 02.

