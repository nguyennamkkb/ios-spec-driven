---
name: dev-spec-driven
description:
  Spec-driven workflow for iOS delivery. Use when creating requirements, design, tasks, executing tasks in autopilot, maintaining traceability and checkpoint gates.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Spec-Driven iOS Workflow (Autopilot)

## Purpose
Use this skill as the workflow contract for all spec agents:
- `write-spec`
- `write-design`
- `write-tasks`
- `execute-tasks`

This skill defines stage transitions, quality gates, and traceability expectations.

---

## 1) Source of Truth Files

Each feature lives in:

```text
{{IDE_CONFIG_DIR}}specs/[feature-name]/
  requirements.md
  design.md
  tasks.md
  spec-state.json
```

Required roles:
- `requirements.md`: user stories + EARS acceptance criteria.
- `design.md`: architecture + iOS feature design + properties.
- `tasks.md`: machine-readable registry + implementation checklist.
- `spec-state.json`: workflow stage and execution mode.

---

## 2) State Machine (Required)

```text
draft_requirements
  -> approved_requirements
  -> draft_design
  -> approved_design
  -> draft_tasks
  -> approved_tasks
  -> executing
  -> blocked | done
```

Rules:
- Never skip stages.
- Never start execution before `approved_tasks`.
- Any major requirement/design change during execution returns stage to a draft state.

---

## 3) Approval Gates

Explicit user approval is required after each document:
- `requirements.md` -> continue to design
- `design.md` -> continue to tasks
- `tasks.md` -> start execution

If user requests edits:
- revise current document
- keep current draft stage
- ask for approval again

---

## 4) Requirements Contract

Required format:
- User story per requirement.
- EARS acceptance criteria per story.
- stable IDs and explicit error handling.

ID conventions:
- User Story: `US-XXX`
- Acceptance Criteria: `AC-XXX.Y`

EARS examples:
- `WHEN [event] THEN THE SYSTEM SHALL [response]`
- `IF [condition] THEN THE SYSTEM SHALL [response]`
- `WHILE [state] THE SYSTEM SHALL [response]`

---

## 5) Design Contract (iOS-first)

Design must include:
- overview and architecture
- components/interfaces and data models
- error handling and testing strategy
- feature breakdown per screen (states/actions/files)
- navigation/integration flow
- correctness properties (`P1`, `P2`, ...)

Do not include production implementation code.

---

## 6) Tasks Contract (Hybrid Format)

`tasks.md` must include all of the following:

1) `Task Registry` table (machine-readable)
- columns: `ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint`

2) Implementation checklist sections (human-readable)
- Shared -> Feature tasks -> Integration

3) `Dependency Matrix`
- defines allowed parallelism and ordering

4) `Traceability Matrix`
- maps task to AC/design/property/status

Allowed status values:
- `pending | in_progress | blocked | done`

Task types:
- `normal | pbt | integration`

---

## 7) Autopilot Execution Policy

Default policy:
- sequential by dependency order
- transaction per task
- automatic continuation within current phase

Task transaction:
1. validate dependencies
2. mark `in_progress`
3. implement task
4. run scoped checks
5. mark `done` or `blocked`
6. update traceability rows

Stop conditions:
- first blocked task
- phase gate failure
- explicit user stop

---

## 8) Phase Gate Policy

At checkpoint boundary, all must pass:
1. build
2. traceability validation

Only then move to next checkpoint.

Recommended build flow uses `mcp-xcode` skill.

---

## 9) iOS Quality Gates

Before marking feature section complete:
- all declared UI states implemented (loading/empty/error/success)
- ViewModel state transitions tested
- accessibility checks for key interactions
- component reuse decision recorded

For UI tasks with design input:
- use Framelink MCP context from `mcp-figma`
- map tokens/components before coding

---

## 10) Traceability and Validation

Run:

```bash
python {{IDE_CONFIG_DIR}}scripts/validate_traceability.py [feature-name]
```

Validation must ensure:
- AC references exist
- design section references exist
- every task has AC + design references
- traceability matrix rows are present

---

## 11) Execution Modes

- `autopilot` (default): automatic within phase, strict gates.
- `manual`: execute one task and stop.

Parallel execution is optional and only allowed if dependency matrix declares no conflicts.
