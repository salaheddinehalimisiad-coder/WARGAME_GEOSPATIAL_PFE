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
- **SIG** : Global Mapper est le seul outil SIG du projet. QGIS est totalement exclu.
- **Unités** : Niveau minimal d'agrégation fixé au bataillon.
- **Équipements** : Capacités abstraites uniquement (aucune arme réelle détaillée).
- **Incertitude** : Séparation stricte État Réel (Umpire) vs État Perçu (Blue/Red).
- **Git & CI/CD** : Travail sur branches dédiées par phase, push systématique après chaque validation avec preuves, passage obligatoire de la CI (zéro régression).
- **Développement** : Progression séquentielle stricte, validation par preuves, pas de développement prématuré.

## Prochaine étape
Phase 0 — Cadrage, initialisation de l'environnement, structure propre et premier push vers le dépôt distant.

## Historique
- Adoption du Master Prompt v1.0 complet et mise en conformité des règles agent et de la checklist de référence.
- Mise en place du workflow Git, du `.gitignore`, du guide de branches par phase, de la CI/CD GitHub Actions et configuration du remote GitHub.
