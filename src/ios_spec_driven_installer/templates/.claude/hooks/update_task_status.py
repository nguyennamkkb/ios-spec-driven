#!/usr/bin/env python3
"""
Hook script to track file changes and suggest task updates.
Runs after Write/Edit operations to help track spec progress.
"""

import json
import sys
import os
import re
from pathlib import Path


def find_related_spec(file_path):
    """Find spec folder that might be related to this file change."""
    specs_dir = Path(".claude/specs")
    if not specs_dir.exists():
        return None

    # Get feature name from file path
    # e.g., Features/Login/Views/LoginView.swift -> login
    parts = Path(file_path).parts
    for part in parts:
        feature_name = (
            part.lower()
            .replace("view", "")
            .replace("viewmodel", "")
            .replace("service", "")
        )
        for spec_folder in specs_dir.iterdir():
            if spec_folder.is_dir() and feature_name in spec_folder.name.lower():
                return spec_folder
    return None


def get_pending_tasks(tasks_file):
    """Get list of pending tasks from tasks.md."""
    if not tasks_file.exists():
        return []

    content = tasks_file.read_text()
    # Find unchecked tasks.
    # Common patterns in this repo:
    # - [ ] **3.1.2.1** Create Foo
    # - [ ] 3.1.2.1 Create Foo
    patterns = [
        r"- \[ \] \*\*(\d+(?:\.\d+)+)\*\*\s+(.+?)(?:\n|$)",
        r"- \[ \] (\d+(?:\.\d+)+)\s+(.+?)(?:\n|$)",
    ]

    for pattern in patterns:
        matches = re.findall(pattern, content)
        if matches:
            return [(task_id.strip(), desc.strip()) for task_id, desc in matches]

    return []


def main():
    try:
        input_data = json.load(sys.stdin)
        file_path = input_data.get("tool_input", {}).get("file_path", "")

        if not file_path:
            sys.exit(0)

        # Skip if editing spec files themselves
        if ".claude/specs" in file_path:
            sys.exit(0)

        # Skip non-Swift files
        if not file_path.endswith(".swift"):
            sys.exit(0)

        # Find related spec
        spec_folder = find_related_spec(file_path)
        if not spec_folder:
            sys.exit(0)

        tasks_file = spec_folder / "tasks.md"
        pending_tasks = get_pending_tasks(tasks_file)

        if pending_tasks:
            print(f"\n📋 Spec: {spec_folder.name}")
            print(f"📝 File changed: {file_path}")
            print(f"⏳ Pending tasks:")
            for task_id, desc in pending_tasks[:3]:  # Show max 3
                print(f"   - [{task_id}] {desc[:50]}...")
            if len(pending_tasks) > 3:
                print(f"   ... and {len(pending_tasks) - 3} more")
            print(f"\n💡 Remember to update tasks.md when task is complete!")

    except Exception as e:
        # Silent fail - don't block the workflow
        pass


if __name__ == "__main__":
    main()
