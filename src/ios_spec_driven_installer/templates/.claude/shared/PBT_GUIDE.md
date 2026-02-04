# Property-Based Testing Guide

## Framework: SwiftCheck

We use **SwiftCheck** for property-based testing in iOS projects.

### Installation

Add to `Package.swift`:

```swift
dependencies: [
    .package(url: "https://github.com/typelift/SwiftCheck", from: "0.12.0")
]

targets: [
    .testTarget(
        name: "YourTests",
        dependencies: ["SwiftCheck"]
    )
]
```

Or via Xcode:
1. File → Add Package Dependencies
2. Enter: `https://github.com/typelift/SwiftCheck`
3. Select version: 0.12.0 or later

---

## Property Types & Templates

### 1. Round-Trip Property

**Definition**: Encode then decode returns original value

**Template**:
```swift
import XCTest
import SwiftCheck
@testable import YourModule

final class ModelPropertyTests: XCTestCase {
    func testRoundTripProperty() {
        property("User round-trip: encode then decode = original") <- forAll { (user: User) in
            let encoder = JSONEncoder()
            let decoder = JSONDecoder()
            
            guard let data = try? encoder.encode(user),
                  let decoded = try? decoder.decode(User.self, from: data) else {
                return false
            }
            
            return user == decoded
        }
    }
}
```

**Arbitrary Generator**:
```swift
extension User: Arbitrary {
    public static var arbitrary: Gen<User> {
        return Gen.compose { c in
            return User(
                id: c.generate(using: UUID.arbitrary),
                name: c.generate(using: String.arbitrary),
                email: c.generate(using: String.arbitrary),
                age: c.generate(using: Int.arbitrary.suchThat { $0 >= 0 && $0 <= 120 })
            )
        }
    }
}
```

---

### 2. Invariant Property

**Definition**: Condition always true after any operation

**Template**:
```swift
func testStateInvariantProperty() {
    property("ViewModel state always valid") <- forAll { (actions: [Action]) in
        let viewModel = MyViewModel()
        
        for action in actions {
            viewModel.perform(action)
        }
        
        // Invariant: state must be one of valid states
        return [.idle, .loading, .success, .error].contains(viewModel.state)
    }
}
```

**Custom Action Generator**:
```swift
enum Action: Arbitrary {
    case load
    case refresh
    case cancel
    
    static var arbitrary: Gen<Action> {
        return Gen.one(of: [
            Gen.pure(.load),
            Gen.pure(.refresh),
            Gen.pure(.cancel)
        ])
    }
}
```

---

### 3. Idempotent Property

**Definition**: Multiple executions = single execution

**Template**:
```swift
func testDeleteIdempotentProperty() {
    property("Delete twice = delete once") <- forAll { (itemId: UUID) in
        let service = MyService()
        
        // Delete once
        try? service.delete(itemId)
        let resultAfterOne = service.exists(itemId)
        
        // Delete again
        try? service.delete(itemId)
        let resultAfterTwo = service.exists(itemId)
        
        // Both should be false (item deleted)
        return resultAfterOne == false && resultAfterTwo == false
    }
}
```

---

### 4. Commutative Property

**Definition**: Order doesn't matter

**Template**:
```swift
func testAddCommutativeProperty() {
    property("Add A then B = Add B then A") <- forAll { (a: Item, b: Item) in
        let list1 = MyList()
        list1.add(a)
        list1.add(b)
        
        let list2 = MyList()
        list2.add(b)
        list2.add(a)
        
        // Order shouldn't matter for set-like collections
        return list1.items.sorted() == list2.items.sorted()
    }
}
```

---

## Common Generators

### String with Constraints

```swift
// Non-empty string
let nonEmptyString = String.arbitrary.suchThat { !$0.isEmpty }

// Email-like string
let emailString = Gen.compose { c in
    let name = c.generate(using: String.arbitrary.suchThat { !$0.isEmpty })
    let domain = c.generate(using: String.arbitrary.suchThat { !$0.isEmpty })
    return "\(name)@\(domain).com"
}
```

### Int with Range

```swift
// Age: 0-120
let ageGen = Int.arbitrary.suchThat { $0 >= 0 && $0 <= 120 }

// Positive int
let positiveInt = Int.arbitrary.suchThat { $0 > 0 }
```

### Array with Size

```swift
// Array of 1-10 items
let smallArray = Gen.sized { size in
    Gen.arrayOf(String.arbitrary, size: Gen.choose((1, 10)))
}
```

### Optional

```swift
// 50% chance of nil
let optionalString = Gen.frequency([
    (1, Gen.pure(nil)),
    (1, String.arbitrary.map { Optional($0) })
])
```

---

## Best Practices

### 1. Test Count

Run at least **100 tests** per property:

```swift
property("My property", arguments: CheckerArguments(maxTestCaseSize: 100)) <- forAll { ... }
```

### 2. Shrinking

SwiftCheck automatically shrinks failing cases. Help it by providing good generators:

```swift
// Bad: Too broad
let badGen = Int.arbitrary

// Good: Constrained
let goodGen = Int.arbitrary.suchThat { $0 >= 0 && $0 <= 100 }
```

### 3. Property Statement in Comments

Always include property statement:

```swift
// Property: For any User, encode then decode returns original
// Validates: AC-001.1, AC-001.2
func testUserRoundTrip() { ... }
```

### 4. Separate PBT from Unit Tests

```
Tests/
├── UnitTests/
│   └── ViewModelTests.swift
└── PropertyTests/
    └── ViewModelPropertyTests.swift
```

---

## Integration with Spec Workflow

### In design.md

```markdown
## 5. Correctness Properties

| # | Property | Type | Validates | Statement |
|---|----------|------|-----------|-----------|
| P1 | User round-trip | Round-trip | AC-001.1 | Encode then decode = original |
| P2 | State invariant | Invariant | AC-002.1 | State always valid |
```

### In tasks.md

```markdown
- [ ] **2.1.3** [PBT] Property P1: User round-trip
  - Property: Encode then decode = original
  - File: `Tests/PropertyTests/UserPropertyTests.swift`
  - Framework: SwiftCheck
  - Validates: AC-001.1
  - Optional: Yes
```

### In execute-tasks agent

When implementing PBT task:
1. Read property statement from design.md
2. Choose appropriate template (round-trip, invariant, etc.)
3. Implement using SwiftCheck
4. Run with 100+ test cases
5. If fails → Report to user (don't auto-fix)

---

## Troubleshooting

### SwiftCheck not found

```bash
# Clean and rebuild
rm -rf .build
swift build
```

### Test timeout

```swift
// Reduce test count
property("My property", arguments: CheckerArguments(maxTestCaseSize: 50)) <- ...
```

### Generator too slow

```swift
// Use simpler generators
let fastGen = Gen.choose((0, 100))  // Instead of complex arbitrary
```

---

## Examples

See complete examples in:
- `.claude/specs/example-todo-list/` (if exists)
- `Tests/PropertyTests/` in your project

---

*Last updated: February 2026*
*Framework: SwiftCheck 0.12.0+*
