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
- phase-end gates
- recovery loops after failures

---

## 1) Standard Commands

- `discover_projs`
- `list_schemes`
- `build_sim` (default gate command)
- `build_run_sim` (optional, run intent)
- `show_build_settings`
- `clean`
- `test_sim` (optional/manual)
- `doctor` (diagnostics)

Default gate policy:
- Use `build_sim` only for phase-end build gates.
- Do not run or boot simulator by default.

---

## 2) Gate Sequence (Required)

At each phase-end gate:
1. discover project/workspace
2. list scheme (if not cached)
3. build for simulator in Debug
4. if needed, clean + rebuild

Only pass phase-end gate when build passes.

Recommended order:

```text
discover_projs
-> list_schemes
-> build_sim (Debug)
-> clean (optional, on unstable build cache)
-> build_sim (Debug, clean rebuild if needed)
```

---

## 3) Scoped Checks by Task Type

- model/service task: compile impacted module files
- ViewModel task: compile impacted feature module
- UI task: compile impacted UI targets
- integration task: compile integrated feature path

Note: tests are optional/manual and not part of checkpoint gate.

Optional commands by intent:
- run intent (explicit user request only): `build_run_sim`
- manual test intent: `test_sim`
- diagnostics: `show_build_settings`, `doctor`

Simulator launch restrictions:
- `build_run_sim`, `boot_sim`, and `open_sim` are user-triggered only.
- Never use run/boot simulator tools in default autopilot phase gates.

---

## 4) Failure Recovery Policy

Retry tiers:
- Attempt 1-2: direct code fix, rerun scoped checks
- Attempt 3: review design/task mismatch, then rerun
- Still failing: mark task `blocked` and stop autopilot

Never advance to next phase while build is failing.

---

## 5) Pre-Completion Gate (Feature/Phase)

Before marking phase done:
- clean build
- no unresolved compile errors
- update task statuses and traceability rows

---

## 6) Checklist

- [ ] MCP server reachable (tool calls available)
- [ ] Project/workspace discovered via `discover_projs`
- [ ] Correct scheme selected
- [ ] Build passes for changed code
- [ ] Failures triaged with retry policy
- [ ] Gate result reflected in task/phase status
- [ ] Traceability validation passed
