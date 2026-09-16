# WORKFLOW GIT, GESTION DES BRANCHES & PIPELINE CI/CD

Ce document décrit la gouvernance Git, le cycle de vie des branches par phase, les règles de commit, le push systématique et le fonctionnement du pipeline CI/CD pour le projet **Wargame Géospatial PFE**.

---

## 1. Dépôt distant officiel

- **URL du dépôt** : `https://github.com/salaheddinehalimisiad-coder/WARGAME_GEOSPATIAL_PFE`
- **Protocole recommandé** : HTTPS ou SSH selon les identifiants configurés.

---

## 2. Structure et Arborescence des Branches

Le modèle de branches suit un GitFlow adapté à la progression séquentielle par phases :

```text
main (stable / livrables officiels)
 │
 └── develop (intégration continue)
      │
      ├── phase/00-initialisation-environnement
      ├── phase/01-analyse-et-architecture
      ├── phase/02-sig-global-mapper
      ├── phase/03-qa-donnees-sig
      ├── phase/04-grille-hexagonale
      ├── phase/05-postgis
      └── ...
```

### Rôles des branches :
1. **`main`** :
   - Branche de référence ultime.
   - Ne contient que des versions certifiées fonctionnelles et documentées.
   - Toute fusion dans `main` est étiquetée avec un Tag sémantique (`v0.1.0`, `v1.0.0`, etc.).

2. **`develop`** :
   - Branche d'intégration globale.
   - Reçoit les fusions des branches de phases une fois que celles-ci sont validées à 100% (PASS).

3. **Branches de Phase (`phase/<num>-<nom>`)** :
   - Une branche dédiée par phase de la roadmap.
   - Permet d'isoler le travail en cours sans perturber l'intégration.
   - Nommage normalisé :
     - `phase/00-init`
     - `phase/01-architecture`
     - `phase/02-sig-global-mapper`
     - `phase/03-qa-sig`
     - `phase/04-grille-hexagonale`
     - etc.

---

## 3. Convention de Commits & Push Systématique

### Format des commits (Conventional Commits)
Chaque commit doit être atomique, précis et suivre la nomenclature :
- `feat(<portée>)`: Ajout d'une fonctionnalité métier.
- `fix(<portée>)`: Correction d'un bug ou d'une anomalie.
- `docs(<portée>)`: Ajout ou modification de documentation (spécifications, ADR, guides).
- `test(<portée>)`: Ajout ou ajustement de tests unitaires ou d'intégration.
- `chore(<portée>)`: Tâches de maintenance, outillage, configuration CI/CD ou Git.
- `refactor(<portée>)`: Modification interne sans changement fonctionnel.

### Règle du Push Systématique
- À chaque fin de tâche ou d'étape validée par des preuves :
  1. Les tests locaux sont exécutés.
  2. Les fichiers de suivi (`PROJECT_MEMORY.md`, `CHANGELOG.md`) sont mis à jour.
  3. Le commit est créé.
  4. La commande `git push` est exécutée immédiatement vers la branche distante.
- **Bénéfice** : Traçabilité temps réel, sauvegarde distante permanente et déclenchement instantané de la CI.

---

## 4. Pipeline CI/CD (GitHub Actions)

Le pipeline d'intégration continue est défini dans `.github/workflows/ci.yml`.

### Déclencheurs :
- Tout `push` sur les branches `main`, `develop`, et `phase/**`.
- Toute `pull_request` ciblant `main` ou `develop`.

### Étapes automatisées de la CI :
1. **Contrôle d'intégrité & Conformité** :
   - Vérification de la présence des documents maîtres (`MASTER_PROMPT.md`, `AGENT_RULES.md`, etc.).
   - Vérification de l'exclusion stricte de logiciels non autorisés (ex: contrôle automatisé de non-présence de QGIS dans le workflow).
2. **Linting & Validations syntaxiques** :
   - Analyse Markdown et syntaxe des scripts.
3. **Compilation et Tests unitaires & intégration** (progressifs selon les phases) :
   - Tests C++20 via GoogleTest.
   - Tests d'intégration des scripts de validation de couches SIG.
   - Tests de schémas PostGIS et requêtes spatiales.
4. **Statut de validation** :
   - Tout échec de test ou non-conformité bloque l'étape et nécessite correction immédiate avant toute fusion.
