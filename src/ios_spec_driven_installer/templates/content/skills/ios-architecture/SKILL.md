---
name: ios-architecture
description: 
  SwiftUI project structure guidance. Use when creating new projects, new features, new screens, file placement, file naming, folder organization, code refactoring, ViewModel separation, standard directory structure, MVVM. Follows user intent rather than enforcing specific architectural patterns.
allowed-tools: Read, Grep, Glob, Bash
---

# SwiftUI MVVM Structure (User-Driven)

## Table of Contents
- [1. Directory Structure](#1-directory-structure) ... L15-L40
- [2. Naming Conventions](#2-naming-conventions) ..... L42-L80
- [3. Organization Rules](#3-organization-rules) ..... L82-L110
- [4. Feature Example](#4-feature-example) ........... L112-L140

---

## 1. Directory Structure

```
ProjectName/
├── App/
│   └── ProjectNameApp.swift
├── Core/
│   ├── Extensions/
│   ├── Utilities/
│   └── Network/
├── Features/
│   └── FeatureName/
│       ├── Views/
│       ├── ViewModels/
│       ├── Models/
│       └── Services/
├── {{IDE_CONFIG_DIR}}shared/
│   ├── Components/
│   ├── Styles/
│   └── Modifiers/
├── Resources/
└── Tests/
```

### Folder Purposes

| Folder | Purpose |
|--------|---------|
| `App/` | App entry point, app-level configuration |
| `Core/` | Shared code across app (Extensions, Network, Utilities) |
| `Features/` | Feature modules (Authentication, Home, Profile...) |
| `{{IDE_CONFIG_DIR}}shared/` | Reusable UI components (Buttons, Cards, Modifiers) |
| `Resources/` | Assets, Localizable, Info.plist |
| `Tests/` | Unit tests, UI tests |

---

## 2. Naming Conventions

### Folder Naming
- `Features/` - Feature modules by functionality
- `Core/` - App-wide shared code
- `{{IDE_CONFIG_DIR}}shared/` - Reusable UI components
- `Services/` - Business logic, API services
- `Resources/` - Assets, Localizable, Info.plist

### File Naming

| Type | Convention | Example |
|------|------------|---------|
| View | `[Feature]View.swift` | `LoginView.swift` |
| ViewModel | `[Feature]ViewModel.swift` | `LoginViewModel.swift` |
| Model | `[EntityName].swift` | `User.swift` |
| Service | `[Name]Service.swift` | `AuthService.swift` |
| Extension | `[Type]+Extensions.swift` | `String+Extensions.swift` |
| Component | `[DescriptiveName].swift` | `PrimaryButton.swift` |
| Protocol | `[Name]Protocol.swift` | `AuthServiceProtocol.swift` |

### Component Naming

| Type | Location | Example |
|------|----------|---------|
| Button | `{{IDE_CONFIG_DIR}}shared/Components/Buttons/` | `PrimaryButton.swift` |
| Input | `{{IDE_CONFIG_DIR}}shared/Components/Inputs/` | `PrimaryTextField.swift` |
| Card | `{{IDE_CONFIG_DIR}}shared/Components/Cards/` | `ItemCard.swift` |
| Modal | `{{IDE_CONFIG_DIR}}shared/Components/Modals/` | `ConfirmationModal.swift` |
| Feedback | `{{IDE_CONFIG_DIR}}shared/Components/Feedback/` | `LoadingView.swift` |

---

## 3. Organization Rules

### MVVM Responsibilities

| Layer | Responsibility | Contains |
|-------|----------------|----------|
| View | UI only, no logic | SwiftUI views, layout, styling |
| ViewModel | State + business logic | @Published properties, methods |
| Model | Data structure only | Structs, Codable, Identifiable |
| Service | API + data persistence | Network calls, local storage |

### Rules

1. Each feature is a separate folder in `Features/`
2. Each feature has subfolders: `Views/`, `ViewModels/`, `Models/`, `Services/`
3. View contains UI only, no business logic
4. ViewModel contains state and business logic
5. Model is data structure only
6. Service handles API and data persistence
7. Components in `{{IDE_CONFIG_DIR}}shared/` are reusable across features

### Dependencies Direction

```
View → ViewModel → Service → Model
  ↓         ↓          ↓
  UI      Logic      Data
```

- View depends on ViewModel
- ViewModel depends on Service
- Service depends on Model
- Model has no dependencies

### Implementation Approach (User-Driven)

**Follow user's explicit intent:**
- If user requests "logic first": start with Models/Services, then ViewModels, then Views
- If user requests "UI first": start with Views/ViewModels wiring, then harden logic
- If user has no preference: follow existing codebase patterns or discuss trade-offs

**Pattern usage is optional, not enforced:**
- Use Singleton only for genuine global state (e.g., SessionManager, AppState)
- Use Delegate for 1-1 callbacks (e.g., form submission, coordinator events)
- Use Observer (@Published/Combine) for reactive state changes
- Use Dependency Injection (protocol + constructor) for testability when needed
- Avoid over-engineering; prefer simplicity that juniors can understand

---

## 4. Feature Example

### Authentication Feature

```
Features/
└── Authentication/
    ├── Views/
    │   ├── LoginView.swift
    │   ├── RegisterView.swift
    │   └── Components/
    │       ├── AuthHeader.swift
    │       └── SocialLoginButtons.swift
    ├── ViewModels/
    │   ├── LoginViewModel.swift
    │   └── RegisterViewModel.swift
    ├── Models/
    │   ├── User.swift
    │   ├── LoginRequest.swift
    │   └── LoginResponse.swift
    └── Services/
        ├── AuthService.swift
        └── AuthServiceProtocol.swift
```

### File Contents Overview

| File | Contains |
|------|----------|
| `LoginView.swift` | UI layout, bindings to ViewModel |
| `LoginViewModel.swift` | @Published state, login(), validate() |
| `User.swift` | User struct with Codable |
| `AuthService.swift` | API calls for login, register |

---

## Checklist

### When creating new feature:
- [ ] Create folder in `Features/[FeatureName]/`
- [ ] Create subfolders: `Views/`, `ViewModels/`, `Models/`, `Services/`
- [ ] Follow naming conventions
- [ ] Keep View logic-free
- [ ] Keep Model data-only

### When creating new screen:
- [ ] Create `[Name]View.swift` in `Views/`
- [ ] Create `[Name]ViewModel.swift` in `ViewModels/`
- [ ] Create models if needed in `Models/`
- [ ] Add Preview for View

### When creating reusable component:
- [ ] Place in `{{IDE_CONFIG_DIR}}shared/Components/[Type]/`
- [ ] Make it configurable via parameters
- [ ] Add Preview
- [ ] Document usage

---

## Autopilot Integration Contract

When used with spec agents:
- `design.md` sections define feature modules and file plan based on user intent.
- `tasks.md` Task Registry must reference real paths under this structure.
- Task order follows user's explicit direction (not a hardcoded template):
  - If user wants logic-first: Models/Services → ViewModels → Views → Integration
  - If user wants UI-first: Views → ViewModels → Logic hardening → Integration
  - If user has preference: follow their stated order

Required alignment:
- Every task file path must map to `Features/[FeatureName]/...` or shared folders.
- Respect existing codebase patterns when present.
- Do not impose Clean Architecture or complex patterns unless user explicitly requests.
