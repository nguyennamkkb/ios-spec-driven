# Release Checklist

Quick reference for creating a new release.

## 🚀 Quick Release (Recommended)

### Via GitHub UI

1. Go to **Actions** tab on GitHub
2. Select **"Merge to Main"** workflow
3. Click **"Run workflow"**
4. Configure:
   - Source branch: `dev`
   - Create release: ✅ Yes
   - Version bump: `patch` (or `minor`/`major`)
5. Click **"Run workflow"**
6. Wait ~2 minutes
7. ✅ Done! Check **Releases** tab

### Via GitHub CLI

```bash
# Patch release (2.1.0 → 2.1.1)
gh workflow run merge-to-main.yml \
  -f source_branch=dev \
  -f create_release=true \
  -f version_bump=patch

# Minor release (2.1.0 → 2.2.0)
gh workflow run merge-to-main.yml \
  -f source_branch=dev \
  -f create_release=true \
  -f version_bump=minor

# Major release (2.1.0 → 3.0.0)
gh workflow run merge-to-main.yml \
  -f source_branch=dev \
  -f create_release=true \
  -f version_bump=major
```

---

## 📋 Pre-Release Checklist

Before creating a release, ensure:

- [ ] All tests pass on `dev` branch
- [ ] README.md is up to date
- [ ] CHANGELOG or commit messages are clear
- [ ] Version bump type is correct (patch/minor/major)
- [ ] No breaking changes (or document them)
- [ ] Installation tested locally:
  ```bash
  uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven-claude@dev ios-spec-driven install /tmp/test
  ```

---

## 🔍 Post-Release Verification

After release is created:

1. **Check Release Page**:
   - Go to **Releases** tab
   - Verify release notes
   - Check attached files (`.tar.gz`, `.whl`)

2. **Test Installation**:
   ```bash
   # Test with new tag
   uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven-claude@v2.2.0 ios-spec-driven install /tmp/test
   
   # Verify
   uvx --from git+https://github.com/nguyennamkkb/ios-spec-driven-claude@v2.2.0 ios-spec-driven status /tmp/test
   ```

3. **Update Documentation** (if needed):
   - Update README with new version
   - Update examples with new tag

---

## 🐛 Rollback (If Needed)

If release has issues:

1. **Delete tag**:
   ```bash
   git tag -d v2.2.0
   git push origin :refs/tags/v2.2.0
   ```

2. **Delete release** on GitHub:
   - Go to Releases → Edit → Delete

3. **Fix issues** on `dev` branch

4. **Create new release** with patch version

---

## 📊 Version History

| Version | Date | Type | Description |
|---------|------|------|-------------|
| 2.1.0 | 2026-02-05 | Minor | UVX installer implementation |
| 2.0.0 | 2026-02-04 | Major | Complete toolkit refactor |

---

## 🎯 Version Bump Guidelines

### Patch (X.Y.Z → X.Y.Z+1)
- Bug fixes
- Documentation updates
- Minor improvements
- No new features

**Example**: `2.1.0` → `2.1.1`

### Minor (X.Y.Z → X.Y+1.0)
- New features
- New skills/agents
- Enhancements
- Backward compatible

**Example**: `2.1.0` → `2.2.0`

### Major (X.Y.Z → X+1.0.0)
- Breaking changes
- Major refactoring
- API changes
- Not backward compatible

**Example**: `2.1.0` → `3.0.0`

---

## 📝 Commit Message Format

Use conventional commits for better changelogs:

```bash
# Features
git commit -m "feat: add new skill for SwiftUI previews"

# Bug fixes
git commit -m "fix: resolve installation path issue"

# Documentation
git commit -m "docs: update installation guide"

# Chores
git commit -m "chore: bump version to 2.2.0"

# Refactoring
git commit -m "refactor: improve installer logic"

# Tests
git commit -m "test: add integration tests"
```

---

## 🔗 Useful Links

- [GitHub Actions](https://github.com/nguyennamkkb/ios-spec-driven-claude/actions)
- [Releases](https://github.com/nguyennamkkb/ios-spec-driven-claude/releases)
- [CICD_GUIDE.md](CICD_GUIDE.md) - Detailed CI/CD documentation
- [Semantic Versioning](https://semver.org/)

---

*Last updated: February 5, 2026*
