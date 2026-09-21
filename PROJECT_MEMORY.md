# PROJECT MEMORY

## État actuel du projet
**Étape validée :** ÉTAPE 01 — Analyse détaillée du cahier des charges (`PASS`, 7/7 sous-tâches terminées)<br>
**Étape active :** ÉTAPE 02 — Architecture fonctionnelle et technique (`IN_PROGRESS`, 0/9 sous-tâches terminées)<br>
**Progression globale :** 6,07 % (15 / 247 sous-tâches)<br>
**Étapes validées (PASS) :** 2 / 31 (ÉTAPE 00, ÉTAPE 01)<br>
**Branche active :** `phase/02-architecture` — **Ne pas fusionner avant validation.**

## Source de vérité

| Document | Rôle |
|:---|:---|
| `Cahier_des_charges_PFE_Wargame_geospatial.docx` v1.0 | Référence contractuelle absolue |
| `MASTER_PROMPT.md` | Règles maîtresses du projet |
| `docs/ROADMAP.md` | Progression par sous-tâches |
| `docs/ETAT_AVANCEMENT.md` | Tableau de bord (généré automatiquement) |
| `CHANGELOG.md` | Historique des changements significatifs |
| `docs/etapes/ETAPE_XX.md` | Notes légères par étape |

## Décisions techniques validées

1. **Global Mapper** = outil SIG/ETL du projet (choix interne, pas obligation contractuelle ; CdC Section 17 recommande QGIS à titre indicatif).
2. **Échelon minimal : bataillon** — aucune sous-entité individuelle représentée.
3. **Abstraction capacitaire totale** — zéro désignation d'armement ou caractéristique technique réelle.
4. **Séparation hermétique** : État Réel (Umpire/moteur) vs États Perçus Blue/Red — aucun client joueur n'accède à l'état réel.
5. **Critères d'acceptation officiels** : 9 critères textuels contractuels CdC Section 24 (`CRIT-01` à `CRIT-09`), validés contradictoirement sans exigence inventée ni altération.
6. **Principe architectural** : « Autonomous First — CommandView Ready » (CdC Section 16, 33).
7. **Déterminisme** via PRNG `std::mt19937_64` + seed de scénario — **Proposition [C] à confirmer en ÉTAPE 02**.

## Décisions encore ouvertes (à confirmer en ÉTAPE 02)
- Choix définitif du système de coordonnées hexagonales (axiales `(q,r)` vs H3).
- Confirmation du modèle de détail des structures de données C++.
- Confirmation de l'architecture de déploiement Docker Compose.

## Contraintes à respecter
- Jamais modifier manuellement `ETAT_AVANCEMENT.md` — toujours via `python scripts/update_progress.py`.
- Jamais démarrer une étape sans que la précédente soit `PASS`.
- Pas de données SIG brutes dans Git (`data/raw/*` ignoré).
- Pas de noms d'armes ou caractéristiques techniques réelles.
- Pas de fusion dans `main`/`develop` sans validation contradictoire.

## Politique documentaire (en vigueur depuis 2026-09-19)
- **Notes légères par étape** dans `docs/etapes/ETAPE_XX.md` (concis, pas de gros rapports).
- **Pas de rapports JSON automatiques** à chaque étape (sauf exception justifiée).
- **PROJECT_MEMORY.md** : mémoire durable, mise à jour en fin de chaque étape.
- **CHANGELOG.md** : changements significatifs et commits importants uniquement.
- **Rapport final** : construit uniquement en fin de projet à partir des sources accumulées.

## Fichiers à archiver (ne pas enrichir, ne pas supprimer)
- `docs/rapports/rapport_etape_01.md` / `.json`
- `docs/rapports/rapport_audit_source_etape_01.md` / `.json`
- `docs/rapports/rapport_audit_arborescence.json`
- `docs/rapport_mise_a_niveau_documentation.json` (doublon exact de `docs/rapports/rapport_mise_a_niveau_documentation.json`)

## Erreurs / pièges à ne pas reproduire
- Ne pas introduire d'exigences arbitraires (seuils de latence, FPS, nombres de tours) sans source dans le CdC.
- Ne pas présenter une proposition d'architecture interne comme une exigence contractuelle.
- Ne pas créer de nomenclature de critères d'acceptation sans base textuelle dans le CdC.
- Ne pas commencer une étape fonctionnelle pendant une phase documentaire/gouvernance.

## Travaux restant à faire
- ÉTAPE 02 : Architecture fonctionnelle et technique (`IN_PROGRESS`, 9 sous-tâches à auditer et concevoir).
