<a id="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

<div align="center">
  <h1 align="center">iOS Spec-Driven Development Toolkit</h1>
  <p align="center">
    English | <a href="README.vi.md">Tiếng Việt</a>
    <br />
    <br />
    A production-oriented workflow kit for Claude Code and OpenCode.
    <br />
    Move from idea to implementation with clear artifacts: requirements -> design -> tasks -> code.
    <br />
    <br />
    <a href="https://github.com/nguyennamkkb/ios-spec-driven"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/nguyennamkkb/ios-spec-driven/issues">Report Bug</a>
    ·
    <a href="https://github.com/nguyennamkkb/ios-spec-driven/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#about">About</a></li>
    <li><a href="#why-it-works">Why It Works</a></li>
    <li><a href="#workflow-modes">Workflow Modes</a></li>
    <li><a href="#what-you-get">What You Get</a></li>
    <li><a href="#getting-started">Getting Started</a></li>
    <li><a href="#delivery-artifacts">Delivery Artifacts</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>

## About

Many AI coding sessions lose quality at handoff: requirements are vague, design decisions are scattered, and implementation is hard to validate.

This toolkit introduces a disciplined execution model for iOS teams:

- define outcomes before coding
- convert outcomes into structured specs
- map implementation tasks to acceptance criteria
- execute with consistent standards and review checkpoints

It supports both new product definition and feature-by-feature delivery in existing codebases.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Why It Works

- **Single delivery path** from idea to implementation, reducing context switching
- **Traceable specs** that connect requirements, design, and tasks
- **Reusable standards** for architecture, UI components, testing, and execution flow
- **Dual-IDE support** with automatic template transformation for Claude Code and OpenCode
- **Agentized workflow** that keeps progress predictable across team members

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Workflow Modes

### 1) Full Documentation Mode (new products)

Use this when starting from an idea and you need market-backed target documentation before implementation.

`@write-project-docs` is used to:

- research market context, user segments, and competing patterns
- clarify product goals and success criteria
- produce a complete target documentation set for delivery alignment

```text
@write-project-docs Create complete documentation for [project name]
```

Example:

```text
@write-project-docs Create complete documentation for fitness tracking app
```

### 2) Feature Delivery Mode (existing products)

Use this to ship one feature at a time with clear traceability.

```text
Create spec for [feature name]
```

Example:

```text
Create spec for user login feature
```

Fast path for small changes:

```text
Quick implementation of [small feature]
```

Example:

```text
Update design: add caching layer for dashboard data
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## What You Get

### 7 Specialized Skills

| Skill | Purpose |
|---|---|
| `dev-spec-driven` | Workflow orchestration and process discipline |
| `ios-architecture` | MVVM, Clean Architecture, SwiftUI patterns |
| `ios-components` | Reusable UI component standards |
| `ios-ui-ux` | UX patterns and accessibility |
| `ios-debug` | Debugging and performance optimization |
| `mcp-xcode` | Build, test, simulator, analysis |
| `mcp-figma` | Figma extraction and design handoff |

### 14 Workflow Agents

#### Project Documentation Workflow

| Agent | Output |
|---|---|
| `write-project-docs` | Orchestrates complete 5-document project flow |
| `write-project-overview` | `Project_Overview.md` |
| `write-use-cases` | `Use_Cases.md` |
| `write-functional-requirements` | `Functional_Requirements.md` |
| `write-wireframes` | `Wireframes.md` |
| `write-ux-flows` | `UX_Flows.md` |
| `review-project-docs` | Review and consistency checks |

#### Feature Development Workflow

| Agent | Output |
|---|---|
| `write-spec` | `requirements.md` |
| `write-design` | `design.md` |
| `write-tasks` | `tasks.md` |
| `execute-tasks` | SwiftUI implementation + tests |
| `refine-spec` | Update existing specs |
| `quick-implement` | Direct implementation for small scope |
| `research-prd` | PRD draft from research context |

### Shared Guides

- `COMPONENT_FORMAT.md`
- `PBT_GUIDE.md`
- `PARALLEL_EXECUTION_GUIDE.md`
- `SPEC_WORKFLOW_GUIDE.md`

### Design Style System (DSS)

- DSS in this toolkit means shared UI style tokens and usage conventions, not overall system architecture design.
- Runtime style tokens are managed in `shared/Styles/` (for example: `AppColors.swift`, `AppFonts.swift`, `AppSpacing.swift`).
- `COMPONENT_FORMAT.md` defines style usage conventions and code patterns for consistent UI implementation.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Getting Started

### Prerequisite

- Install [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Install for Claude Code

```bash
uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven ios-spec-driven install --ide claude
```

### Install for OpenCode

```bash
uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven ios-spec-driven install --ide opencode
```

### Configure Figma Token (Framelink MCP)

After installation, replace `YOUR_FIGMA_TOKEN` with your own personal access token:

- Claude Code: `.mcp.json`
- OpenCode: `.opencode/opencode.json`

How to create a Figma token:

- Follow Figma guide: https://help.figma.com/hc/en-us/articles/8085703771159-Manage-personal-access-tokens
- Required permissions: **File content (read)** and **Dev resources (read)**

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Delivery Artifacts

### Full Documentation Mode Output

```text
[.claude|.opencode]/specs/[project-name]/
  Project_Overview.md
  Use_Cases.md
  Functional_Requirements.md
  Wireframes.md
  UX_Flows.md
```

### Feature Delivery Mode Output

```text
[.claude|.opencode]/specs/[feature-name]/
  requirements.md
  design.md
  tasks.md
```

Typical delivery sequence:

```text
Idea
  -> market research and positioning
  -> project docs (target artifacts)
  -> feature planning
  -> implementation
  -> verification
```

Typical feature sequence:

```text
Idea
  -> requirements
  -> design
  -> tasks
  -> implementation
  -> verification
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Roadmap

- [ ] Improve automated tests for installer and template transformations
- [ ] Introduce release channels (`stable` and `dev`)
- [ ] Expand docs for multilingual team onboarding
- [ ] Extend validation for full project-document workflows

See [open issues](https://github.com/nguyennamkkb/ios-spec-driven/issues) for ongoing discussions.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Contact

Nguyen Nam - nguyennamkkb@gmail.com

Project Link: [https://github.com/nguyennamkkb/ios-spec-driven](https://github.com/nguyennamkkb/ios-spec-driven)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS -->
[contributors-shield]: https://img.shields.io/github/contributors/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[contributors-url]: https://github.com/nguyennamkkb/ios-spec-driven/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[forks-url]: https://github.com/nguyennamkkb/ios-spec-driven/network/members
[stars-shield]: https://img.shields.io/github/stars/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[stars-url]: https://github.com/nguyennamkkb/ios-spec-driven/stargazers
[issues-shield]: https://img.shields.io/github/issues/nguyennamkkb/ios-spec-driven.svg?style=for-the-badge
[issues-url]: https://github.com/nguyennamkkb/ios-spec-driven/issues
