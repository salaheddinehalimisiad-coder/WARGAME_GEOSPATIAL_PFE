# PROJECT MEMORY

## État actuel du projet
L'**ÉTAPE 01 — Analyse détaillée du cahier des charges** est officiellement validée (**`PASS`**) :
- **Spécifications fonctionnelles formelles** : Rédaction complète de [`docs/SPECIFICATIONS_FONCTIONNELLES.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/SPECIFICATIONS_FONCTIONNELLES.md) couvrant l'exploitation du MNT, la discrétisation hexagonale (coordonnées axiales/cubiques), le modèle d'unités à l'échelon minimal bataillon, l'abstraction capacitaire des équipements, la modélisation des capteurs (LOS, masquage crêtes, incertitude), l'étanchéité absolue entre État Réel et États Perçus, la boucle OODA et l'indicateur synthétique de charge décisionnelle.
- **Matrice de traçabilité intégrale** : Rédaction de [`docs/MATRICE_TRACABILITE.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/MATRICE_TRACABILITE.md) associant 100% des 35 sections du Cahier des charges Version 1.0 aux modules logiciels, aux 31 étapes de la roadmap et aux méthodes de test/validation. Définition du protocole de mesure de performance sans seuils arbitraires, du déterminisme de simulation (`std::mt19937_64`) et des 15 critères majeurs de recette finale `[REC-01]` à `[REC-15]`.
- **Suivi d'avancement consolidé** :
  - **Avancement global calculé** : **6,07 %** (15 sous-tâches cochées sur 247 au total).
  - **Étapes validées (PASS)** : **2 / 31** (ÉTAPE 00 et ÉTAPE 01 validées à 100 %).
  - **Étape active** : **ÉTAPE 02 — Architecture fonctionnelle et technique** (Statut : `PLANNED`, 0 / 9 sous-tâches — 0,00 %).
  - **Sous-tâches validées de l'ÉTAPE 01 (7/7)** :
    - `P01-T01-S01` [x] (Exigences fonctionnelles terrain et grille hexagonale).
    - `P01-T01-S02` [x] (Exigences unités bataillon, équipements abstraits, capteurs).
    - `P01-T01-S03` [x] (Règles de l'arbitre et séparation étanche réel / perçu).
    - `P01-T01-S04` [x] (Spécification des rôles Blue, Red, Umpire dans `docs/SPECIFICATIONS_FONCTIONNELLES.md`).
    - `P01-T02-S01` [x] (Tableau de correspondance 35 sections CdC <-> composants).
    - `P01-T02-S02` [x] (Contraintes non-fonctionnelles, reproductibilité et protocole de benchmark).
    - `P01-T02-S03` [x] (Critères d'acceptation de recette finale dans `docs/MATRICE_TRACABILITE.md`).
- **Tableau de bord synchronisé** : [`docs/ETAT_AVANCEMENT.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ETAT_AVANCEMENT.md) généré automatiquement avec donut vectoriel [`docs/assets/progress/progress_donut.svg`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/assets/progress/progress_donut.svg) et application interactive [`docs/dashboard.html`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/dashboard.html).
- **Rapports d'étape archivés** : [`docs/rapports/rapport_etape_01.json`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/rapports/rapport_etape_01.json) consolidé.

## Référence officielle
`Cahier_des_charges_PFE_Wargame_geospatial.docx` — Version 1.0 (PFE 2026–2027).

## Règles maîtresses
- **SIG & ETL** : Global Mapper est l'unique outil SIG du workflow courant (aucun SIG concurrent actif).
- **Principe d'intégration** : « Autonomous First — CommandView Ready » (PFE 100% autonome, architecture et APIs préparées pour une intégration ultérieure dans le C4ISR CommandView).
- **Unités** : Niveau minimal d'agrégation fixé au bataillon.
- **Équipements** : Capacités abstraites uniquement (aucune arme réelle détaillée).
- **Incertitude** : Séparation stricte État Réel (Umpire) vs État Perçu (Blue/Red).
- **Suivi d'avancement** : Ne jamais modifier manuellement le pourcentage d'avancement ; toujours cocher les sous-tâches réelles dans `docs/ROADMAP.md` puis exécuter `python scripts/update_progress.py`.
- **Développement** : Progression séquentielle stricte, une seule étape active à la fois, validation par preuves, zéro développement prématuré d'étapes aval.

## Prochaine étape
**ÉTAPE 02 — Architecture fonctionnelle et technique** (Statut : `PLANNED`. En attente de validation et d'instruction formelle de démarrage).

## Historique récent
- **Validation PASS ÉTAPE 01** : Extraction intégrale des exigences du CdC, création de `docs/SPECIFICATIONS_FONCTIONNELLES.md` et `docs/MATRICE_TRACABILITE.md` (35 sections CdC mappées, critères [REC-01] à [REC-15], protocoles de performance) ; complétion des 7 sous-tâches (7/7) ; passage à 6,07 % d'avancement global (15/247 sous-tâches).
- **Nettoyage arborescence** : Suppression du dossier dupliqué imbriqué `WARGAME_GEOSPATIAL_PFE/` et création du répertoire centralisé `docs/rapports/`.
- **Validation PASS ÉTAPE 00** : Matérialisation de l'arborescence normalisée (`src/`, `tests/`, `docker/`, `data/raw/`, `data/processed/`, `data/vector/`, `data/raster/`) avec fichiers `.gitkeep`.
