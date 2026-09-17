#!/usr/bin/env python3
"""
Script de calcul automatique de l'avancement du projet WARGAME_GEOSPATIAL_PFE.
Source de vérité : docs/ROADMAP.md
Génère :
  - docs/ETAT_AVANCEMENT.md
  - docs/assets/progress/progress_donut.svg

Usage :
  python scripts/update_progress.py
"""

import sys
import re
import math
from pathlib import Path
from datetime import datetime

# Configure safe UTF-8 output on Windows
if sys.platform == "win32" and hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except Exception:
        pass

ROOT_DIR = Path(__file__).resolve().parent.parent
ROADMAP_FILE = ROOT_DIR / "docs" / "ROADMAP.md"
DASHBOARD_FILE = ROOT_DIR / "docs" / "ETAT_AVANCEMENT.md"
DONUT_SVG_FILE = ROOT_DIR / "docs" / "assets" / "progress" / "progress_donut.svg"

RE_STEP = re.compile(r"^##\s+ÉTAPE\s+(\d{2})\s+[—\-]\s+(.+)$")
RE_TASK = re.compile(r"^###\s+Tâche\s+(T\d{2}-\d{2})\s+[—\-]\s+(.+)$")
RE_SUBTASK = re.compile(r"^-\s+\[([ xX])\]\s+(P\d{2}-T\d{2}-S\d{2})\s+[—\-]\s+(.+)$")
RE_BLOCKED_STEP = re.compile(r"\[BLOCKED\]", re.IGNORECASE)


def parse_roadmap(roadmap_path: Path):
    if not roadmap_path.exists():
        raise FileNotFoundError(f"Fichier introuvable : {roadmap_path}")

    with open(roadmap_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    steps = []
    current_step = None
    current_task = None
    all_subtask_ids = set()
    duplicate_ids = []

    for line_num, raw_line in enumerate(lines, start=1):
        line = raw_line.strip()

        # Check step
        m_step = RE_STEP.match(line)
        if m_step:
            step_num = m_step.group(1)
            step_title = m_step.group(2).strip()
            is_blocked = bool(RE_BLOCKED_STEP.search(step_title))
            current_step = {
                "num": step_num,
                "title": step_title,
                "is_blocked": is_blocked,
                "tasks": [],
                "subtasks": []
            }
            steps.append(current_step)
            current_task = None
            continue

        # Check task
        m_task = RE_TASK.match(line)
        if m_task and current_step:
            task_id = m_task.group(1)
            task_title = m_task.group(2).strip()
            current_task = {
                "id": task_id,
                "title": task_title,
                "subtasks": []
            }
            current_step["tasks"].append(current_task)
            continue

        # Check subtask
        m_sub = RE_SUBTASK.match(line)
        if m_sub and current_step:
            checked = m_sub.group(1).strip().lower() == "x"
            subtask_id = m_sub.group(2).strip()
            subtask_title = m_sub.group(3).strip()

            if subtask_id in all_subtask_ids:
                duplicate_ids.append((subtask_id, line_num))
            all_subtask_ids.add(subtask_id)

            sub_item = {
                "id": subtask_id,
                "title": subtask_title,
                "checked": checked,
                "line": line_num,
                "step_num": current_step["num"],
                "step_title": current_step["title"]
            }
            current_step["subtasks"].append(sub_item)
            if current_task:
                current_task["subtasks"].append(sub_item)
            continue

    if duplicate_ids:
        msg = f"Erreur critique : identifiants de sous-tâches dupliqués détectés : {duplicate_ids}"
        raise ValueError(msg)

    return steps


def calculate_metrics(steps):
    total_subtasks = 0
    completed_subtasks = 0
    completed_subtask_list = []
    pending_subtask_list = []

    steps_metrics = []
    active_step = None
    completed_steps_count = 0

    for step in steps:
        subtasks = step["subtasks"]
        s_total = len(subtasks)
        s_completed = sum(1 for s in subtasks if s["checked"])
        s_remaining = s_total - s_completed
        s_pct = (s_completed / s_total * 100.0) if s_total > 0 else 0.0

        for s in subtasks:
            if s["checked"]:
                completed_subtask_list.append(s)
            else:
                pending_subtask_list.append(s)

        total_subtasks += s_total
        completed_subtasks += s_completed

        # Status determination
        if step["is_blocked"]:
            status = "BLOCKED"
        elif s_total == 0:
            status = "PLANNED"
        elif s_completed == 0:
            status = "PLANNED"
        elif s_completed < s_total:
            status = "IN_PROGRESS"
        else:
            status = "PASS"
            completed_steps_count += 1

        step_data = {
            "num": step["num"],
            "title": step["title"],
            "total": s_total,
            "completed": s_completed,
            "remaining": s_remaining,
            "pct": s_pct,
            "status": status,
            "is_blocked": step["is_blocked"]
        }
        steps_metrics.append(step_data)

    # Determine single active step
    for step_data in steps_metrics:
        if step_data["status"] in ("IN_PROGRESS", "BLOCKED"):
            active_step = step_data
            break
    if not active_step:
        for step_data in steps_metrics:
            if step_data["status"] == "PLANNED":
                active_step = step_data
                break

    global_pct = (completed_subtasks / total_subtasks * 100.0) if total_subtasks > 0 else 0.0
    remaining_subtasks = total_subtasks - completed_subtasks
    total_steps = len(steps_metrics)
    remaining_steps = total_steps - completed_steps_count

    return {
        "total_subtasks": total_subtasks,
        "completed_subtasks": completed_subtasks,
        "remaining_subtasks": remaining_subtasks,
        "global_pct": global_pct,
        "total_steps": total_steps,
        "completed_steps_count": completed_steps_count,
        "remaining_steps": remaining_steps,
        "active_step": active_step,
        "steps_metrics": steps_metrics,
        "completed_subtask_list": completed_subtask_list,
        "pending_subtask_list": pending_subtask_list
    }


def generate_donut_svg(metrics, output_path: Path):
    pct = metrics["global_pct"]
    total = metrics["total_subtasks"]
    completed = metrics["completed_subtasks"]
    remaining = metrics["remaining_subtasks"]

    # Dimensions
    cx, cy = 200, 200
    radius = 130
    stroke_width = 32

    # Circumference
    circumference = 2 * math.pi * radius
    dash_completed = (pct / 100.0) * circumference
    dash_remaining = circumference - dash_completed

    # SVG construction
    svg_content = f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 400" width="680" height="400" style="background:#ffffff; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <filter id="card-shadow" x="-5%" y="-5%" width="110%" height="110%">
      <feDropShadow dx="0" dy="4" stdDeviation="8" flood-color="#0f172a" flood-opacity="0.06"/>
    </filter>
    <linearGradient id="progress-grad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#2563eb" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
  </defs>

  <!-- Background Card -->
  <rect x="10" y="10" width="660" height="380" rx="16" fill="#ffffff" stroke="#e2e8f0" stroke-width="1.5" filter="url(#card-shadow)" />

  <!-- Donut Ring Background (Remaining) -->
  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="#f1f5f9" stroke-width="{stroke_width}" />

  <!-- Donut Ring Progress (Completed) -->
  <circle cx="{cx}" cy="{cy}" r="{radius}" fill="none" stroke="url(#progress-grad)" stroke-width="{stroke_width}"
          stroke-dasharray="{circumference:.3f}"
          stroke-dashoffset="{circumference - dash_completed:.3f}"
          stroke-linecap="round"
          transform="rotate(-90 {cx} {cy})" />

  <!-- Center Text -->
  <text x="{cx}" y="{cy - 12}" text-anchor="middle" font-size="44" font-weight="800" fill="#0f172a">{pct:.2f} %</text>
  <text x="{cx}" y="{cy + 22}" text-anchor="middle" font-size="14" font-weight="600" fill="#64748b" letter-spacing="1">AVANCEMENT GLOBAL</text>
  <text x="{cx}" y="{cy + 42}" text-anchor="middle" font-size="12" font-weight="500" fill="#94a3b8">{completed} / {total} sous-tâches</text>

  <!-- Right Panel Info -->
  <g transform="translate(400, 70)">
    <!-- Header -->
    <text x="0" y="0" font-size="18" font-weight="700" fill="#0f172a">Synthèse du Projet</text>
    <text x="0" y="20" font-size="12" font-weight="500" fill="#64748b">Wargame Géospatial PFE — Promotion 2026-2027</text>

    <!-- Stat 1: Completed -->
    <g transform="translate(0, 50)">
      <circle cx="10" cy="10" r="7" fill="#2563eb" />
      <text x="26" y="14" font-size="14" font-weight="600" fill="#1e293b">Sous-tâches terminées</text>
      <text x="230" y="14" font-size="15" font-weight="700" fill="#2563eb" text-anchor="end">{completed}</text>
      <rect x="0" y="24" width="230" height="1" fill="#f1f5f9" />
    </g>

    <!-- Stat 2: Remaining -->
    <g transform="translate(0, 85)">
      <circle cx="10" cy="10" r="7" fill="#cbd5e1" />
      <text x="26" y="14" font-size="14" font-weight="600" fill="#1e293b">Sous-tâches restantes</text>
      <text x="230" y="14" font-size="15" font-weight="700" fill="#64748b" text-anchor="end">{remaining}</text>
      <rect x="0" y="24" width="230" height="1" fill="#f1f5f9" />
    </g>

    <!-- Stat 3: Total -->
    <g transform="translate(0, 120)">
      <circle cx="10" cy="10" r="7" fill="#0f172a" />
      <text x="26" y="14" font-size="14" font-weight="600" fill="#1e293b">Total des sous-tâches</text>
      <text x="230" y="14" font-size="15" font-weight="700" fill="#0f172a" text-anchor="end">{total}</text>
      <rect x="0" y="24" width="230" height="1" fill="#f1f5f9" />
    </g>

    <!-- Stat 4: Active Step -->
    <g transform="translate(0, 160)">
      <rect x="0" y="0" width="230" height="58" rx="8" fill="#f8fafc" stroke="#e2e8f0" stroke-width="1" />
      <text x="12" y="20" font-size="11" font-weight="700" fill="#3b82f6" letter-spacing="0.5">ÉTAPE ACTIVE</text>
      <text x="12" y="42" font-size="13" font-weight="700" fill="#0f172a">ÉTAPE {metrics['active_step']['num']} — {metrics['active_step']['title'][:20] + ('...' if len(metrics['active_step']['title']) > 20 else '')}</text>
    </g>
  </g>
</svg>
"""
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(svg_content.strip() + "\n")


def generate_dashboard_md(metrics, output_path: Path):
    pct_formatted = f"{metrics['global_pct']:.2f} %".replace(".", ",")
    active_step = metrics["active_step"]

    # Recent completed (max 5)
    recent_completed = metrics["completed_subtask_list"][-5:] if metrics["completed_subtask_list"] else []
    
    # Upcoming tasks (next 5 pending from active step or globally)
    upcoming_tasks = [s for s in metrics["pending_subtask_list"] if s["step_num"] == active_step["num"]][:5]
    if not upcoming_tasks:
        upcoming_tasks = metrics["pending_subtask_list"][:5]

    # Blocked tasks
    blocked_steps = [s for s in metrics["steps_metrics"] if s["status"] == "BLOCKED"]

    # Table rows
    table_rows = []
    for s in metrics["steps_metrics"]:
        status_badge = f"`{s['status']}`"
        pct_str = f"{s['pct']:.2f} %".replace(".", ",")
        table_rows.append(f"| ÉTAPE {s['num']} — {s['title']} | {s['total']} | {s['completed']} | {s['remaining']} | {pct_str} | {status_badge} |")

    table_md = "\n".join(table_rows)

    completed_md = "\n".join([f"- [x] `{s['id']}` — {s['title']} *(ÉTAPE {s['step_num']})*" for s in recent_completed]) if recent_completed else "*Aucune sous-tâche encore terminée.*"
    upcoming_md = "\n".join([f"- [ ] `{s['id']}` — {s['title']} *(ÉTAPE {s['step_num']})*" for s in upcoming_tasks]) if upcoming_tasks else "*Toutes les tâches sont terminées.*"

    blocked_md = ""
    if blocked_steps:
        blocked_md = "\n".join([f"- **ÉTAPE {s['num']} — {s['title']}** : Étape bloquée." for s in blocked_steps])
    else:
        blocked_md = "*Aucune tâche bloquée actuellement.*"

    md_content = f"""# ÉTAT D’AVANCEMENT DU PROJET

**Dernière mise à jour automatique :** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}  
**Source de vérité :** [`docs/ROADMAP.md`](file:///c:/Users/salah/Desktop/WARGAME_GEOSPATIAL_PFE/docs/ROADMAP.md)  
**Outil de synchronisation :** `python scripts/update_progress.py`

---

## Progression globale

![Graphique d'avancement](assets/progress/progress_donut.svg)

<div align="center">

# **{pct_formatted}**
### Avancement réel calculé sur les sous-tâches terminales

</div>

### Statistiques consolidées

| Indicateur | Valeur |
|---|---:|
| **Sous-tâches totales** | {metrics['total_subtasks']} |
| **Sous-tâches terminées** | {metrics['completed_subtasks']} |
| **Sous-tâches restantes** | {metrics['remaining_subtasks']} |
| **Pourcentage global** | **{pct_formatted}** |
| **Étapes terminées (PASS)** | {metrics['completed_steps_count']} / {metrics['total_steps']} |
| **Étape active** | **ÉTAPE {active_step['num']} — {active_step['title']}** |
| **Étapes restantes** | {metrics['remaining_steps']} |

---

## Étape active

**ÉTAPE {active_step['num']} — {active_step['title']}**
- **Statut :** `{active_step['status']}`
- **Progression de l'étape :** {active_step['completed']} / {active_step['total']} sous-tâches ({active_step['pct']:.2f} %)
- **Règle de l'étape active unique :** Cette étape doit être intégralement validée avec preuves avant tout engagement sur l'étape suivante.

---

## Dernières tâches terminées

{completed_md}

---

## Prochaines tâches

{upcoming_md}

---

## Tâches bloquées

{blocked_md}

---

## Avancement détaillé par étape

| Étape | Total | Terminées | Restantes | Avancement | Statut |
|:---|---:|---:|---:|---:|:---:|
{table_md}

---

*Ce tableau de bord est généré automatiquement. Ne pas modifier manuellement. Pour mettre à jour l'avancement, cocher les cases dans `docs/ROADMAP.md` puis exécuter `python scripts/update_progress.py`.*
"""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(md_content.strip() + "\n")


def main():
    print("=== Mise à jour de l'avancement du projet ===")
    print(f"Lecture de la feuille de route : {ROADMAP_FILE}")
    steps = parse_roadmap(ROADMAP_FILE)
    print(f"Nombre d'étapes identifiées : {len(steps)}")

    metrics = calculate_metrics(steps)
    print(f"Total sous-tâches : {metrics['total_subtasks']}")
    print(f"Sous-tâches cochées : {metrics['completed_subtasks']}")
    print(f"Sous-tâches restantes : {metrics['remaining_subtasks']}")
    print(f"Avancement global : {metrics['global_pct']:.2f} %")
    print(f"Étape active : ÉTAPE {metrics['active_step']['num']} — {metrics['active_step']['title']}")

    print(f"Génération du graphique donut SVG : {DONUT_SVG_FILE}")
    generate_donut_svg(metrics, DONUT_SVG_FILE)

    print(f"Génération du tableau de bord : {DASHBOARD_FILE}")
    generate_dashboard_md(metrics, DASHBOARD_FILE)

    print("=== Mise à jour terminée avec succès ===")


if __name__ == "__main__":
    main()
