# PROJECT MEMORY

## État actuel du projet
L'**ÉTAPE 01 — Analyse détaillée du cahier des charges** a fait l'objet d'un **audit critique des sources** pour éliminer tout risque de contamination par d'anciens cadrages.
- **Statut actuel de l'ÉTAPE 01** : **`IN_PROGRESS`** (en attente de revue et validation client du rapport d'audit).
- **Source contractuelle unique et exclusive** : `Cahier_des_charges_PFE_Wargame_geospatial.docx` Version 1.0 (PFE 2026–2027).
- **Spécifications fonctionnelles auditées** : Réécriture de [`docs/SPECIFICATIONS_FONCTIONNELLES.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/SPECIFICATIONS_FONCTIONNELLES.md) avec classification systématique des exigences :
  - `[A]` Directement présente dans le cahier des charges (MNT, hexagones, bataillon min, abstraction matérielle, séparation Réel/Perçu, horloge configurable, décision observable, charge décisionnelle paramétrable, rôles Blue/Red/Umpire, journalisation, rejeu, 9 critères d'acceptation).
  - `[B]` Déduite de façon raisonnable sans extrapolation arbitraire.
  - `[C]` Proposition d'architecture à valider (PRNG `std::mt19937_64`, coordonnées axiales `(q,r)`, conteneurisation Docker, choix ETL Global Mapper).
  - `[D]` Éléments d'anciens cadrages formellement identifiés et purgés (suppression de la boucle rigide en 4 phases, suppression de REC-01..REC-15, suppression des classes rigides Inconnu/Catégorie/Identifié, suppression de VPC, suppression des probabilités de détection et décotes temporelles hardcodées, suppression de l'attribut psychologique subjectif moral 0-100%).
- **Matrice de traçabilité auditée** : Réécriture de [`docs/MATRICE_TRACABILITE.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/MATRICE_TRACABILITE.md) :
  - Dénombrement exact de 35 sections principales dans le fichier officiel XML du CdC (100% tracées).
  - Distinction formelle de la nature de chaque ligne (Exigence du cahier, Interprétation, Décision d'architecture, Choix technologique, Proposition future).
  - Clarification du statut de Global Mapper : choix technologique d'ingénierie interne validé par le projet, distinct des technologies indicatives recommandées dans la Section 17 du CdC (QGIS/GDAL).
  - Remplacement de la nomenclature arbitraire REC-01..15 par les 9 critères contractuels de la Section 24 du CdC (`CRIT-01` à `CRIT-09`).
- **Suivi d'avancement consolidé** :
  - **Avancement global calculé** : **5,67 %** (14 sous-tâches cochées sur 247 au total).
  - **Étapes validées (PASS)** : **1 / 31** (ÉTAPE 00 validée).
  - **Étape active** : **ÉTAPE 01 — Analyse détaillée du cahier des charges** (Statut : `IN_PROGRESS`, 6 / 7 sous-tâches — 85,71 %).
  - **Sous-tâches de l'ÉTAPE 01** :
    - `P01-T01-S01` [x] (Exigences fonctionnelles terrain et grille hexagonale).
    - `P01-T01-S02` [x] (Exigences unités bataillon, équipements abstraits, capteurs).
    - `P01-T01-S03` [x] (Règles de l'arbitre et séparation étanche réel / perçu).
    - `P01-T01-S04` [x] (Spécification des rôles Blue, Red, Umpire dans `docs/SPECIFICATIONS_FONCTIONNELLES.md`).
    - `P01-T02-S01` [x] (Tableau de correspondance 35 sections CdC <-> composants).
    - `P01-T02-S02` [x] (Contraintes non-fonctionnelles, reproductibilité et protocole de benchmark).
    - `P01-T02-S03` [ ] (Validation finale des critères d'acceptation - en cours d'audit).
- **Rapports d'audit archivés** :
  - [`docs/rapports/rapport_audit_source_etape_01.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/rapports/rapport_audit_source_etape_01.md)
  - [`docs/rapports/rapport_audit_source_etape_01.json`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/rapports/rapport_audit_source_etape_01.json)

## Référence officielle unique
`Cahier_des_charges_PFE_Wargame_geospatial.docx` — Version 1.0 (PFE 2026–2027).

## Règles maîtresses
- **SIG & ETL** : Global Mapper est l'unique outil SIG/ETL du projet (choix d'ingénierie interne).
- **Principe d'intégration** : « Autonomous First — CommandView Ready » (PFE 100% autonome, architecture et APIs préparées pour une intégration ultérieure dans le C4ISR CommandView).
- **Unités** : Niveau minimal d'agrégation fixé au bataillon.
- **Équipements** : Capacités abstraites uniquement (aucune arme réelle détaillée).
- **Incertitude** : Séparation stricte État Réel (Umpire) vs État Perçu (Blue/Red).
- **Suivi d'avancement** : Ne jamais modifier manuellement le pourcentage d'avancement ; toujours cocher les sous-tâches réelles dans `docs/ROADMAP.md` puis exécuter `python scripts/update_progress.py`.
- **Développement** : Progression séquentielle stricte, une seule étape active à la fois, validation par preuves, zéro développement prématuré d'étapes aval.

## Prochaine étape
Finalisation de la validation de l'**ÉTAPE 01** après revue contradictoire du rapport d'audit par le client.
**ÉTAPE 02 — Architecture fonctionnelle et technique** (Statut : `PLANNED`. Ne pas démarrer).
