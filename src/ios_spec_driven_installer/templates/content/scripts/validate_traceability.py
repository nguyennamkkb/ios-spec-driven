#!/usr/bin/env python3
"""
Traceability Validation Script

Validates references across spec files:
- US-XXX in requirements.md
- AC-XXX.Y in requirements.md
- Design sections (3.1, 3.2, etc.) in design.md
- Properties (P1, P2, etc.) in design.md
- Tasks (X.Y.Z) in tasks.md

Usage:
    python validate_traceability.py <feature-name>
    python validate_traceability.py user-authentication
"""

import re
import sys
from pathlib import Path
from typing import Dict, List, Set, Tuple
from dataclasses import dataclass


@dataclass
class ValidationResult:
    """Result of traceability validation"""
    is_valid: bool
    broken_references: List[str]
    orphaned_items: List[str]
    missing_references: List[str]
    warnings: List[str]


class TraceabilityValidator:
    """Validates traceability across spec files"""
    
    def __init__(self, feature_name: str):
        self.feature_name = feature_name
        self.spec_dir = Path(f"{{{{IDE_CONFIG_DIR}}}}specs/{feature_name}")
        
        # Collections
        self.user_stories: Set[str] = set()
        self.acceptance_criteria: Set[str] = set()
        self.design_sections: Set[str] = set()
        self.properties: Set[str] = set()
        self.tasks: Set[str] = set()
        
        # References
        self.task_ac_refs: Dict[str, List[str]] = {}
        self.task_design_refs: Dict[str, List[str]] = {}
        self.property_ac_refs: Dict[str, List[str]] = {}

    
    def validate(self) -> ValidationResult:
        """Run full validation"""
        if not self.spec_dir.exists():
            return ValidationResult(
                is_valid=False,
                broken_references=[f"Spec directory not found: {self.spec_dir}"],
                orphaned_items=[],
                missing_references=[],
                warnings=[]
            )
        
        # Parse all files
        self._parse_requirements()
        self._parse_design()
        self._parse_tasks()
        
        # Validate references
        broken_refs = self._find_broken_references()
        orphaned = self._find_orphaned_items()
        missing = self._find_missing_references()
        warnings = self._find_warnings()
        
        is_valid = len(broken_refs) == 0 and len(missing) == 0
        
        return ValidationResult(
            is_valid=is_valid,
            broken_references=broken_refs,
            orphaned_items=orphaned,
            missing_references=missing,
            warnings=warnings
        )
    
    def _parse_requirements(self):
        """Parse requirements.md for US and AC"""
        req_file = self.spec_dir / "requirements.md"
        if not req_file.exists():
            return
        
        content = req_file.read_text()
        
        # Find User Stories: ### US-001: Title
        us_pattern = r'###\s+(US-\d+):'
        self.user_stories = set(re.findall(us_pattern, content))
        
        # Find Acceptance Criteria: - AC-001.1: ...
        ac_pattern = r'-\s+(AC-\d+\.\d+):'
        self.acceptance_criteria = set(re.findall(ac_pattern, content))
    
    def _parse_design(self):
        """Parse design.md for sections and properties"""
        design_file = self.spec_dir / "design.md"
        if not design_file.exists():
            return
        
        content = design_file.read_text()
        
        # Find Design Sections: ### 3.1 Feature: ...
        section_pattern = r'###\s+(\d+\.\d+)\s+Feature:'
        self.design_sections = set(re.findall(section_pattern, content))
        
        # Find Properties: | P1 | ... |
        property_pattern = r'\|\s+(P\d+)\s+\|'
        self.properties = set(re.findall(property_pattern, content))
        
        # Find Property AC references
        prop_ref_pattern = r'\|\s+(P\d+)\s+\|[^|]+\|[^|]+\|\s+(AC-[\d.]+(?:,\s*AC-[\d.]+)*)\s+\|'
        for match in re.finditer(prop_ref_pattern, content):
            prop = match.group(1)
            ac_refs = [ac.strip() for ac in match.group(2).split(',')]
            self.property_ac_refs[prop] = ac_refs
    
    def _parse_tasks(self):
        """Parse tasks.md for tasks and references"""
        tasks_file = self.spec_dir / "tasks.md"
        if not tasks_file.exists():
            return
        
        content = tasks_file.read_text()
        
        # Find Tasks
        task_pattern = r'-\s+\[[x\s]\]\s+\*\*(\d+\.\d+\.\d+(?:\.\d+)?)\*\*'
        self.tasks = set(re.findall(task_pattern, content))
        
        # Find Task references
        task_blocks = re.split(r'-\s+\[[x\s]\]\s+\*\*(\d+\.\d+\.\d+(?:\.\d+)?)\*\*', content)
        
        for i in range(1, len(task_blocks), 2):
            task_id = task_blocks[i]
            task_content = task_blocks[i + 1] if i + 1 < len(task_blocks) else ""
            
            # Find AC references
            ac_refs_match = re.search(r'Refs:\s+(AC-[\d.,\s]+)', task_content)
            if ac_refs_match:
                ac_refs = [ac.strip() for ac in ac_refs_match.group(1).replace(',', ' ').split()]
                self.task_ac_refs[task_id] = ac_refs
            
            # Find Design references
            design_refs_match = re.search(r'Design:\s+([\d.]+)', task_content)
            if design_refs_match:
                self.task_design_refs[task_id] = [design_refs_match.group(1)]
    
    def _find_broken_references(self) -> List[str]:
        """Find references that point to non-existent items"""
        broken = []
        
        # Check task AC references
        for task_id, ac_refs in self.task_ac_refs.items():
            for ac_ref in ac_refs:
                if ac_ref not in self.acceptance_criteria:
                    broken.append(f"Task {task_id} references {ac_ref} (NOT FOUND)")
        
        # Check task Design references
        for task_id, design_refs in self.task_design_refs.items():
            for design_ref in design_refs:
                if design_ref not in self.design_sections:
                    broken.append(f"Task {task_id} references Design {design_ref} (NOT FOUND)")
        
        # Check property AC references
        for prop_id, ac_refs in self.property_ac_refs.items():
            for ac_ref in ac_refs:
                if ac_ref not in self.acceptance_criteria:
                    broken.append(f"Property {prop_id} validates {ac_ref} (NOT FOUND)")
        
        return broken
    
    def _find_orphaned_items(self) -> List[str]:
        """Find items not referenced by anything"""
        orphaned = []
        
        # Find orphaned ACs
        referenced_acs = set()
        for ac_refs in self.task_ac_refs.values():
            referenced_acs.update(ac_refs)
        for ac_refs in self.property_ac_refs.values():
            referenced_acs.update(ac_refs)
        
        for ac in self.acceptance_criteria:
            if ac not in referenced_acs:
                orphaned.append(f"{ac} not referenced by any task or property")
        
        return orphaned
    
    def _find_missing_references(self) -> List[str]:
        """Find tasks that should have references but don't"""
        missing = []
        
        for task_id in self.tasks:
            if task_id not in self.task_ac_refs:
                missing.append(f"Task {task_id} has no AC reference")
        
        return missing
    
    def _find_warnings(self) -> List[str]:
        """Find potential issues"""
        warnings = []
        
        if len(self.properties) == 0:
            warnings.append("No correctness properties defined")
        
        pbt_tasks = [t for t in self.tasks if 'PBT' in str(t)]
        if len(pbt_tasks) == 0:
            warnings.append("No PBT tasks found")
        
        return warnings


def print_result(result: ValidationResult, feature_name: str):
    """Print validation result"""
    print(f"\n{'='*60}")
    print(f"Traceability Validation: {feature_name}")
    print(f"{'='*60}\n")
    
    if result.is_valid:
        print("✅ VALIDATION PASSED\n")
    else:
        print("❌ VALIDATION FAILED\n")
    
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
    
    if not any([result.broken_references, result.missing_references, 
                result.orphaned_items, result.warnings]):
        print("✨ No issues found!\n")
    
    print(f"{'='*60}\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python validate_traceability.py <feature-name>")
        sys.exit(1)
    
    feature_name = sys.argv[1]
    validator = TraceabilityValidator(feature_name)
    result = validator.validate()
    print_result(result, feature_name)
    sys.exit(0 if result.is_valid else 1)


if __name__ == "__main__":
    main()
