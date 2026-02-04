---
name: write-tasks
description: Create implementation plan from design. Use when creating tasks.md, breaking down work by feature, planning implementation.
tools: Read, Write, Grep, Glob
skills: dev-spec-driven
---

# Write Tasks Agent

## Objective
Read `requirements.md` and `design.md`, create `tasks.md` with:
- Tasks organized by feature (maps to Design section 3.X)
- Each feature complete before moving to next
- NO code, only task listing

## Output
File `tasks.md` in `.claude/specs/[feature-name]/`

---


## Prerequisites Validation

Before creating tasks.md, MUST validate:

### Step 1: Check requirements.md exists
```bash
if [ ! -f ".claude/specs/[feature-name]/requirements.md" ]; then
    echo "❌ ERROR: requirements.md not found"
    exit 1
fi
```

### Step 2: Check design.md exists
```bash
if [ ! -f ".claude/specs/[feature-name]/design.md" ]; then
    echo "❌ ERROR: design.md not found"
    echo "Please create design.md first using write-design agent"
    exit 1
fi
```

### Step 3: Validate design.md content
- Must have Section 2 (Shared)
- Must have Section 3 (Features) with at least 1 feature
- Must have Section 5 (Correctness Properties)

### Step 4: If validation fails
```
❌ Cannot create tasks.md

Reason: [requirements.md | design.md] not found or invalid

Please:
1. Create missing file first
2. Or check file location: .claude/specs/[feature-name]/
```

### Step 5: If validation passes
→ Continue to create tasks.md

---

## Template Tasks.md

```markdown
# [Feature Name] - Implementation Plan

## Table of Contents
- [1. Overview](#1-overview) .......................... L20-L40
- [2. Shared Tasks](#2-shared-tasks) ................. L42-L90
  - [2.1 Models](#21-models) ......................... L45-L60
  - [2.2 Services](#22-services) ..................... L62-L80
  - [2.3 Dependencies](#23-dependencies) ............. L82-L90
- [3. Feature Tasks](#3-feature-tasks) ............... L92-L280
  - [3.1 Feature: List Screen](#31-feature-list-screen) L95-L150
  - [3.2 Feature: Detail Screen](#32-feature-detail-screen) L152-L210
  - [3.3 Feature: Form Screen](#33-feature-form-screen) L212-L270
- [4. Integration Tasks](#4-integration-tasks) ....... L282-L310
- [5. Progress](#5-progress) ......................... L312-L340

---

## 1. Overview

**Feature:** [Feature name]
**Design:** design.md
**Requirements:** requirements.md

### Approach
Implement in order:
1. Shared (Models, Services) - foundation
2. Feature 3.1 (List Screen) - complete
3. Feature 3.2 (Detail Screen) - complete
4. Feature 3.3 (Form Screen) - complete
5. Integration - connect all

### Estimation
| Section | Tasks | Effort |
|---------|-------|--------|
| Shared | X | Low |
| Feature 3.1 | X | Medium |
| Feature 3.2 | X | Medium |
| Feature 3.3 | X | High |
| Integration | X | Low |
| **Total** | **XX** | **X days** |
```


---

## 2. Shared Tasks

> ⚠️ Complete Shared before starting Features

### 2.1 Models

- [ ] **2.1.1** Create [Name] model
  - File: `Features/[Name]/Models/[Name].swift`
  - Design: 2.1 Data Models
  - Refs: AC-001.1

- [ ] **2.1.2** Create [Name]Response model
  - File: `Features/[Name]/Models/[Name]Response.swift`
  - Design: 2.1 Data Models
  - Refs: AC-001.1

- [ ] **2.1.3** [PBT] Model round-trip property
  - Property: P2 - Encode then decode = original
  - File: `Tests/[Name]ModelTests.swift`
  - Design: 5. Correctness Properties
  - Optional: Yes

**Checkpoint 2.1:** ⬜ Build + all models compile

### 2.2 Services

- [ ] **2.2.1** Create [Name]Service protocol
  - File: `Features/[Name]/Services/[Name]Service.swift`
  - Methods: fetchList(), fetchDetail(id), create(), update(), delete()
  - Design: 2.2 Services
  - Refs: AC-001.1, AC-002.1

- [ ] **2.2.2** Implement [Name]Service
  - File: `Features/[Name]/Services/[Name]ServiceImpl.swift`
  - API endpoints from Design 2.2
  - Error handling from Design 2.2
  - Refs: AC-001.1, AC-002.1

**Checkpoint 2.2:** ⬜ Build + service methods callable

**Checkpoint 2:** ⬜ Shared complete, ready for Features

---

## 3. Feature Tasks

> ⚠️ Complete each Feature before moving to next
> Order: 3.1 → 3.2 → 3.3

---

### 3.1 Feature: List Screen

**Design:** Section 3.1
**Refs:** US-001, AC-001.1, AC-001.3

#### 3.1.1 ViewModel

- [ ] **3.1.1.1** Create [Name]ViewModel
  - File: `Features/[Name]/ViewModels/[Name]ViewModel.swift`
  - States: Loading, Empty, Error, Success (Design 3.1.3)
  - Actions: load(), refresh(), search(), selectItem() (Design 3.1.4)
  - Refs: AC-001.1, AC-001.3

- [ ] **3.1.1.2** [PBT] State invariant property
  - Property: P1 - Valid state transitions
  - File: `Tests/[Name]ViewModelTests.swift`
  - Optional: Yes

**Checkpoint 3.1.1:** ⬜ ViewModel compiles + unit tests pass

#### 3.1.2 Views

- [ ] **3.1.2.1** Create [Name]Card component
  - File: `Features/[Name]/Views/Components/[Name]Card.swift`
  - Wireframe: Design 3.1.1 - Item Card
  - Refs: AC-001.1

- [ ] **3.1.2.2** Create [Name]View
  - File: `Features/[Name]/Views/[Name]View.swift`
  - Wireframe: Design 3.1.1
  - States: Loading, Empty, Error, Success
  - Refs: AC-001.1, AC-001.3

**Checkpoint 3.1.2:** ⬜ Views compile + Preview works

#### 3.1.3 Verify

- [ ] **3.1.3.1** Verify Acceptance Checklist
  - [ ] AC-001.1: List displays correct data
  - [ ] AC-001.3: Error state displays correctly
  - [ ] Loading state works
  - [ ] Empty state works
  - [ ] Pull to refresh works

**Checkpoint 3.1:** ✅ Feature List Screen complete


---

### 3.2 Feature: Detail Screen

**Design:** Section 3.2
**Refs:** US-001, AC-001.2

#### 3.2.1 ViewModel

- [ ] **3.2.1.1** Create [Name]DetailViewModel
  - File: `Features/[Name]/ViewModels/[Name]DetailViewModel.swift`
  - States: Loading, Error, Success, NotFound (Design 3.2.3)
  - Actions: load(id), edit(), delete() (Design 3.2.4)
  - Refs: AC-001.2

**Checkpoint 3.2.1:** ⬜ ViewModel compiles + unit tests pass

#### 3.2.2 Views

- [ ] **3.2.2.1** Create [Name]Header component
  - File: `Features/[Name]/Views/Components/[Name]Header.swift`
  - Wireframe: Design 3.2.1 - Hero section
  - Refs: AC-001.2

- [ ] **3.2.2.2** Create [Name]DetailView
  - File: `Features/[Name]/Views/[Name]DetailView.swift`
  - Wireframe: Design 3.2.1
  - States: Loading, Error, Success, NotFound
  - Refs: AC-001.2

**Checkpoint 3.2.2:** ⬜ Views compile + Preview works

#### 3.2.3 Verify

- [ ] **3.2.3.1** Verify Acceptance Checklist
  - [ ] AC-001.2: Detail displays correct data
  - [ ] Loading state works
  - [ ] Error state works
  - [ ] NotFound state works

**Checkpoint 3.2:** ✅ Feature Detail Screen complete

---

### 3.3 Feature: Form Screen

**Design:** Section 3.3
**Refs:** US-002, AC-002.1, AC-002.2

#### 3.3.1 ViewModel

- [ ] **3.3.1.1** Create [Name]FormViewModel
  - File: `Features/[Name]/ViewModels/[Name]FormViewModel.swift`
  - States: Idle, Editing, Validating, Submitting, Success, Error (Design 3.3.3)
  - Validation: Design 3.3.4
  - Actions: updateField(), validate(), submit(), cancel() (Design 3.3.5)
  - Refs: AC-002.1, AC-002.2

- [ ] **3.3.1.2** [PBT] Form validation property
  - Property: P3 - Invalid input → cannot submit
  - File: `Tests/[Name]FormViewModelTests.swift`
  - Optional: Yes

**Checkpoint 3.3.1:** ⬜ ViewModel compiles + validation tests pass

#### 3.3.2 Views

- [ ] **3.3.2.1** Create [Name]FormView
  - File: `Features/[Name]/Views/[Name]FormView.swift`
  - Wireframe: Design 3.3.1
  - Inline validation errors
  - Refs: AC-002.1, AC-002.2

**Checkpoint 3.3.2:** ⬜ Views compile + Preview works

#### 3.3.3 Verify

- [ ] **3.3.3.1** Verify Acceptance Checklist
  - [ ] AC-002.1: Create succeeds
  - [ ] AC-002.2: Validation works
  - [ ] Inline validation errors display
  - [ ] Submit loading state works
  - [ ] Success dismiss works
  - [ ] Cancel dismiss works

**Checkpoint 3.3:** ✅ Feature Form Screen complete


---

## 4. Integration Tasks

> ⚠️ Start only after all Features complete

- [ ] **4.1** Wire navigation List → Detail
  - Navigation: Push
  - Data: itemId
  - Design: 4.2 Navigation Table
  - Refs: AC-001.1, AC-001.2

- [ ] **4.2** Wire navigation List → Form (Add)
  - Navigation: Sheet
  - Data: mode: .create
  - Design: 4.2 Navigation Table
  - Refs: AC-002.1

- [ ] **4.3** Wire navigation Detail → Form (Edit)
  - Navigation: Sheet
  - Data: mode: .edit(item)
  - Design: 4.2 Navigation Table
  - Refs: AC-002.1

- [ ] **4.4** Handle Form dismiss + refresh
  - Callback: onSave → refresh list/detail
  - Design: 4.2 Navigation Table

- [ ] **4.5** Connect to app entry point
  - Entry: Tab/Navigation
  - Design: 4.1 Flow Diagram

- [ ] **4.6** [PBT] Delete idempotent property
  - Property: P4 - Delete twice = delete once
  - File: `Tests/[Name]IntegrationTests.swift`
  - Optional: Yes

**Checkpoint 4:** ✅ Integration complete, full flow works

---

## 5. Progress

### By Section

| Section | Total | Done | Status |
|---------|-------|------|--------|
| 2. Shared | 5 | 0 | ⬜ |
| 3.1 List Screen | 5 | 0 | ⬜ |
| 3.2 Detail Screen | 4 | 0 | ⬜ |
| 3.3 Form Screen | 4 | 0 | ⬜ |
| 4. Integration | 6 | 0 | ⬜ |
| **Total** | **24** | **0** | **0%** |

### Checkpoints

| Checkpoint | Status | Date |
|------------|--------|------|
| 2. Shared complete | ⬜ | - |
| 3.1 List Screen complete | ⬜ | - |
| 3.2 Detail Screen complete | ⬜ | - |
| 3.3 Form Screen complete | ⬜ | - |
| 4. Integration complete | ⬜ | - |
| **Feature Complete** | ⬜ | - |

### PBT Tasks (Optional)

| Task | Property | Status |
|------|----------|--------|
| 2.1.3 | P2 - Model round-trip | ⬜ |
| 3.1.1.2 | P1 - State invariant | ⬜ |
| 3.3.1.2 | P3 - Form validation | ⬜ |
| 4.6 | P4 - Delete idempotent | ⬜ |

---

## Notes

### Execution Rules
1. Complete Shared (Section 2) first
2. Complete each Feature in order 3.1 → 3.2 → 3.3
3. Each Feature must pass Checkpoint before moving to next
4. Integration (Section 4) only after all Features done
5. Build + test after each Checkpoint

### Task ID Format
- `[Section].[Subsection].[Task]` (e.g., 3.1.2.1)
- Maps to Design section (e.g., Task 3.1.x → Design 3.1)

### Checkpoint Rules
- ⬜ = Not started
- 🔄 = In progress
- ✅ = Done
- Checkpoint = gate to next section

```

---

## Process

### Step 1: Read specs
1. Read `design.md` → List Features (Section 3.X)
2. Read `requirements.md` → List AC-xxx

### Step 2: Map tasks by feature

| Design Section | Tasks Section |
|----------------|---------------|
| 2. Shared | 2. Shared Tasks |
| 3.1 Feature: List | 3.1 Feature: List Screen |
| 3.2 Feature: Detail | 3.2 Feature: Detail Screen |
| 3.3 Feature: Form | 3.3 Feature: Form Screen |
| 4. Navigation | 4. Integration Tasks |

### Step 3: Write tasks.md
- Follow template above
- Each Feature has: ViewModel tasks → View tasks → Verify tasks
- Each section has Checkpoint

---

## Rules

### Feature Independence
- Each Feature (3.1, 3.2, 3.3) is independent unit
- Complete Feature before moving to next
- DO NOT work on multiple Features in parallel

### Checkpoints
- Each section has Checkpoint
- Checkpoint = Build pass + tests pass + checklist done
- DO NOT skip Checkpoints

### Task Structure
- Task ID: `X.Y.Z.W`
- MUST have: File, Design reference, Refs (AC-xxx)
- PBT task: add Property, Optional: Yes

---

## Step 3: ASK USER CONFIRMATION (REQUIRED)

After creating `tasks.md`, MUST display:

```
✅ Created: .claude/specs/[feature-name]/tasks.md

📋 Summary:
- Total Tasks: X
- Shared Tasks: Y
- Feature Tasks: Z
- Integration Tasks: W
- Estimated Effort: N days

🔍 Please review the tasks.md file

❓ What would you like to do?
1. ✅ Start implementation (invoke execute-tasks)
2. ✏️ Request modifications to tasks
3. ⏸️ Stop here, continue later
```

**CRITICAL RULES:**
- DO NOT automatically start implementation without user confirmation
- DO NOT invoke execute-tasks agent automatically
- WAIT for explicit user response
- If user selects "Start" → Call execute-tasks agent
- If user selects "Modify" → Apply changes → Ask again
- If user selects "Stop" → End here

---


---

## Parallel Execution Support

### Add to tasks.md

After creating task sections, ADD:

```markdown
## Parallel Execution Plan

### Group 1: Shared (Sequential)
[List shared tasks]

### Group 2: ViewModels (Parallel)
[List ViewModel tasks from all features]

### Group 3: Views (Parallel)
[List View tasks from all features]

### Group 4: Integration (Sequential)
[List integration tasks]
```

### Add Dependency Matrix

```markdown
## Task Dependencies

| Task | Depends On | Can Parallel With |
|------|------------|-------------------|
| 3.1.1.1 | 2.1.1 | 3.2.1.1, 3.3.1.1 |
| 3.2.1.1 | 2.1.1 | 3.1.1.1, 3.3.1.1 |
```

See `Shared/PARALLEL_EXECUTION_GUIDE.md` for details.

