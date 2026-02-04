---
inclusion: always
---

# iOS Spec-Driven Toolkit - Development Guide

## 🎯 Project Overview

This is an **installer package** for iOS Spec-Driven Development Toolkit, not the toolkit itself.

**Purpose**: Distribute and install the toolkit to user projects via UVX.

## 📁 Working Directory

### Primary Development Location

```
src/ios_spec_driven_installer/templates/.claude/
```

**This is where you develop:**
- Skills (`.claude/skills/`)
- Agents (`.claude/agents/`)
- Scripts (`.claude/scripts/`)
- Guides (`.claude/shared/`)

### DO NOT Edit

- ❌ Root `.claude/` (doesn't exist anymore)
- ❌ Root `.mcp.json` (doesn't exist anymore)
- ✅ Only edit in `templates/` directory

## 🔧 Development Workflow

### 1. Modify Skills/Agents

```bash
# Edit skills
vim src/ios_spec_driven_installer/templates/.claude/skills/dev-spec-driven/SKILL.md

# Edit agents
vim src/ios_spec_driven_installer/templates/.claude/agents/write-spec.md

# Edit guides
vim src/ios_spec_driven_installer/templates/.claude/shared/PBT_GUIDE.md
```

### 2. Test Changes

```bash
# Install to test directory
source .venv/bin/activate
ios-spec-driven install /tmp/test-project --force

# Test in the installed location
cd /tmp/test-project
# Use Claude Code to test the toolkit
```

### 3. Validate

```bash
# Check installation
ios-spec-driven status /tmp/test-project

# Verify files
ls -la /tmp/test-project/.claude/
```

### 4. Commit Changes

```bash
# Add changes
git add src/ios_spec_driven_installer/templates/.claude/

# Commit with clear message
git commit -m "feat: improve write-spec agent with better validation"

# Push to dev branch
git push origin dev
```

## 📂 Directory Structure

```
ios-spec-driven-claude/
├── src/
│   └── ios_spec_driven_installer/
│       ├── cli.py                    # CLI commands (rarely change)
│       ├── installer.py              # Installation logic (rarely change)
│       └── templates/                # ← MAIN WORKING AREA
│           ├── .claude/              # ← DEVELOP HERE
│           │   ├── skills/           # 7 skills
│           │   │   ├── dev-spec-driven/
│           │   │   ├── ios-architecture/
│           │   │   ├── ios-components/
│           │   │   ├── ios-ui-ux/
│           │   │   ├── ios-debug/
│           │   │   ├── mcp-xcode/
│           │   │   └── mcp-figma/
│           │   ├── agents/           # 7 agents
│           │   │   ├── write-spec.md
│           │   │   ├── write-design.md
│           │   │   ├── write-tasks.md
│           │   │   ├── execute-tasks.md
│           │   │   ├── refine-spec.md
│           │   │   ├── quick-implement.md
│           │   │   └── research-prd.md
│           │   ├── scripts/          # Validation scripts
│           │   │   └── validate_traceability.py
│           │   ├── shared/           # Guides
│           │   │   ├── COMPONENT_FORMAT.md
│           │   │   ├── PBT_GUIDE.md
│           │   │   └── PARALLEL_EXECUTION_GUIDE.md
│           │   ├── hooks/            # Hooks (if any)
│           │   ├── settings.json
│           │   └── settings.local.json
│           ├── .mcp.json             # MCP server config
│           └── __init__.py
├── .github/workflows/                # CI/CD (automated testing)
├── pyproject.toml                    # Package config
├── MANIFEST.in                       # Package manifest
└── README.md                         # User documentation
```

## 🎯 Development Goals

### Current Version: 2.1.0

### Focus Areas

1. **Skills Improvement**
   - Enhance skill descriptions
   - Add more examples
   - Improve error handling

2. **Agents Enhancement**
   - Better prompts
   - More robust workflows
   - Improved error recovery

3. **Guides Expansion**
   - More detailed examples
   - Best practices
   - Common patterns

4. **Scripts Optimization**
   - Faster validation
   - Better error messages
   - More checks

## 📝 File Naming Conventions

### Skills
- Location: `templates/.claude/skills/<skill-name>/SKILL.md`
- Format: Always `SKILL.md` (uppercase)
- Frontmatter required: `name`, `description`, `keywords`

### Agents
- Location: `templates/.claude/agents/<agent-name>.md`
- Format: `<agent-name>.md` (lowercase with hyphens)
- Frontmatter required: `name`, `description`, `tools`, `skills`

### Guides
- Location: `templates/.claude/shared/<GUIDE_NAME>.md`
- Format: `<GUIDE_NAME>.md` (uppercase with underscores)
- No frontmatter required

## 🔍 Common Tasks

### Add New Skill

```bash
# 1. Create skill directory
mkdir -p src/ios_spec_driven_installer/templates/.claude/skills/new-skill

# 2. Create SKILL.md
vim src/ios_spec_driven_installer/templates/.claude/skills/new-skill/SKILL.md

# 3. Add frontmatter
---
name: new-skill
description: Description of the skill
keywords: [keyword1, keyword2]
---

# 4. Test and commit
```

### Add New Agent

```bash
# 1. Create agent file
vim src/ios_spec_driven_installer/templates/.claude/agents/new-agent.md

# 2. Add frontmatter
---
name: new-agent
description: Description of the agent
tools: [tool1, tool2]
skills: [skill1, skill2]
---

# 3. Test and commit
```

### Update Guide

```bash
# 1. Edit guide
vim src/ios_spec_driven_installer/templates/.claude/shared/GUIDE_NAME.md

# 2. Test and commit
```

## ⚠️ Important Rules

1. **Always work in `templates/` directory**
   - Never create `.claude/` at root
   - All changes must be in `src/.../templates/.claude/`

2. **Test before commit**
   - Install to test directory
   - Verify changes work
   - Check for errors

3. **Use dev branch**
   - Never commit directly to main
   - Always use dev branch
   - Merge to main when ready

4. **Clear commit messages**
   - Use conventional commits
   - `feat:`, `fix:`, `docs:`, `refactor:`
   - Be descriptive

5. **Update README if needed**
   - Document new features
   - Update examples
   - Keep it concise

## 🚀 Release Process

### When Ready to Release

1. **Test thoroughly**
   ```bash
   ios-spec-driven install /tmp/test --force
   # Test all features
   ```

2. **Update version** (if needed)
   ```bash
   # Edit pyproject.toml
   version = "2.2.0"
   
   # Edit __init__.py
   __version__ = "2.2.0"
   
   # Edit cli.py
   @click.version_option(version="2.2.0")
   ```

3. **Commit and push**
   ```bash
   git add .
   git commit -m "chore: bump version to 2.2.0"
   git push origin dev
   ```

4. **Merge to main**
   ```bash
   git checkout main
   git merge dev
   git push origin main
   ```

5. **Create tag** (optional)
   ```bash
   git tag v2.2.0
   git push origin v2.2.0
   ```

## 📚 Resources

- **Skills Documentation**: Each skill has detailed docs in `SKILL.md`
- **Agent Documentation**: Each agent has frontmatter with description
- **Guides**: Comprehensive guides in `shared/` directory
- **README**: User-facing documentation

## 🎓 Best Practices

1. **Keep skills focused** - One skill, one purpose
2. **Make agents clear** - Clear inputs, outputs, and steps
3. **Write good guides** - Examples, templates, best practices
4. **Test everything** - Don't break existing functionality
5. **Document changes** - Update docs when changing behavior

---

**Remember**: This is an installer package. Users will install the toolkit to their projects. Your changes here will be distributed to all users.
