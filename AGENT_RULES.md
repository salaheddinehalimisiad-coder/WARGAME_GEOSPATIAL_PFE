# AGENT RULES — WARGAME GÉOSPATIAL PFE

1. **Référence unique** : Le cahier des charges officiel (`Cahier_des_charges_PFE_Wargame_geospatial.docx` — Version 1.0) est la référence absolue.
2. **SIG & ETL** : Global Mapper est l'outil SIG principal de référence du projet. Les outils open source QGIS, GDAL et PROJ (recommandés par le cahier des charges) sont mobilisés en complément selon les nécessités techniques (conversions, reprojections, scripts ETL).
3. **Hiérarchie des sources** : Cahier des charges > Décisions validées > Documentation > Code réel > Propositions.
4. **Documents persistants** : Lire `MASTER_PROMPT.md`, `AGENT_RULES.md`, `PROJECT_PROMPT.md`, `PROJECT_MEMORY.md`, `CHANGELOG.md` et les documents sous `docs/` avant toute tâche.
5. **Comprendre avant de coder** : Inspecter le code et les fichiers réels avant toute modification ; analyser l'architecture en amont.
6. **Progression séquentielle** : Travailler par petits lots vérifiables. Pas de "big bang", pas de développement prématuré de couches aval.
7. **Validation par preuves** : Ne jamais déclarer une étape terminée sans résultats testables et preuves concrètes.
8. **Préservation** : Protéger les composants déjà validés et toutes les données sources. Ne pas casser les contrats existants sans décision explicite.
9. **Séparation stricte des couches** : Ne jamais mélanger prétraitement SIG, modèle de domaine, moteur de simulation et IHM.
10. **Incertitude** : Distinguer strictement l'état réel (arbitre) de l'état perçu (Blue/Red).
11. **Abstraction opérationnelle** : Le niveau minimal d'agrégation est le bataillon. Ne jamais reproduire de caractéristiques techniques d'armes réelles (utiliser des paramètres abstraits : capacité, portée relative, mobilité, etc.).
12. **Gestion de version Git & Branches** :
    - Travailler sur des branches isolées par phase/étape (`phase/<id>-<nom>`).
    - Ne fusionner sur `develop` / `main` qu'après validation PASS.
    - Utiliser les Conventional Commits (`feat:`, `fix:`, `docs:`, `test:`, `refactor:`, `chore:`).
13. **Push systématique & CI/CD** :
    - Pousser (`git push`) systématiquement vers le dépôt GitHub distant dès qu'une étape est validée.
    - S'assurer que le pipeline CI/CD GitHub Actions passe avec succès (zéro régression, linter, tests d'intégration).
14. **Traçabilité** : Documenter les décisions techniques structurantes et consigner les modifications dans `PROJECT_MEMORY.md` et `CHANGELOG.md`.
15. **Validation utilisateur** : Ne pas passer à l'étape suivante sans validation explicite du responsable du projet.
16. **Principe « Autonomous First — CommandView Ready »** : Le prototype doit fonctionner de façon 100% autonome pour le PFE tout en préparant des interfaces ouvertes (REST/OpenAPI, WebSocket, événements, données spatiales) compatibles avec une intégration ultérieure dans CommandView (C4ISR).

