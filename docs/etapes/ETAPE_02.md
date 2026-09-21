# ÉTAPE 02 — Architecture fonctionnelle et technique

**Statut :** `IN_PROGRESS` (1 / 9 sous-tâches terminées)<br>
**Date d'ouverture :** 2026-09-21<br>
**Branche Git :** `phase/02-architecture`<br>
**Sous-tâches prévues :** 9 (T02-01 : 4 sous-tâches, T02-02 : 5 sous-tâches)

---

## Objectif
Concevoir l'architecture modulaire globale du système, définir les contrats d'interface, la séparation stricte des responsabilités et structurer les spécifications techniques.

## Base de référence et artefacts existants
- Les 6 diagrammes vectoriels SVG d'architecture déjà présents dans `docs/assets/architecture/` (et archivés dans `docs/assets/architecture/source/`) constituent la base de référence validée de l'étape et ne doivent pas être recréés :
  1. `architecture_globale.svg`
  2. `architecture_pipeline_sig.svg`
  3. `architecture_donnees.svg`
  4. `architecture_flux_simulation.svg`
  5. `architecture_blue_red_umpire.svg`
  6. `architecture_technique.svg`

## État d'avancement
- **`P02-T01-S01` [PASS]** : Définition architecturale du découpage en modules C++20 (`core`, `terrain`, `units`, `sim`, `api`) validée formellement. Responsabilités, graphe acyclique de dépendances (DAG), dépendances interdites, propriété des données (`terrain` pour le terrain, `sim` pour le WorldState), séparation hermétique Réel/Perçu et rôles Blue/Red/Umpire formalisés dans `docs/ARCHITECTURE.md`.
