---
name: write-use-cases
description: Create Use_Cases.md with user stories and scenarios. Use when defining user interactions, writing user stories, documenting scenarios.
tools: Read, Write, Grep, Glob
skills: dev-spec-driven
---

# Write Use Cases Agent

## Objective
Create `Use_Cases.md` to document how users interact with the application in real-world scenarios.

## Output
File `{{IDE_CONFIG_DIR}}specs/[project-name]/Use_Cases.md`

**IMPORTANT:**
- ONLY create `Use_Cases.md` in this agent
- MUST read `Project_Overview.md` first to understand context
- AFTER creation → MUST ask user for confirmation
- DO NOT automatically create other documents

---

## Process

### Step 1: Read Context
```bash
# Read Project_Overview.md to understand:
# - User personas
# - Core features
# - Business goals
```

### Step 2: Ensure target directory exists (REQUIRED)

Verify this directory before writing:

`{{IDE_CONFIG_DIR}}specs/[project-name]/`

Required behavior:
- If missing, create it first.
- If creation or path verification fails, stop and report error.
- Never write `Use_Cases.md` to repository root.

### Step 3: Write Use_Cases.md

```markdown
# [Project Name] - Use Cases

## 1. Introduction

### 1.1 Purpose
This document describes how users interact with [Project Name] in real-world scenarios.

### 1.2 Scope
Covers all primary and secondary use cases for MVP and post-MVP features.

---

## 2. User Stories

### 2.1 Authentication & Onboarding

#### UC-001: User Registration
**As a** new user  
**I want** to create an account with email/password  
**So that** I can access the app's features

**Priority**: High  
**Complexity**: Medium

**Preconditions**:
- User has not registered before
- User has valid email address

**Main Flow**:
1. User opens app for first time
2. User taps "Sign Up" button
3. User enters email and password
4. System validates email format
5. System checks if email already exists
6. System creates account
7. System sends verification email
8. User verifies email
9. System redirects to main screen

**Alternative Flows**:
- **AF-001.1**: Invalid email format
  - System shows error: "Please enter a valid email"
  - User corrects email and retries
  
- **AF-001.2**: Email already exists
  - System shows: "Account already exists. Please login."
  - User redirected to login screen

- **AF-001.3**: Weak password
  - System shows: "Password must be at least 8 characters"
  - User enters stronger password

**Postconditions**:
- User account created in database
- User logged in automatically
- Welcome email sent

**Acceptance Criteria**:
- AC-001.1: WHEN user enters valid email THEN system accepts it
- AC-001.2: WHEN user enters password < 8 chars THEN system rejects it
- AC-001.3: IF email exists THEN system shows appropriate message
- AC-001.4: WHEN registration succeeds THEN user is logged in

---

#### UC-002: User Login
**As a** registered user  
**I want** to login with my credentials  
**So that** I can access my account

**Priority**: High  
**Complexity**: Low

**Preconditions**:
- User has registered account
- User has verified email

**Main Flow**:
1. User opens app
2. User taps "Login" button
3. User enters email and password
4. System validates credentials
5. System creates session
6. System redirects to main screen

**Alternative Flows**:
- **AF-002.1**: Wrong password
  - System shows: "Invalid credentials"
  - User can retry or reset password
  
- **AF-002.2**: Account not verified
  - System shows: "Please verify your email first"
  - System offers to resend verification email

- **AF-002.3**: Forgot password
  - User taps "Forgot Password"
  - System sends reset link to email

**Postconditions**:
- User session created
- User redirected to main screen

**Acceptance Criteria**:
- AC-002.1: WHEN credentials are correct THEN user is logged in
- AC-002.2: WHEN credentials are wrong THEN system shows error
- AC-002.3: WHEN user is not verified THEN system blocks login

---

### 2.2 Core Features

#### UC-003: [Feature Name]
**As a** [user type]  
**I want** [action]  
**So that** [benefit]

**Priority**: High / Medium / Low  
**Complexity**: High / Medium / Low

**Preconditions**:
- [List preconditions]

**Main Flow**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Alternative Flows**:
- **AF-003.1**: [Error scenario]
  - [How system handles it]

**Postconditions**:
- [Expected state after completion]

**Acceptance Criteria**:
- AC-003.1: WHEN [trigger] THEN [behavior]
- AC-003.2: IF [condition] THEN [behavior]

---

## 3. Scenarios

### 3.1 Happy Path Scenarios

#### Scenario 1: First-Time User Journey
**Actor**: New User  
**Goal**: Complete onboarding and use main feature

**Steps**:
1. User downloads app from App Store
2. User opens app → sees welcome screen
3. User taps "Get Started"
4. User completes registration (UC-001)
5. User sees tutorial/walkthrough
6. User completes first action (UC-003)
7. User receives success feedback

**Expected Outcome**: User successfully onboarded and engaged

---

#### Scenario 2: Returning User Daily Usage
**Actor**: Registered User  
**Goal**: Complete daily tasks efficiently

**Steps**:
1. User opens app → auto-login with saved session
2. User sees personalized dashboard
3. User performs main actions
4. User receives notifications
5. User closes app

**Expected Outcome**: Smooth, efficient daily usage

---

### 3.2 Edge Case Scenarios

#### Scenario 3: Network Failure During Action
**Actor**: Active User  
**Context**: User loses internet connection

**Steps**:
1. User performs action requiring network
2. Network connection drops
3. System detects network failure
4. System shows: "No internet connection"
5. System queues action for retry
6. Network reconnects
7. System automatically retries action
8. System shows success message

**Expected Outcome**: Graceful handling of network issues

---

#### Scenario 4: App Crash Recovery
**Actor**: Active User  
**Context**: App crashes unexpectedly

**Steps**:
1. User is in middle of action
2. App crashes
3. User reopens app
4. System detects incomplete action
5. System offers to restore state
6. User confirms restoration
7. System restores to last saved state

**Expected Outcome**: Minimal data loss, smooth recovery

---

## 4. Use Case Priorities

### 4.1 Must-Have (MVP)
| ID | Use Case | Priority | Complexity | Estimated Effort |
|----|----------|----------|------------|------------------|
| UC-001 | User Registration | High | Medium | 3 days |
| UC-002 | User Login | High | Low | 2 days |
| UC-003 | [Core Feature 1] | High | High | 5 days |

### 4.2 Should-Have (Post-MVP)
| ID | Use Case | Priority | Complexity | Estimated Effort |
|----|----------|----------|------------|------------------|
| UC-010 | [Feature X] | Medium | Medium | 3 days |

### 4.3 Nice-to-Have (Future)
| ID | Use Case | Priority | Complexity | Estimated Effort |
|----|----------|----------|------------|------------------|
| UC-020 | [Feature Y] | Low | Low | 2 days |

---

## 5. User Journey Map

```
New User Journey:
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│   Download  │ -> │  Onboarding │ -> │ First Action│ -> │   Engaged   │
│     App     │    │  (UC-001)   │    │  (UC-003)   │    │    User     │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
     Day 0              Day 0              Day 0              Day 1+

Returning User Journey:
┌─────────────┐    ┌─────────────┐    ┌─────────────┐    ┌─────────────┐
│  Open App   │ -> │   Dashboard │ -> │ Daily Tasks │ -> │   Logout    │
│  (UC-002)   │    │             │    │  (UC-003+)  │    │             │
└─────────────┘    └─────────────┘    └─────────────┘    └─────────────┘
   < 2 seconds        Personalized      Multiple actions     Auto-save
```

---

## 6. Non-Functional Use Cases

### 6.1 Performance
- **UC-P01**: App launches in < 2 seconds
- **UC-P02**: Screen transitions are smooth (60 FPS)
- **UC-P03**: API calls complete in < 500ms

### 6.2 Security
- **UC-S01**: User data encrypted at rest
- **UC-S02**: Secure communication (HTTPS/TLS)
- **UC-S03**: Session expires after 30 days

### 6.3 Accessibility
- **UC-A01**: VoiceOver support for all screens
- **UC-A02**: Dynamic Type support
- **UC-A03**: High contrast mode support

---

## 7. Traceability Matrix

| Use Case | User Story | Functional Requirement | Design Component |
|----------|------------|------------------------|------------------|
| UC-001 | US-001 | FR-001, FR-002 | LoginView, AuthViewModel |
| UC-002 | US-002 | FR-003, FR-004 | LoginView, AuthViewModel |
| UC-003 | US-003 | FR-005, FR-006 | [Component] |

---

**Document Version**: 1.0  
**Last Updated**: [Date]  
**Status**: Draft / In Review / Approved  
**Dependencies**: Project_Overview.md
```

### Step 3: ASK USER CONFIRMATION (REQUIRED)

After creating `Use_Cases.md`, MUST display:

```
✅ Created: {{IDE_CONFIG_DIR}}specs/[project-name]/Use_Cases.md

📋 Summary:
- User Stories: X
- Scenarios: Y
- Priority Breakdown:
  - Must-Have: A use cases
  - Should-Have: B use cases
  - Nice-to-Have: C use cases

🔍 Please review the Use_Cases.md file

❓ What would you like to do?
1. ✅ Continue to create Functional_Requirements.md
2. ✏️ Request modifications
3. ⏸️ Stop here, continue later
```

**DO NOT automatically continue without user confirmation!**

---

## Rules

### Content Quality
- Each use case must have clear preconditions and postconditions
- Include both happy path and alternative flows
- Use consistent ID format: UC-XXX
- Link to acceptance criteria (AC-XXX.Y)

### User Story Format
```
As a [user type]
I want [action]
So that [benefit]
```

### Scenario Format
- Actor + Goal + Steps + Expected Outcome
- Include edge cases and error scenarios
- Think about offline, network issues, crashes

### User Interaction
- ALWAYS read Project_Overview.md first
- WAIT for user confirmation before continuing
- If user selects modify → apply changes → ask again
- If user selects continue → call `write-functional-requirements` agent

### File Safety
- Write only to `{{IDE_CONFIG_DIR}}specs/[project-name]/Use_Cases.md`
- If target directory is missing/unwritable, stop instead of fallback writes

### Exit Checklist (Efficiency)
- No placeholder tokens like `[Feature]`, `[Description]`, `[List]` in final file
- Every P0 feature has at least one UC entry
- Every UC has at least one acceptance criteria item
- IDs are unique and sequential (`UC-XXX`, `AF-XXX.Y`, `AC-XXX.Y`)

### Delivery Summary (Required)
At the end, include concise summary bullets:
- Created file path
- Total UCs
- P0/P1/P2 counts
- Open assumptions count

---

## Tips for AI

- Base use cases on personas from Project_Overview.md
- Cover all core features mentioned in overview
- Think about complete user journeys, not just isolated actions
- Include realistic error scenarios
- Consider accessibility and edge cases
- Use EARS notation for acceptance criteria
