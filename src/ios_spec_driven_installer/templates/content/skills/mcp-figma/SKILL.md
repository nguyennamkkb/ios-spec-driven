---
name: mcp-figma
description: Figma integration for design specs. Use when getting colors, typography, spacing from Figma, exporting component specs, syncing design tokens, implementing UI from Figma design.
allowed-tools: Read, Write, MCP
---

# Figma MCP Integration

## Table of Contents
- [1. MCP Tools](#1-mcp-tools)
- [2. Setup Design System](#2-setup-design-system)
- [3. Implement Screen](#3-implement-screen)
- [4. Export Assets](#4-export-assets)
- [5. Deep UI/UX Analysis](#5-deep-uiux-analysis)
- [6. Checklist](#6-checklist)

---

## 1. MCP Tools

### figma_get_file
Get Figma file information.
- Input: fileKey (from URL)
- Output: File metadata, document structure, pages/frames
- Use: Explore design file, get screen list

### figma_get_node
Get specific node details (frame, component, screen).
- Input: fileKey, nodeId
- Output: Layout, colors, typography, effects, children
- Use: Implement specific screen, get component specs

### figma_get_styles
Get design tokens.
- Input: fileKey
- Output: Color styles, text styles, effect styles
- Use: Setup design system, create {{IDE_CONFIG_DIR}}shared/Styles/ files

### figma_export_image
Export image from node.
- Input: fileKey, nodeId, format (png/jpg/svg/pdf), scale
- Output: Image URL
- Use: Export icons, illustrations, assets


---

## 2. Setup Design System

### Workflow (First Time)
1. Run `figma_get_styles` with fileKey
2. Create `{{IDE_CONFIG_DIR}}shared/Styles/AppColors.swift`
3. Create `{{IDE_CONFIG_DIR}}shared/Styles/AppFonts.swift`
4. Create `{{IDE_CONFIG_DIR}}shared/Styles/AppSpacing.swift`
5. Update `{{IDE_CONFIG_DIR}}shared/COMPONENT_FORMAT.md`

### Figma to SwiftUI Mapping

| Figma | SwiftUI |
|-------|---------|
| Frame | VStack/HStack/ZStack |
| Auto Layout (vertical) | VStack(spacing: X) |
| Auto Layout (horizontal) | HStack(spacing: X) |
| Padding | .padding() |
| Fill | .background(Color) |
| Stroke | .border() |
| Corner Radius | .cornerRadius() |
| Shadow | .shadow() |

---

## 3. Implement Screen

### Workflow
1. Get file structure: `figma_get_file`
2. Find nodeId of target screen
3. Get screen details: `figma_get_node`
4. Map Figma layout → SwiftUI
5. Use design tokens from {{IDE_CONFIG_DIR}}shared/Styles/

---

## 4. Export Assets

| Asset Type | Format | Scale |
|------------|--------|-------|
| Icons | PDF | 1x |
| Illustrations | PNG | 3x |
| Photos | JPG | 2x/3x |

### Figma URL Parsing
- File: `figma.com/file/{fileKey}/{name}`
- Node: `figma.com/file/{fileKey}/{name}?node-id={nodeId}`

---

## 5. Deep UI/UX Analysis

Use this section before implementation when quality matters.

### 5.1 Screen Audit (per node)

For each target screen, extract:
- Layout structure (containers, spacing system, breakpoints)
- Typography scale (title/body/caption hierarchy)
- Color roles (primary/surface/text/error/success)
- Component states (default/focus/pressed/disabled/loading/error/empty)
- Interaction patterns (tap, swipe, drag, long press, transitions)

### 5.2 UX Heuristic Review

Evaluate each screen with these checks:
- Clarity: primary action obvious within 3 seconds
- Feedback: every action has visible response
- Error prevention: destructive actions require confirmation
- Recovery: clear path after error and offline state
- Consistency: same pattern for same intent across screens

### 5.3 Accessibility Review

Verify design intent supports:
- Touch target >= 44x44 pt
- Text contrast target >= WCAG AA
- Dynamic Type scaling
- VoiceOver reading order and labels
- Color not used as the only signal

### 5.4 Flow Completeness

Check full flow states exist in Figma:
- Happy path
- Empty state
- Loading/skeleton
- Validation and server/network errors
- Permission denied / blocked states

### 5.5 Required Output (before coding)

Produce a concise report:

```markdown
## Figma UI/UX Analysis Summary
- Screens analyzed: N
- Components extracted: N
- Missing states: [list]
- Accessibility risks: [list]
- Consistency issues: [list]

## Implementation Decisions
- Token mapping: [done/pending]
- Reusable components to create: [list]
- UX fixes applied during implementation: [list]
```

---

## 6. Checklist

### Setup Project
- [ ] Get design tokens with figma_get_styles
- [ ] Create AppColors.swift
- [ ] Create AppFonts.swift
- [ ] Create AppSpacing.swift

### Implement Screen
- [ ] Get nodeId from Figma URL
- [ ] Run figma_get_node for specs
- [ ] Map layout to SwiftUI
- [ ] Use design tokens
- [ ] Export assets if needed

### Deep UI/UX Quality Gate
- [ ] Component states covered (default/loading/error/empty)
- [ ] Interaction feedback defined for key actions
- [ ] Accessibility checks documented
- [ ] UX risks documented with proposed fixes
