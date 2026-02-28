# Specification Workflow Guide

## Overview

This guide explains how to use the 5-document specification workflow for iOS projects. The workflow creates a complete, traceable specification set before implementation begins.

---

## 📚 The 5 Documents

### 1. Project_Overview.md
**Purpose**: High-level vision and architecture  
**Agent**: `@write-project-overview`  
**Contains**:
- Problem statement and solution
- User personas
- Technology stack
- Development roadmap
- Success metrics

**When to use**: Starting a new project, defining vision

---

### 2. Use_Cases.md
**Purpose**: User stories and scenarios  
**Agent**: `@write-use-cases`  
**Contains**:
- User stories (As a... I want... So that...)
- Scenarios (happy path + edge cases)
- Priority breakdown
- User journey maps

**When to use**: After Project Overview, to define user interactions

---

### 3. Functional_Requirements.md
**Purpose**: Detailed feature specifications  
**Agent**: `@write-functional-requirements`  
**Contains**:
- Functional requirements (FR-XXX)
- Non-functional requirements (NFR-XXX)
- Input/output specifications
- Business rules
- Validation rules
- Error handling

**When to use**: After Use Cases, to specify exact behavior

---

### 4. Wireframes.md
**Purpose**: UI mockups and screen layouts  
**Agent**: `@write-wireframes`  
**Contains**:
- ASCII wireframes for all screens
- Component specifications
- Design system (colors, typography, spacing)
- Responsive design rules
- Accessibility requirements

**When to use**: After Functional Requirements, to design UI

---

### 5. UX_Flows.md
**Purpose**: User journey diagrams  
**Agent**: `@write-ux-flows`  
**Contains**:
- Mermaid flow diagrams
- User journeys (new user, returning user)
- Feature flows
- Error handling flows
- Navigation patterns

**When to use**: After Wireframes, to map complete user experience

---

## 🚀 Usage Methods

### Method 1: Full Workflow (Recommended for New Projects)

Use the orchestrator agent to create all 5 documents in sequence:

```
@write-project-docs Create complete documentation for [project name]
```

**Example**:
```
@write-project-docs Create complete documentation for fitness tracking app
```

**What happens**:
1. Agent asks questions about your project
2. Creates Project_Overview.md → waits for your approval
3. Creates Use_Cases.md → waits for your approval
4. Creates Functional_Requirements.md → waits for your approval
5. Creates Wireframes.md → waits for your approval
6. Creates UX_Flows.md → waits for your approval
7. Runs cross-review (consistency + traceability) and proposes fixes
8. Shows completion summary
9. Suggests implementation spec queue (project-setup first, then priority features)
10. Asks which spec to start first and can invoke `write-spec` immediately

**Time**: 30-60 minutes total  
**Benefit**: Complete, consistent specification set

**Handoff rule**:
- First implementation spec should be `project-setup` to establish architecture and shared foundation.
- Then proceed with top MVP/High-priority features from `Functional_Requirements.md` and `Use_Cases.md`.

---

### Method 2: Individual Documents

Create documents one at a time:

```
@write-project-overview Create project overview for [project name]
@write-use-cases Create use cases for [project name]
@write-functional-requirements Create functional requirements for [project name]
@write-wireframes Create wireframes for [project name]
@write-ux-flows Create UX flows for [project name]
```

**When to use**:
- Updating existing specs
- Working on specific sections
- Iterating on one document

---

### Method 3: Modify Existing Documents

Update documents after creation:

```
@write-use-cases Add use case for social login to [project name]
@write-wireframes Update login screen wireframe for [project name]
@write-ux-flows Add error handling flow for network failures
```

---

## 📋 Workflow Steps

### Step 1: Preparation

Before starting, gather:
- Clear problem statement
- Target user information
- Core feature list
- Technology preferences (if any)
- Timeline/budget constraints (if any)

---

### Step 2: Create Project Overview

```
@write-project-overview Create project overview for MyApp
```

**Agent will ask**:
- What problem does your app solve?
- Who are your target users?
- What are the must-have features?
- Any technology preferences?
- Timeline or deadlines?

**Review checklist**:
- [ ] Problem statement is clear
- [ ] User personas are realistic
- [ ] Technology stack is appropriate
- [ ] Roadmap is achievable
- [ ] Success metrics are measurable

**Approve or request changes**

---

### Step 3: Create Use Cases

```
@write-use-cases Create use cases for MyApp
```

**Agent will**:
- Read Project_Overview.md
- Create user stories for each persona
- Define scenarios (happy path + errors)
- Prioritize use cases

**Review checklist**:
- [ ] All user personas covered
- [ ] User stories follow format (As a... I want... So that...)
- [ ] Scenarios include error cases
- [ ] Priorities make sense
- [ ] Acceptance criteria are clear

**Approve or request changes**

---

### Step 4: Create Functional Requirements

```
@write-functional-requirements Create functional requirements for MyApp
```

**Agent will**:
- Read Project_Overview.md and Use_Cases.md
- Create detailed requirements for each feature
- Define validation rules
- Specify error handling
- Add non-functional requirements

**Review checklist**:
- [ ] All use cases have corresponding requirements
- [ ] Input/output clearly specified
- [ ] Business rules documented
- [ ] Error handling comprehensive
- [ ] Non-functional requirements measurable

**Approve or request changes**

---

### Step 5: Create Wireframes

```
@write-wireframes Create wireframes for MyApp
```

**Agent will**:
- Read all previous documents
- Create ASCII wireframes for all screens
- Define design system
- Specify components
- Document accessibility

**Review checklist**:
- [ ] All screens from use cases included
- [ ] Wireframes are clear and understandable
- [ ] Design system is consistent
- [ ] Accessibility considered
- [ ] Responsive design addressed

**Approve or request changes**

---

### Step 6: Create UX Flows

```
@write-ux-flows Create UX flows for MyApp
```

**Agent will**:
- Read all previous documents
- Create Mermaid diagrams for user journeys
- Map feature flows
- Document error handling flows
- Show navigation patterns

**Review checklist**:
- [ ] All user journeys mapped
- [ ] Error paths included
- [ ] Loading states shown
- [ ] Navigation is logical
- [ ] Diagrams are clear

**Approve or request changes**

---

### Step 7: Completion

After all documents are approved:

1. **Review traceability**:
   - User personas → User stories → Requirements → Wireframes → Flows
   
2. **Share with team**:
   - Developers: For implementation
   - Designers: For high-fidelity mockups
   - QA: For test planning
   - Stakeholders: For approval

3. **Start implementation**:
   ```
   @write-spec Create requirements for [first feature]
   ```

---

## 🔄 Document Dependencies

```
Project_Overview.md (Foundation)
    ↓
Use_Cases.md (User perspective)
    ↓
Functional_Requirements.md (Technical specs)
    ↓
Wireframes.md (Visual design)
    ↓
UX_Flows.md (User experience)
```

**Important**: Create documents in this order for best results.

---

## ✅ Best Practices

### Do's

✅ **Start with clear problem statement**
- Understand the "why" before the "what"

✅ **Involve stakeholders early**
- Get feedback on Project Overview before proceeding

✅ **Be specific with requirements**
- Use numbers, not vague terms (< 2 seconds, not "fast")

✅ **Include error scenarios**
- Think about what can go wrong

✅ **Review each document before proceeding**
- Each document builds on previous ones

✅ **Keep documents updated**
- Modify as requirements change

✅ **Use consistent terminology**
- Same terms across all documents

---

### Don'ts

❌ **Don't skip Project Overview**
- It's the foundation for everything else

❌ **Don't rush through approvals**
- Take time to review each document

❌ **Don't ignore non-functional requirements**
- Performance, security, accessibility matter

❌ **Don't forget error handling**
- Happy path is not enough

❌ **Don't create documents out of order**
- Dependencies exist for a reason

❌ **Don't let documents get stale**
- Update when requirements change

---

## 🎯 Example Workflow

### Scenario: Creating a Todo List App

#### 1. Start Full Workflow
```
@write-project-docs Create complete documentation for Todo List app
```

#### 2. Answer Questions
```
Agent: What problem does your app solve?
You: Users need a simple way to track daily tasks

Agent: Who are your target users?
You: Busy professionals, students, anyone who needs task management

Agent: What are the must-have features?
You: Create tasks, mark complete, set due dates, categories

Agent: Any technology preferences?
You: iOS, SwiftUI, offline-first

Agent: Timeline?
You: 8 weeks to MVP
```

#### 3. Review Project Overview
```
Agent: ✅ Created Project_Overview.md
- User personas: 2 (Professional, Student)
- Core features: 5
- Tech stack: iOS 15+, SwiftUI, Core Data
- Roadmap: 3 phases

Review and approve?
You: Looks good, continue
```

#### 4. Review Use Cases
```
Agent: ✅ Created Use_Cases.md
- User stories: 8
- Scenarios: 12
- Priority: 5 High, 3 Medium

Review and approve?
You: Add use case for recurring tasks
Agent: [Updates document]
You: Approved, continue
```

#### 5. Review Functional Requirements
```
Agent: ✅ Created Functional_Requirements.md
- Functional requirements: 15
- Non-functional requirements: 8
- Categories: Performance, Security, Usability

Review and approve?
You: Approved, continue
```

#### 6. Review Wireframes
```
Agent: ✅ Created Wireframes.md
- Total screens: 8
- Common components: 6
- Design system defined

Review and approve?
You: Approved, continue
```

#### 7. Review UX Flows
```
Agent: ✅ Created UX_Flows.md
- User journeys: 4
- Feature flows: 8
- Mermaid diagrams: 12

Review and approve?
You: Approved
```

#### 8. Completion
```
Agent: 🎉 Specification Set Complete!

All 5 documents created in .opencode/specs/todo-list-app/

Next steps:
1. Generate traceability matrix
2. Export specifications
3. Share with team

What would you like to do next?
You: Generate traceability matrix
```

#### 9. Implementation
```
@write-spec Create requirements for task creation feature
```

---

## 📊 Traceability

Each document links to the next:

```
Project_Overview.md
  └─ User Persona: "Busy Professional"
      └─ Use_Cases.md
          └─ UC-001: Create Task
              └─ Functional_Requirements.md
                  └─ FR-001: Task Creation
                      └─ Wireframes.md
                          └─ WF-003: Create Task Screen
                              └─ UX_Flows.md
                                  └─ Flow: Task Creation Journey
```

This ensures every line of code traces back to user needs.

---

## 🛠️ Troubleshooting

### Problem: Agent creates wrong content

**Solution**: Be specific in your instructions
```
❌ "Create specs for my app"
✅ "Create project overview for fitness tracking app that helps users log workouts and track progress"
```

---

### Problem: Document is too generic

**Solution**: Provide more details when agent asks questions
```
❌ "Users want to track things"
✅ "Users want to track daily workouts with sets, reps, weight, and see progress over time"
```

---

### Problem: Want to modify existing document

**Solution**: Use the specific agent with modification request
```
@write-use-cases Add use case for social sharing to fitness app
```

---

### Problem: Documents are inconsistent

**Solution**: Use full workflow instead of creating individually
```
@write-project-docs Create complete documentation for fitness app
```

---

### Problem: Lost progress mid-workflow

**Solution**: Check what's already created, continue from there
```
# Check existing documents
ls .opencode/specs/[project-name]/

# Continue with next document
@write-functional-requirements Create functional requirements for [project-name]
```

---

## 📈 Success Metrics

After completing the workflow, you should have:

✅ **Complete documentation**
- All 5 documents created
- No gaps in coverage

✅ **Clear traceability**
- Every requirement traces to user need
- Every screen traces to requirement

✅ **Team alignment**
- Everyone understands the vision
- No ambiguity in requirements

✅ **Implementation ready**
- Developers can start coding
- Designers can create mockups
- QA can plan tests

✅ **Maintainable specs**
- Easy to update as requirements change
- Clear structure for modifications

---

## 🎓 Learning Resources

### For Beginners
1. Start with small project (Todo app, Notes app)
2. Use full workflow (@write-project-docs)
3. Review each document carefully
4. Ask for modifications if unclear

### For Advanced Users
1. Create documents individually for flexibility
2. Customize agents for your workflow
3. Add project-specific templates
4. Integrate with design tools (Figma)

---

## 💡 Tips

1. **Start small**: Don't try to spec entire app at once
2. **Iterate**: Specs evolve, update as you learn
3. **Involve team**: Get feedback early and often
4. **Be specific**: Vague specs lead to vague code
5. **Think user-first**: Always start with user needs
6. **Document decisions**: Explain "why" not just "what"
7. **Keep it simple**: Complexity is the enemy
8. **Use examples**: Show, don't just tell
9. **Test assumptions**: Validate with users early
10. **Stay consistent**: Use same terms throughout

---

## 🔗 Related Guides

- `COMPONENT_FORMAT.md` - SwiftUI component standards
- `PBT_GUIDE.md` - Property-based testing guide
- `PARALLEL_EXECUTION_GUIDE.md` - Parallel execution guide

---

## ⚙️ Feature Autopilot Contract (Agent + Skill Alignment)

For feature-level workflow (`write-spec`, `write-design`, `write-tasks`, `execute-tasks`), use this contract:

### State Machine

```text
draft_requirements -> approved_requirements
-> draft_design -> approved_design
-> draft_tasks -> approved_tasks
-> executing -> blocked | done
```

### Required Files

```text
{{IDE_CONFIG_DIR}}specs/[feature-name]/
  requirements.md
  design.md
  tasks.md
  spec-state.json
```

### Project Docs Directory Preflight (Required)

Before creating any project documentation file (`Project_Overview.md`, `Use_Cases.md`, `Functional_Requirements.md`, `Wireframes.md`, `UX_Flows.md`), ensure this directory exists:

`{{IDE_CONFIG_DIR}}specs/[project-name]/`

Rules:
- If missing, create it first.
- If directory cannot be created/verified, stop the workflow.
- Never write documentation files to repository root as fallback.

### Task Schema (tasks.md)

Must include:
- Task Registry (machine-readable)
- Dependency Matrix
- Traceability Matrix
- Implementation checklist sections

Allowed status values:
- `pending`, `in_progress`, `blocked`, `done`

### Phase-End Gates

A phase can advance only when all pass:
1. Build (mcp-xcode simulator flow: `discover_projs -> list_schemes -> build_sim`)
2. Traceability validation script

Note:
- Run full debug/build gate at end of each phase (not every internal checkpoint).
- Default gate is build-only on simulator (`build_sim`); do not run/boot simulator unless user explicitly requests it.

### Task Completion Sync Rule

When marking a task as `done` or `blocked`, synchronize all three locations:
1. **Task Registry** (table): Update status column.
2. **Checklist markdown**: Change `- [ ] **TASK_ID**` to `- [x] **TASK_ID**` when done; keep `[ ]` when blocked.
3. **Traceability Matrix**: Update status column to match.

This ensures visual progress tracking in the markdown file matches the machine-readable registry.

After `write-tasks` generates `tasks.md`:
- Default behavior is stop-and-confirm.
- Do not auto-run `execute-tasks` from a generic approval.
- Start execution only when user gives explicit execution intent.

### iOS Quality Gate

Before marking UI tasks complete:
- loading/empty/error/success states implemented
- accessibility checks completed
- component reuse decision recorded

### Parallel Policy

Default is sequential autopilot.
Parallel execution is allowed only when dependency matrix explicitly permits it.

---

## Philosophy: Quality Framework, Not Pattern Enforcement

This toolkit provides a **quality and traceability framework** for spec-driven iOS development. It does NOT enforce specific architectural patterns or implementation orders.

**What the toolkit controls:**
- Document structure and traceability (requirements → design → tasks → code)
- Quality gates (build verification, traceability validation)
- Task status tracking and synchronization
- Phase-end checkpoints

**What the toolkit does NOT enforce:**
- Specific architectural patterns (Clean Architecture, VIPER, etc.)
- Mandatory implementation order (logic-first vs UI-first)
- Specific design patterns (Singleton, Delegate, Observer, DI) unless user requests
- Code style or framework choices beyond basic MVVM/SwiftUI conventions

**User intent always takes precedence:**
- Follow user's explicit direction for implementation approach
- Respect existing codebase patterns when present
- Use suggested patterns only when complexity demands or user asks
- Junior developers should find the approach simple and understandable

---

**Version**: 1.0  
**Last Updated**: 2026-02-06  
**Status**: Production Ready
