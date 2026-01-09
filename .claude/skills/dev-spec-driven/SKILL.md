---
name: dev-spec-driven
description: Spec-driven development workflow for iOS. Use when creating new features, writing requirements, design documents, implementation plans, EARS notation, user stories, acceptance criteria, property-based testing.
allowed-tools: Read, Write, Grep, Glob
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
- ✅ = Done (Build pass + tests pass + checklist done)

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

### 7.2 When to Use Which Agent

| Situation | Agent |
|-----------|-------|
| Create new feature from scratch | write-spec → write-design → write-tasks |
| Have requirements, need design | write-design → write-tasks |
| Have design, need tasks | write-tasks |
| Implement task | execute-tasks |
| Add/modify requirements | refine-spec |
| Sync tasks with code | refine-spec |

### 7.3 Rules
- Each agent creates 1 file
- After each file → User confirm
- DO NOT skip agents in chain
