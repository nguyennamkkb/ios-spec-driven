---
name: mcp-xcode
description: Build and test iOS apps with Xcode. Use when building projects, running tests, checking errors, getting build logs, listing schemes, clean builds, archiving apps.
allowed-tools: Read, MCP, Bash
---

# Xcode MCP Integration

## Table of Contents
- [1. MCP Tools](#1-mcp-tools)
- [2. Workflows](#2-workflows)
- [3. Error Handling](#3-error-handling)
- [4. Build Configurations](#4-build-configurations)
- [5. Checklist](#5-checklist)

---

## 1. MCP Tools

### xcode_list_schemes
List all schemes in project.
- Input: None (auto-detect)
- Output: Scheme list, default scheme
- Use: First setup, before build

### xcode_build
Build project or workspace.
- Input: scheme (required), configuration (Debug/Release), clean (true/false)
- Output: Build status, errors, warnings, build time
- Use: After implementing tasks, before commit

### xcode_test
Run unit and UI tests.
- Input: scheme (required), testPlan (optional), only (specific test)
- Output: Test results, failed details, coverage
- Use: After writing tests, before commit

### xcode_clean
Clean build folder.
- Input: scheme (required)
- Output: Clean status
- Use: Unclear build errors, after dependency changes

### xcode_get_build_settings
Get project build settings.
- Input: scheme, configuration
- Output: All build settings
- Use: Debug build issues


---

## 2. Workflows

### Setup Project (First Time)
1. `xcode_list_schemes` → Save scheme name
2. `xcode_build` with scheme, Debug config
3. Fix errors if any

### After Task Implementation
1. `xcode_build` with scheme
2. Success → Continue
3. Failed → Fix errors → Rebuild

### After Phase Completion
1. `xcode_clean`
2. `xcode_build` with clean: true
3. `xcode_test`
4. All pass → git commit

### Pre-Commit
1. xcode_clean
2. xcode_build (clean: true)
3. xcode_test
4. All pass → commit

---

## 3. Error Handling

### Common Build Errors

| Error | Fix |
|-------|-----|
| Syntax error | Read file, fix syntax |
| Type mismatch | Check types, convert if needed |
| Missing import | Add import statement |
| Unresolved identifier | Check declaration, DI |

### Common Test Errors

| Error | Fix |
|-------|-----|
| Test timeout | Increase timeout or check async |
| Assertion failed | Check logic, update test/code |
| Missing test target | Check scheme includes tests |

---

## 4. Build Configurations

### Debug vs Release

| Setting | Debug | Release |
|---------|-------|---------|
| Optimization | None | Aggressive |
| Debug Symbols | Yes | No |
| Build Time | Fast | Slow |
| App Size | Large | Small |

### Destinations
- Simulator: `platform=iOS Simulator,name=iPhone 15 Pro`
- Device: `platform=iOS,id=[UDID]`
- Generic: `generic/platform=iOS`

---

## 5. Checklist

### Each Build
- [ ] Correct scheme name
- [ ] Appropriate configuration
- [ ] Read errors if any
- [ ] Fix errors top to bottom

### Each Test Run
- [ ] Build passes first
- [ ] Scheme includes test targets
- [ ] Read failed test details

### Pre-Commit
- [ ] Clean build
- [ ] All tests pass
- [ ] No warnings (or acceptable)
