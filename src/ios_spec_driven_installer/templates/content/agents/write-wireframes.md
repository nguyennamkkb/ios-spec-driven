---
name: write-wireframes
description: Create Wireframes.md with UI mockups and screen descriptions. Use when designing UI, creating mockups, documenting screens.
tools: Read, Write, Grep, Glob, WebSearch, WebFetch
skills: dev-spec-driven, ios-ui-ux, ios-components
---

# Write Wireframes Agent

## Objective
Create `Wireframes.md` to document UI design and screen layouts with ASCII art and descriptions.

## Output
File `{{IDE_CONFIG_DIR}}specs/[project-name]/Wireframes.md`

**IMPORTANT:**
- ONLY create `Wireframes.md` in this agent
- MUST read previous documents for context
- AFTER creation → MUST ask user for confirmation
- DO NOT automatically create other documents

---

## Process

### Step 1: Read Context
```bash
# Read to understand:
# - Project_Overview.md: User personas, goals
# - Use_Cases.md: User flows, interactions
# - Functional_Requirements.md: Features to design
```

### Step 2: Write Wireframes.md

```markdown
# [Project Name] - Wireframes

## 1. Introduction

### 1.1 Purpose
This document provides visual representations of all screens and UI components for [Project Name].

### 1.2 Design Principles
- **Simplicity**: Clean, uncluttered interfaces
- **Consistency**: Unified design language across screens
- **Accessibility**: Support for VoiceOver, Dynamic Type
- **iOS Native**: Follow Apple Human Interface Guidelines

### 1.3 Design System
- **Typography**: SF Pro (system font)
- **Color Palette**: 
  - Primary: #007AFF (iOS Blue)
  - Secondary: #5856D6 (iOS Purple)
  - Success: #34C759 (iOS Green)
  - Error: #FF3B30 (iOS Red)
  - Background: System Background
  - Text: Label, Secondary Label
- **Spacing**: 8pt grid system
- **Corner Radius**: 8pt for cards, 12pt for buttons

---

## 2. Screen Inventory

| Screen ID | Screen Name | Priority | Related FR | Status |
|-----------|-------------|----------|------------|--------|
| WF-001 | Splash Screen | High | - | Draft |
| WF-002 | Onboarding | High | - | Draft |
| WF-003 | Login | High | FR-002 | Draft |
| WF-004 | Registration | High | FR-001 | Draft |
| WF-005 | Main Dashboard | High | FR-003 | Draft |
| WF-006 | [Feature Screen] | High | FR-XXX | Draft |

---

## 3. Authentication Screens

### WF-001: Splash Screen
**Purpose**: App launch screen with branding  
**Related**: -  
**Priority**: High

#### Layout
```
┌─────────────────────────────────────┐
│                                     │
│                                     │
│                                     │
│            [App Logo]               │
│                                     │
│          [App Name]                 │
│                                     │
│         [Loading...]                │
│                                     │
│                                     │
│                                     │
│                                     │
└─────────────────────────────────────┘
```

#### Components
- **App Logo**: Centered, 120x120pt
- **App Name**: SF Pro Display, 24pt, Bold
- **Loading Indicator**: System activity indicator

#### Behavior
- Shows for max 2 seconds
- Auto-transitions to Onboarding (first launch) or Main Dashboard (logged in)
- No user interaction

---

### WF-002: Onboarding
**Purpose**: Introduce app features to new users  
**Related**: UC-001  
**Priority**: High

#### Layout
```
┌─────────────────────────────────────┐
│  [Skip]                             │
│                                     │
│         [Feature Image]             │
│                                     │
│      Feature Title                  │
│                                     │
│   Feature description text that     │
│   explains the benefit to users     │
│                                     │
│         ● ○ ○                       │
│                                     │
│      [Next Button]                  │
│                                     │
└─────────────────────────────────────┘
```

#### Components
- **Skip Button**: Top-right, text button
- **Feature Image**: Illustration, 200x200pt
- **Title**: SF Pro Display, 28pt, Bold
- **Description**: SF Pro Text, 17pt, Regular, 2-3 lines
- **Page Indicator**: 3 dots, current page highlighted
- **Next Button**: Primary button, full width, 50pt height

#### Behavior
- Swipe left/right to navigate pages
- Tap "Next" to advance
- Tap "Skip" to go directly to Registration
- Last page shows "Get Started" instead of "Next"

#### Screens
1. **Page 1**: [Feature 1 benefit]
2. **Page 2**: [Feature 2 benefit]
3. **Page 3**: [Feature 3 benefit]

---

### WF-003: Login
**Purpose**: Authenticate existing users  
**Related**: UC-002, FR-002  
**Priority**: High

#### Layout
```
┌─────────────────────────────────────┐
│  [< Back]                           │
│                                     │
│      Welcome Back                   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Email                       │   │
│  │ [email input field]         │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Password                    │   │
│  │ [password input field] [👁] │   │
│  └─────────────────────────────┘   │
│                                     │
│           [Forgot Password?]        │
│                                     │
│      [Login Button]                 │
│                                     │
│  ─────────── or ───────────         │
│                                     │
│      [Sign Up]                      │
│                                     │
└─────────────────────────────────────┘
```

#### Components
- **Back Button**: Navigation bar, top-left
- **Title**: "Welcome Back", 34pt, Bold
- **Email Field**: 
  - Label: "Email", 13pt
  - Input: Text field, keyboard type: email
  - Height: 50pt
- **Password Field**:
  - Label: "Password", 13pt
  - Input: Secure text field
  - Toggle: Eye icon to show/hide
  - Height: 50pt
- **Forgot Password**: Text button, 15pt
- **Login Button**: Primary button, full width, 50pt
- **Sign Up Button**: Secondary button, full width, 50pt

#### States
- **Default**: All fields empty, button enabled
- **Typing**: Keyboard shown, fields active
- **Loading**: Button shows spinner, fields disabled
- **Error**: Red border on invalid field, error message below
- **Success**: Transition to Main Dashboard

#### Validation
- Email: Real-time format validation
- Password: Min 8 characters
- Error messages appear below fields

---

### WF-004: Registration
**Purpose**: Create new user account  
**Related**: UC-001, FR-001  
**Priority**: High

#### Layout
```
┌─────────────────────────────────────┐
│  [< Back]                           │
│                                     │
│      Create Account                 │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Full Name                   │   │
│  │ [text input]                │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Email                       │   │
│  │ [email input]               │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │ Password                    │   │
│  │ [password input] [👁]       │   │
│  └─────────────────────────────┘   │
│  Password strength: [====    ]      │
│                                     │
│  ☐ I agree to Terms & Privacy       │
│                                     │
│      [Sign Up Button]               │
│                                     │
│  Already have account? [Login]      │
│                                     │
└─────────────────────────────────────┘
```

#### Components
- **Name Field**: Text input, 50pt height
- **Email Field**: Email keyboard, validation
- **Password Field**: Secure input, show/hide toggle
- **Password Strength**: Progress bar (weak/medium/strong)
- **Terms Checkbox**: Required to enable button
- **Sign Up Button**: Primary button, disabled until valid
- **Login Link**: Text button

#### Validation
- Name: Min 2 characters
- Email: Valid format, uniqueness checked on submit
- Password: 
  - Min 8 characters
  - 1 uppercase, 1 lowercase, 1 number
  - Strength indicator updates in real-time
- Terms: Must be checked

#### States
- **Default**: Button disabled
- **Valid**: All fields valid, terms checked, button enabled
- **Loading**: Spinner on button
- **Error**: Field-specific error messages
- **Success**: Show success message, redirect to Main Dashboard

---

## 4. Main Screens

### WF-005: Main Dashboard
**Purpose**: Primary screen after login  
**Related**: UC-003, FR-003  
**Priority**: High

#### Layout
```
┌─────────────────────────────────────┐
│  [☰]  Dashboard        [🔔] [👤]   │
├─────────────────────────────────────┤
│                                     │
│  Good morning, [Name]! 👋           │
│                                     │
│  ┌─────────────────────────────┐   │
│  │  [Quick Action Card 1]      │   │
│  │  Icon | Title               │   │
│  │  Description                │   │
│  └─────────────────────────────┘   │
│                                     │
│  ┌─────────────────────────────┐   │
│  │  [Quick Action Card 2]      │   │
│  │  Icon | Title               │   │
│  │  Description                │   │
│  └─────────────────────────────┘   │
│                                     │
│  Recent Activity                    │
│  ┌─────────────────────────────┐   │
│  │ [Item 1]              [>]   │   │
│  ├─────────────────────────────┤   │
│  │ [Item 2]              [>]   │   │
│  ├─────────────────────────────┤   │
│  │ [Item 3]              [>]   │   │
│  └─────────────────────────────┘   │
│                                     │
└─────────────────────────────────────┘
│  [Home] [Search] [Add] [Profile]   │
└─────────────────────────────────────┘
```

#### Components
- **Navigation Bar**:
  - Menu icon (left): Opens side menu
  - Title: "Dashboard"
  - Notifications icon (right): Badge if unread
  - Profile icon (right): Opens profile
- **Greeting**: Personalized, time-based
- **Quick Action Cards**: 
  - 2-3 cards, 150pt height
  - Icon, title, description
  - Tap to navigate
- **Recent Activity**:
  - List of recent items
  - Swipe actions: Delete, Archive
  - Tap to view details
- **Tab Bar**:
  - Home, Search, Add, Profile
  - Selected tab highlighted

#### States
- **Loading**: Skeleton screens for cards
- **Empty**: "No recent activity" message
- **Error**: Retry button if data fails to load

---

### WF-006: [Feature Screen]
**Purpose**: [Screen purpose]  
**Related**: UC-XXX, FR-XXX  
**Priority**: High / Medium / Low

#### Layout
```
┌─────────────────────────────────────┐
│  [< Back]  [Screen Title]  [Action]│
├─────────────────────────────────────┤
│                                     │
│  [Main content area]                │
│                                     │
│  ┌─────────────────────────────┐   │
│  │                             │   │
│  │  [Content component]        │   │
│  │                             │   │
│  └─────────────────────────────┘   │
│                                     │
│  [Additional components]            │
│                                     │
│                                     │
│      [Primary Action Button]        │
│                                     │
└─────────────────────────────────────┘
```

#### Components
- [List components]

#### Behavior
- [Describe interactions]

#### States
- [List states]

---

## 5. Common Components

### 5.1 Navigation Bar
```
┌─────────────────────────────────────┐
│  [< Back]  [Title]         [Action] │
└─────────────────────────────────────┘
```
- Height: 44pt (compact), 96pt (large title)
- Back button: System chevron + text
- Title: Centered or large title
- Action: Icon or text button

---

### 5.2 Buttons

#### Primary Button
```
┌─────────────────────────────┐
│      [Button Text]          │
└─────────────────────────────┘
```
- Height: 50pt
- Corner radius: 12pt
- Background: Primary color
- Text: White, 17pt, Semibold
- States: Default, Pressed, Disabled, Loading

#### Secondary Button
```
┌─────────────────────────────┐
│      [Button Text]          │
└─────────────────────────────┘
```
- Height: 50pt
- Corner radius: 12pt
- Background: Clear
- Border: 1pt, Primary color
- Text: Primary color, 17pt, Semibold

---

### 5.3 Text Fields
```
┌─────────────────────────────┐
│ Label                       │
│ [Input text]                │
└─────────────────────────────┘
```
- Height: 50pt
- Corner radius: 8pt
- Background: Secondary background
- Border: 1pt (default), 2pt (focused), red (error)
- Label: 13pt, Secondary label color
- Input: 17pt, Label color

---

### 5.4 Cards
```
┌─────────────────────────────┐
│  [Icon]  Title              │
│                             │
│  Description text           │
│                             │
│  [Action]                   │
└─────────────────────────────┘
```
- Corner radius: 12pt
- Shadow: 0 2 8 rgba(0,0,0,0.1)
- Padding: 16pt
- Background: System background

---

### 5.5 Lists
```
┌─────────────────────────────┐
│ [Icon] Title        [>]     │
│        Subtitle             │
├─────────────────────────────┤
│ [Icon] Title        [>]     │
│        Subtitle             │
└─────────────────────────────┘
```
- Row height: 60pt (with subtitle), 44pt (without)
- Separator: 1pt, Separator color
- Swipe actions: Delete, Edit, Archive

---

## 6. Responsive Design

### 6.1 Device Support
- iPhone SE (375pt width) - Minimum
- iPhone 14 (390pt width) - Primary
- iPhone 14 Pro Max (430pt width) - Large
- iPad (768pt width) - Optional

### 6.2 Orientation
- Portrait: Primary
- Landscape: Supported for main screens

### 6.3 Adaptive Layout
- Use Auto Layout with constraints
- Stack views for flexible layouts
- Safe area insets respected
- Dynamic Type support

---

## 7. Accessibility

### 7.1 VoiceOver
- All interactive elements labeled
- Meaningful labels (not "Button")
- Logical reading order

### 7.2 Dynamic Type
- All text scales with system settings
- Minimum 11pt, maximum 34pt
- Layout adapts to larger text

### 7.3 Color Contrast
- Text: 4.5:1 minimum
- Interactive elements: 3:1 minimum
- Support for high contrast mode

### 7.4 Touch Targets
- Minimum: 44x44pt
- Recommended: 48x48pt
- Adequate spacing between targets

---

## 8. Dark Mode

All screens support dark mode with:
- System background colors
- Elevated backgrounds for cards
- Adjusted shadows and borders
- Semantic colors (not hardcoded)

---

## 9. Design Assets

### 9.1 Icons
- SF Symbols for system icons
- Custom icons: 24x24pt, 1pt stroke
- Asset catalog with light/dark variants

### 9.2 Images
- @2x and @3x resolutions
- WebP format for efficiency
- Lazy loading for lists

### 9.3 Animations
- Spring animations (duration: 0.3s, damping: 0.7)
- Fade transitions for content
- Slide transitions for navigation

---

## 10. Figma Links

[If you have Figma designs, add links here]

- Design System: [Link]
- Wireframes: [Link]
- High-Fidelity Mockups: [Link]
- Prototype: [Link]

---

**Document Version**: 1.0  
**Last Updated**: [Date]  
**Status**: Draft / In Review / Approved  
**Dependencies**: Project_Overview.md, Use_Cases.md, Functional_Requirements.md
```

### Step 3: ASK USER CONFIRMATION (REQUIRED)

After creating `Wireframes.md`, MUST display:

```
✅ Created: {{IDE_CONFIG_DIR}}specs/[project-name]/Wireframes.md

📋 Summary:
- Total Screens: X
- Authentication Screens: A
- Main Screens: B
- Common Components: C

🔍 Please review the Wireframes.md file

❓ What would you like to do?
1. ✅ Continue to create UX_Flows.md
2. ✏️ Request modifications
3. ⏸️ Stop here, continue later
```

**DO NOT automatically continue without user confirmation!**

---

## Rules

### Content Quality
- Use ASCII art for clear visual representation
- Include all interactive elements
- Specify dimensions (pt for iOS)
- Document all states (default, loading, error, success)

### iOS Design Standards
- Follow Apple Human Interface Guidelines
- Use SF Symbols for icons
- Support Dynamic Type and VoiceOver
- Include dark mode considerations
- Respect safe area insets

### Component Documentation
- List all UI components per screen
- Specify sizes, colors, typography
- Document interactions and behaviors
- Include validation and error states

### User Interaction
- ALWAYS read previous documents for context
- WAIT for user confirmation before continuing
- If user selects modify → apply changes → ask again
- If user selects continue → call `write-ux-flows` agent

### Exit Checklist (Efficiency)
- No placeholder tokens like `[Screen]`, `[Description]`, `[Component]` in final file
- Every P0 FR has at least one related screen (`WF-XXX`)
- Each screen includes states (default/loading/error/success where relevant)
- IDs are unique and sequential (`WF-XXX`)

### Delivery Summary (Required)
At the end, include concise summary bullets:
- Created file path
- Total screens
- FRs covered / total P0 FRs
- Open assumptions count

---

## Tips for AI

- Base wireframes on functional requirements
- Think mobile-first (small screens)
- Keep layouts simple and clean
- Use consistent spacing (8pt grid)
- Consider thumb zones for important actions
- Include empty states and error states
- Think about loading states
- Reference iOS native patterns
