# PROJECT MEMORY

## État actuel
Alignement complet du projet :
- Master Prompt v1.0 issu du cahier des charges officiel Version 1.0 (PFE 2026–2027).
- Gouvernance Git initialisée : `main` (production/stable), `develop` (intégration), branches isolées par phases (`phase/<id>-<nom>`).
- Remote officiel configuré : `https://github.com/salaheddinehalimisiad-coder/WARGAME_GEOSPATIAL_PFE.git`.
- Pipeline CI/CD GitHub Actions opérationnel (`.github/workflows/ci.yml`).

## Référence officielle
`Cahier_des_charges_PFE_Wargame_geospatial.docx` — Version 1.0.

## Règles maîtresses
- **SIG & ETL** : Global Mapper est l'outil principal de référence pour la préparation SIG. Complété par la suite open source recommandée par le cahier des charges (QGIS, GDAL, PROJ) selon les nécessités techniques.
- **Principe d'intégration** : « Autonomous First — CommandView Ready » (PFE 100% autonome, architecture et APIs préparées pour une intégration ultérieure dans le C4ISR CommandView).
- **Unités** : Niveau minimal d'agrégation fixé au bataillon.
- **Équipements** : Capacités abstraites uniquement (aucune arme réelle détaillée).
- **Incertitude** : Séparation stricte État Réel (Umpire) vs État Perçu (Blue/Red).
- **Git & CI/CD** : Travail sur branches dédiées par phase, push systématique après chaque validation avec preuves, passage obligatoire de la CI (zéro régression).
- **Développement** : Progression séquentielle stricte, validation par preuves, pas de développement prématuré.

## Prochaine étape
ÉTAPE 00 — Initialisation du projet (dépôt, structure, documentation initiale, environnement, CI/CD).

## Historique
- Clarification et alignement : intégration du principe « Autonomous First — CommandView Ready » (Section 33 du CdC) et ouverture du pipeline SIG (Global Mapper principal + QGIS, GDAL, PROJ).
- Intégration du Master Prompt v1.0 officiel (62 sections).
- Mise en place du workflow Git, du `.gitignore`, du guide de branches par phase, de la CI/CD GitHub Actions et synchronisation avec GitHub.

