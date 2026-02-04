---
name: write-design
description: Write technical design for features. Use when designing architecture, wireframes, file/folder structure, data flow, state management.
tools: Read, Write, Grep, Glob
skills: dev-spec-driven, ios-architecture
---

# Write Design Agent

## Objective
Create `design.md` from `requirements.md` with focus on:
- Organizing by independent feature/screen
- Each feature complete, not partial
- NO sample code

## Output
File `design.md` in `.claude/specs/[feature-name]/`

---


## Prerequisites Validation

Before creating design.md, MUST validate:

### Step 1: Check requirements.md exists
```bash
# Check file exists
if [ ! -f ".claude/specs/[feature-name]/requirements.md" ]; then
    echo "❌ ERROR: requirements.md not found"
    echo "Please create requirements.md first using write-spec agent"
    exit 1
fi
```

### Step 2: Validate requirements.md content
- Must have at least 1 User Story (US-XXX)
- Must have Acceptance Criteria (AC-XXX.Y)
- Must use EARS notation

### Step 3: If validation fails
```
❌ Cannot create design.md

Reason: requirements.md not found or invalid

Please:
1. Create requirements.md first: "Write requirements for [feature]"
2. Or check file location: .claude/specs/[feature-name]/requirements.md
```

### Step 4: If validation passes
→ Continue to create design.md

---

## Template Design.md

```markdown
# [Feature Name] - Technical Design

## Table of Contents
- [1. Overview](#1-overview) .......................... L20-L35
- [2. Shared](#2-shared) ............................. L37-L80
  - [2.1 Data Models](#21-data-models) ............... L40-L55
  - [2.2 Services](#22-services) ..................... L57-L70
  - [2.3 Dependencies](#23-dependencies) ............. L72-L80
- [3. Features](#3-features) ......................... L82-L300
  - [3.1 Feature: List Screen](#31-feature-list-screen) L85-L150
  - [3.2 Feature: Detail Screen](#32-feature-detail-screen) L152-L220
  - [3.3 Feature: Form Screen](#33-feature-form-screen) L222-L290
- [4. Navigation](#4-navigation) ..................... L302-L330
- [5. Correctness Properties](#5-correctness-properties) L332-L360

---

## 1. Overview

**Feature:** [Feature name]
**Refs:** US-001, US-002, ...

### Goals
- [Goal 1]
- [Goal 2]

### Scope
- Includes: [list]
- Excludes: [list]

### Feature List
| # | Feature | Screen | Priority | Refs |
|---|---------|--------|----------|------|
| 1 | List Screen | [Name]View | P0 | US-001 |
| 2 | Detail Screen | [Name]DetailView | P0 | US-001 |
| 3 | Form Screen | [Name]FormView | P1 | US-002 |
```


---

## 2. Shared

### 2.1 Data Models

| Model | Fields | Usage |
|-------|--------|-------|
| [Name] | id, title, description, createdAt | Main entity |
| [Name]Response | items, total, page | API list response |
| [Name]Request | query, page, limit | API request |

**Relationships:**
```
[Parent] 1 ──── * [Child]
```

**Files:**
- `Features/[Name]/Models/[Name].swift`
- `Features/[Name]/Models/[Name]Response.swift`

### 2.2 Services

| Service | Methods | Refs |
|---------|---------|------|
| [Name]Service | fetchList(), fetchDetail(id), create(), update(), delete() | AC-001.1, AC-002.1 |

**API Contracts:**
| Endpoint | Method | Request | Response | Refs |
|----------|--------|---------|----------|------|
| /api/[name] | GET | query, page | [Name]Response | AC-001.1 |
| /api/[name]/{id} | GET | - | [Name] | AC-001.2 |
| /api/[name] | POST | [Name]Request | [Name] | AC-002.1 |

**Error Handling:**
| Code | Handling |
|------|----------|
| 400 | Show validation error |
| 401 | Redirect to login |
| 404 | Show not found |
| 500 | Show retry |

**Files:**
- `Features/[Name]/Services/[Name]Service.swift`

### 2.3 Dependencies

| Dependency | Purpose | Required |
|------------|---------|----------|
| [Library] | [Purpose] | Yes/No |

---

## 3. Features

> ⚠️ Each feature is an independent, complete unit.
> Implement in order: 3.1 → 3.2 → 3.3

---

### 3.1 Feature: List Screen

**Refs:** US-001, AC-001.1, AC-001.3

#### 3.1.1 Wireframe

```
┌────────────────────────────┐
│ ◀ Back        Title    ⋮  │  <- Navigation Bar
├────────────────────────────┤
│ 🔍 Search...               │  <- Search Bar (optional)
├────────────────────────────┤
│  ┌──────────────────────┐  │
│  │ [Item Card]          │  │  <- List Item
│  │ Title                │  │
│  │ Subtitle        →    │  │
│  └──────────────────────┘  │
│  ┌──────────────────────┐  │
│  │ [Item Card]          │  │
│  └──────────────────────┘  │
│  ... (scrollable)          │
├────────────────────────────┤
│  [ + Add New ]             │  <- FAB/Bottom CTA
└────────────────────────────┘
```

#### 3.1.2 Components

| Component | Type | Responsibility |
|-----------|------|----------------|
| [Name]View | View | Main list screen |
| [Name]ViewModel | ViewModel | State + logic |
| [Name]Card | Component | List item UI |

#### 3.1.3 States

| State | Condition | UI |
|-------|-----------|-----|
| Loading | Initial fetch | ProgressView |
| Empty | items.isEmpty | EmptyView + CTA |
| Error | fetch failed | ErrorView + Retry |
| Success | items.count > 0 | List |

#### 3.1.4 Actions

| Action | Trigger | Effect |
|--------|---------|--------|
| load() | onAppear | Fetch list |
| refresh() | Pull to refresh | Reload list |
| search(query) | Search input | Filter list |
| selectItem(id) | Tap item | Navigate to Detail |
| addNew() | Tap CTA | Navigate to Form |

#### 3.1.5 Files

| File | Responsibility |
|------|----------------|
| `Views/[Name]View.swift` | Main screen |
| `Views/Components/[Name]Card.swift` | List item |
| `ViewModels/[Name]ViewModel.swift` | State + logic |

#### 3.1.6 Acceptance Checklist

- [ ] AC-001.1: List displays correct data
- [ ] AC-001.3: Error state displays correctly
- [ ] Loading state works
- [ ] Empty state works
- [ ] Pull to refresh works
- [ ] Navigate to Detail works


---

### 3.2 Feature: Detail Screen

**Refs:** US-001, AC-001.2

#### 3.2.1 Wireframe

```
┌────────────────────────────┐
│ ◀ Back        Title    ⋮  │  <- Navigation Bar
├────────────────────────────┤
│  ┌──────────────────────┐  │
│  │   [Hero Image]       │  │  <- Header
│  └──────────────────────┘  │
│  Title                     │  <- Content
│  ─────────────────────     │
│  Description text here     │
│  that can be multiple      │
│  lines...                  │
│  ┌──────────────────────┐  │
│  │ [Related Section]    │  │  <- Optional
│  └──────────────────────┘  │
├────────────────────────────┤
│  [ Edit ]    [ Delete ]    │  <- Actions
└────────────────────────────┘
```

#### 3.2.2 Components

| Component | Type | Responsibility |
|-----------|------|----------------|
| [Name]DetailView | View | Detail screen |
| [Name]DetailViewModel | ViewModel | State + logic |
| [Name]Header | Component | Hero section |

#### 3.2.3 States

| State | Condition | UI |
|-------|-----------|-----|
| Loading | Initial fetch | ProgressView |
| Error | fetch failed | ErrorView + Retry |
| Success | item != nil | Content |
| NotFound | 404 | NotFoundView |

#### 3.2.4 Actions

| Action | Trigger | Effect |
|--------|---------|--------|
| load(id) | onAppear | Fetch detail |
| edit() | Tap Edit | Navigate to Form |
| delete() | Tap Delete | Confirm + Delete |
| goBack() | Tap Back | Pop navigation |

#### 3.2.5 Files

| File | Responsibility |
|------|----------------|
| `Views/[Name]DetailView.swift` | Detail screen |
| `Views/Components/[Name]Header.swift` | Hero section |
| `ViewModels/[Name]DetailViewModel.swift` | State + logic |

#### 3.2.6 Acceptance Checklist

- [ ] AC-001.2: Detail displays correct data
- [ ] Loading state works
- [ ] Error state works
- [ ] Edit navigation works
- [ ] Delete with confirmation works

---

### 3.3 Feature: Form Screen

**Refs:** US-002, AC-002.1, AC-002.2

#### 3.3.1 Wireframe

```
┌────────────────────────────┐
│ ✕ Cancel      Title   Save │  <- Navigation Bar
├────────────────────────────┤
│  Label                     │
│  ┌──────────────────────┐  │
│  │ Text input           │  │  <- Input field
│  └──────────────────────┘  │
│  ⚠️ Error message          │  <- Validation error
│  Label                     │
│  ┌──────────────────────┐  │
│  │ Text input           │  │
│  └──────────────────────┘  │
│  Label                     │
│  ┌──────────────────────┐  │
│  │ Dropdown         ▼   │  │  <- Picker
│  └──────────────────────┘  │
├────────────────────────────┤
│  [ Save ]                  │  <- Primary CTA
└────────────────────────────┘
```

#### 3.3.2 Components

| Component | Type | Responsibility |
|-----------|------|----------------|
| [Name]FormView | View | Form screen |
| [Name]FormViewModel | ViewModel | Validation + submit |

#### 3.3.3 States

| State | Condition | UI |
|-------|-----------|-----|
| Idle | Initial | Empty form |
| Editing | Has input | Form with data |
| Validating | On submit | Check fields |
| Submitting | API call | Loading indicator |
| Success | Submit done | Dismiss + callback |
| Error | Submit failed | Error message |

#### 3.3.4 Validation Rules

| Field | Rules | Error Message |
|-------|-------|---------------|
| title | required, min 3 chars | "Title is required" |
| description | optional, max 500 chars | "Too long" |

#### 3.3.5 Actions

| Action | Trigger | Effect |
|--------|---------|--------|
| updateField(field, value) | Input change | Update state |
| validate() | On submit | Check all fields |
| submit() | Tap Save | API call |
| cancel() | Tap Cancel | Dismiss |

#### 3.3.6 Files

| File | Responsibility |
|------|----------------|
| `Views/[Name]FormView.swift` | Form screen |
| `ViewModels/[Name]FormViewModel.swift` | Validation + submit |

#### 3.3.7 Acceptance Checklist

- [ ] AC-002.1: Create succeeds
- [ ] AC-002.2: Validation works
- [ ] Inline validation errors display
- [ ] Submit loading state works
- [ ] Success dismiss + callback works
- [ ] Cancel dismiss works


---

## 4. Navigation

### 4.1 Flow Diagram

```
┌─────────────┐     tap item     ┌─────────────────┐
│  List       │ ───────────────▶ │  Detail         │
│  Screen     │                  │  Screen         │
└──────┬──────┘                  └────────┬────────┘
       │                                  │
       │ tap add                          │ tap edit
       ▼                                  ▼
┌─────────────────────────────────────────────────┐
│                  Form Screen                     │
│              (Modal presentation)                │
└─────────────────────────────────────────────────┘
```

### 4.2 Navigation Table

| From | To | Trigger | Presentation | Data |
|------|----|---------|--------------|------|
| List | Detail | Tap item | Push | itemId |
| List | Form | Tap Add | Sheet | mode: .create |
| Detail | Form | Tap Edit | Sheet | mode: .edit(item) |
| Form | List/Detail | Save success | Dismiss | refresh flag |

---

## 5. Correctness Properties

| # | Property | Type | Validates | Statement |
|---|----------|------|-----------|-----------|
| P1 | List-Detail consistency | Invariant | AC-001.1, AC-001.2 | Item in list = item in detail |
| P2 | Model round-trip | Round-trip | AC-001.1 | Encode then decode = original |
| P3 | Form validation | Invariant | AC-002.2 | Invalid input → cannot submit |
| P4 | Delete idempotent | Idempotent | AC-002.1 | Delete twice = delete once |

---

## Folder Structure

```
Features/
└── [FeatureName]/
    ├── Views/
    │   ├── [Name]View.swift          <- 3.1
    │   ├── [Name]DetailView.swift    <- 3.2
    │   ├── [Name]FormView.swift      <- 3.3
    │   └── Components/
    │       ├── [Name]Card.swift      <- 3.1
    │       └── [Name]Header.swift    <- 3.2
    ├── ViewModels/
    │   ├── [Name]ViewModel.swift     <- 3.1
    │   ├── [Name]DetailViewModel.swift <- 3.2
    │   └── [Name]FormViewModel.swift <- 3.3
    ├── Models/
    │   ├── [Name].swift              <- 2.1
    │   └── [Name]Response.swift      <- 2.1
    └── Services/
        └── [Name]Service.swift       <- 2.2
```

---

## Rules

### Feature Independence
1. Each feature (3.1, 3.2, 3.3) is an independent unit
2. Each feature has: Wireframe, Components, States, Actions, Files, Checklist
3. Implement features in order, complete one before moving to next

### Checklist
- Each feature MUST have Acceptance Checklist
- Checklist maps to AC-xxx
- Feature is "done" only when all checklist items pass

### Naming
- Feature section: `3.X Feature: [Screen Name]`
- Sub-sections: `3.X.1 Wireframe`, `3.X.2 Components`, ...

### Table of Contents
- Update line numbers after completion
- Format: `[Section](#anchor) ... LXXX-LYYY`

---

## Step 3: ASK USER CONFIRMATION (REQUIRED)

After creating `design.md`, MUST display:

```
✅ Created: .claude/specs/[feature-name]/design.md

📋 Summary:
- Features: X screens/components
- Shared: Y models, Z services
- Properties: W correctness properties

🔍 Please review the design.md file

❓ What would you like to do?
1. ✅ Continue to create tasks.md
2. ✏️ Request modifications to design
3. ⏸️ Stop here, continue later
```

**CRITICAL RULES:**
- DO NOT automatically continue without user confirmation
- DO NOT invoke write-tasks agent automatically
- WAIT for explicit user response
- If user selects "Continue" → Call write-tasks agent
- If user selects "Modify" → Apply changes → Ask again
- If user selects "Stop" → End here

---


---

## Property-Based Testing

### In Section 5: Correctness Properties

For each property, specify:

```markdown
| # | Property | Type | Validates | Statement |
|---|----------|------|-----------|-----------|
| P1 | User round-trip | Round-trip | AC-001.1 | Encode then decode = original |
| P2 | State invariant | Invariant | AC-002.1 | State always valid |
| P3 | Form validation | Invariant | AC-003.1 | Invalid input → cannot submit |
| P4 | Delete idempotent | Idempotent | AC-004.1 | Delete twice = delete once |
```

**Property Types**:
- **Round-trip**: Encode/decode, serialize/deserialize
- **Invariant**: Always true after any operation
- **Idempotent**: Multiple executions = single execution
- **Commutative**: Order doesn't matter

**Framework**: SwiftCheck (see `.claude/shared/PBT_GUIDE.md`)

### PBT Task Generation

For each property, tasks.md will include:

```markdown
- [ ] **X.Y.Z** [PBT] Property PX: [name]
  - Property: [statement]
  - File: `Tests/PropertyTests/[Name]PropertyTests.swift`
  - Framework: SwiftCheck
  - Validates: AC-XXX.Y
  - Optional: Yes
```

