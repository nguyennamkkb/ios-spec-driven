# iOS Spec-Driven Development Toolkit

> Professional iOS development workflow with AI-powered automation

[![Version](https://img.shields.io/badge/version-2.1.0-blue.svg)](https://github.com/nguyennamkkb/ios-spec-driven-claude/releases)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-iOS-lightgrey.svg)](https://developer.apple.com/ios/)

---

## 🎯 What is This?

A complete toolkit that transforms iOS development with Claude Code. Instead of scattered AI conversations, you get:

- **📋 Structured Workflow**: Idea → Requirements → Design → Tasks → Code
- **🔗 Complete Traceability**: Every line of code traces back to user stories
- **✅ Quality Gates**: Automated checkpoints ensure nothing is missed
- **🤖 AI-Powered**: 7 specialized skills + 7 workflow agents
- **🚀 Production Ready**: Battle-tested patterns and best practices

### Why Use This?

| Without Toolkit | With Toolkit |
|----------------|--------------|
| ❌ Scattered conversations | ✅ Structured workflow |
| ❌ Lost context | ✅ Complete documentation |
| ❌ No traceability | ✅ Full traceability chain |
| ❌ Manual validation | ✅ Automated validation |
| ❌ Inconsistent quality | ✅ Consistent, high quality |

---

## ⚡ Quick Start

### Install (30 seconds)

```bash
uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven-claude@dev ios-spec-driven install
```

**Requirements**: [UV](https://docs.astral.sh/uv/) (Python package manager)

### Your First Feature

```
"Create spec for user login with email and password"
```

Claude will guide you through:
1. **Requirements** → User stories + acceptance criteria
2. **Design** → Architecture + properties
3. **Tasks** → Implementation plan
4. **Code** → SwiftUI implementation + tests

**Result**: Complete feature with full documentation in ~10 minutes.

### CLI Commands

```bash
ios-spec-driven install [DIR]     # Install toolkit
ios-spec-driven status [DIR]      # Check status
ios-spec-driven uninstall [DIR]   # Uninstall
ios-spec-driven info              # Show info
```

---

## 🎁 What You Get

### 7 Specialized Skills

| Skill | Purpose |
|-------|---------|
| **dev-spec-driven** | Core workflow orchestration |
| **ios-architecture** | MVVM, Clean Architecture, SwiftUI |
| **ios-components** | Reusable UI components |
| **ios-ui-ux** | Design patterns & accessibility |
| **ios-debug** | Error fixing & optimization |
| **mcp-xcode** | Xcode integration (build, test, analyze) |
| **mcp-figma** | Figma design integration |

### 7 Workflow Agents

| Agent | Output |
|-------|--------|
| **write-spec** | `requirements.md` with user stories |
| **write-design** | `design.md` with architecture |
| **write-tasks** | `tasks.md` with implementation plan |
| **execute-tasks** | SwiftUI code + tests |
| **refine-spec** | Update existing specs |
| **quick-implement** | Skip specs, code directly |
| **research-prd** | PRD from research |

### Automation & Validation

- **Traceability Checker**: Validates US → AC → Design → Task → Code
- **Property-Based Testing**: SwiftCheck templates (4 types)
- **Component Standards**: Standardized SwiftUI structure
- **Error Recovery**: Automatic retry with smart limits
- **Parallel Execution**: Run independent tasks simultaneously

### MCP Integrations

- **Xcode MCP**: Build, test, run simulator, analyze
- **Figma MCP**: Fetch designs, extract specs

---

## 📖 Workflow

### Process

```
💡 Idea
  ↓
📋 write-spec → requirements.md
  ↓ [✓ User Confirms]
🎨 write-design → design.md
  ↓ [✓ User Confirms]
📝 write-tasks → tasks.md
  ↓ [✓ User Confirms]
💻 execute-tasks → Code
  ↓ [Checkpoints: Build + Test + Commit]
✅ Done
```

### Usage Examples

#### Full Spec Workflow

```
"Create spec for shopping cart"
```

**Output**:
```
.claude/specs/shopping-cart/
├── requirements.md  # User stories + EARS criteria
├── design.md        # Architecture + properties
└── tasks.md         # Implementation plan + traceability
```

**Time**: ~10-15 minutes

#### Quick Implementation

```
"Quick implementation of dark mode toggle"
```

**Output**: Code directly, no specs  
**Time**: ~2-5 minutes

#### Individual Steps

```
"Write requirements for user profile"
"Write design for user profile"
"Write tasks for user profile"
"Implement task 3.1.2.1"
```

#### Update Specs

```
"Add requirement: filter by priority"
"Update design: add caching layer"
"Sync tasks for todo-list feature"
```

### Spec Structure

**requirements.md**:
```markdown
# User Stories
US-001: As a user, I want to login with email...

# Acceptance Criteria (EARS format)
AC-001.1: WHEN user enters valid email
          THEN system validates format
```

**design.md**:
```markdown
# Architecture
- MVVM pattern
- Combine for reactive updates

# Properties
P1: Valid email always passes validation
P2: Login state persists across sessions
```

**tasks.md**:
```markdown
# Implementation Plan
3.1.1.1 [AC-001.1] Create LoginViewModel
3.1.1.2 [AC-001.1, P1] Add email validation [PBT]
3.1.1.3 [AC-001.1] Implement login flow
```

### Complete Traceability

Every line of code traces back:

```
US-001 (User Story)
  └── AC-001.1 (Acceptance Criteria)
      └── Design 3.1 (Architecture)
          └── Property P1 (Correctness)
              └── Task 3.1.1.2 [PBT]
                  └── LoginViewModel.swift
```

**Validate**:
```bash
python .claude/scripts/validate_traceability.py shopping-cart
```

**Output**:
```
✅ Traceability: 100%
- User Stories: 5
- Acceptance Criteria: 12
- Tasks: 24
```

### Quality Gates

Every checkpoint ensures:
- ✅ Build passes (via mcp-xcode)
- ✅ Tests pass
- ✅ Code committed to git
- ✅ User confirms to continue

### Property-Based Testing

Auto-generated tests with SwiftCheck:

```swift
func testLoginValidation() {
    property("Valid email passes") <- forAll { 
        (email: String) in
        email.contains("@") ==> {
            LoginValidator.validate(email) == true
        }
    }
}
```

**4 Property Types**:
1. **Round-trip**: `encode(decode(x)) == x`
2. **Invariant**: `condition(x) == true`
3. **Idempotent**: `f(f(x)) == f(x)`
4. **Commutative**: `f(x,y) == f(y,x)`

### Feature Independence

Each feature is self-contained:

```
.claude/specs/
├── user-authentication/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
├── shopping-cart/
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
└── user-profile/
    ├── requirements.md
    ├── design.md
    └── tasks.md
```

**Benefits**:
- Work on multiple features in parallel
- Easy to review and update
- Clear ownership and scope

---

## 🌐 Language Support

Use any language you prefer:

```
✅ "Create spec for login feature"
✅ "Tạo spec cho tính năng đăng nhập"
✅ "Create spec cho login feature"
```

**Vietnamese examples**:
```
"Viết requirements cho giỏ hàng"
"Implement task 3.1.2.1"
"Thêm requirement: lọc theo độ ưu tiên"
"Quick implementation của dark mode toggle"
```

---

## 📚 Documentation

- **Skills**: `.claude/skills/*/SKILL.md` - Detailed skill documentation
- **Agents**: `.claude/agents/*.md` - Agent workflows
- **Guides**: `.claude/shared/*.md` - Best practices
  - `COMPONENT_FORMAT.md` - SwiftUI component standards
  - `PBT_GUIDE.md` - Property-based testing guide
  - `PARALLEL_EXECUTION_GUIDE.md` - Parallel execution guide

---

## 📝 License

MIT License - See [LICENSE](LICENSE)

---

**Version**: 2.1.0 • **Status**: ✅ Production Ready

*Built for iOS developers using Claude Code • Optimized for SwiftUI + MVVM*
