---
name: xcode-debug
description: Debug và khắc phục lỗi Xcode. Dùng khi build failed, app crash, lỗi signing, lỗi pod install, lỗi SPM, undefined symbols, memory leak, xem crash log, tại sao build lâu, archive bị lỗi, simulator không chạy, device không nhận.
allowed-tools: Read, Grep, Glob
---

# Xcode Debug & Troubleshooting

## Ưu tiên sử dụng XcodeBuildMCP

**LUÔN dùng XcodeBuildMCP tools thay vì bash commands:**

| Thay vì | Dùng |
|---------|------|
| `xcodebuild -list` | `xcode_list_schemes` |
| `xcodebuild build` | `xcode_build` |
| `xcodebuild test` | `xcode_test` |
| `xcodebuild clean` | `xcode_clean` |

## Quy trình Debug

### 1. List schemes
```
Tool: xcode_list_schemes
→ Xác định scheme name
```

### 2. Build & Check
```
Tool: xcode_build
Parameters:
- scheme: [từ bước 1]
- configuration: Debug
→ Đọc output để tìm errors
```

### 3. Clean nếu cần
```
Tool: xcode_clean
→ Sau đó build lại
```

## Phân loại lỗi phổ biến

| Loại lỗi | Dấu hiệu | Hướng xử lý |
|----------|----------|-------------|
| Compile Error | `error:` trong log | Kiểm tra syntax, missing imports |
| Linker Error | `Undefined symbols` | Kiểm tra linked frameworks, dependencies |
| Signing Error | `Code signing` | Kiểm tra provisioning profile, certificates |
| Pod/SPM Error | `pod install`, `Package.resolved` | Update dependencies |

## Xử lý Dependencies

### CocoaPods
```bash
pod install --repo-update
```

### Swift Package Manager
```bash
swift package resolve
swift package update
```

## Phân tích Crash Logs

**Vị trí crash logs:**
- Device: `~/Library/Logs/DiagnosticReports/`
- Simulator: `~/Library/Logs/DiagnosticReports/`

## Checklist Debug

- [ ] Đọc error message đầy đủ
- [ ] Clean build (xcode_clean)
- [ ] Xóa DerivedData nếu cần
- [ ] Update dependencies (Pod/SPM)
- [ ] Kiểm tra Xcode version compatibility
- [ ] Kiểm tra iOS Deployment Target
- [ ] Verify code signing settings

## Files quan trọng cần kiểm tra

- `*.xcodeproj/project.pbxproj` - Project settings
- `Podfile` / `Package.swift` - Dependencies
- `Info.plist` - App configuration
- `*.entitlements` - App capabilities
