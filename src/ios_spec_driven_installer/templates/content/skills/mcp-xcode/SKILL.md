---
name: mcp-xcode
description: Build and test iOS apps with Xcode MCP during autopilot checkpoints and recovery loops.
allowed-tools: Read, MCP, Bash
---

# Xcode MCP Checkpoint Skill

## Purpose
Provide strict build/test gates for spec-driven autopilot execution.

Use this skill at:
- task-level scoped checks
- checkpoint/phase gates
- recovery loops after failures

---

## 1) Standard Commands

- `xcode_list_schemes`
- `xcode_build`
- `xcode_test`
- `xcode_clean`
- `xcode_get_build_settings`

---

## 2) Gate Sequence (Required)

At each checkpoint:
1. list scheme (if not cached)
2. build in Debug
3. run relevant tests
4. if needed, clean + rebuild

Only pass gate when build and required tests pass.

Recommended order:

```text
xcode_list_schemes
-> xcode_build (Debug)
-> xcode_test (targeted)
-> xcode_test (broader suite at phase end)
```

---

## 3) Scoped Checks by Task Type

- model/service task: unit tests for model/service layer
- ViewModel task: ViewModel tests + state transition tests
- UI task: compile + relevant UI/snapshot tests (if available)
- integration task: end-to-end integration tests for feature flow

---

## 4) Failure Recovery Policy

Retry tiers:
- Attempt 1-2: direct code fix, rerun scoped checks
- Attempt 3: review design/task mismatch, then rerun
- Still failing: mark task `blocked` and stop autopilot

Never advance checkpoint while build/test is failing.

---

## 5) Pre-Completion Gate (Feature/Phase)

Before marking phase done:
- clean build
- full phase test pass
- no unresolved compile errors
- update task statuses and traceability rows

---

## 6) Checklist

- [ ] Correct scheme selected
- [ ] Build passes for changed code
- [ ] Required tests pass for task and phase
- [ ] Failures triaged with retry policy
- [ ] Gate result reflected in task/phase status
