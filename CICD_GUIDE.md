# CI/CD Guide

This guide explains how to use GitHub Actions workflows for automated testing, merging, and releasing.

## 📋 Workflows

### 1. Test Workflow (`test.yml`)

**Triggers**:
- Push to `dev` or `plugin` branches
- Pull requests to `main` or `dev`

**What it does**:
- Tests installation on Ubuntu and macOS
- Tests with Python 3.8 and 3.12
- Runs all CLI commands
- Verifies file installation
- Builds package

**Status**: Runs automatically on push/PR

---

### 2. Merge to Main Workflow (`merge-to-main.yml`)

**Triggers**: Manual (workflow_dispatch)

**What it does**:
1. Merges specified branch (default: `dev`) to `main`
2. Optionally bumps version (patch/minor/major)
3. Updates version in all files
4. Creates git tag
5. Pushes to main

**How to use**:

#### Via GitHub UI:
1. Go to **Actions** tab
2. Select **"Merge to Main"** workflow
3. Click **"Run workflow"**
4. Configure options:
   - **Source branch**: Branch to merge (default: `dev`)
   - **Create release**: Create release after merge (default: `true`)
   - **Version bump**: `none`, `patch`, `minor`, or `major` (default: `patch`)
5. Click **"Run workflow"**

#### Via GitHub CLI:
```bash
# Merge dev to main with patch version bump
gh workflow run merge-to-main.yml \
  -f source_branch=dev \
  -f create_release=true \
  -f version_bump=patch

# Merge without version bump
gh workflow run merge-to-main.yml \
  -f source_branch=dev \
  -f create_release=false \
  -f version_bump=none
```

---

### 3. Release Workflow (`release.yml`)

**Triggers**:
- Push to `main` branch
- Push tags matching `v*` (e.g., `v2.1.0`)

**What it does**:
1. Builds Python package
2. Generates changelog from commits
3. Creates GitHub Release
4. Uploads distribution files

**Status**: Runs automatically when tag is pushed

---

## 🚀 Release Process

### Option 1: Automated (Recommended)

1. **Develop on `dev` branch**:
   ```bash
   git checkout dev
   # Make changes
   git add .
   git commit -m "feat: add new feature"
   git push origin dev
   ```

2. **Merge to main via GitHub Actions**:
   - Go to Actions → "Merge to Main" → Run workflow
   - Select version bump type (patch/minor/major)
   - Enable "Create release"
   - Click "Run workflow"

3. **Done!** 🎉
   - Code merged to main
   - Version bumped
   - Tag created
   - Release published automatically

### Option 2: Manual

1. **Merge dev to main**:
   ```bash
   git checkout main
   git merge dev
   ```

2. **Bump version manually**:
   ```bash
   # Edit pyproject.toml
   version = "2.2.0"
   
   # Edit src/ios_spec_driven_installer/__init__.py
   __version__ = "2.2.0"
   
   # Edit src/ios_spec_driven_installer/cli.py
   @click.version_option(version="2.2.0")
   ```

3. **Commit and tag**:
   ```bash
   git add .
   git commit -m "chore: bump version to 2.2.0"
   git tag -a v2.2.0 -m "Release v2.2.0"
   git push origin main
   git push origin v2.2.0
   ```

4. **Release created automatically** by `release.yml` workflow

---

## 📦 Version Bumping

### Semantic Versioning

Format: `MAJOR.MINOR.PATCH` (e.g., `2.1.0`)

- **MAJOR**: Breaking changes (e.g., `2.1.0` → `3.0.0`)
- **MINOR**: New features, backward compatible (e.g., `2.1.0` → `2.2.0`)
- **PATCH**: Bug fixes, backward compatible (e.g., `2.1.0` → `2.1.1`)

### When to bump:

- **Patch** (`2.1.0` → `2.1.1`):
  - Bug fixes
  - Documentation updates
  - Minor improvements

- **Minor** (`2.1.0` → `2.2.0`):
  - New features
  - New skills/agents
  - Enhancements

- **Major** (`2.1.0` → `3.0.0`):
  - Breaking changes
  - Major refactoring
  - API changes

---

## 🔍 Checking Workflow Status

### Via GitHub UI:
1. Go to **Actions** tab
2. View workflow runs
3. Click on a run to see details

### Via GitHub CLI:
```bash
# List recent workflow runs
gh run list

# View specific run
gh run view <run-id>

# Watch a running workflow
gh run watch
```

---

## 📝 Release Notes

Release notes are automatically generated from commit messages since the last tag.

### Commit Message Format:

Use conventional commits for better changelog:

```bash
feat: add new feature
fix: fix bug in installer
docs: update README
chore: bump version
refactor: improve code structure
test: add tests
```

### Example Changelog:

```markdown
## What's Changed

- feat: add parallel execution guide (abc123)
- fix: include .claude directory in package (def456)
- docs: update installation instructions (ghi789)

## Installation

uvx --from git+https://github.com/user/repo@v2.2.0 ios-spec-driven install
```

---

## 🛠️ Troubleshooting

### Workflow fails on merge

**Problem**: Merge conflicts

**Solution**:
1. Resolve conflicts locally:
   ```bash
   git checkout main
   git pull origin main
   git merge dev
   # Resolve conflicts
   git commit
   git push origin main
   ```

### Version bump fails

**Problem**: Version format incorrect

**Solution**:
- Ensure version in `pyproject.toml` follows `X.Y.Z` format
- Check all version references are updated

### Release not created

**Problem**: Tag not pushed or workflow failed

**Solution**:
1. Check if tag exists: `git tag -l`
2. Push tag manually: `git push origin v2.2.0`
3. Check workflow logs in Actions tab

### Tests fail

**Problem**: Installation or CLI tests fail

**Solution**:
1. Test locally first:
   ```bash
   uv venv
   source .venv/bin/activate
   uv pip install -e .
   ios-spec-driven install /tmp/test --force
   ```
2. Fix issues and push again

---

## 📊 Workflow Permissions

Required permissions in repository settings:

1. **Actions** → **General** → **Workflow permissions**:
   - ✅ Read and write permissions
   - ✅ Allow GitHub Actions to create and approve pull requests

2. **Settings** → **Actions** → **General**:
   - ✅ Allow all actions and reusable workflows

---

## 🎯 Best Practices

1. **Always test on dev first**:
   - Push to `dev` branch
   - Wait for tests to pass
   - Then merge to main

2. **Use meaningful commit messages**:
   - Follow conventional commits
   - Helps generate better changelogs

3. **Review before merging**:
   - Check test results
   - Review changes
   - Ensure version bump is correct

4. **Tag releases properly**:
   - Use `v` prefix (e.g., `v2.1.0`)
   - Follow semantic versioning
   - Add release notes

5. **Monitor workflow runs**:
   - Check Actions tab regularly
   - Fix failures promptly
   - Keep workflows up to date

---

## 📚 Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Semantic Versioning](https://semver.org/)
- [Conventional Commits](https://www.conventionalcommits.org/)
- [GitHub CLI](https://cli.github.com/)

---

*Last updated: February 5, 2026*
