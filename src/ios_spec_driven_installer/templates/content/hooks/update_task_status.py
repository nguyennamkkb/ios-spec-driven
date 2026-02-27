#!/usr/bin/env python3
"""
Hook script to keep task execution context aligned with changed files.

Behavior:
- Detect changed Swift file path from tool input.
- Locate related spec folder.
- Parse tasks.md Task Registry and find matching tasks by file path.
- If exactly one matching task is pending, auto-mark it in_progress.
- Print concise execution hints.
"""

import json
import re
import sys
from pathlib import Path
from typing import Dict, List


def find_related_spec(file_path: str) -> Path | None:
    specs_dir = Path("{{IDE_CONFIG_DIR}}specs")
    if not specs_dir.exists():
        return None

    path_parts = [p.lower() for p in Path(file_path).parts]
    for spec_folder in specs_dir.iterdir():
        if not spec_folder.is_dir():
            continue
        slug = spec_folder.name.lower()
        if any(slug in p or p in slug for p in path_parts if len(p) > 2):
            return spec_folder
    return None


def parse_task_registry(tasks_md: str) -> List[Dict[str, str]]:
    # | ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
    pattern = re.compile(
        r"^\|\s*(\d+(?:\.\d+)+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*"
        r"([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|$",
        re.MULTILINE,
    )

    rows: List[Dict[str, str]] = []
    for m in pattern.finditer(tasks_md):
        rows.append(
            {
                "id": m.group(1).strip(),
                "title": m.group(2).strip(),
                "type": m.group(3).strip().lower(),
                "status": m.group(4).strip().lower(),
                "refs_ac": m.group(5).strip(),
                "refs_design": m.group(6).strip(),
                "files": m.group(7).strip(),
                "checkpoint": m.group(8).strip(),
            }
        )
    return rows


def file_matches_row(changed_file: str, files_cell: str) -> bool:
    targets = [t.strip().strip("`") for t in files_cell.split(",") if t.strip()]
    if not targets:
        return False
    changed = changed_file.replace("\\", "/")
    for target in targets:
        normalized = target.replace("\\", "/")
        if changed.endswith(normalized) or normalized in changed:
            return True
    return False


def update_registry_status(tasks_md: str, task_id: str, new_status: str) -> str:
    # Update only the Task Registry row status cell.
    row_pattern = re.compile(
        rf"^(\|\s*{re.escape(task_id)}\s*\|\s*[^|]+\|\s*[^|]+\|\s*)([^|]+)(\|.*)$",
        re.MULTILINE,
    )
    return row_pattern.sub(rf"\1 {new_status} \3", tasks_md, count=1)


def main() -> None:
    try:
        payload = json.load(sys.stdin)
        changed_path = payload.get("tool_input", {}).get("file_path", "")
        if not changed_path or not changed_path.endswith(".swift"):
            return

        if "{{IDE_CONFIG_DIR}}specs" in changed_path:
            return

        spec_folder = find_related_spec(changed_path)
        if not spec_folder:
            return

        tasks_file = spec_folder / "tasks.md"
        if not tasks_file.exists():
            return

        content = tasks_file.read_text()
        rows = parse_task_registry(content)
        if not rows:
            return

        matched = [r for r in rows if file_matches_row(changed_path, r["files"])]
        if not matched:
            return

        print(f"\n📋 Spec: {spec_folder.name}")
        print(f"📝 File changed: {changed_path}")
        print("🎯 Matched tasks:")
        for row in matched[:5]:
            print(f"   - [{row['id']}] {row['title']} ({row['status']})")

        pending = [r for r in matched if r["status"] == "pending"]
        if len(pending) == 1:
            row = pending[0]
            updated = update_registry_status(content, row["id"], "in_progress")
            if updated != content:
                tasks_file.write_text(updated)
                print(f"\n🔄 Auto-updated task {row['id']} -> in_progress")

        print("💡 Keep task status and traceability rows in sync after completion.")

    except Exception:
        # Silent fail by design; never block user editing flow.
        return


if __name__ == "__main__":
    main()
