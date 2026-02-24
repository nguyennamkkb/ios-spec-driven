# So Sánh 2 Workflows

## 📊 Tổng Quan

Hệ thống có **2 workflows riêng biệt** phục vụ 2 mục đích khác nhau:

---

## 🎯 Workflow 1: Project Documentation (Tài Liệu Dự Án)

### Mục Đích
Tạo **tài liệu tổng quan** cho toàn bộ dự án trước khi bắt đầu code.

### Khi Nào Dùng
- ✅ Bắt đầu dự án mới
- ✅ Cần định nghĩa vision và architecture
- ✅ Muốn có tài liệu đầy đủ trước khi code
- ✅ Team cần hiểu rõ toàn bộ dự án

### Orchestrator Agent
```
@write-project-docs
```

### Output (5 Documents)
```
.opencode/specs/[project-name]/
├── Project_Overview.md          # Vision, architecture, roadmap
├── Use_Cases.md                 # User stories, scenarios
├── Functional_Requirements.md   # Detailed feature specs
├── Wireframes.md                # UI mockups, design system
└── UX_Flows.md                  # User journey diagrams
```

### Thời Gian
30-60 phút cho toàn bộ dự án

### Ví Dụ
```
@write-project-docs Create complete documentation for fitness tracking app
```

**Kết quả**: Tài liệu tổng quan hoàn chỉnh về toàn bộ app

---

## 🚀 Workflow 2: Feature Development (Phát Triển Tính Năng)

### Mục Đích
Tạo **spec chi tiết** cho từng tính năng cụ thể và implement code.

### Khi Nào Dùng
- ✅ Đã có project documentation
- ✅ Cần implement một tính năng cụ thể
- ✅ Muốn spec + code cho feature
- ✅ Development theo từng sprint/iteration

### Orchestrator Agent
```
@write-spec (hoặc gọi trực tiếp)
```

### Output (3 Documents + Code)
```
.opencode/specs/[feature-name]/
├── requirements.md    # User stories + EARS criteria
├── design.md          # Architecture + properties
├── tasks.md           # Implementation plan
└── [Code files]       # SwiftUI implementation
```

### Thời Gian
10-15 phút cho mỗi feature

### Ví Dụ
```
"Create spec for user login feature"
```

**Kết quả**: Spec chi tiết + code implementation cho feature login

---

## 📋 So Sánh Chi Tiết

| Aspect | Project Documentation | Feature Development |
|--------|----------------------|---------------------|
| **Orchestrator** | `@write-project-docs` | `@write-spec` → `@write-design` → `@write-tasks` → `@execute-tasks` |
| **Scope** | Toàn bộ dự án | Một tính năng cụ thể |
| **Documents** | 5 files | 3 files + code |
| **Level** | High-level | Detailed implementation |
| **Output** | Documentation only | Documentation + Code |
| **Time** | 30-60 min | 10-15 min per feature |
| **When** | Start of project | During development |
| **Goal** | Understand project | Implement feature |

---

## 🔄 Workflow Kết Hợp (Recommended)

### Bước 1: Project Documentation (Lần Đầu)

```
@write-project-docs Create complete documentation for Todo App
```

**Output**:
- Project_Overview.md
- Use_Cases.md
- Functional_Requirements.md
- Wireframes.md
- UX_Flows.md

**Thời gian**: 30-60 phút

---

### Bước 2: Feature Development (Lặp Lại)

Sau khi có project documentation, implement từng feature:

#### Feature 1: User Authentication
```
"Create spec for user authentication"
```
**Output**: requirements.md, design.md, tasks.md, code

#### Feature 2: Task Management
```
"Create spec for task management"
```
**Output**: requirements.md, design.md, tasks.md, code

#### Feature 3: Notifications
```
"Create spec for push notifications"
```
**Output**: requirements.md, design.md, tasks.md, code

---

## 🎯 Khi Nào Dùng Cái Nào?

### Dùng Project Documentation Khi:

✅ **Bắt đầu dự án mới**
```
@write-project-docs Create documentation for e-commerce app
```

✅ **Pitch cho stakeholders**
- Cần tài liệu tổng quan để present
- Cần roadmap và timeline

✅ **Onboard team mới**
- Team mới cần hiểu toàn bộ dự án
- Cần architecture overview

✅ **Planning phase**
- Chưa code gì cả
- Cần define scope và requirements

---

### Dùng Feature Development Khi:

✅ **Đã có project documentation**
```
"Create spec for user profile feature"
```

✅ **Sprint planning**
- Chọn feature để implement trong sprint
- Cần breakdown thành tasks

✅ **Iterative development**
- Implement feature by feature
- Continuous delivery

✅ **Bug fixes hoặc enhancements**
```
"Quick implementation of dark mode toggle"
```

---

## 📁 Cấu Trúc Thư Mục

### Sau Project Documentation:
```
.opencode/specs/
└── todo-app/                    # Project documentation
    ├── Project_Overview.md
    ├── Use_Cases.md
    ├── Functional_Requirements.md
    ├── Wireframes.md
    └── UX_Flows.md
```

### Sau Feature Development:
```
.opencode/specs/
├── todo-app/                    # Project documentation
│   ├── Project_Overview.md
│   ├── Use_Cases.md
│   ├── Functional_Requirements.md
│   ├── Wireframes.md
│   └── UX_Flows.md
│
├── user-authentication/         # Feature 1
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
│
├── task-management/             # Feature 2
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
│
└── push-notifications/          # Feature 3
    ├── requirements.md
    ├── design.md
    └── tasks.md
```

---

## 🔗 Traceability

### Project Documentation → Feature Development

```
Project_Overview.md
  └─ Core Feature: "Task Management"
      └─ Use_Cases.md
          └─ UC-003: Create Task
              └─ Functional_Requirements.md
                  └─ FR-003: Task Creation
                      └─ Feature Development
                          └─ task-management/
                              ├── requirements.md (chi tiết UC-003)
                              ├── design.md (implement FR-003)
                              ├── tasks.md (breakdown)
                              └── [Code files]
```

---

## 💡 Best Practices

### 1. Bắt Đầu Với Project Documentation

```
# Bước 1: Tạo project documentation
@write-project-docs Create documentation for Todo App

# Bước 2: Review và approve tất cả 5 documents

# Bước 3: Bắt đầu implement features
"Create spec for user authentication"
"Create spec for task management"
```

### 2. Reference Project Documentation

Khi tạo feature spec, reference project documentation:

```
"Create spec for user authentication based on Project_Overview.md and Use_Cases.md"
```

### 3. Keep Documents Updated

Khi requirements thay đổi:

```
# Update project documentation
@write-project-overview Update project overview with new features

# Update feature specs
@refine-spec Update user authentication spec with OAuth support
```

---

## 🚫 Tránh Nhầm Lẫn

### ❌ Sai: Dùng Project Documentation cho feature cụ thể

```
# SAI - quá tổng quát
@write-project-docs Create documentation for login feature
```

### ✅ Đúng: Dùng Feature Development

```
# ĐÚNG - chi tiết và có code
"Create spec for login feature"
```

---

### ❌ Sai: Dùng Feature Development cho toàn bộ dự án

```
# SAI - thiếu high-level view
"Create spec for entire e-commerce app"
```

### ✅ Đúng: Dùng Project Documentation

```
# ĐÚNG - tổng quan toàn bộ
@write-project-docs Create documentation for e-commerce app
```

---

## 📚 Tài Liệu Liên Quan

- **Project Documentation**: `SPEC_WORKFLOW_GUIDE.md`
- **Feature Development**: `README.md` (existing workflow)
- **Architecture**: `SUBAGENT_ARCHITECTURE.md`
- **Vietnamese Guide**: `HUONG_DAN_SUBAGENT.md`

---

## 🎓 Ví Dụ Hoàn Chỉnh

### Scenario: Tạo Todo App Từ Đầu

#### Phase 1: Project Documentation (Week 0)

```
@write-project-docs Create complete documentation for Todo App
```

**Time**: 1 hour  
**Output**: 5 project documents

---

#### Phase 2: Sprint 1 - Authentication (Week 1-2)

```
"Create spec for user registration"
"Create spec for user login"
"Create spec for password reset"
```

**Time**: 3-4 hours total  
**Output**: 3 feature specs + code

---

#### Phase 3: Sprint 2 - Core Features (Week 3-4)

```
"Create spec for task creation"
"Create spec for task list view"
"Create spec for task completion"
```

**Time**: 3-4 hours total  
**Output**: 3 feature specs + code

---

#### Phase 4: Sprint 3 - Advanced Features (Week 5-6)

```
"Create spec for task categories"
"Create spec for due date reminders"
"Create spec for task search"
```

**Time**: 3-4 hours total  
**Output**: 3 feature specs + code

---

## ✅ Tóm Tắt

| | Project Documentation | Feature Development |
|---|---------------------|---------------------|
| **Command** | `@write-project-docs` | `"Create spec for..."` |
| **Scope** | Entire project | Single feature |
| **Output** | 5 docs (no code) | 3 docs + code |
| **Level** | High-level | Implementation |
| **When** | Start of project | During development |
| **Time** | 30-60 min once | 10-15 min per feature |
| **Purpose** | Understand & plan | Build & deliver |

---

**Version**: 1.0  
**Last Updated**: 2026-02-06  
**Language**: Vietnamese + English
