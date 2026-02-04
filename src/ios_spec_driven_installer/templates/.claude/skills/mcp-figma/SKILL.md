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
- [5. Checklist](#5-checklist)

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
- Use: Setup design system, create .claude/shared/Styles/ files

### figma_export_image
Export image from node.
- Input: fileKey, nodeId, format (png/jpg/svg/pdf), scale
- Output: Image URL
- Use: Export icons, illustrations, assets


---

## 2. Setup Design System

### Workflow (First Time)
1. Run `figma_get_styles` with fileKey
2. Create `.claude/shared/Styles/AppColors.swift`
3. Create `.claude/shared/Styles/AppFonts.swift`
4. Create `.claude/shared/Styles/AppSpacing.swift`
5. Update `.claude/shared/COMPONENT_FORMAT.md`

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
5. Use design tokens from .claude/shared/Styles/

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

## 5. Checklist

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
