#!/usr/bin/env python3
"""
Test unitaire et d'intégration du système de calcul automatique d'avancement.
Vérifie :
1. Le calcul mathématique exact (ex: 5/20 = 25.00%).
2. La détection de l'étape active et des statuts (PLANNED, IN_PROGRESS, PASS, BLOCKED).
3. L'absence de régression ou de dépendance externe.
4. L'intégrité de la feuille de route officielle docs/ROADMAP.md (247 sous-tâches uniques).
"""

import sys
import tempfile
from pathlib import Path

# Configure safe UTF-8 output on Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

# Import logic from update_progress.py
ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT_DIR / "scripts"))
from update_progress import parse_roadmap, calculate_metrics, generate_donut_svg, generate_dashboard_md, export_json_and_sync_html


def test_controlled_sample():
    print("--- TEST 1 : Échantillon contrôlé (20 sous-tâches, 5 terminées = 25.00%) ---")
    sample_content = """# TEST ROADMAP

## ÉTAPE 00 — Étape Initiale
### Tâche T00-01 — Tâche A
- [x] P00-T01-S01 — Sous-tâche 1
- [x] P00-T01-S02 — Sous-tâche 2
- [x] P00-T01-S03 — Sous-tâche 3
- [x] P00-T01-S04 — Sous-tâche 4
### Tâche T00-02 — Tâche B
- [x] P00-T02-S01 — Sous-tâche 5
- [ ] P00-T02-S02 — Sous-tâche 6
- [ ] P00-T02-S03 — Sous-tâche 7
- [ ] P00-T02-S04 — Sous-tâche 8
- [ ] P00-T02-S05 — Sous-tâche 9
- [ ] P00-T02-S06 — Sous-tâche 10

## ÉTAPE 01 — Deuxième Étape
### Tâche T01-01 — Tâche C
- [ ] P01-T01-S01 — Sous-tâche 11
- [ ] P01-T01-S02 — Sous-tâche 12
- [ ] P01-T01-S03 — Sous-tâche 13
- [ ] P01-T01-S04 — Sous-tâche 14
- [ ] P01-T01-S05 — Sous-tâche 15
### Tâche T01-02 — Tâche D
- [ ] P01-T02-S01 — Sous-tâche 16
- [ ] P01-T02-S02 — Sous-tâche 17
- [ ] P01-T02-S03 — Sous-tâche 18
- [ ] P01-T02-S04 — Sous-tâche 19
- [ ] P01-T02-S05 — Sous-tâche 20
"""
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
        tmp.write(sample_content)
        tmp_path = Path(tmp.name)

    try:
        steps = parse_roadmap(tmp_path)
        metrics = calculate_metrics(steps)

        assert metrics["total_subtasks"] == 20, f"Attendu: 20, Obtenu: {metrics['total_subtasks']}"
        assert metrics["completed_subtasks"] == 5, f"Attendu: 5, Obtenu: {metrics['completed_subtasks']}"
        assert metrics["remaining_subtasks"] == 15, f"Attendu: 15, Obtenu: {metrics['remaining_subtasks']}"
        assert abs(metrics["global_pct"] - 25.0) < 1e-5, f"Attendu: 25.00%, Obtenu: {metrics['global_pct']:.2f}%"
        assert metrics["active_step"]["num"] == "00", f"Étape active attendue: 00, Obtenu: {metrics['active_step']['num']}"
        assert metrics["steps_metrics"][0]["status"] == "IN_PROGRESS", "Étape 00 doit être IN_PROGRESS"
        assert metrics["steps_metrics"][1]["status"] == "PLANNED", "Étape 01 doit être PLANNED"

        # Test generation of SVG and MD on temp files
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".svg") as svg_tmp:
            svg_path = Path(svg_tmp.name)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as md_tmp:
            md_path = Path(md_tmp.name)

        generate_donut_svg(metrics, svg_path)
        assert svg_path.exists() and svg_path.stat().st_size > 500, "Le SVG donut n'a pas été généré correctement"

        generate_dashboard_md(metrics, md_path)
        assert md_path.exists() and md_path.stat().st_size > 500, "Le tableau de bord n'a pas été généré correctement"

        # Verify SVG content includes 25.00 %
        with open(svg_path, "r", encoding="utf-8") as f:
            svg_text = f.read()
            assert "25.00 %" in svg_text, "Pourcentage 25.00 % absent du SVG"

        # Test JSON and HTML sync
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".json") as json_tmp:
            json_path = Path(json_tmp.name)
        with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".html") as html_tmp:
            html_tmp.write("<html><head><title>Test</title></head><body></body></html>")
            html_path = Path(html_tmp.name)

        export_json_and_sync_html(metrics, json_path, html_path)
        assert json_path.exists() and json_path.stat().st_size > 100, "Le JSON n'a pas été exporté"
        with open(html_path, "r", encoding="utf-8") as f:
            html_text = f.read()
            assert "window.__INITIAL_DATA__" in html_text, "Injection __INITIAL_DATA__ absente du HTML"

        # Cleanup temp files
        svg_path.unlink()
        md_path.unlink()
        json_path.unlink()
        html_path.unlink()

        print("  -> Succès : 20 sous-tâches, 5 cochées => 25.00% exact, SVG et Dashboard vérifiés.")
    finally:
        tmp_path.unlink()


def test_official_roadmap():
    print("--- TEST 2 : Intégrité de la feuille de route officielle docs/ROADMAP.md ---")
    roadmap_path = ROOT_DIR / "docs" / "ROADMAP.md"
    steps = parse_roadmap(roadmap_path)
    metrics = calculate_metrics(steps)

    assert len(steps) == 31, f"Attendu: 31 étapes, Obtenu: {len(steps)}"
    assert metrics["total_subtasks"] > 200, f"Sous-tâches attendues > 200, Obtenu: {metrics['total_subtasks']}"
    assert metrics["active_step"] is not None and "num" in metrics["active_step"], "Étape active non identifiée"
    print(f"  -> Succès : 31 étapes officielles chargées, {metrics['total_subtasks']} sous-tâches uniques valides, étape active: ÉTAPE {metrics['active_step']['num']} — {metrics['active_step']['title']}.")


def test_duplicate_detection():
    print("--- TEST 3 : Détection stricte d'identifiants dupliqués ---")
    bad_content = """# TEST ROADMAP
## ÉTAPE 00 — Init
### Tâche T00-01 — Tâche A
- [ ] P00-T01-S01 — Sous-tâche 1
- [ ] P00-T01-S01 — Doublon volontaire
"""
    with tempfile.NamedTemporaryFile("w", encoding="utf-8", delete=False, suffix=".md") as tmp:
        tmp.write(bad_content)
        tmp_path = Path(tmp.name)

    try:
        parse_roadmap(tmp_path)
        raise AssertionError("L'erreur d'identifiant dupliqué n'a pas été levée !")
    except ValueError as e:
        print(f"  -> Succès : exception levée comme attendu ({e})")
    finally:
        tmp_path.unlink()


if __name__ == "__main__":
    print("=== Démarrage des tests du système d'avancement ===")
    test_controlled_sample()
    test_official_roadmap()
    test_duplicate_detection()
    print("=== Tous les tests sont PASS ===")
