---
name: ios-components
description: 
  Create UI components for SwiftUI. Use when creating buttons, cards, input fields, modals, bottom sheets, loading views, empty states, creating components from design images, coding UI from Figma, making custom views, creating reusable views.
allowed-tools: Read, Grep, Glob, Bash
---

# SwiftUI Reusable Components

## Table of Contents
- [1. Reuse First Strategy](#1-reuse-first-strategy) . L15-L80
- [2. Workflow](#2-workflow) ......................... L82-L120
- [3. Component Locations](#3-component-locations) ... L122-L150
- [4. Design Integration](#4-design-integration) ..... L152-L200
- [5. Style Files](#5-style-files) ................... L202-L250
- [6. Checklist](#6-checklist) ....................... L252-L280

---

## 1. Reuse First Strategy

### Core Principle
**ALWAYS try to reuse existing components before creating new ones.**

Benefits:
- Consistency across the app
- Less code to maintain
- Faster development
- Fewer bugs

---

### Decision Tree

```
Need a UI component?
    │
    ├─→ Search existing components
    │       │
    │       ├─→ Found exact match?
    │       │       └─→ ✅ Use it!
    │       │
    │       ├─→ Found similar component?
    │       │       │
    │       │       ├─→ Can customize with parameters?
    │       │       │       └─→ ✅ Add parameters & use!
    │       │       │
    │       │       └─→ Need minor changes?
    │       │               └─→ ✅ Extend or compose!
    │       │
    │       └─→ Nothing similar?
    │               └─→ ⚠️ Create new component
    │
    └─→ Document for future reuse
```

---

### Step-by-Step: Search Before Create

#### 1. Search by Type
```bash
# List all components by category
ls {{IDE_CONFIG_DIR}}shared/Components/Buttons/
ls {{IDE_CONFIG_DIR}}shared/Components/Cards/
ls {{IDE_CONFIG_DIR}}shared/Components/Inputs/
```

#### 2. Search by Name Pattern
```bash
# Search for button-related components
find {{IDE_CONFIG_DIR}}shared/Components -name "*Button*"

# Search for card-related components
find {{IDE_CONFIG_DIR}}shared/Components -name "*Card*"
```

#### 3. Grep for Similar Functionality
```bash
# Search for components with specific features
grep -r "loading" {{IDE_CONFIG_DIR}}shared/Components/
grep -r "icon" {{IDE_CONFIG_DIR}}shared/Components/
```

---

### Reuse Strategies

#### Strategy 1: Use As-Is
Component already does what you need.

```swift
// Existing: PrimaryButton.swift
// Just use it!
PrimaryButton(title: "Submit", action: submit)
```

#### Strategy 2: Customize with Parameters
Component is close, add parameters to make it flexible.

**Before:**
```swift
struct PrimaryButton: View {
    let title: String
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            Text(title)
                .foregroundColor(.white)
        }
        .background(Color.primary)
    }
}
```

**After (add icon parameter):**
```swift
struct PrimaryButton: View {
    let title: String
    let icon: String? = nil  // ← Add optional parameter
    let action: () -> Void
    
    var body: some View {
        Button(action: action) {
            HStack {
                if let icon = icon {
                    Image(systemName: icon)
                }
                Text(title)
            }
            .foregroundColor(.white)
        }
        .background(Color.primary)
    }
}
```

#### Strategy 3: Compose Multiple Components
Combine existing components to create new functionality.

```swift
// Reuse existing components
struct LoginForm: View {
    var body: some View {
        VStack(spacing: Spacing.md) {
            // Reuse existing input component
            TextInputField(placeholder: "Email", text: $email)
            
            // Reuse existing input component
            SecureInputField(placeholder: "Password", text: $password)
            
            // Reuse existing button component
            PrimaryButton(title: "Login", action: login)
        }
    }
}
```

#### Strategy 4: Extend with ViewModifier
Add functionality without modifying original component.

```swift
// Create reusable modifier
struct ShakeEffect: ViewModifier {
    let shakes: Int
    
    func body(content: Content) -> some View {
        content
            .modifier(ShakeAnimation(shakes: shakes))
    }
}

// Use with any component
PrimaryButton(title: "Submit", action: submit)
    .modifier(ShakeEffect(shakes: errorCount))
```

---

## 2. Workflow

### Step 1: Read Standard Format File
ALWAYS read this file before working with components:
```
{{IDE_CONFIG_DIR}}shared/COMPONENT_FORMAT.md
```
This file contains code format, style guide, and project rules.

### Step 2: Search Existing Components (REUSE FIRST!)
```bash
# Browse by category
ls {{IDE_CONFIG_DIR}}shared/Components/Buttons/
ls {{IDE_CONFIG_DIR}}shared/Components/Cards/
ls {{IDE_CONFIG_DIR}}shared/Components/Inputs/

# Search by name
find {{IDE_CONFIG_DIR}}shared/Components -name "*Button*"

# Search by functionality
grep -r "loading" {{IDE_CONFIG_DIR}}shared/Components/
```

### Step 3: Evaluate Reuse Options
- Can use as-is? → Use it!
- Need customization? → Add parameters
- Need combination? → Compose components
- Nothing similar? → Create new (last resort)

### Step 4: If Creating New Component
- Use design tokens from `{{IDE_CONFIG_DIR}}shared/Styles/`
- Follow format from `COMPONENT_FORMAT.md`
- Make it reusable (add parameters)
- Add Preview
- Document usage

---

## 3. Component Locations

| Type | Location |
|------|----------|
| Button | `{{IDE_CONFIG_DIR}}shared/Components/Buttons/` |
| Input | `{{IDE_CONFIG_DIR}}shared/Components/Inputs/` |
| Card | `{{IDE_CONFIG_DIR}}shared/Components/Cards/` |
| Modal | `{{IDE_CONFIG_DIR}}shared/Components/Modals/` |
| Layout | `{{IDE_CONFIG_DIR}}shared/Components/Layouts/` |
| Feedback | `{{IDE_CONFIG_DIR}}shared/Components/Feedback/` |
| Navigation | `{{IDE_CONFIG_DIR}}shared/Components/Navigation/` |

### Common Feedback Components

| Component | Purpose | Reuse For |
|-----------|---------|-----------|
| `LoadingView.swift` | Loading indicator | Any loading state |
| `EmptyStateView.swift` | Empty state with message + CTA | Empty lists, no data |
| `ErrorView.swift` | Error state with retry | API errors, failures |
| `SkeletonView.swift` | Skeleton loading placeholder | Content loading |
| `ToastView.swift` | Toast notifications | Success/error messages |

---

## 4. Design Integration

### When User Sends UI Design Image

1. **First: Check if similar components exist**
   - Search existing components
   - Can you compose existing ones?
   - Can you customize existing ones?

2. **Analyze the image to understand:**
   - UI style (rounded, sharp, gradient, flat...)
   - Color scheme
   - Typography style
   - Spacing pattern
   - Shadow/elevation style

3. **Update or create `{{IDE_CONFIG_DIR}}shared/COMPONENT_FORMAT.md` with:**
   - Code template for components
   - Style rules extracted from design
   - Specific examples

4. **Update `{{IDE_CONFIG_DIR}}shared/Styles/` if needed:**
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

## 5. Style Files

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

## 6. Checklist

### Before creating component:
- [ ] Read `{{IDE_CONFIG_DIR}}shared/COMPONENT_FORMAT.md`
- [ ] **Search existing components** (ls, find, grep)
- [ ] **Evaluate reuse options** (use as-is, customize, compose)
- [ ] Record reuse evidence (components checked and why not reused)
- [ ] Identify design tokens needed
- [ ] Only create new if nothing can be reused

### When creating component:
- [ ] Use design tokens from `{{IDE_CONFIG_DIR}}shared/Styles/`
- [ ] Create file in correct folder by type
- [ ] Follow format from COMPONENT_FORMAT.md
- [ ] **Make component reusable** (add parameters for flexibility)
- [ ] Add Preview with multiple examples
- [ ] Document parameters and usage

### After creating component:
- [ ] Test in Preview
- [ ] Test with different data/states
- [ ] Test dark mode if applicable
- [ ] **Document for future reuse**
- [ ] Consider: Can this replace similar components?
