---
name: dev-spec-driven
description: |
  Spec-driven development workflow for iOS. Use when creating new features, writing requirements, design documents, implementation plans, EARS notation, user stories, acceptance criteria, property-based testing, spec workflow, traceability.
allowed-tools: Read, Write, Edit, Grep, Glob
---

# Spec-Driven Development

## Table of Contents
- [1. Concept](#1-concept) ........................... L20-L50
- [2. Workflow](#2-workflow) ......................... L52-L100
- [3. Requirements Format](#3-requirements-format) ... L102-L160
- [4. Design Format](#4-design-format) ............... L162-L250
- [5. Tasks Format](#5-tasks-format) ................. L252-L340
- [6. Traceability](#6-traceability) ................. L342-L380
- [7. Agents](#7-agents) ............................. L382-L420

---

## 1. Concept

### Spec Files
Each feature requires 3 files in `.claude/specs/[feature-name]/`:

| File | Content | Agent |
|------|---------|-------|
| `requirements.md` | User stories + EARS acceptance criteria | write-spec |
| `design.md` | Architecture + Features + Wireframes | write-design |
| `tasks.md` | Feature-based implementation plan | write-tasks |

### Directory Structure
```
.claude/specs/
├── user-authentication/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
├── product-catalog/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
└── shopping-cart/
    └── ...
```

### Core Principles
1. **Feature-based**: Organized by feature, each feature is independent
2. **Traceability**: US → AC → Property → Task all have IDs and references
3. **Checkpoints**: User confirmation after each step
4. **No code in spec**: Specs describe only, no sample code


## How to Use This Skill

### Quick Start

**For new features:**
```
You: "Create spec for user authentication feature"
```

Claude will:
1. Invoke `write-spec` agent → Create `requirements.md`
2. Ask for your confirmation
3. Invoke `write-design` agent → Create `design.md`
4. Ask for your confirmation
5. Invoke `write-tasks` agent → Create `tasks.md`
6. Ask for your confirmation
7. Invoke `execute-tasks` agent → Start implementation

### Manual Control

**Create only requirements:**
```
You: "Write requirements for shopping cart"
```
→ Creates only `requirements.md`, stops for confirmation

**Create only design:**
```
You: "Write design for shopping cart"
```
→ Requires existing `requirements.md`, creates `design.md`

**Create only tasks:**
```
You: "Write tasks for shopping cart"
```
→ Requires existing `design.md`, creates `tasks.md`

**Implement specific task:**
```
You: "Implement task 3.1.2.1"
```
→ Executes single task from `tasks.md`

**Implement next task:**
```
You: "Implement next task"
```
→ Finds first uncompleted task and implements it

### Batch Mode

**Create all specs at once:**
```
You: "Create full spec (requirements + design + tasks) for user profile feature"
```

Claude will create all 3 files but ask for confirmation between each step.

### Agent Invocation

Agents are invoked automatically based on your request:

| Your Request | Agent Invoked | Output |
|--------------|---------------|--------|
| "Create spec for X" | write-spec | requirements.md |
| "Write design for X" | write-design | design.md |
| "Write tasks for X" | write-tasks | tasks.md |
| "Implement task Y" | execute-tasks | Code |
| "Modify requirements" | refine-spec | Updated specs |

You don't need to explicitly call agents - just describe what you want.

### Workflow Confirmation

After each file is created, Claude will ask:

```
✅ Created: requirements.md

❓ What would you like to do?
1. ✅ Continue to create design.md
2. ✏️ Request modifications
3. ⏸️ Stop here, continue later
```

**Important**: Claude will NOT automatically continue without your confirmation.

### File Locations

All spec files are created in:
```
.claude/specs/[feature-name]/
├── requirements.md
├── design.md
└── tasks.md
```

Example:
```
.claude/specs/user-authentication/
├── requirements.md
├── design.md
└── tasks.md
```

### Modifying Existing Specs

**To update requirements:**
```
You: "Add new requirement: users can reset password"
```
→ Invokes `refine-spec` agent to update `requirements.md`

**To update design:**
```
You: "Change List Screen to use grid layout instead"
```
→ Updates `design.md` and affected tasks in `tasks.md`

### Implementation Flow

When implementing tasks:

1. **Phase by Phase**: Complete all tasks in Phase 2 (Shared) before Phase 3 (Features)
2. **Feature by Feature**: Complete Feature 3.1 before Feature 3.2
3. **Checkpoint Gates**: Build must pass before moving to next phase
4. **User Confirmation**: Required after each phase completion

Example:
```
You: "Start implementing shopping cart"

Claude:
- Implements task 2.1.1 (Create models)
- Implements task 2.1.2 (Create service)
- Builds with mcp-xcode
- ✅ Checkpoint 2 complete
- Asks: "Continue to Feature 3.1?"
```

### Tips

**For small features (<4 hours):**
```
You: "Quick implementation of settings toggle - skip full spec"
```
→ Claude invokes `quick-implement` agent (no spec files, direct implementation)

**For complex features:**
```
You: "Create detailed spec for payment system with Stripe integration"
```
→ Claude will create comprehensive specs with all details

**Explicit lightweight mode:**
```
You: "Use quick-implement for dark mode toggle"
```
→ Forces lightweight mode even if feature seems complex

**When stuck:**
```
You: "Show me what specs exist"
You: "What's the status of shopping cart implementation?"
You: "What task should I do next?"
```

### Common Commands

| Command | Result |
|---------|--------|
| "Create spec for X" | Full workflow (requirements → design → tasks) |
| "Write requirements for X" | Only requirements.md |
| "Implement next task" | Execute next uncompleted task |
| "Implement task 3.1.2.1" | Execute specific task |
| "Show task status" | Display progress |
| "Update requirement: ..." | Modify existing spec |
| "Build and test" | Run mcp-xcode build + tests |

---

## Example (End-to-End)

This repo includes a complete example feature spec you can copy and adapt:

- `.claude/specs/example-todo-list/requirements.md`
- `.claude/specs/example-todo-list/design.md`
- `.claude/specs/example-todo-list/tasks.md`

Use it as a reference for:
- What “good” EARS acceptance criteria look like
- How design sections map to tasks and checkpoints
- How traceability (US/AC/Property/Task) stays consistent



---

## 2. Workflow

### 2.1 Overview Flow

```
Idea
    ↓
┌─────────────────┐
│ write-spec      │ → requirements.md
└────────┬────────┘
         ↓ [User Confirm]
┌─────────────────┐
│ write-design    │ → design.md
└────────┬────────┘
         ↓ [User Confirm]
┌─────────────────┐
│ write-tasks     │ → tasks.md
└────────┬────────┘
         ↓ [User Confirm]
┌─────────────────┐
│ execute-tasks   │ → Code
└─────────────────┘
```

### 2.2 User Confirmation (REQUIRED)

| After Creating | Ask User |
|----------------|----------|
| `requirements.md` | Continue to design? / Modify? / Stop? |
| `design.md` | Continue to tasks? / Modify? / Stop? |
| `tasks.md` | Start implementation? / Modify? / Stop? |

**Prompt Format:**
```
❓ What would you like to do?
1. ✅ Continue to next step
2. ✏️ Request modifications
3. ⏸️ Stop here, continue later
```

### 2.3 Rules
- **NEVER** automatically create the next file without asking user
- **ALWAYS** wait for user confirmation before continuing
- User selects **Modify** → Apply changes → Ask again

---

## 3. Requirements Format

### 3.1 Template

```markdown
# [Feature Name] - Requirements

## Table of Contents
- [1. Overview](#1-overview)
- [2. User Stories](#2-user-stories)
- [3. Non-Functional Requirements](#3-non-functional-requirements)

## 1. Overview
[Brief feature description - 2-3 sentences]

## 2. User Stories

### US-001: [Story name]
**As a** [role]
**I want** [action]
**So that** [benefit]

#### Acceptance Criteria
- AC-001.1: WHEN [trigger] THE SYSTEM SHALL [behavior]
- AC-001.2: WHEN [trigger] THE SYSTEM SHALL [behavior]
- AC-001.3: IF [error] THEN THE SYSTEM SHALL [error handling]

### US-002: [Story name]
...

## 3. Non-Functional Requirements
- NFR-001: Performance - [requirement]
- NFR-002: Security - [requirement]
```

### 3.2 EARS Patterns

| Pattern | Format | Example |
|---------|--------|---------|
| Event-driven | WHEN [event] THE SYSTEM SHALL [response] | WHEN user taps login THE SYSTEM SHALL validate credentials |
| State-driven | WHILE [state] THE SYSTEM SHALL [behavior] | WHILE offline THE SYSTEM SHALL show cached data |
| Unwanted | IF [condition] THEN THE SYSTEM SHALL [response] | IF password invalid THEN THE SYSTEM SHALL show error |
| Optional | WHERE [feature enabled] THE SYSTEM SHALL [behavior] | WHERE premium user THE SYSTEM SHALL show advanced features |

### 3.3 Rules
- Each User Story has ID: `US-XXX`
- Each Acceptance Criteria has ID: `AC-XXX.Y`
- EARS notation required for AC
- Must have error handling criteria (IF...THEN)

---

## 4. Design Format

### 4.1 Main Structure

```markdown
# [Feature Name] - Technical Design

## Table of Contents
- [1. Overview](#1-overview)
- [2. Shared](#2-shared)
- [3. Features](#3-features)
  - [3.1 Feature: List Screen](#31-feature-list-screen)
  - [3.2 Feature: Detail Screen](#32-feature-detail-screen)
  - [3.3 Feature: Form Screen](#33-feature-form-screen)
- [4. Navigation](#4-navigation)
- [5. Correctness Properties](#5-correctness-properties)
```

### 4.2 Shared Section

| Subsection | Content |
|------------|---------|
| 2.1 Data Models | Models table + Relationships |
| 2.2 Services | Service methods + API Contracts |
| 2.3 Dependencies | External + Internal dependencies |

### 4.3 Feature Section (EACH FEATURE INDEPENDENT)

Each feature (3.1, 3.2, 3.3) has 6 parts:

| Subsection | Content |
|------------|---------|
| 3.X.1 Wireframe | ASCII diagram |
| 3.X.2 Components | Table: Component, Type, Responsibility |
| 3.X.3 States | Table: State, Condition, UI |
| 3.X.4 Actions | Table: Action, Trigger, Effect |
| 3.X.5 Files | Table: File, Responsibility |
| 3.X.6 Acceptance Checklist | Checklist mapped to AC-xxx |

### 4.4 Correctness Properties

| Type | Description | Example |
|------|-------------|---------|
| Invariant | Always true after any operation | "Balance >= 0 after any transaction" |
| Round-trip | Encode/decode returns original value | "JSON encode then decode = original" |
| Idempotent | Multiple executions = single execution | "Delete twice = delete once" |
| Commutative | Order doesn't matter | "Add A then B = Add B then A" |

### 4.5 Rules
- Each feature is an independent, complete unit
- Each feature MUST have Acceptance Checklist
- NO sample code, description only
- Table of contents has line numbers for fast AI navigation

---

## 5. Tasks Format

### 5.1 Main Structure

```markdown
# [Feature Name] - Implementation Plan

## Table of Contents
- [1. Overview](#1-overview)
- [2. Shared Tasks](#2-shared-tasks)
- [3. Feature Tasks](#3-feature-tasks)
  - [3.1 Feature: List Screen](#31-feature-list-screen)
  - [3.2 Feature: Detail Screen](#32-feature-detail-screen)
  - [3.3 Feature: Form Screen](#33-feature-form-screen)
- [4. Integration Tasks](#4-integration-tasks)
- [5. Progress](#5-progress)
```

### 5.2 Task Sections

| Section | Content | When |
|---------|---------|------|
| 2. Shared Tasks | Models, Services | Do first |
| 3.1 Feature: List | ViewModel → Views → Verify | After Shared |
| 3.2 Feature: Detail | ViewModel → Views → Verify | After 3.1 |
| 3.3 Feature: Form | ViewModel → Views → Verify | After 3.2 |
| 4. Integration | Navigation, Entry point | After all Features |

### 5.3 Each Feature Has 3 Parts

| Part | Tasks |
|------|-------|
| X.1 ViewModel | Create ViewModel, [PBT] property |
| X.2 Views | Create components, Create main view |
| X.3 Verify | Verify Acceptance Checklist |

### 5.4 Checkpoints

Each section has a Checkpoint:
```
**Checkpoint 3.1:** ⬜ Feature List Screen complete
```

Checkpoint = Gate to next section:
- ⬜ = Not started
- 🔄 = In progress
- ✅ = Done (Build pass + errors fixed + committed + user confirmed)

**What "Done" means**:
1. ✅ Build passes (via mcp-xcode)
2. ✅ All errors fixed (using ios-debug if needed)
3. ✅ Changes committed to git
4. ✅ User confirms to continue

### 5.5 Task Format

```markdown
- [ ] **3.1.2.1** Create [Name]View
  - File: `Features/[Name]/Views/[Name]View.swift`
  - Wireframe: Design 3.1.1
  - Refs: AC-001.1, AC-001.3
```

### 5.6 Rules
- Task ID: `[Section].[Subsection].[Task]` (e.g., 3.1.2.1)
- MUST have: File, Design reference, Refs (AC-xxx)
- Complete each Feature before moving to next Feature
- DO NOT work on multiple Features in parallel
- DO NOT skip Checkpoints

---

## 6. Traceability

### 6.1 Traceability Chain

```
US-001 (User Story)
  └── AC-001.1 (Acceptance Criteria)
        └── Design 3.1 (Feature section)
              └── Property P1 (Correctness Property)
                    └── Task 3.1.1.2 [PBT] (Property-based test)
```

### 6.2 Traceability Matrix (in tasks.md)

| AC | Design Section | Tasks | Status |
|----|----------------|-------|--------|
| AC-001.1 | 3.1 List Screen | 3.1.1.1, 3.1.2.2 | ⬜ |
| AC-001.2 | 3.2 Detail Screen | 3.2.1.1, 3.2.2.2 | ⬜ |
| AC-002.1 | 3.3 Form Screen | 3.3.1.1, 3.3.2.1 | ⬜ |

### 6.3 Rules
- Every AC MUST have a task
- Every task MUST reference AC or Design section
- Every Property MUST reference AC

---

## 7. Agents

### 7.1 Agent Chain

| Agent | Input | Output | Skill |
|-------|-------|--------|-------|
| write-spec | Idea | requirements.md | dev-spec-driven |
| write-design | requirements.md | design.md | dev-spec-driven, ios-architecture |
| write-tasks | design.md | tasks.md | dev-spec-driven |
| execute-tasks | tasks.md | Code | dev-spec-driven, ios-architecture, ios-components |
| refine-spec | Feedback | Updated specs | dev-spec-driven |
| quick-implement | Simple idea | Code (no specs) | dev-spec-driven, ios-architecture, ios-components |

### 7.2 When to Use Which Agent

| Situation | Agent |
|-----------|-------|
| Create new feature from scratch | write-spec → write-design → write-tasks |
| Have requirements, need design | write-design → write-tasks |
| Have design, need tasks | write-tasks |
| Implement task | execute-tasks |
| Add/modify requirements | refine-spec |
| Sync tasks with code | refine-spec |
| Quick implementation (<4 hours) | quick-implement |

### 7.3 Rules
- Each agent creates 1 file
- After each file → User confirm
- DO NOT skip agents in chain

---

## 8. Advanced Features

### 8.1 Traceability Validation

**Automatic validation of references across spec files.**

#### Usage

```bash
# Validate traceability for a feature
python .claude/scripts/validate_traceability.py user-authentication
```

#### What It Checks

- ✅ All AC references in tasks.md exist in requirements.md
- ✅ All Design references in tasks.md exist in design.md
- ✅ All Property AC references exist
- ⚠️ Orphaned ACs (not referenced by any task)
- ⚠️ Missing references in tasks

#### Example Output

```
============================================================
Traceability Validation: user-authentication
============================================================

❌ VALIDATION FAILED

🔴 Broken References (1):
  - Task 3.1.2.1 references AC-005.3 (NOT FOUND)

🟠 Orphaned Items (1):
  - AC-003.2 not referenced by any task or property

============================================================
```

#### When to Run

- After creating tasks.md
- After modifying any spec file
- Before starting implementation
- As part of CI/CD pipeline

#### Integration

Add to execute-tasks agent:
```markdown
### Before Implementation

1. Validate traceability
2. Fix any broken references
3. Proceed with implementation
```

---

### 8.2 Property-Based Testing

**Framework: SwiftCheck**

#### Installation

```swift
// Package.swift
dependencies: [
    .package(url: "https://github.com/typelift/SwiftCheck", from: "0.12.0")
]
```

#### Property Types

| Type | Description | Example |
|------|-------------|---------|
| Round-trip | Encode then decode = original | JSON serialization |
| Invariant | Always true after operation | State always valid |
| Idempotent | Multiple = single execution | Delete twice = once |
| Commutative | Order doesn't matter | Add A then B = Add B then A |

#### Template Example

```swift
import SwiftCheck

func testUserRoundTrip() {
    property("User round-trip") <- forAll { (user: User) in
        let encoded = try! JSONEncoder().encode(user)
        let decoded = try! JSONDecoder().decode(User.self, from: encoded)
        return user == decoded
    }
}
```

#### In Workflow

1. **design.md**: Define properties in Section 5
2. **tasks.md**: Create [PBT] tasks (optional)
3. **execute-tasks**: Implement using SwiftCheck templates
4. **Run**: 100+ random inputs per property

#### Full Guide

See `.claude/shared/PBT_GUIDE.md` for:
- Complete templates for each property type
- Custom generators
- Best practices
- Troubleshooting

---

### 8.3 Parallel Task Execution

**Execute independent tasks simultaneously to reduce time.**

#### When to Use

✅ **Safe for parallel**:
- Tasks in different features (3.1.x and 3.2.x)
- No shared files
- No data dependencies

❌ **Must stay sequential**:
- Tasks in same feature (3.1.1 before 3.1.2)
- Shared files
- Data dependencies

#### Usage

```bash
# Sequential (default)
execute-tasks 3.1.1.1

# Parallel
execute-tasks --parallel 3.1.1.1,3.2.1.1,3.3.1.1
```

#### Example: Time Savings

```
Sequential:
- 3.1.1.1 ViewModel (1h)
- 3.2.1.1 ViewModel (1h)
- 3.3.1.1 ViewModel (1h)
Total: 3h

Parallel:
- 3.1.1.1, 3.2.1.1, 3.3.1.1 (max 1h)
Total: 1h

Savings: 67% faster!
```

#### Conflict Detection

Before parallel execution:
1. Check file conflicts
2. Check data dependencies
3. Check resource conflicts
4. If conflicts → Force sequential

#### In tasks.md

```markdown
## Parallel Execution Plan

### Group 2: ViewModels (Parallel)
- 3.1.1.1 List ViewModel
- 3.2.1.1 Detail ViewModel
- 3.3.1.1 Form ViewModel

**Checkpoint 3.x.1**: ⬜ ALL ViewModels complete
```

#### Full Guide

See `.claude/shared/PARALLEL_EXECUTION_GUIDE.md` for:
- Dependency graphs
- Conflict detection rules
- Error handling
- Best practices

---

### 8.4 Summary of Advanced Features

| Feature | Purpose | Status | Guide |
|---------|---------|--------|-------|
| Traceability Validation | Auto-check references | ✅ Ready | `.claude/scripts/validate_traceability.py` |
| Property-Based Testing | SwiftCheck integration | ✅ Ready | `.claude/shared/PBT_GUIDE.md` |
| Parallel Execution | Faster implementation | 🧪 Experimental | `.claude/shared/PARALLEL_EXECUTION_GUIDE.md` |

---

