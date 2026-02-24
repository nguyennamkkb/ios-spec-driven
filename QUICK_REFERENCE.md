# Quick Reference - 2 Workflows

## 🎯 Chọn Workflow Nào?

### 📋 Project Documentation → `@write-project-docs`
**Khi**: Bắt đầu dự án mới  
**Output**: 5 tài liệu tổng quan  
**Time**: 30-60 phút  
**Mục đích**: Hiểu toàn bộ dự án

```bash
@write-project-docs Create documentation for [project name]
```

---

### �� Feature Development → `"Create spec for..."`
**Khi**: Implement tính năng cụ thể  
**Output**: 3 tài liệu + code  
**Time**: 10-15 phút/feature  
**Mục đích**: Build và deliver feature

```bash
"Create spec for [feature name]"
```

---

## 📊 So Sánh Nhanh

| | Project Docs | Feature Dev |
|---|-------------|-------------|
| **Agent** | `@write-project-docs` | `@write-spec` |
| **Scope** | Toàn dự án | 1 feature |
| **Docs** | 5 files | 3 files |
| **Code** | ❌ No | ✅ Yes |
| **Level** | High-level | Detailed |
| **When** | Start | During dev |

---

## 🔄 Workflow Đề Xuất

```
1. @write-project-docs (1 lần, đầu dự án)
   ↓
2. "Create spec for feature 1" (lặp lại)
   ↓
3. "Create spec for feature 2" (lặp lại)
   ↓
4. "Create spec for feature 3" (lặp lại)
```

---

## 📁 Output Structure

```
.opencode/specs/
├── [project-name]/           # From @write-project-docs
│   ├── Project_Overview.md
│   ├── Use_Cases.md
│   ├── Functional_Requirements.md
│   ├── Wireframes.md
│   └── UX_Flows.md
│
├── [feature-1]/              # From "Create spec for..."
│   ├── requirements.md
│   ├── design.md
│   └── tasks.md
│
└── [feature-2]/              # From "Create spec for..."
    ├── requirements.md
    ├── design.md
    └── tasks.md
```

---

## 💡 Examples

### Project Documentation
```
@write-project-docs Create documentation for fitness tracking app
@write-project-docs Create documentation for e-commerce platform
@write-project-docs Create documentation for social media app
```

### Feature Development
```
"Create spec for user authentication"
"Create spec for shopping cart"
"Create spec for push notifications"
"Create spec for dark mode"
```

---

## 🚫 Common Mistakes

❌ **Wrong**: `@write-project-docs Create documentation for login feature`  
✅ **Right**: `"Create spec for login feature"`

❌ **Wrong**: `"Create spec for entire app"`  
✅ **Right**: `@write-project-docs Create documentation for [app name]`

---

## 📚 Full Docs

- Project Documentation: `SPEC_WORKFLOW_GUIDE.md`
- Feature Development: `README.md`
- Comparison: `WORKFLOW_COMPARISON.md`
- Vietnamese: `HUONG_DAN_SUBAGENT.md`
