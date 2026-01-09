---
name: ios-debug
description: Debug and fix iOS/Swift errors. Use when encountering compile errors, runtime errors, crashes, memory leaks, performance issues, SwiftUI preview not working, build failures.
allowed-tools: Read, Edit, Grep, Glob
---

# iOS Debug Guide

## Table of Contents
- [1. Compile Errors](#1-compile-errors) ............. L15-L120
- [2. SwiftUI Errors](#2-swiftui-errors) ............. L122-L200
- [3. Runtime Errors](#3-runtime-errors) ............. L202-L280
- [4. Build Errors](#4-build-errors) ................. L282-L330
- [5. Performance Issues](#5-performance-issues) ..... L332-L400
- [6. Debug Workflow](#6-debug-workflow) ............. L402-L450
- [7. Debug Tools](#7-debug-tools) ................... L452-L500
- [8. Checklist](#8-checklist) ....................... L502-L550

---

## 1. Compile Errors

### 1.1 Syntax Errors

#### Missing Brace/Bracket
```
Error: Expected '}' at end of closure
```
**Fix:**
- Count `{` and `}` pairs
- Use Xcode auto-indent to detect
- Check nested closures

#### Missing Comma
```
Error: Expected ',' separator
```
**Fix:**
- Check array/dictionary literals
- Check function parameters

### 1.2 Type Errors

#### Type Mismatch
```
Error: Cannot convert value of type 'String' to expected argument type 'Int'
```
**Fix:**
```swift
// Bad
let age: Int = "25"

// Good
let age: Int = Int("25") ?? 0
```

#### Optional Unwrapping
```
Error: Value of optional type 'String?' must be unwrapped
```
**Fix:**
```swift
// Option 1: Optional binding
if let name = getName() {
    print(name.uppercased())
}

// Option 2: Nil coalescing
let name = getName() ?? "Unknown"

// Option 3: Optional chaining
print(getName()?.uppercased() ?? "")
```

#### Cannot Infer Type
```
Error: Type of expression is ambiguous without more context
```
**Fix:**
```swift
// Bad
let items = []

// Good
let items: [String] = []
let items = [String]()
```

### 1.3 Access Control

```
Error: 'init' is inaccessible due to 'private' protection level
```
**Fix:**
- Change `private` to `internal` or `public`
- Or access from within the same file

### 1.4 Protocol Conformance

```
Error: Type 'MyClass' does not conform to protocol 'Codable'
```
**Fix:**
- Implement required methods/properties
- Ensure all properties are Codable for auto-synthesis

---

## 2. SwiftUI Errors

### 2.1 View Body Type

#### Multiple Views Without Container
```
Error: Function declares an opaque return type, but has no return statements
```
**Fix:**
```swift
// Bad
var body: some View {
    Text("Hello")
    Text("World")
}

// Good
var body: some View {
    VStack {
        Text("Hello")
        Text("World")
    }
}
```

#### Too Many Views (ViewBuilder Limit)
```
Error: Extra argument in call
```
**Fix:**
```swift
// Use Group to organize
VStack {
    Group {
        Text("1")
        Text("2")
        // ... up to 10
    }
    Group {
        Text("11")
        // ...
    }
}
```

### 2.2 State Management

#### @State Outside View
```
Error: @State can only be applied to properties of structs
```
**Fix:** Use `@State` only in View structs, use `@Published` in ObservableObject classes

#### @Published Outside ObservableObject
```
Error: @Published can only be applied to classes
```
**Fix:** Use `@Published` only in classes conforming to ObservableObject

### 2.3 Preview Errors

```
Error: Cannot preview in this file
```
**Fix:**
- Ensure PreviewProvider exists
- Provide mock data if needed
- Check for runtime errors in view

---

## 3. Runtime Errors

### 3.1 Force Unwrap Crash

```
Fatal error: Unexpectedly found nil while unwrapping an Optional value
```
**Fix:**
```swift
// Bad
let name = user.name!

// Good
guard let name = user.name else { return }
// or
let name = user.name ?? "Unknown"
```

### 3.2 Array Index Out of Bounds

```
Fatal error: Index out of range
```
**Fix:**
```swift
// Bad
let item = items[5]

// Good
guard items.indices.contains(5) else { return }
let item = items[5]

// Or use safe subscript extension
extension Array {
    subscript(safe index: Int) -> Element? {
        indices.contains(index) ? self[index] : nil
    }
}
```

### 3.3 Main Thread Violation

```
Warning: Publishing changes from background threads is not allowed
```
**Fix:**
```swift
// Bad
DispatchQueue.global().async {
    self.items = newItems // UI update on background
}

// Good
DispatchQueue.global().async {
    let newItems = fetchItems()
    DispatchQueue.main.async {
        self.items = newItems
    }
}

// Or with async/await
Task {
    let newItems = await fetchItems()
    await MainActor.run {
        self.items = newItems
    }
}
```

### 3.4 Memory Leaks (Retain Cycles)

**Fix:**
```swift
// Bad - Strong reference cycle
onComplete = {
    self.doSomething() // Strong self
}

// Good - Weak self
onComplete = { [weak self] in
    self?.doSomething()
}
```

---

## 4. Build Errors

### 4.1 Missing File
```
Error: No such file or directory
```
**Fix:**
- Check file exists in project
- Check file added to target
- Clean build folder

### 4.2 Duplicate Symbols
```
Error: Duplicate symbol '_OBJC_CLASS_$_MyClass'
```
**Fix:**
- Check file added to target multiple times
- Remove duplicate

### 4.3 Framework Not Found
```
Error: Framework not found 'SomeFramework'
```
**Fix:**
- Check SPM dependencies resolved
- Check CocoaPods installed
- Clean + rebuild

### 4.4 Code Signing
```
Error: Code signing failed
```
**Fix:**
- Check provisioning profile
- Check bundle identifier
- Check team selection

---

## 5. Performance Issues

### 5.1 Slow View Rendering

**Symptoms:** UI lag, slow scrolling

**Debug:**
```swift
.onAppear {
    print("⏱️ View appeared: \(Date())")
}
```

**Fix:**
- Use lazy loading for lists
- Reduce view complexity
- Cache computed values
- Use `@StateObject` instead of `@ObservedObject` for owned objects

### 5.2 Memory Warning

**Symptoms:** App crash on low memory

**Fix:**
- Release unused objects
- Reduce image sizes
- Implement pagination
- Use weak references appropriately

### 5.3 Network Timeout

**Symptoms:** Requests fail, long loading

**Fix:**
- Increase timeout
- Optimize API
- Add retry logic
- Show appropriate loading states

---

## 6. Debug Workflow

### Step 1: Read Error Message
- File path
- Line number
- Error description

### Step 2: Locate Issue
- Go to file and line
- Read surrounding code
- Check recent changes

### Step 3: Understand Context
- What is the code trying to do?
- What are the inputs?
- What are the expected outputs?

### Step 4: Apply Fix
- Fix based on patterns above
- Test the fix
- Rebuild

### Step 5: Verify
- Build success
- Tests pass
- No new warnings

---

## 7. Debug Tools

### 7.1 Print Debugging
```swift
print("🔍 Debug: \(variable)")
print("🔍 Type: \(type(of: variable))")
dump(complexObject)
```

### 7.2 Breakpoints
- Set breakpoint at issue line
- Inspect variables
- Step through code

### 7.3 LLDB Commands
```
po variable          // Print object
p variable           // Print value
bt                   // Backtrace
frame variable       // All variables in frame
```

### 7.4 View Hierarchy
- Xcode → Debug → View Debugging
- Inspect view layout
- Check constraints

---

## 8. Checklist

### When Encountering Compile Error
- [ ] Read full error message
- [ ] Locate file and line number
- [ ] Check syntax (braces, commas)
- [ ] Check types
- [ ] Check imports

### When Encountering Runtime Error
- [ ] Check crash log
- [ ] Identify crash line
- [ ] Check force unwraps
- [ ] Check array access
- [ ] Check thread safety

### When Encountering Performance Issue
- [ ] Profile with Instruments
- [ ] Check memory usage
- [ ] Check CPU usage
- [ ] Optimize hot paths
- [ ] Add caching

### Before Commit
- [ ] No compile errors
- [ ] No runtime crashes
- [ ] No memory leaks
- [ ] Tests pass
- [ ] Performance acceptable
