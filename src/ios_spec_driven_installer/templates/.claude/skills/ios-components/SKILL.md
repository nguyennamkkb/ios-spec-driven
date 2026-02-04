---
name: ios-components
description: |
  Create UI components for SwiftUI. Use when creating buttons, cards, input fields, modals, bottom sheets, loading views, empty states, creating components from design images, coding UI from Figma, making custom views, creating reusable views.
allowed-tools: Read, Grep, Glob, Bash
---

# SwiftUI Reusable Components

## Table of Contents
- [1. Workflow](#1-workflow) ......................... L15-L50
- [2. Component Locations](#2-component-locations) ... L52-L80
- [3. Design Integration](#3-design-integration) ..... L82-L130
- [4. Style Files](#4-style-files) ................... L132-L180
- [5. Checklist](#5-checklist) ....................... L182-L200

---

## 1. Workflow

### Step 1: Read Standard Format File
ALWAYS read this file before creating components:
```
.claude/shared/COMPONENT_FORMAT.md
```
This file contains code format, style guide, and project rules.

### Step 2: Reference Existing Components
```
.claude/shared/Components/     # View existing components
.claude/shared/Styles/         # View design tokens
.claude/shared/Modifiers/      # View custom modifiers
```

### Step 3: Create File in Correct Folder
Follow the component locations table below.

### Step 4: Implement Component
- Use design tokens from `.claude/shared/Styles/`
- Follow format from `COMPONENT_FORMAT.md`
- Add Preview

---

## 2. Component Locations

| Type | Location |
|------|----------|
| Button | `.claude/shared/Components/Buttons/` |
| Input | `.claude/shared/Components/Inputs/` |
| Card | `.claude/shared/Components/Cards/` |
| Modal | `.claude/shared/Components/Modals/` |
| Layout | `.claude/shared/Components/Layouts/` |
| Feedback | `.claude/shared/Components/Feedback/` |
| Navigation | `.claude/shared/Components/Navigation/` |

### Feedback Components

| Component | Purpose |
|-----------|---------|
| `LoadingView.swift` | Loading indicator |
| `EmptyStateView.swift` | Empty state with message + CTA |
| `ErrorView.swift` | Error state with retry |
| `SkeletonView.swift` | Skeleton loading placeholder |
| `ToastView.swift` | Toast notifications |

---

## 3. Design Integration

### When User Sends UI Design Image

1. **Analyze the image to understand:**
   - UI style (rounded, sharp, gradient, flat...)
   - Color scheme
   - Typography style
   - Spacing pattern
   - Shadow/elevation style

2. **Update or create `.claude/shared/COMPONENT_FORMAT.md` with:**
   - Code template for components
   - Style rules extracted from design
   - Specific examples

3. **Update `.claude/shared/Styles/` if needed:**
   - AppColors.swift
   - AppFonts.swift
   - AppSpacing.swift

### COMPONENT_FORMAT.md

This is the most important file - contains project's standard format.
If it doesn't exist, create it when user sends first design image.
If it exists, read and follow it.

File contents include:
- Code template for struct View
- Naming conventions
- Style conventions (corner radius, shadows, colors...)
- Example component

---

## 4. Style Files

### AppColors.swift

```swift
import SwiftUI

extension Color {
    // Primary Colors
    static let primary = Color(hex: "#007AFF")
    static let secondary = Color(hex: "#5856D6")
    
    // Semantic Colors
    static let success = Color(hex: "#34C759")
    static let warning = Color(hex: "#FF9500")
    static let error = Color(hex: "#FF3B30")
    
    // Neutral Colors
    static let textPrimary = Color(hex: "#000000")
    static let textSecondary = Color(hex: "#8E8E93")
    static let background = Color(hex: "#FFFFFF")
}
```

### AppFonts.swift

```swift
import SwiftUI

extension Font {
    // Headings
    static let h1 = Font.system(size: 34, weight: .bold)
    static let h2 = Font.system(size: 28, weight: .bold)
    static let h3 = Font.system(size: 22, weight: .semibold)
    
    // Body
    static let bodyRegular = Font.system(size: 17, weight: .regular)
    static let bodyBold = Font.system(size: 17, weight: .semibold)
    
    // Small
    static let caption = Font.system(size: 13, weight: .regular)
    static let footnote = Font.system(size: 11, weight: .regular)
}
```

### AppSpacing.swift

```swift
import SwiftUI

enum Spacing {
    static let xs: CGFloat = 4
    static let sm: CGFloat = 8
    static let md: CGFloat = 16
    static let lg: CGFloat = 24
    static let xl: CGFloat = 32
    static let xxl: CGFloat = 48
}
```

---

## 5. Checklist

### Before creating component:
- [ ] Read `.claude/shared/COMPONENT_FORMAT.md`
- [ ] Check existing components in `.claude/shared/Components/`
- [ ] Identify design tokens needed

### When creating component:
- [ ] Use design tokens from `.claude/shared/Styles/`
- [ ] Create file in correct folder by type
- [ ] Follow format from COMPONENT_FORMAT.md
- [ ] Make component configurable via parameters
- [ ] Add Preview

### After creating component:
- [ ] Test in Preview
- [ ] Test with different data
- [ ] Test dark mode if applicable
- [ ] Document usage if complex
