---
name: ios-ui-ux
description: |
  UI/UX design principles for iOS. Use when designing screens, making UI look good, user flow design, handling loading states, empty states, error states, animations, navigation patterns, accessibility, dark mode, form design, better UX.
allowed-tools: Read, Grep, Glob
---

# UI/UX Design Principles

## Table of Contents
- [1. Design Philosophy](#1-design-philosophy) ....... L15-L40
- [2. Navigation Patterns](#2-navigation-patterns) ... L42-L70
- [3. States & Feedback](#3-states--feedback) ........ L72-L110
- [4. Interaction Patterns](#4-interaction-patterns) . L112-L150
- [5. Visual Hierarchy](#5-visual-hierarchy) ......... L152-L190
- [6. Accessibility](#6-accessibility) ............... L192-L220
- [7. Performance UX](#7-performance-ux) ............. L222-L250
- [8. Checklist](#8-checklist) ....................... L252-L280

---

## 1. Design Philosophy

### Core Values
- **Simple first** - Prioritize simplicity, avoid over-complication
- **Consistency** - Consistent throughout the app
- **Feedback** - Always respond to user actions
- **Accessibility** - Design for all users

### Design Style
- Minimalist / Clean
- iOS native feel (follow Human Interface Guidelines)
- Light mode first, support dark mode

### Key Principles
1. Content over chrome
2. Clarity over decoration
3. Depth through layering
4. Direct manipulation

---

## 2. Navigation Patterns

### Main Structure
- Tab Bar for main navigation (max 5 tabs)
- Navigation Stack for drill-down
- Modal/Sheet for temporary actions

### Rules
- No more than 3 levels deep in navigation stack
- Back button always visible
- Swipe back gesture enabled
- Clear navigation hierarchy

### Navigation Types

| Type | Use Case | Presentation |
|------|----------|--------------|
| Push | Drill-down to detail | NavigationStack |
| Sheet | Temporary task | .sheet() |
| Full Screen | Immersive content | .fullScreenCover() |
| Tab | Main sections | TabView |

---

## 3. States & Feedback

### Every Screen Must Handle

| State | Display |
|-------|---------|
| Loading | Skeleton or ProgressView |
| Empty | Illustration + message + CTA |
| Error | Message + retry button |
| Success | Confirmation + next action |

### State Diagram

```
         ┌─────────┐
         │  Idle   │
         └────┬────┘
              │ load()
              ▼
         ┌─────────┐
    ┌────│ Loading │────┐
    │    └─────────┘    │
    │ error             │ success
    ▼                   ▼
┌─────────┐       ┌─────────┐
│  Error  │       │ Success │
└────┬────┘       └────┬────┘
     │ retry()         │ refresh()
     └────────┬────────┘
              ▼
         ┌─────────┐
         │ Loading │
         └─────────┘
```

### User Feedback
- Haptic feedback for important actions
- Animation for state transitions (0.3s default)
- Toast/Snackbar for light confirmations
- Progress indicators for long operations

---

## 4. Interaction Patterns

### Touch Targets
- Minimum 44x44pt for tappable elements
- Spacing between buttons: 8pt minimum
- Adequate padding around interactive elements

### Gestures

| Gesture | Use Case |
|---------|----------|
| Tap | Primary action |
| Long press | Secondary options |
| Swipe | Delete, archive, quick actions |
| Pull to refresh | Reload data |
| Pinch | Zoom |
| Pan | Scroll, drag |

### Forms
- Inline validation
- Clear error messages
- Auto-focus next field
- Appropriate keyboard type
- Show/hide password toggle
- Clear button for text fields

### Form Validation

| Timing | Use Case |
|--------|----------|
| On blur | Field-level validation |
| On change | Real-time feedback (optional) |
| On submit | Full form validation |

---

## 5. Visual Hierarchy

### Typography Scale

| Style | Usage | Weight |
|-------|-------|--------|
| Large Title | Screen titles | Bold |
| Title | Section headers | Bold |
| Headline | Important text | Semibold |
| Body | Main content | Regular |
| Callout | Secondary content | Regular |
| Caption | Labels, hints | Regular |
| Footnote | Legal, timestamps | Regular |

### Spacing System
- Base unit: 8pt
- Use: 4, 8, 16, 24, 32, 48
- Consistent spacing throughout app

### Colors

| Type | Usage |
|------|-------|
| Primary | Brand color for CTAs |
| Secondary | Supporting actions |
| Destructive | Red for delete/danger |
| Success | Green for success states |
| Warning | Yellow/Orange for warnings |
| Error | Red for error states |

### Elevation/Shadows
- Use sparingly
- Consistent shadow styles
- Higher elevation = more important

---

## 6. Accessibility

### Required
- VoiceOver labels for all interactive elements
- Dynamic Type support
- Minimum contrast ratio 4.5:1
- Don't use color as only indicator
- Support reduced motion

### VoiceOver

```swift
Button("Submit") {
    // action
}
.accessibilityLabel("Submit form")
.accessibilityHint("Double tap to submit your information")
```

### Dynamic Type

```swift
Text("Hello")
    .font(.body) // Automatically scales
```

### Contrast
- Text on background: 4.5:1 minimum
- Large text: 3:1 minimum
- Interactive elements: clearly distinguishable

---

## 7. Performance UX

### Loading
- Skeleton screens instead of spinners when possible
- Optimistic UI for fast actions
- Lazy loading for long lists
- Progressive loading for images

### Skeleton Example

```
┌────────────────────────────┐
│ ████████████               │  <- Title placeholder
│ ████████████████████████   │  <- Subtitle placeholder
│                            │
│ ████████████████████████   │  <- Content placeholder
│ ████████████████           │
└────────────────────────────┘
```

### Offline
- Cache important data
- Show offline indicator
- Queue actions to sync later
- Graceful degradation

### Performance Tips
- Avoid blocking main thread
- Use lazy loading for lists
- Cache computed values
- Optimize images
- Minimize re-renders

---

## 8. Checklist

### When Designing New Screen

- [ ] Define user goal for the screen
- [ ] Handle all 4 states (loading, empty, error, success)
- [ ] Touch targets >= 44pt
- [ ] VoiceOver labels
- [ ] Dark mode compatible
- [ ] Keyboard handling (if has input)
- [ ] Animation for transitions
- [ ] Consistent with app style

### When Implementing

- [ ] Use design tokens (colors, fonts, spacing)
- [ ] Add accessibility labels
- [ ] Support Dynamic Type
- [ ] Test with VoiceOver
- [ ] Test dark mode
- [ ] Test different screen sizes
- [ ] Handle keyboard appearance

### Before Release

- [ ] All states implemented
- [ ] Accessibility audit passed
- [ ] Performance acceptable
- [ ] Animations smooth (60fps)
- [ ] No layout issues on different devices
