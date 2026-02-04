# Helper Scripts

Quick reference for CI/CD helper scripts.

## 📜 Available Scripts

### 1. `test-workflow.sh`

**Purpose**: Trigger test workflow by pushing to dev branch

**Usage**:
```bash
./test-workflow.sh
```

**What it does**:
- Creates a test commit
- Pushes to dev branch
- Automatically triggers test workflow

**When to use**:
- Test CI/CD setup
- Verify workflows are working
- Before creating release

---

### 2. `trigger-release.sh`

**Purpose**: Trigger merge-to-main workflow via GitHub API

**Usage**:
```bash
# Set GitHub token first
export GITHUB_TOKEN=your_token_here

# Trigger with patch version bump (default)
./trigger-release.sh

# Trigger with minor version bump
./trigger-release.sh minor

# Trigger with major version bump
./trigger-release.sh major
```

**What it does**:
- Calls GitHub API to trigger workflow
- Merges dev to main
- Bumps version
- Creates release

**Requirements**:
- GitHub Personal Access Token with `repo` and `workflow` scopes
- Token must be exported as `GITHUB_TOKEN`

**Get token**:
1. Go to: https://github.com/settings/tokens
2. Generate new token (classic)
3. Select scopes: `repo`, `workflow`
4. Copy token
5. Export: `export GITHUB_TOKEN=your_token_here`

---

### 3. `check-workflow-status.sh`

**Purpose**: Check status of recent workflow runs

**Usage**:
```bash
# Set GitHub token first
export GITHUB_TOKEN=your_token_here

# Check status
./check-workflow-status.sh
```

**What it shows**:
- Latest 5 workflow runs
- Status (queued/in_progress/completed)
- Conclusion (success/failure/cancelled)
- Links to view details

**Requirements**:
- GitHub Personal Access Token
- `jq` command (for JSON parsing)

**Install jq**:
```bash
# macOS
brew install jq

# Ubuntu
sudo apt-get install jq
```

---

## 🚀 Quick Start

### Test CI/CD Setup

```bash
# 1. Test workflow
./test-workflow.sh

# 2. Wait ~5-10 minutes

# 3. Check results
open https://github.com/nguyennamkkb/ios-spec-driven-claude/actions
```

### Create Release

```bash
# 1. Set GitHub token
export GITHUB_TOKEN=your_token_here

# 2. Trigger release
./trigger-release.sh patch

# 3. Check status
./check-workflow-status.sh

# 4. View release
open https://github.com/nguyennamkkb/ios-spec-driven-claude/releases
```

---

## 🔐 GitHub Token Setup

### Create Token

1. Go to: https://github.com/settings/tokens
2. Click "Generate new token (classic)"
3. Name: "CI/CD Scripts"
4. Expiration: 90 days (or custom)
5. Select scopes:
   - ✅ `repo` (Full control of private repositories)
   - ✅ `workflow` (Update GitHub Action workflows)
6. Click "Generate token"
7. Copy token (you won't see it again!)

### Save Token

**Option 1: Export in shell**
```bash
export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx
```

**Option 2: Add to shell profile**
```bash
# Add to ~/.zshrc or ~/.bashrc
echo 'export GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx' >> ~/.zshrc
source ~/.zshrc
```

**Option 3: Use .env file**
```bash
# Create .env file
echo 'GITHUB_TOKEN=ghp_xxxxxxxxxxxxxxxxxxxx' > .env

# Load before running scripts
source .env
./trigger-release.sh
```

⚠️ **Security**: Never commit tokens to git!

---

## 🎯 Common Workflows

### Test Before Release

```bash
# 1. Test locally
uv venv
source .venv/bin/activate
uv pip install -e .
ios-spec-driven install /tmp/test --force

# 2. Test CI/CD
./test-workflow.sh

# 3. Wait for tests to pass

# 4. Create release
export GITHUB_TOKEN=your_token
./trigger-release.sh patch
```

### Emergency Hotfix

```bash
# 1. Fix issue on dev branch
git checkout dev
# make fixes
git commit -m "fix: critical bug"
git push origin dev

# 2. Test
./test-workflow.sh

# 3. Release immediately
export GITHUB_TOKEN=your_token
./trigger-release.sh patch
```

### Major Version Release

```bash
# 1. Ensure all tests pass
./test-workflow.sh

# 2. Review changes
git log main..dev --oneline

# 3. Create major release
export GITHUB_TOKEN=your_token
./trigger-release.sh major

# 4. Update documentation
# Update README with breaking changes
```

---

## 📊 Troubleshooting

### Script not executable

```bash
chmod +x test-workflow.sh
chmod +x trigger-release.sh
chmod +x check-workflow-status.sh
```

### GitHub token not working

```bash
# Check if token is set
echo $GITHUB_TOKEN

# Test token
curl -H "Authorization: Bearer $GITHUB_TOKEN" \
  https://api.github.com/user
```

### Workflow not triggering

1. Check if workflows exist in `.github/workflows/`
2. Check if workflows are pushed to GitHub
3. Check repository permissions
4. Check token scopes

### jq not found

```bash
# macOS
brew install jq

# Ubuntu
sudo apt-get install jq

# Or use without jq
curl -s ... | python3 -m json.tool
```

---

## 🔗 Related Documentation

- [CICD_GUIDE.md](CICD_GUIDE.md) - Detailed CI/CD documentation
- [RELEASE_CHECKLIST.md](RELEASE_CHECKLIST.md) - Release checklist
- [WORKFLOW_TEST_RESULTS.md](WORKFLOW_TEST_RESULTS.md) - Test results

---

*Last updated: February 5, 2026*
