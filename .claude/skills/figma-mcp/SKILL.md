---
name: figma-mcp
description: Sử dụng Figma MCP để lấy design từ Figma, export assets, đọc design tokens. Dùng khi cần xây dựng UI theo Figma design, lấy colors/fonts/spacing từ Figma.
allowed-tools: Read, Write, Grep, Glob
---

# Figma MCP Usage

## Khi nào dùng
- Xây dựng UI theo Figma design
- Lấy design tokens (colors, fonts, spacing)
- Export assets (icons, images)
- Đọc component specs từ Figma

## MCP Tools

### 1. figma_get_file
Lấy thông tin file Figma.

```
Tool: figma_get_file
Parameters:
- file_key: Figma file key (từ URL)
- node_id: ID của node cụ thể (optional)
```

**Lấy file_key từ URL:**
```
https://www.figma.com/file/ABC123xyz/MyDesign
                          ↑
                      file_key = ABC123xyz
```

### 2. figma_get_node
Lấy thông tin chi tiết của 1 node/frame.

```
Tool: figma_get_node
Parameters:
- file_key: Figma file key
- node_id: Node ID (từ URL sau ?node-id=)
```

### 3. figma_get_styles
Lấy design tokens/styles từ file.

```
Tool: figma_get_styles
Parameters:
- file_key: Figma file key
```

**Output bao gồm:**
- Colors
- Text styles (fonts)
- Effects (shadows)
- Grids

### 4. figma_export_assets
Export images/icons.

```
Tool: figma_export_assets
Parameters:
- file_key: Figma file key
- node_ids: Array of node IDs to export
- format: png | jpg | svg | pdf
- scale: 1 | 2 | 3 (for @2x, @3x)
```

### 5. figma_get_components
Lấy danh sách components trong file.

```
Tool: figma_get_components
Parameters:
- file_key: Figma file key
```

## Workflow: Figma → SwiftUI

### 1. Lấy Design Tokens
```
figma_get_styles → Extract colors, fonts, spacing
                 → Tạo AppColors.swift, AppFonts.swift
```

### 2. Lấy Component Specs
```
figma_get_node → Đọc frame properties
              → Tạo SwiftUI component
```

### 3. Export Assets
```
figma_export_assets → Download icons/images
                    → Add to Assets.xcassets
```

## Convert Figma → SwiftUI

### Colors
```
Figma: #FF5733 (opacity 100%)
Swift: Color(hex: "FF5733")
```

### Fonts
```
Figma: Inter, 16px, Semi Bold
Swift: .system(size: 16, weight: .semibold)
```

### Spacing
```
Figma: padding 16px
Swift: .padding(16)
```

### Corner Radius
```
Figma: corner radius 8px
Swift: .cornerRadius(8)
```

### Shadows
```
Figma: shadow X:0 Y:4 Blur:8 Color:#000 20%
Swift: .shadow(color: .black.opacity(0.2), radius: 4, x: 0, y: 4)
```

## Output Files

Sau khi đọc Figma, tạo/update các files:

### Shared/Styles/AppColors.swift
```swift
import SwiftUI

extension Color {
    // From Figma
    static let primary = Color(hex: "FF5733")
    static let secondary = Color(hex: "33FF57")
    static let background = Color(hex: "F5F5F5")
}
```

### Shared/Styles/AppFonts.swift
```swift
import SwiftUI

extension Font {
    // From Figma
    static let heading = Font.system(size: 24, weight: .bold)
    static let body = Font.system(size: 16, weight: .regular)
    static let caption = Font.system(size: 12, weight: .medium)
}
```

### Shared/COMPONENT_FORMAT.md
```markdown
# Component Format (from Figma)

## Style Guide
- Corner radius: 8px (small), 16px (large)
- Shadow: 0 4 8 black 20%
- Spacing: 8, 16, 24, 32

## Button Style
- Height: 48px
- Corner radius: 8px
- Font: Semi Bold 16px
```

## Quy tắc
- LUÔN lấy design tokens từ Figma trước khi code UI
- Update COMPONENT_FORMAT.md với style từ Figma
- Export assets với @2x, @3x scales
- Giữ naming consistent với Figma
