# Component Format Standard

This document defines the standard format for all SwiftUI components in this project.

## Component Template

```swift
import SwiftUI

/// [Brief description of what this component does]
///
/// Usage:
/// ```
/// [ComponentName](
///     parameter1: value1,
///     parameter2: value2
/// )
/// ```
struct [ComponentName]: View {
    // MARK: - Properties
    
    /// [Description of property]
    let property1: Type
    
    /// [Description of property]
    @Binding var property2: Type
    
    // MARK: - Body
    
    var body: some View {
        // Implementation
    }
}

// MARK: - Preview

#Preview {
    [ComponentName](
        property1: sampleValue1,
        property2: .constant(sampleValue2)
    )
}
```

## Naming Conventions

### Component Names
- Use descriptive names: `PrimaryButton`, `UserCard`, `LoadingView`
- Suffix with component type when ambiguous: `LoginFormView`, `ProfileHeaderView`
- Avoid generic names: ❌ `MyView`, `CustomButton`

### File Names
- Match struct name: `PrimaryButton.swift`
- One component per file
- Location: `.claude/shared/Components/[Category]/[ComponentName].swift`

## Style Guidelines

### 1. Use Design Tokens

```swift
// ✅ Good - Use design tokens
Text("Hello")
    .font(.bodyRegular)
    .foregroundColor(.textPrimary)
    .padding(.md)

// ❌ Bad - Hardcoded values
Text("Hello")
    .font(.system(size: 17))
    .foregroundColor(Color(red: 0, green: 0, blue: 0))
    .padding(16)
```

### 2. Make Components Configurable

```swift
// ✅ Good - Configurable
struct PrimaryButton: View {
    let title: String
    let action: () -> Void
    var isLoading: Bool = false
    var isDisabled: Bool = false
    
    var body: some View {
        Button(action: action) {
            if isLoading {
                ProgressView()
            } else {
                Text(title)
            }
        }
        .disabled(isDisabled || isLoading)
    }
}

// ❌ Bad - Hardcoded
struct PrimaryButton: View {
    var body: some View {
        Button("Submit") {
            // Hardcoded action
        }
    }
}
```

### 3. Add Documentation

```swift
/// A primary action button with loading and disabled states.
///
/// Use this for main CTAs like "Submit", "Save", "Continue".
///
/// - Parameters:
///   - title: The button text
///   - action: Action to perform on tap
///   - isLoading: Shows loading indicator when true
///   - isDisabled: Disables button when true
struct PrimaryButton: View {
    // ...
}
```

### 4. Always Include Preview

```swift
#Preview {
    VStack(spacing: 16) {
        PrimaryButton(
            title: "Normal",
            action: {}
        )
        
        PrimaryButton(
            title: "Loading",
            action: {},
            isLoading: true
        )
        
        PrimaryButton(
            title: "Disabled",
            action: {},
            isDisabled: true
        )
    }
    .padding()
}
```

## Component Categories

### Buttons
Location: `.claude/shared/Components/Buttons/`

Examples:
- `PrimaryButton.swift` - Main CTA
- `SecondaryButton.swift` - Secondary actions
- `TextButton.swift` - Text-only button
- `IconButton.swift` - Icon-only button

### Inputs
Location: `.claude/shared/Components/Inputs/`

Examples:
- `PrimaryTextField.swift` - Text input
- `SecureTextField.swift` - Password input
- `SearchField.swift` - Search input
- `TextEditor.swift` - Multi-line input

### Cards
Location: `.claude/shared/Components/Cards/`

Examples:
- `ItemCard.swift` - List item card
- `InfoCard.swift` - Information display
- `ActionCard.swift` - Card with actions

### Feedback
Location: `.claude/shared/Components/Feedback/`

Examples:
- `LoadingView.swift` - Loading indicator
- `EmptyStateView.swift` - Empty state
- `ErrorView.swift` - Error state
- `ToastView.swift` - Toast notification

### Layouts
Location: `.claude/shared/Components/Layouts/`

Examples:
- `ScreenContainer.swift` - Screen wrapper
- `SectionHeader.swift` - Section header
- `Divider.swift` - Custom divider

## Common Patterns

### Loading State

```swift
struct MyView: View {
    @StateObject private var viewModel = MyViewModel()
    
    var body: some View {
        Group {
            if viewModel.isLoading {
                LoadingView()
            } else {
                contentView
            }
        }
    }
    
    private var contentView: some View {
        // Main content
    }
}
```

### Empty State

```swift
if viewModel.items.isEmpty {
    EmptyStateView(
        icon: "tray",
        title: "No Items",
        message: "Add your first item to get started",
        actionTitle: "Add Item",
        action: viewModel.addItem
    )
} else {
    List(viewModel.items) { item in
        ItemCard(item: item)
    }
}
```

### Error State

```swift
if let error = viewModel.error {
    ErrorView(
        message: error.localizedDescription,
        retryAction: viewModel.retry
    )
}
```

## Accessibility

### VoiceOver Labels

```swift
Button(action: action) {
    Image(systemName: "plus")
}
.accessibilityLabel("Add item")
.accessibilityHint("Double tap to add a new item")
```

### Dynamic Type

```swift
// ✅ Automatically scales
Text("Hello")
    .font(.bodyRegular)

// ❌ Fixed size
Text("Hello")
    .font(.system(size: 17))
```

### Minimum Touch Target

```swift
// Ensure 44x44pt minimum
Button(action: action) {
    Image(systemName: "xmark")
        .frame(width: 44, height: 44)
}
```

## Dark Mode Support

```swift
// Use semantic colors that adapt automatically
.foregroundColor(.textPrimary)
.background(.background)

// Or define custom colors with dark mode variants
extension Color {
    static let customBackground = Color(
        light: Color(hex: "#FFFFFF"),
        dark: Color(hex: "#1C1C1E")
    )
}
```

## Testing Components

### Preview with Different States

```swift
#Preview("States") {
    VStack(spacing: 20) {
        MyComponent(state: .idle)
        MyComponent(state: .loading)
        MyComponent(state: .success)
        MyComponent(state: .error)
    }
}
```

### Preview with Different Sizes

```swift
#Preview("Sizes") {
    VStack {
        MyComponent()
            .previewLayout(.sizeThatFits)
        
        MyComponent()
            .frame(width: 320)
            .previewLayout(.sizeThatFits)
    }
}
```

### Preview Dark Mode

```swift
#Preview("Dark Mode") {
    MyComponent()
        .preferredColorScheme(.dark)
}
```

## Checklist

Before committing a new component:

- [ ] Follows naming conventions
- [ ] Uses design tokens (colors, fonts, spacing)
- [ ] Configurable via parameters
- [ ] Has documentation comments
- [ ] Includes Preview
- [ ] Supports Dark Mode
- [ ] Has accessibility labels
- [ ] Supports Dynamic Type
- [ ] Minimum 44pt touch targets
- [ ] Handles all states (loading, empty, error)

---

*Last updated: February 2026*
