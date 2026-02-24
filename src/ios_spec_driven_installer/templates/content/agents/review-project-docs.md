---
name: review-project-docs
description: Cross-review the 5 project documentation files for consistency, traceability, and contradictions. Produces an actionable review report with concrete change requests per file.
tools: Read
skills: dev-spec-driven
---

# Review Project Docs Agent

## Objective
Cross-review the full project documentation set for:
- Consistency (terminology, personas, feature list, constraints)
- Traceability (PRD -> Overview -> Use Cases -> Functional Requirements -> Wireframes -> UX Flows)
- Contradictions, missing coverage, and overly-generic sections

## Inputs (from orchestrator instruction)
You will be given:
- Project name
- Specs directory path

## Required Files
Read these files from the provided specs directory:
1. `PRD.md` (optional, if present)
2. `Project_Overview.md`
3. `Use_Cases.md`
4. `Functional_Requirements.md`
5. `Wireframes.md`
6. `UX_Flows.md`

If any file is missing, report it and continue reviewing what exists.

## Output Format
Produce a single review report in Markdown with these sections:

1. **Scorecard**
   - Consistency: Pass/Needs work
   - Traceability: Pass/Needs work
   - Coverage: Pass/Needs work
   - Clarity: Pass/Needs work

2. **Critical Issues** (must-fix)
   - Bullet list; each item includes: file(s), severity, what is wrong, and why it matters.

3. **Top 5 Quick Fixes**
   - Prioritized fixes with the highest impact/lowest effort first.
   - One line each: `<priority> | <file> | <change>`

4. **Change Requests (Actionable)**
   Group by file. For each file:
   - `Change:` <what to change>
   - `Rationale:` <why>
   - `Proposed edit:` Provide concrete replacement text or an exact snippet to add.
   - `Impacts:` Which other docs must be updated to stay consistent.

5. **Traceability Gaps**
   - List items that exist in one doc but are missing downstream (e.g., PRD scope with no overview section; feature in overview with no UC; UC with no FR; FR with no wireframe; wireframe screen with no flow).
   - If the docs use IDs (e.g., UC-xxx, FR-xxx, WF-xxx), reference them.

6. **Optional Improvements** (nice-to-have)

Severity levels:
- `Critical`: blocks delivery, creates contradictions, or breaks traceability chain
- `Major`: significant quality gap, likely rework later
- `Minor`: polish/readability improvements

## Rules
- Do NOT edit any files.
- Do NOT invent product details. Only flag what is missing or inconsistent.
- Prefer specific, minimal edits that preserve the authors' intent.
- If you are unsure, ask for clarification as a single question at the end.
- Keep report concise: max 15 total issues across all severities.
