# REFERENCE CHECKLIST DU PROJET

Ce document définit les critères d'intégrité, de conformité et de validation formelle applicables à chaque étape du projet **WARGAME GÉOSPATIAL PFE**.

---

## 1. Règles d'or du projet

- [ ] Conformité stricte avec le cahier des charges officiel (`Cahier_des_charges_PFE_Wargame_geospatial.docx` — Version 1.0).
- [ ] Règle SIG absolue : **Global Mapper** est l'unique outil SIG du workflow courant (aucun SIG concurrent actif).
- [ ] Échelon minimal fixé au **bataillon** et maintien d'une abstraction totale des matériels (aucune arme réelle détaillée).
- [ ] Respect absolu de la séparation étanche **État Réel (Umpire)** vs **État Perçu (Blue / Red)**.
- [ ] Application du principe directeur **« Autonomous First — CommandView Ready »**.
- [ ] Progression séquentielle stricte : une seule étape active à la fois, passage à l'étape suivante conditionné à une validation avec preuves.
- [ ] Gouvernance Git : travail sur branches isolées par phase (`phase/XX-*`), commits sémantiques et push systématique après validation.

---

## 2. Check-list de mise à niveau structurelle

### Documentation
- [x] Master Prompt cohérent (Version 1.0 alignée sur le cahier des charges)
- [x] Roadmap détaillée (`docs/ROADMAP.md` exhaustif sur 31 étapes)
- [x] État d’avancement créé (`docs/ETAT_AVANCEMENT.md`)
- [x] Calcul automatique opérationnel (`scripts/update_progress.py`)
- [x] Donut généré (`docs/assets/progress/progress_donut.svg`)
- [x] Architecture visuelle générée (6 diagrammes SVG professionnels)
- [x] Diagrammes intégrés dans `docs/ARCHITECTURE.md` (zéro schéma ASCII)
- [x] Cohérence documentaire vérifiée sur l'ensemble des documents maîtres

### Roadmap
- [x] Toutes les 31 étapes présentes (ÉTAPE 00 à ÉTAPE 30)
- [x] Tâches détaillées avec objectifs et descriptions
- [x] Sous-tâches détaillées avec actions concrètes et vérifiables (zéro formule vague)
- [x] Identifiants uniques au format normalisé `PXX-TYY-SZZ`
- [x] Cases à cocher standard Markdown (`- [ ]` / `- [x]`)
- [x] Critères d’acceptation formels pour chaque étape
- [x] Livrables identifiés avec chemins d'accès prévisionnels
- [x] Tests unitaires, d'intégration ou de validation spécifiés

### Suivi
- [x] Calcul du pourcentage automatique basé sur les sous-tâches feuilles
- [x] Avancement par étape avec taux de complétion et statuts normalisés
- [x] Étape active clairement identifiée (`ÉTAPE 00 — Initialisation du projet`)
- [x] Tâches bloquées surveillées
- [x] Tâches terminées traçables
- [x] Tâches restantes quantifiées

### Architecture
- [x] Architecture globale vectorielle (`architecture_globale.svg`)
- [x] Pipeline SIG vectoriel (`architecture_pipeline_sig.svg`)
- [x] Modèle de données relationnel vectoriel (`architecture_donnees.svg`)
- [x] Flux de simulation et boucle OODA vectoriel (`architecture_flux_simulation.svg`)
- [x] Cloisonnement Blue / Red / Umpire vectoriel (`architecture_blue_red_umpire.svg`)
- [x] Architecture technique et déploiement vectoriel (`architecture_technique.svg`)
- [x] Format vectoriel SVG de haute résolution
- [x] Fond blanc professionnel (`#ffffff`) adapté à l'écran, l'impression et la soutenance
- [x] Sources modifiables conservées dans `docs/assets/architecture/source/`

---

## 3. Procédure pour chaque étape de la roadmap

Avant d'engager une nouvelle étape :
1. [ ] Vérifier que l'étape précédente est formellement déclarée `PASS`.
2. [ ] Définir les objectifs, entrées et sorties précises.
3. [ ] Créer la branche Git dédiée `phase/XX-<nom>`.
4. [ ] Ne commencer aucun développement de composant aval prématuré.
5. [ ] Exécuter les tests locaux et recueillir les éléments de preuve tangibles.
6. [ ] Cocher les sous-tâches réalisées dans `docs/ROADMAP.md`.
7. [ ] Exécuter `python scripts/update_progress.py` pour synchroniser le tableau de bord et le donut.
8. [ ] Mettre à jour `PROJECT_MEMORY.md` et `CHANGELOG.md`.
9. [ ] S'arrêter et attendre la validation explicite du responsable avant de fusionner et passer à l'étape suivante.
