---
name: write-tasks
description: Create implementation plan from design. Use when creating tasks.md, breaking down work by feature, planning implementation.
tools: Read, Write, Grep, Glob
skills: dev-spec-driven
---

# Write Tasks Agent

## Objective
Create a strict, execution-ready `tasks.md` for autopilot task implementation.

## Output
- `{{IDE_CONFIG_DIR}}specs/[feature-name]/tasks.md`
- update `{{IDE_CONFIG_DIR}}specs/[feature-name]/spec-state.json`

## Prerequisites
- `requirements.md` exists.
- `design.md` exists.
- `spec-state.json` has `stage = approved_design`.

If prerequisites fail, stop and ask user to complete prior stage.

---

## State Machine
- On entry: set `stage = draft_tasks`.
- On approval: set `stage = approved_tasks` and `execution.mode = autopilot`.

---

## Tasks Document Format (Required)

```markdown
# [Feature Name] - Implementation Plan

## Execution Mode
- Mode: autopilot
- Policy: run sequentially by default
- Gate: stop on phase boundary or blocking error

## Task Registry (Machine Readable)

| ID | Title | Type | Status | Refs AC | Refs Design | Files | Checkpoint |
|---|---|---|---|---|---|---|---|
| 2.1.1 | Create model | normal | pending | AC-001.1 | 4 | Features/X/Models/X.swift | 2.1 |
| 2.1.2 | Model property test | pbt | pending | AC-001.1 | 7 | Tests/XPropertyTests.swift | 2.1 |
| 3.1.1 | Build list ViewModel | normal | pending | AC-001.2 | 3 | Features/X/ViewModels/XViewModel.swift | 3.1 |

## Dependency Matrix
| Task | Depends On | Can Parallel With |
|---|---|---|
| 3.1.1 | 2.1.1 | 3.2.1 |
| 3.2.1 | 2.1.1 | 3.1.1 |

## 1. Shared Tasks
- [ ] **2.1.1** Create model
  - Refs: AC-001.1
  - Design: 4
  - File: `Features/X/Models/X.swift`

- [ ] **2.2.1** Create service protocol and implementation
  - Refs: AC-001.1, AC-001.2
  - Design: 3, 4
  - File: `Features/X/Services/XService.swift`

- [ ] **2.3.1** [PBT] Model round-trip property
  - Refs: AC-001.1
  - Design: 9
  - File: `Tests/PropertyTests/XModelPropertyTests.swift`
  - Optional: Yes

**Checkpoint 2:** Build passes and shared unit tests pass

## 2. Feature Tasks
- [ ] **3.1.1** Build list ViewModel
  - Refs: AC-001.2
  - Design: 3
  - File: `Features/X/ViewModels/XViewModel.swift`

- [ ] **3.1.2** Build list screen UI states
  - Refs: AC-001.2, AC-001.3
  - Design: 7.1
  - File: `Features/X/Views/XView.swift`

- [ ] **3.2.1** Build detail ViewModel and view
  - Refs: AC-001.4
  - Design: 7.2
  - File: `Features/X/Views/XDetailView.swift`

- [ ] **3.3.1** Build form validation and submit flow
  - Refs: AC-002.1, AC-002.2
  - Design: 7.3
  - File: `Features/X/Views/XFormView.swift`

**Checkpoint 3.1:** List feature complete (build + tests)
**Checkpoint 3.2:** Detail feature complete (build + tests)
**Checkpoint 3.3:** Form feature complete (build + tests)

## 3. Integration Tasks
- [ ] **4.1.1** Wire navigation

- [ ] **4.2.1** Wire callbacks and refresh propagation
  - Refs: AC-001.2, AC-002.1
  - Design: 8
  - File: `Features/X/Coordinator/XCoordinator.swift`

- [ ] **4.3.1** Integration tests for core user flow
  - Refs: AC-001.2, AC-002.1
  - Design: 6, 8
  - File: `Tests/IntegrationTests/XFlowTests.swift`

**Checkpoint 4:** Full feature integrated and tested

## Traceability Matrix
| Task ID | AC | Design | Property | Status |
|---|---|---|---|---|
| 2.1.1 | AC-001.1 | 4 | - | pending |
| 2.3.1 | AC-001.1 | 9 | P2 | pending |
| 3.1.2 | AC-001.2, AC-001.3 | 7.1 | - | pending |
| 4.3.1 | AC-001.2, AC-002.1 | 6, 8 | - | pending |

## Progress
| Section | Total | Done | Status |
|---|---:|---:|---|
| Shared | 0 | 0 | ⬜ |
| Feature | 0 | 0 | ⬜ |
| Integration | 0 | 0 | ⬜ |
```

---

## Task Rules
- Every task must map to at least one AC.
- Every task must reference a design section.
- Status starts at `pending`.
- Allowed status: `pending | in_progress | blocked | done`.
- Use checkpoint IDs as phase gates.
- Only include coding tasks (write/modify/test code).
- Use iOS-first implementation order: Shared -> List -> Detail -> Form -> Integration.
- Each feature task set must include ViewModel, View, and Verify tasks.
- PBT tasks are optional by default but must still be in registry and matrix.

## Autopilot Sequencing Rules
- Default execution order follows checkpoint order.
- Autopilot may continue automatically inside same phase.
- On first blocked task, stop and report root cause and suggested fix.
- Parallel tasks are allowed only when dependency matrix explicitly allows it.

---

## Approval Gate (Required)

After writing/updating `tasks.md`, always ask:

```text
✅ Updated: {{IDE_CONFIG_DIR}}specs/[feature-name]/tasks.md

Do the tasks look good?

1. ✅ Approve and start autopilot execution
2. ✏️ Request changes
3. ⏸️ Stop here
```

Behavior:
- If approved: set `stage = approved_tasks`, invoke `execute-tasks` with `autopilot`.
- If changes requested: revise tasks, keep `stage = draft_tasks`, ask again.
- If stop: end.
