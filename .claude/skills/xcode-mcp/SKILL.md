---
name: xcode-mcp
description: Sử dụng XcodeBuildMCP để build, run, test iOS/macOS apps. Dùng thay cho lệnh bash xcodebuild. Dùng khi cần build project, run app, chạy tests, check errors, list schemes.
allowed-tools: Read, Grep, Glob
---

# XcodeBuildMCP Usage

## Khi nào dùng
- Build project iOS/macOS
- Run app trên simulator/device
- Chạy unit tests, UI tests
- Check build errors
- List schemes, destinations

## MCP Tools

### 1. xcode_build
Build project với scheme và destination.

```
Tool: xcode_build
Parameters:
- scheme: Tên scheme (required)
- project: Path to .xcodeproj (optional nếu có workspace)
- workspace: Path to .xcworkspace (optional)
- configuration: Debug | Release (default: Debug)
- destination: Simulator/device destination
```

**Ví dụ:**
```json
{
  "scheme": "MyApp",
  "workspace": "MyApp.xcworkspace",
  "configuration": "Debug",
  "destination": "platform=iOS Simulator,name=iPhone 15"
}
```

### 2. xcode_test
Chạy tests.

```
Tool: xcode_test
Parameters:
- scheme: Tên scheme (required)
- project/workspace: Path (optional)
- destination: Simulator destination
- testPlan: Test plan name (optional)
```

**Ví dụ:**
```json
{
  "scheme": "MyAppTests",
  "workspace": "MyApp.xcworkspace",
  "destination": "platform=iOS Simulator,name=iPhone 15"
}
```

### 3. xcode_clean
Clean build folder.

```
Tool: xcode_clean
Parameters:
- scheme: Tên scheme
- project/workspace: Path
```

### 4. xcode_list_schemes
List tất cả schemes trong project.

```
Tool: xcode_list_schemes
Parameters:
- project: Path to .xcodeproj
- workspace: Path to .xcworkspace
```

### 5. xcode_list_destinations
List available simulators/devices.

```
Tool: xcode_list_destinations
Parameters:
- scheme: Tên scheme
- project/workspace: Path
```

### 6. xcode_show_build_settings
Xem build settings.

```
Tool: xcode_show_build_settings
Parameters:
- scheme: Tên scheme
- project/workspace: Path
- configuration: Debug | Release
```

## Workflow phổ biến

### Build & Check Errors
```
1. xcode_list_schemes → Lấy scheme name
2. xcode_build → Build project
3. Đọc output → Check errors/warnings
```

### Run Tests
```
1. xcode_list_schemes → Tìm test scheme
2. xcode_test → Chạy tests
3. Đọc output → Check pass/fail
```

### Clean Build
```
1. xcode_clean → Clean
2. xcode_build → Build lại
```

## Thay thế bash commands

| Bash Command | XcodeBuildMCP Tool |
|--------------|-------------------|
| `xcodebuild -list` | `xcode_list_schemes` |
| `xcodebuild -scheme X build` | `xcode_build` |
| `xcodebuild test` | `xcode_test` |
| `xcodebuild clean` | `xcode_clean` |
| `xcodebuild -showBuildSettings` | `xcode_show_build_settings` |

## Quy tắc
- LUÔN dùng XcodeBuildMCP thay vì bash xcodebuild
- List schemes trước khi build nếu không biết scheme name
- Check destinations trước khi run/test
