#!/usr/bin/env python3
"""
Traceability validation for spec-driven workflow.

Validates references across:
- requirements.md (AC IDs)
- design.md (design sections + properties)
- tasks.md (task registry + checklist tasks + traceability matrix)
"""

import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Set


@dataclass
class ValidationResult:
    is_valid: bool
    broken_references: List[str]
    orphaned_items: List[str]
    missing_references: List[str]
    warnings: List[str]


@dataclass
class TaskMeta:
    task_id: str
    title: str
    task_type: str
    status: str
    ac_refs: List[str]
    design_refs: List[str]


class TraceabilityValidator:
    def __init__(self, feature_name: str):
        self.feature_name = feature_name
        self.spec_dir = Path(f"{{{{IDE_CONFIG_DIR}}}}specs/{feature_name}")

        self.acceptance_criteria: Set[str] = set()
        self.design_sections: Set[str] = set()
        self.properties: Set[str] = set()
        self.property_ac_refs: Dict[str, List[str]] = {}

        self.tasks: Dict[str, TaskMeta] = {}
        self.traceability_rows: Dict[str, Dict[str, str]] = {}

    def validate(self) -> ValidationResult:
        if not self.spec_dir.exists():
            return ValidationResult(
                is_valid=False,
                broken_references=[f"Spec directory not found: {self.spec_dir}"],
                orphaned_items=[],
                missing_references=[],
                warnings=[],
            )

        self._parse_requirements()
        self._parse_design()
        self._parse_tasks()

        broken = self._find_broken_references()
        orphaned = self._find_orphaned_items()
        missing = self._find_missing_references()
        warnings = self._find_warnings()

        return ValidationResult(
            is_valid=(len(broken) == 0 and len(missing) == 0),
            broken_references=broken,
            orphaned_items=orphaned,
            missing_references=missing,
            warnings=warnings,
        )

    def _parse_requirements(self) -> None:
        req_file = self.spec_dir / "requirements.md"
        if not req_file.exists():
            return

        content = req_file.read_text()
        ac_pattern = r"\b(AC-\d+\.\d+)\b"
        self.acceptance_criteria = set(re.findall(ac_pattern, content))

    def _parse_design(self) -> None:
        design_file = self.spec_dir / "design.md"
        if not design_file.exists():
            return

        content = design_file.read_text()

        # Markdown heading sections like "## 4. Data Models" or "### 3.1 Feature"
        section_pattern = r"^#{2,3}\s+(\d+(?:\.\d+)*)\b"
        self.design_sections = set(re.findall(section_pattern, content, re.MULTILINE))

        # Property rows in markdown tables
        for line in content.splitlines():
            m = re.match(r"^\|\s*(P\d+)\s*\|", line)
            if m:
                prop = m.group(1)
                self.properties.add(prop)
                acs = re.findall(r"\bAC-\d+\.\d+\b", line)
                if acs:
                    self.property_ac_refs[prop] = acs

    def _parse_tasks(self) -> None:
        tasks_file = self.spec_dir / "tasks.md"
        if not tasks_file.exists():
            return

        content = tasks_file.read_text()
        self._parse_task_registry(content)
        self._parse_checklist_tasks(content)
        self._parse_traceability_matrix(content)

    def _parse_task_registry(self, content: str) -> None:
        # Expected row:
        # | 2.1.1 | Create model | normal | pending | AC-001.1 | 4 | file.swift | 2.1 |
        row_pattern = re.compile(
            r"^\|\s*(\d+(?:\.\d+)+)\s*\|\s*([^|]+?)\s*\|\s*([^|]+?)\s*\|\s*"
            r"([^|]+?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|$"
        )

        for line in content.splitlines():
            m = row_pattern.match(line.strip())
            if not m:
                continue
            task_id, title, ttype, status, ac_refs, design_refs, _, _ = m.groups()
            ac_list = re.findall(r"\bAC-\d+\.\d+\b", ac_refs)
            design_list = re.findall(r"\b\d+(?:\.\d+)*\b", design_refs)
            self.tasks[task_id] = TaskMeta(
                task_id=task_id,
                title=title.strip(),
                task_type=ttype.strip().lower(),
                status=status.strip().lower(),
                ac_refs=ac_list,
                design_refs=design_list,
            )

    def _parse_checklist_tasks(self, content: str) -> None:
        # Supports:
        # - [ ] **3.1.1** Build ViewModel
        # - [x] 3.1.2 Wire navigation
        pattern = re.compile(
            r"^-\s+\[[x\s]\]\s+(?:\*\*)?(\d+(?:\.\d+)+)(?:\*\*)?\s+(.+)$",
            re.MULTILINE,
        )

        for m in pattern.finditer(content):
            task_id = m.group(1)
            title = m.group(2).strip()
            if task_id not in self.tasks:
                inferred_type = "pbt" if "[pbt]" in title.lower() else "normal"
                self.tasks[task_id] = TaskMeta(
                    task_id=task_id,
                    title=title,
                    task_type=inferred_type,
                    status="unknown",
                    ac_refs=[],
                    design_refs=[],
                )

    def _parse_traceability_matrix(self, content: str) -> None:
        # Expected row:
        # | 2.1.1 | AC-001.1 | 4 | P1 | pending |
        row_pattern = re.compile(
            r"^\|\s*(\d+(?:\.\d+)+)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|\s*([^|]*?)\s*\|$"
        )

        for line in content.splitlines():
            m = row_pattern.match(line.strip())
            if not m:
                continue
            task_id, acs, design_ref, prop, status = m.groups()
            if task_id.lower() == "task id":
                continue
            self.traceability_rows[task_id] = {
                "acs": ", ".join(re.findall(r"\bAC-\d+\.\d+\b", acs)),
                "design": ", ".join(re.findall(r"\b\d+(?:\.\d+)*\b", design_ref)),
                "property": ", ".join(re.findall(r"\bP\d+\b", prop)),
                "status": status.strip().lower(),
            }

    def _find_broken_references(self) -> List[str]:
        broken: List[str] = []

        for task in self.tasks.values():
            for ac in task.ac_refs:
                if ac not in self.acceptance_criteria:
                    broken.append(f"Task {task.task_id} references {ac} (NOT FOUND)")
            for dref in task.design_refs:
                if dref not in self.design_sections:
                    broken.append(
                        f"Task {task.task_id} references Design {dref} (NOT FOUND)"
                    )

        for prop, acs in self.property_ac_refs.items():
            for ac in acs:
                if ac not in self.acceptance_criteria:
                    broken.append(f"Property {prop} validates {ac} (NOT FOUND)")

        for task_id, row in self.traceability_rows.items():
            for ac in re.findall(r"\bAC-\d+\.\d+\b", row["acs"]):
                if ac not in self.acceptance_criteria:
                    broken.append(
                        f"Traceability row {task_id} references {ac} (NOT FOUND)"
                    )

        return broken

    def _find_orphaned_items(self) -> List[str]:
        orphaned: List[str] = []

        referenced_acs: Set[str] = set()
        for task in self.tasks.values():
            referenced_acs.update(task.ac_refs)
        for prop_acs in self.property_ac_refs.values():
            referenced_acs.update(prop_acs)
        for row in self.traceability_rows.values():
            referenced_acs.update(re.findall(r"\bAC-\d+\.\d+\b", row["acs"]))

        for ac in sorted(self.acceptance_criteria):
            if ac not in referenced_acs:
                orphaned.append(f"{ac} not referenced by any task/property/matrix row")

        return orphaned

    def _find_missing_references(self) -> List[str]:
        missing: List[str] = []
        for task in self.tasks.values():
            if not task.ac_refs:
                missing.append(f"Task {task.task_id} has no AC reference")
            if not task.design_refs:
                missing.append(f"Task {task.task_id} has no Design reference")
        return missing

    def _find_warnings(self) -> List[str]:
        warnings: List[str] = []

        if len(self.properties) == 0:
            warnings.append("No correctness properties defined")

        pbt_tasks = [
            t
            for t in self.tasks.values()
            if t.task_type == "pbt" or "[pbt]" in t.title.lower()
        ]
        if len(pbt_tasks) == 0:
            warnings.append("No PBT tasks found")

        if len(self.traceability_rows) == 0:
            warnings.append("No Traceability Matrix rows found")

        return warnings


def print_result(result: ValidationResult, feature_name: str) -> None:
    print(f"\n{'=' * 60}")
    print(f"Traceability Validation: {feature_name}")
    print(f"{'=' * 60}\n")

    print("✅ VALIDATION PASSED\n" if result.is_valid else "❌ VALIDATION FAILED\n")

    if result.broken_references:
        print(f"🔴 Broken References ({len(result.broken_references)}):")
        for ref in result.broken_references:
            print(f"  - {ref}")
        print()

    if result.missing_references:
        print(f"🟡 Missing References ({len(result.missing_references)}):")
        for ref in result.missing_references:
            print(f"  - {ref}")
        print()

    if result.orphaned_items:
        print(f"🟠 Orphaned Items ({len(result.orphaned_items)}):")
        for item in result.orphaned_items:
            print(f"  - {item}")
        print()

    if result.warnings:
        print(f"⚠️  Warnings ({len(result.warnings)}):")
        for warning in result.warnings:
            print(f"  - {warning}")
        print()

    if not any(
        [
            result.broken_references,
            result.missing_references,
            result.orphaned_items,
            result.warnings,
        ]
    ):
        print("✨ No issues found!\n")

    print(f"{'=' * 60}\n")


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python validate_traceability.py <feature-name>")
        sys.exit(1)

    feature_name = sys.argv[1]
    validator = TraceabilityValidator(feature_name)
    result = validator.validate()
    print_result(result, feature_name)

    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
