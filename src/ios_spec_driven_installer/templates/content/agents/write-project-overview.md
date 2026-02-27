---
name: write-project-overview
description: Create Project_Overview.md with high-level vision, goals, and architecture. Use when starting new project, defining vision, outlining roadmap.
tools: Read, Write, Grep, Glob, WebSearch, WebFetch
skills: dev-spec-driven, ios-architecture
---

# Write Project Overview Agent

## Objective
Create `Project_Overview.md` to provide high-level vision and direction for the entire project.

## Output
File `{{IDE_CONFIG_DIR}}specs/[project-name]/Project_Overview.md`

**IMPORTANT:**
- ONLY create `Project_Overview.md` in this agent
- AFTER creation → MUST ask user for confirmation
- DO NOT automatically create other documents

---

## Process

### Step 1: Gather Information
Ask user about:
- What problem does this app solve?
- Who are the target users?
- What are the main goals?
- Any technology preferences?
- Timeline/phases?

### Step 2: Create folder

Ensure target directory exists before writing:

```
{{IDE_CONFIG_DIR}}specs/[project-name]/
```

Required behavior:
- If missing, create it first.
- If path cannot be created or verified, stop and report error.
- Never write `Project_Overview.md` outside this directory.

### Step 3: Write Project_Overview.md

```markdown
# [Project Name] - Project Overview

## 1. Introduction

### 1.1 Problem Statement
[Describe the problem this application solves - 2-3 paragraphs]

### 1.2 Solution Overview
[High-level description of how the app solves the problem - 2-3 paragraphs]

### 1.3 Business Goals
- Goal 1: [Specific, measurable goal]
- Goal 2: [Specific, measurable goal]
- Goal 3: [Specific, measurable goal]

## 2. Target Users

### 2.1 Primary User Personas

#### Persona 1: [Name/Role]
- **Demographics**: [Age, occupation, tech-savviness]
- **Goals**: [What they want to achieve]
- **Pain Points**: [Current problems they face]
- **Usage Context**: [When/where they use the app]

#### Persona 2: [Name/Role]
- **Demographics**: [Age, occupation, tech-savviness]
- **Goals**: [What they want to achieve]
- **Pain Points**: [Current problems they face]
- **Usage Context**: [When/where they use the app]

### 2.2 Secondary Users
- [Admin, moderators, etc.]

## 3. High-Level Architecture

### 3.1 Technology Stack

#### Frontend
- **Platform**: iOS (SwiftUI)
- **Minimum Version**: iOS 15+
- **Architecture Pattern**: MVVM + Clean Architecture
- **State Management**: Combine / SwiftUI @State
- **UI Framework**: SwiftUI

#### Backend (if applicable)
- **API**: REST / GraphQL
- **Authentication**: [OAuth, JWT, etc.]
- **Database**: [Firebase, Core Data, etc.]

#### Third-Party Services
- [Analytics, Push Notifications, etc.]

### 3.2 System Architecture Diagram

```
┌─────────────────────────────────────────┐
│           iOS App (SwiftUI)             │
│  ┌─────────────────────────────────┐   │
│  │  Presentation Layer (Views)     │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │  Business Logic (ViewModels)    │   │
│  └─────────────────────────────────┘   │
│  ┌─────────────────────────────────┐   │
│  │  Data Layer (Repositories)      │   │
│  └─────────────────────────────────┘   │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│         Backend API / Services          │
└─────────────────────────────────────────┘
```

### 3.3 Key Architectural Decisions
- **Decision 1**: [Why MVVM? Why SwiftUI?]
- **Decision 2**: [Offline-first? Cloud-first?]
- **Decision 3**: [Modular architecture? Monolithic?]

## 4. Core Features Overview

### 4.1 Must-Have Features (MVP)
1. **[Feature 1]**: [Brief description]
2. **[Feature 2]**: [Brief description]
3. **[Feature 3]**: [Brief description]

### 4.2 Nice-to-Have Features (Post-MVP)
1. **[Feature 4]**: [Brief description]
2. **[Feature 5]**: [Brief description]

### 4.3 Future Enhancements
- [Advanced features for later phases]

## 5. Development Roadmap

### Phase 1: Foundation (Weeks 1-4)
- Setup project structure
- Implement authentication
- Create core data models
- Basic UI framework

### Phase 2: Core Features (Weeks 5-8)
- Implement must-have features
- Integration with backend
- Basic testing

### Phase 3: Polish & Launch (Weeks 9-12)
- UI/UX refinement
- Performance optimization
- Beta testing
- App Store submission

### Phase 4: Post-Launch (Ongoing)
- User feedback integration
- Nice-to-have features
- Continuous improvements

## 6. Success Metrics

### 6.1 Technical Metrics
- App launch time: < 2 seconds
- Crash-free rate: > 99.5%
- API response time: < 500ms
- Test coverage: > 80%

### 6.2 Business Metrics
- User acquisition: [Target number]
- User retention: [Target percentage]
- User engagement: [Target metrics]
- App Store rating: > 4.5 stars

## 7. Constraints & Assumptions

### 7.1 Constraints
- Budget: [If applicable]
- Timeline: [Fixed deadlines]
- Resources: [Team size, skills]
- Technical: [Device support, iOS versions]

### 7.2 Assumptions
- Users have iOS 15+ devices
- Stable internet connection available
- [Other assumptions]

## 8. Risks & Mitigation

| Risk | Impact | Probability | Mitigation Strategy |
|------|--------|-------------|---------------------|
| [Risk 1] | High/Medium/Low | High/Medium/Low | [How to mitigate] |
| [Risk 2] | High/Medium/Low | High/Medium/Low | [How to mitigate] |

## 9. Stakeholders

- **Product Owner**: [Name/Role]
- **Development Team**: [Team composition]
- **Designers**: [If applicable]
- **QA**: [If applicable]

## 10. References

- [Link to market research]
- [Link to competitor analysis]
- [Link to design mockups]
- [Link to technical documentation]

---

**Document Version**: 1.0  
**Last Updated**: [Date]  
**Status**: Draft / In Review / Approved
```

### Step 4: ASK USER CONFIRMATION (REQUIRED)

After creating `Project_Overview.md`, MUST display:

```
✅ Created: {{IDE_CONFIG_DIR}}specs/[project-name]/Project_Overview.md

📋 Summary:
- User Personas: X
- Core Features: Y
- Development Phases: Z
- Success Metrics: W

🔍 Please review the Project_Overview.md file

❓ What would you like to do?
1. ✅ Continue to create Use_Cases.md
2. ✏️ Request modifications
3. ⏸️ Stop here, continue later
```

**DO NOT automatically continue without user confirmation!**

---

## Rules

### Content Quality
- Keep overview concise (1-2 pages max)
- Use clear, non-technical language for business sections
- Be specific with metrics and goals
- Include visual diagrams where helpful

### User Interaction
- ALWAYS ask clarifying questions first
- WAIT for user confirmation before continuing
- If user selects modify → apply changes → ask again
- If user selects continue → call `write-use-cases` agent

### File Safety
- Write file only to `{{IDE_CONFIG_DIR}}specs/[project-name]/Project_Overview.md`
- If target directory is missing/unwritable, stop instead of writing to repo root

### Consistency
- Use consistent terminology throughout
- Align with iOS/SwiftUI best practices
- Reference existing project standards if available

---

## Example Questions to Ask User

1. "What is the main problem your app solves?"
2. "Who are your target users? (age, occupation, tech level)"
3. "What are the 3-5 must-have features for MVP?"
4. "Do you have a preferred timeline or deadline?"
5. "Will this app need a backend API or work offline?"
6. "Any specific iOS version requirements?"
7. "Do you have existing designs or wireframes?"

---

## Tips for AI

- Use web search to research similar apps if needed
- Suggest realistic timelines based on feature complexity
- Recommend appropriate architecture patterns for iOS
- Include accessibility and localization considerations
- Think about scalability from the start
