---
name: mcp-xcode
description: Build iOS apps with Xcode MCP during autopilot checkpoints and recovery loops.
allowed-tools: Read, MCP, Bash
---

# Xcode MCP Checkpoint Skill

## Purpose
Provide strict build gates for spec-driven autopilot execution.

Use this skill at:
- task-level scoped checks
- checkpoint/phase gates
- recovery loops after failures

---

## 1) Standard Commands

- `xcode_list_schemes`
- `xcode_build`
- `xcode_test` (optional/manual)
- `xcode_clean`
- `xcode_get_build_settings`

---

## 2) Gate Sequence (Required)

At each checkpoint:
1. list scheme (if not cached)
2. build in Debug
3. if needed, clean + rebuild

Only pass gate when build passes.

Recommended order:

```text
xcode_list_schemes
-> xcode_build (Debug)
-> xcode_clean (optional, on unstable build cache)
-> xcode_build (Debug, clean rebuild if needed)
```

---

## 3) Scoped Checks by Task Type

- model/service task: compile impacted module files
- ViewModel task: compile impacted feature module
- UI task: compile impacted UI targets
- integration task: compile integrated feature path

Note: tests are optional/manual and not part of checkpoint gate.

---

## 4) Failure Recovery Policy

Retry tiers:
- Attempt 1-2: direct code fix, rerun scoped checks
- Attempt 3: review design/task mismatch, then rerun
- Still failing: mark task `blocked` and stop autopilot

Never advance checkpoint while build is failing.

---

## 5) Pre-Completion Gate (Feature/Phase)

Before marking phase done:
- clean build
- no unresolved compile errors
- update task statuses and traceability rows

---

## 6) Checklist

- [ ] Correct scheme selected
- [ ] Build passes for changed code
- [ ] Failures triaged with retry policy
- [ ] Gate result reflected in task/phase status
- [ ] Traceability validation passed
