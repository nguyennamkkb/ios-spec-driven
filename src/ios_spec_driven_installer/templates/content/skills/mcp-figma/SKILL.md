---
name: mcp-figma
description: Framelink MCP integration for Figma design context. Use for extracting tokens, component structure, and screen-level UI specs before SwiftUI implementation.
allowed-tools: Read, Write, MCP
---

# Framelink MCP (Figma)

## Purpose
Use this skill for design-informed UI implementation in `execute-tasks`.

Primary outcomes:
- reliable token extraction
- state-complete UI specs
- component reuse decisions
- accessibility-aware implementation notes

---

## 1) Prerequisites

- MCP server: Framelink MCP for Figma
- Valid personal token configured in MCP command args
- Figma URL (file or node) for the target UI task

Token docs:
- https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens

Required token scopes:
- `File content (read)`
- `Dev resources (read)`

---

## 2) URL and Target Resolution

Support both:
- file URL: `figma.com/file/{fileKey}/{name}`
- node URL: `figma.com/file/{fileKey}/{name}?node-id={nodeId}`

Flow:
1. parse `fileKey`
2. if `node-id` exists, use it as primary target
3. otherwise pick target frame by feature/screen name

---

## 3) Design Extraction Workflow

1. Fetch file and node context using Framelink MCP tools.
2. Extract:
   - layout hierarchy
   - spacing and sizing rhythm
   - typography styles
   - color roles (surface/text/action/error/success)
   - component variants and states
3. Map extracted tokens to local style files under `{{IDE_CONFIG_DIR}}shared/Styles/`.
   - `AppColors.swift` for color roles
   - `AppFonts.swift` for typography scale/weights
   - `AppSpacing.swift` for spacing rhythm
   - If any file is missing, create it in `shared/Styles` before coding
4. Record reusable components and missing variants.

Style persistence rules:
- Do not keep design tokens only in task notes or temporary code.
- Do not hardcode extracted values in feature views when shared token files are the correct destination.
- Update `{{IDE_CONFIG_DIR}}shared/COMPONENT_FORMAT.md` when new token naming/patterns are introduced.
- Treat this mapping and persistence flow as the Design Style System (DSS) contract for implementation.

---

## 4) Reuse-First Enforcement

Before creating new UI component:
1. search existing shared components
2. evaluate use-as-is / parameterize / compose
3. create new component only if no compatible candidate exists

Required task note:
- `Reuse: <component>`
or
- `New: <component> | Reason: <why reuse was not possible>`

---

## 5) iOS UI Completeness Gate

For each target screen, verify:
- loading state
- empty state
- error state
- success/default state

Accessibility checks:
- touch target >= 44x44pt
- readable contrast intent
- dynamic type compatibility
- VoiceOver labels/hints for key actions

---

## 6) Output Contract (for execution)

Before coding, produce a short report:

```markdown
## Figma Analysis Summary
- Target screens: [list]
- Tokens mapped: [list]
- Style files updated: [list under {{IDE_CONFIG_DIR}}shared/Styles/]
- Reusable components: [list]
- Missing states: [list]
- Accessibility risks: [list]

## Implementation Decisions
- Reuse decisions: [list]
- New components required: [list]
- Deviations from design (if any): [list]
```

This report feeds `execute-tasks` task notes and traceability updates.
