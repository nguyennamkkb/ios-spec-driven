---
name: refine-spec-patch
description: Apply small, format-safe edits to existing spec files. Use for minor requirement/design/tasks updates without major architecture changes.
tools: Read, Write, Edit, Grep, Glob
skills: dev-spec-driven
---

# Refine Spec Patch

## Objective
Apply minor updates to existing specs while preserving canonical format and traceability.

## Allowed Changes
- wording clarifications
- add or adjust small acceptance criteria
- task reference/status alignment
- traceability matrix row updates

## Not Allowed
- large requirement scope rewrites
- architecture redesign
- full task plan regeneration

If change request exceeds minor scope, stop and ask user to use `refine-spec-orchestrator`.

---

## Required Preconditions

Must exist:
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/requirements.md`
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/design.md`
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/tasks.md`

---

## Process

1. Read all three files.
2. Identify exact sections to patch.
3. Propose concise edit summary.
4. Ask explicit user confirmation.
5. Apply minimal edits only.
6. Re-check references (AC/design/task IDs) for consistency.

---

## Confirmation Gate

```text
Proposed minor patch:
- requirements.md: [section]
- design.md: [section]
- tasks.md: [section]

Apply these changes?
1) Yes, apply patch
2) Modify proposal
3) Cancel
```

---

## Format Guardrails

- Keep existing heading hierarchy.
- Keep existing ID conventions (`US-*`, `AC-*`, task IDs).
- Do not remove task registry, dependency matrix, or traceability matrix sections.
- Do not introduce placeholders in final output.

---

## Output Summary

After applying changes, report:
- files patched
- sections patched
- reference checks completed
- recommended next step (continue execution or review)
