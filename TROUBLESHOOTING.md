# OpenCode Agent Troubleshooting Guide

## ✅ FIXED: Automatic Tool Format Transformation

**As of version 2.1.0**, the installer automatically transforms agent tool formats when installing for OpenCode. You no longer need to manually fix tool formats!

### How It Works

When you install with `--ide opencode`, the installer:
1. Reads agent files from `templates/content/agents/`
2. Automatically transforms tool format from Claude Code to OpenCode
3. Installs the transformed files to `.opencode/agents/`

**Example transformation:**

```yaml
# Source (Claude Code format)
tools: Read, Write, Grep, Glob, WebSearch

# Installed (OpenCode format)
tools:
  write: true
  grepSearch: true
  fileSearch: true
  webSearch: true
```

### Tool Name Mapping

| Claude Code | OpenCode | Notes |
|------------|----------|-------|
| `Read` | (removed) | Automatic in OpenCode |
| `Write` | `write` | Lowercase |
| `Edit` | `edit` | Lowercase |
| `Grep` | `grepSearch` | Different name |
| `Glob` | `fileSearch` | Different name |
| `Bash` | `bash` | Lowercase |
| `WebSearch` | `webSearch` | camelCase |
| `WebFetch` | `webFetch` | camelCase |

---

## Common Errors and Solutions

### Error: "Invalid input: expected record, received string tools"

**Note:** This error should not occur with version 2.1.0+ if you installed using the CLI. If you still see this error, you may be using an older version or manually edited files.

#### 🔴 Problem

When defining agents in Markdown files (`.md`), you get this error:

```
Configuration is invalid at /path/to/.opencode/agents/agent-name.md
↳ Invalid input: expected record, received string tools
```

#### 🔍 Root Cause

In **Markdown agents**, the `tools` field in frontmatter must be a **YAML object** (key-value pairs), not a comma-separated string.

#### ❌ Wrong Format

```yaml
---
name: my-agent
description: My agent description
tools: write, edit, bash, webSearch
---
```

This format treats `tools` as a string, which causes the error.

#### ✅ Correct Format

```yaml
---
name: my-agent
description: My agent description
tools:
  write: true
  edit: true
  bash: true
  webSearch: true
---
```

Each tool must be on its own line with `true` or `false` value.

---

## Tool Names Reference

### ⚠️ Common Mistakes

| ❌ Wrong | ✅ Correct | Description |
|---------|-----------|-------------|
| `Read` | (not needed) | Reading is automatic |
| `Write` | `write` | Must be lowercase |
| `Edit` | `edit` | Must be lowercase |
| `Bash` | `bash` | Must be lowercase |
| `Grep` | `grepSearch` | Wrong tool name |
| `Glob` | `fileSearch` | Wrong tool name |
| `WebSearch` | `webSearch` | Must be camelCase |
| `WebFetch` | `webFetch` | Must be camelCase |
| `web_search` | `webSearch` | Wrong format |

### ✅ Valid Tool Names

| Tool Name | Purpose | Example |
|-----------|---------|---------|
| `write` | Create/overwrite files | Create new file |
| `edit` | Modify existing files | Update code |
| `bash` | Execute shell commands | Run scripts, git commands |
| `grepSearch` | Search text in files | Find code patterns |
| `fileSearch` | Find files by name/pattern | Locate files |
| `webSearch` | Search the web | Research information |
| `webFetch` | Fetch web page content | Get documentation |
| `todo` | Manage todo list | Track tasks |

---

## Format Differences: JSON vs Markdown

### JSON Config (`opencode.json`)

In JSON config, tools use the **same object format**:

```json
{
  "agent": {
    "my-agent": {
      "description": "My agent",
      "mode": "subagent",
      "tools": {
        "write": true,
        "edit": true,
        "bash": true
      }
    }
  }
}
```

### Markdown Config (`.opencode/agents/*.md`)

In Markdown frontmatter, tools use **YAML object format**:

```yaml
---
name: my-agent
description: My agent
mode: subagent
tools:
  write: true
  edit: true
  bash: true
---

# Agent Prompt Content

Your agent instructions go here...
```

**Key difference**: YAML requires proper indentation (2 spaces).

---

## Complete Example: Markdown Agent

```yaml
---
name: code-reviewer
description: Reviews code for best practices and potential issues. Use when reviewing pull requests, checking code quality, finding bugs.
mode: subagent
tools:
  write: false
  edit: false
  grepSearch: true
  fileSearch: true
  bash: false
skills: code-review, security
---

# Code Reviewer Agent

## Objective
Review code for:
- Security vulnerabilities
- Performance issues
- Best practices violations
- Code smells

## Process
1. Read the code files
2. Analyze for issues
3. Provide detailed feedback
4. Suggest improvements

## Rules
- Focus on critical issues first
- Provide specific examples
- Suggest concrete fixes
```

---

## Validation Checklist

Before saving your agent file, check:

- [ ] `tools` is a YAML object (not a string)
- [ ] Each tool has `: true` or `: false`
- [ ] Tool names are lowercase/camelCase (not capitalized)
- [ ] Indentation is 2 spaces (not tabs)
- [ ] Tool names are correct (see reference table)
- [ ] No trailing commas in YAML
- [ ] Frontmatter starts and ends with `---`

---

## Quick Fix Script

If you have many agents to fix, use this pattern:

**Before:**
```yaml
tools: write, edit, bash
```

**After:**
```yaml
tools:
  write: true
  edit: true
  bash: true
```

**Regex Find:** `tools: (.+)`

**Replace with:**
```
tools:
  $1
```

Then manually format each tool on its own line with `: true`.

---

## Testing Your Agent

After fixing, test your agent:

1. **Reload OpenCode** - Restart or reload config
2. **Check for errors** - Look for validation messages
3. **Invoke agent** - Try `@agent-name` in chat
4. **Verify tools** - Confirm agent can use expected tools

---

## Additional Resources

- [OpenCode Agents Documentation](https://opencode.ai/docs/agents/)
- [OpenCode Tools Documentation](https://opencode.ai/docs/tools/)
- [YAML Syntax Guide](https://yaml.org/spec/1.2/spec.html)

---

## Common Questions

### Q: Why can't I use `Read` as a tool?

**A:** OpenCode automatically allows agents to read files. You don't need to explicitly grant read permission.

### Q: What's the difference between `grepSearch` and `fileSearch`?

**A:** 
- `grepSearch` - Search **content** inside files (like `grep`)
- `fileSearch` - Search **file names** by pattern (like `find`)

### Q: Can I use wildcards for tools?

**A:** Yes, in JSON config you can use wildcards:

```json
{
  "tools": {
    "mcp-server-*": false  // Disable all MCP server tools
  }
}
```

But in Markdown frontmatter, you must list each tool explicitly.

### Q: How do I disable all tools?

**A:** Set each tool to `false`:

```yaml
tools:
  write: false
  edit: false
  bash: false
```

Or in JSON, you can use a wildcard:

```json
{
  "tools": {
    "*": false,
    "grepSearch": true,  // Only allow search
    "fileSearch": true
  }
}
```

---

## Error Messages Reference

| Error Message | Cause | Solution |
|--------------|-------|----------|
| `expected record, received string tools` | Tools is a string | Use YAML object format |
| `Unknown tool: Read` | Invalid tool name | Remove `Read` (automatic) |
| `Unknown tool: Grep` | Wrong tool name | Use `grepSearch` |
| `Unknown tool: Glob` | Wrong tool name | Use `fileSearch` |
| `Invalid YAML syntax` | Indentation error | Use 2 spaces, not tabs |

---

## Testing Your Installation

### Verify OpenCode Installation

After installing with `--ide opencode`, verify the transformation worked:

```bash
# Install
ios-spec-driven install /path/to/project --ide opencode --force

# Check an agent file
cat /path/to/project/.opencode/agents/write-spec.md
```

**Expected frontmatter:**

```yaml
---
name: write-spec
description: Write requirements for new features...
tools:
  write: true
  grepSearch: true
  fileSearch: true
  webSearch: true
  webFetch: true
skills: dev-spec-driven
---
```

### Verify Claude Code Installation

For Claude Code, tools remain in array format:

```bash
# Install
ios-spec-driven install /path/to/project --ide claude --force

# Check an agent file
cat /path/to/project/.claude/agents/write-spec.md
```

**Expected frontmatter:**

```yaml
---
name: write-spec
description: Write requirements for new features...
tools: Read, Write, Grep, Glob, WebSearch, WebFetch
skills: dev-spec-driven
---
```

---

*Last updated: 2025-02-05*
*OpenCode Version: Latest*
*Toolkit Version: 2.1.0+*
