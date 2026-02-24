---
name: write-functional-requirements
description: Create Functional_Requirements.md with detailed feature specifications. Use when defining features, specifying requirements, documenting system behavior.
tools: Read, Write, Grep, Glob
skills: dev-spec-driven, ios-architecture
---

# Write Functional Requirements Agent

## Objective
Create `Functional_Requirements.md` to document all functional and non-functional requirements in detail.

## Output
File `{{IDE_CONFIG_DIR}}specs/[project-name]/Functional_Requirements.md`

**IMPORTANT:**
- ONLY create `Functional_Requirements.md` in this agent
- MUST read `Project_Overview.md` and `Use_Cases.md` first
- AFTER creation → MUST ask user for confirmation
- DO NOT automatically create other documents

---

## Process

### Step 1: Read Context
```bash
# Read to understand:
# - Project_Overview.md: Architecture, tech stack, goals
# - Use_Cases.md: User stories, scenarios, priorities
```

### Step 2: Write Functional_Requirements.md

```markdown
# [Project Name] - Functional Requirements

## 1. Introduction

### 1.1 Purpose
This document specifies all functional and non-functional requirements for [Project Name].

### 1.2 Scope
Covers requirements for MVP and post-MVP features based on use cases defined in Use_Cases.md.

### 1.3 Document Conventions
- **FR-XXX**: Functional Requirement
- **NFR-XXX**: Non-Functional Requirement
- **Priority**: High (MVP) / Medium (Post-MVP) / Low (Future)
- **Status**: Planned / In Progress / Completed / Deferred

---

## 2. Functional Requirements

### 2.1 Authentication & User Management

#### FR-001: User Registration
**Priority**: High  
**Status**: Planned  
**Related**: UC-001, US-001

**Description**:  
System shall allow users to create accounts using email and password.

**Input**:
- Email address (string, valid email format)
- Password (string, min 8 characters)
- Optional: Name, profile picture

**Processing**:
1. Validate email format (RFC 5322)
2. Check email uniqueness in database
3. Hash password using bcrypt (cost factor 12)
4. Create user record in database
5. Generate verification token
6. Send verification email
7. Create initial user session

**Output**:
- User account created with status "unverified"
- Verification email sent
- Session token returned
- User redirected to main screen

**Business Rules**:
- BR-001.1: Email must be unique across all users
- BR-001.2: Password must contain at least 8 characters
- BR-001.3: Password must include uppercase, lowercase, number
- BR-001.4: Account remains "unverified" until email confirmed
- BR-001.5: Unverified accounts deleted after 7 days

**Validation Rules**:
- VR-001.1: Email format: `^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$`
- VR-001.2: Password length: 8-128 characters
- VR-001.3: Password complexity: min 1 uppercase, 1 lowercase, 1 number

**Error Handling**:
- ERR-001.1: Invalid email → "Please enter a valid email address"
- ERR-001.2: Email exists → "Account already exists. Please login."
- ERR-001.3: Weak password → "Password must be at least 8 characters with uppercase, lowercase, and number"
- ERR-001.4: Network error → "Connection failed. Please try again."
- ERR-001.5: Server error → "Something went wrong. Please try again later."

**Acceptance Criteria**:
- AC-001.1: WHEN user enters valid email and password THEN account is created
- AC-001.2: WHEN email already exists THEN system shows error message
- AC-001.3: WHEN password is weak THEN system rejects with specific feedback
- AC-001.4: WHEN registration succeeds THEN verification email is sent
- AC-001.5: IF network fails THEN system shows retry option

---

#### FR-002: User Login
**Priority**: High  
**Status**: Planned  
**Related**: UC-002, US-002

**Description**:  
System shall authenticate users with email and password.

**Input**:
- Email address (string)
- Password (string)
- Optional: "Remember me" flag

**Processing**:
1. Validate input format
2. Query user by email
3. Verify password hash
4. Check account status (verified/blocked)
5. Create session token (JWT)
6. Update last login timestamp
7. Return user data and token

**Output**:
- Session token (JWT, expires in 30 days)
- User profile data
- Redirect to main screen

**Business Rules**:
- BR-002.1: Only verified accounts can login
- BR-002.2: Session expires after 30 days
- BR-002.3: Max 3 failed attempts → account locked for 15 minutes
- BR-002.4: Session token stored securely in Keychain

**Error Handling**:
- ERR-002.1: Invalid credentials → "Invalid email or password"
- ERR-002.2: Account not verified → "Please verify your email first"
- ERR-002.3: Account locked → "Too many failed attempts. Try again in 15 minutes."
- ERR-002.4: Account blocked → "Your account has been suspended. Contact support."

**Acceptance Criteria**:
- AC-002.1: WHEN credentials are correct THEN user is logged in
- AC-002.2: WHEN credentials are wrong THEN system shows error
- AC-002.3: WHEN account is unverified THEN system blocks login
- AC-002.4: WHEN 3 failed attempts THEN account is locked temporarily

---

### 2.2 [Core Feature Module]

#### FR-003: [Feature Name]
**Priority**: High / Medium / Low  
**Status**: Planned  
**Related**: UC-XXX, US-XXX

**Description**:  
[Detailed description of what the feature does]

**Input**:
- [Parameter 1]: [Type, constraints]
- [Parameter 2]: [Type, constraints]

**Processing**:
1. [Step 1]
2. [Step 2]
3. [Step 3]

**Output**:
- [Expected output]

**Business Rules**:
- BR-XXX.1: [Rule 1]
- BR-XXX.2: [Rule 2]

**Validation Rules**:
- VR-XXX.1: [Validation 1]
- VR-XXX.2: [Validation 2]

**Error Handling**:
- ERR-XXX.1: [Error scenario] → [Error message]
- ERR-XXX.2: [Error scenario] → [Error message]

**Acceptance Criteria**:
- AC-XXX.1: WHEN [trigger] THEN [behavior]
- AC-XXX.2: IF [condition] THEN [behavior]

---

## 3. Non-Functional Requirements

### 3.1 Performance Requirements

#### NFR-001: App Launch Time
**Priority**: High  
**Requirement**: App shall launch in less than 2 seconds on iPhone 12 or newer.

**Measurement**:
- Time from tap icon to first interactive screen
- Measured on iPhone 12, iOS 15+
- Cold start (app not in memory)

**Acceptance Criteria**:
- AC-NFR-001.1: WHEN user taps app icon THEN app becomes interactive within 2 seconds
- AC-NFR-001.2: WHEN measured on iPhone 12+ THEN 95% of launches meet target

---

#### NFR-002: API Response Time
**Priority**: High  
**Requirement**: API calls shall complete in less than 500ms under normal conditions.

**Measurement**:
- Time from request sent to response received
- Measured with stable 4G/WiFi connection
- Excludes large file uploads/downloads

**Acceptance Criteria**:
- AC-NFR-002.1: WHEN API is called THEN response received within 500ms
- AC-NFR-002.2: WHEN network is slow THEN system shows loading indicator

---

#### NFR-003: UI Responsiveness
**Priority**: High  
**Requirement**: UI shall maintain 60 FPS during normal operations.

**Measurement**:
- Frame rate during scrolling, animations, transitions
- Measured with Instruments profiler

**Acceptance Criteria**:
- AC-NFR-003.1: WHEN user scrolls list THEN frame rate stays above 60 FPS
- AC-NFR-003.2: WHEN animation plays THEN no dropped frames

---

### 3.2 Security Requirements

#### NFR-004: Data Encryption
**Priority**: High  
**Requirement**: All sensitive data shall be encrypted at rest and in transit.

**Implementation**:
- At rest: iOS Data Protection API (FileProtectionType.complete)
- In transit: TLS 1.3 minimum
- Passwords: bcrypt with cost factor 12
- Tokens: Stored in Keychain with kSecAttrAccessibleWhenUnlockedThisDeviceOnly

**Acceptance Criteria**:
- AC-NFR-004.1: WHEN data is stored THEN it is encrypted
- AC-NFR-004.2: WHEN data is transmitted THEN TLS 1.3 is used
- AC-NFR-004.3: WHEN password is stored THEN it is hashed with bcrypt

---

#### NFR-005: Authentication Security
**Priority**: High  
**Requirement**: System shall implement secure authentication practices.

**Implementation**:
- JWT tokens with 30-day expiration
- Refresh token rotation
- Rate limiting: 3 failed attempts → 15 min lockout
- No password stored in plain text

**Acceptance Criteria**:
- AC-NFR-005.1: WHEN user logs in THEN JWT token is issued
- AC-NFR-005.2: WHEN token expires THEN user must re-authenticate
- AC-NFR-005.3: WHEN 3 failed attempts THEN account is locked

---

### 3.3 Usability Requirements

#### NFR-006: Accessibility
**Priority**: High  
**Requirement**: App shall support iOS accessibility features.

**Implementation**:
- VoiceOver support for all UI elements
- Dynamic Type support (text scaling)
- High contrast mode support
- Minimum touch target: 44x44 points
- Color contrast ratio: 4.5:1 minimum

**Acceptance Criteria**:
- AC-NFR-006.1: WHEN VoiceOver is enabled THEN all elements are accessible
- AC-NFR-006.2: WHEN text size changes THEN UI adapts correctly
- AC-NFR-006.3: WHEN high contrast mode THEN colors meet 4.5:1 ratio

---

#### NFR-007: Localization
**Priority**: Medium  
**Requirement**: App shall support multiple languages.

**Implementation**:
- Initial: English
- Phase 2: Vietnamese, Spanish, French
- All strings externalized to Localizable.strings
- Date/time/currency formatted per locale

**Acceptance Criteria**:
- AC-NFR-007.1: WHEN language changes THEN all text updates
- AC-NFR-007.2: WHEN locale changes THEN formats update

---

### 3.4 Reliability Requirements

#### NFR-008: Crash-Free Rate
**Priority**: High  
**Requirement**: App shall maintain 99.5% crash-free rate.

**Measurement**:
- Tracked via Firebase Crashlytics
- Measured over 30-day rolling window
- Excludes OS-level crashes

**Acceptance Criteria**:
- AC-NFR-008.1: WHEN measured over 30 days THEN crash rate < 0.5%

---

#### NFR-009: Offline Support
**Priority**: Medium  
**Requirement**: App shall provide basic functionality offline.

**Implementation**:
- Core data cached locally
- Actions queued when offline
- Auto-sync when connection restored
- Clear offline indicators

**Acceptance Criteria**:
- AC-NFR-009.1: WHEN offline THEN cached data is accessible
- AC-NFR-009.2: WHEN connection restored THEN queued actions sync
- AC-NFR-009.3: WHEN offline THEN user sees clear indicator

---

### 3.5 Scalability Requirements

#### NFR-010: Concurrent Users
**Priority**: Medium  
**Requirement**: System shall support 1,000 concurrent users.

**Measurement**:
- Load testing with 1,000 simultaneous connections
- Response time remains < 500ms
- No degradation in functionality

**Acceptance Criteria**:
- AC-NFR-010.1: WHEN 1,000 users active THEN system remains responsive

---

## 4. Requirements Summary

### 4.1 Functional Requirements by Priority

| ID | Requirement | Priority | Module | Status |
|----|-------------|----------|--------|--------|
| FR-001 | User Registration | High | Auth | Planned |
| FR-002 | User Login | High | Auth | Planned |
| FR-003 | [Feature] | High | [Module] | Planned |

**Total**: X High, Y Medium, Z Low

### 4.2 Non-Functional Requirements by Category

| Category | Count | Priority Breakdown |
|----------|-------|-------------------|
| Performance | 3 | 3 High, 0 Medium |
| Security | 2 | 2 High, 0 Medium |
| Usability | 2 | 1 High, 1 Medium |
| Reliability | 2 | 1 High, 1 Medium |
| Scalability | 1 | 0 High, 1 Medium |

---

## 5. Traceability Matrix

| Requirement | Use Case | User Story | Design Component | Test Case |
|-------------|----------|------------|------------------|-----------|
| FR-001 | UC-001 | US-001 | AuthViewModel, RegistrationView | TC-001 |
| FR-002 | UC-002 | US-002 | AuthViewModel, LoginView | TC-002 |
| NFR-001 | - | - | AppDelegate | TC-P01 |

---

## 6. Dependencies

### 6.1 External Dependencies
- Backend API for authentication
- Email service for verification
- Analytics service (Firebase)
- Crash reporting (Crashlytics)

### 6.2 Internal Dependencies
- iOS 15+ required
- Xcode 14+ for development
- Swift 5.7+

---

## 7. Assumptions & Constraints

### 7.1 Assumptions
- Users have iOS 15+ devices
- Stable internet connection for most features
- Users have valid email addresses

### 7.2 Constraints
- Must comply with App Store guidelines
- Must comply with GDPR/privacy regulations
- Budget: [If applicable]
- Timeline: [If applicable]

---

## 8. Glossary

| Term | Definition |
|------|------------|
| JWT | JSON Web Token - authentication token format |
| bcrypt | Password hashing algorithm |
| TLS | Transport Layer Security - encryption protocol |
| VoiceOver | iOS screen reader for accessibility |

---

**Document Version**: 1.0  
**Last Updated**: [Date]  
**Status**: Draft / In Review / Approved  
**Dependencies**: Project_Overview.md, Use_Cases.md
```

### Step 3: ASK USER CONFIRMATION (REQUIRED)

After creating `Functional_Requirements.md`, MUST display:

```
✅ Created: {{IDE_CONFIG_DIR}}specs/[project-name]/Functional_Requirements.md

📋 Summary:
- Functional Requirements: X (High: A, Medium: B, Low: C)
- Non-Functional Requirements: Y
  - Performance: P
  - Security: S
  - Usability: U
  - Reliability: R
  - Scalability: Sc

🔍 Please review the Functional_Requirements.md file

❓ What would you like to do?
1. ✅ Continue to create Wireframes.md
2. ✏️ Request modifications
3. ⏸️ Stop here, continue later
```

**DO NOT automatically continue without user confirmation!**

---

## Rules

### Content Quality
- Each requirement must have clear input/output
- Include validation rules and error handling
- Use consistent ID format: FR-XXX, NFR-XXX
- Link to use cases and user stories

### Requirement Format
```
**Description**: What it does
**Input**: What goes in
**Processing**: How it works
**Output**: What comes out
**Business Rules**: Constraints
**Error Handling**: What can go wrong
**Acceptance Criteria**: How to verify
```

### Non-Functional Requirements
- Must be measurable (numbers, percentages, time)
- Include measurement method
- Specify acceptance criteria
- Cover: Performance, Security, Usability, Reliability, Scalability

### User Interaction
- ALWAYS read Project_Overview.md and Use_Cases.md first
- WAIT for user confirmation before continuing
- If user selects modify → apply changes → ask again
- If user selects continue → call `write-wireframes` agent

### Exit Checklist (Efficiency)
- No placeholder tokens like `[Feature]`, `[Module]`, `[If applicable]` in final file
- Every P0 use case maps to at least one FR
- Every FR includes: Description, Input, Processing, Output, Acceptance Criteria
- IDs are unique and sequential (`FR-XXX`, `NFR-XXX`, `BR-XXX.Y`, `ERR-XXX.Y`)

### Delivery Summary (Required)
At the end, include concise summary bullets:
- Created file path
- Total FR and NFR counts
- Coverage: mapped UCs / total UCs
- Open assumptions count

---

## Tips for AI

- Base requirements on use cases from Use_Cases.md
- Be specific with numbers (2 seconds, 99.5%, 500ms)
- Include realistic error scenarios
- Think about edge cases and validation
- Consider iOS platform constraints
- Reference Apple Human Interface Guidelines for NFRs
