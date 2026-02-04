#!/bin/bash

# Trigger "Merge to Main" workflow via GitHub API
# Usage: ./trigger-release.sh [patch|minor|major]

set -e

# Configuration
REPO_OWNER="nguyennamkkb"
REPO_NAME="ios-spec-driven-claude"
WORKFLOW_FILE="merge-to-main.yml"
SOURCE_BRANCH="dev"
VERSION_BUMP="${1:-patch}"

# Colors
GREEN='\033[0;32m'
BLUE='\033[0;34m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

echo -e "${BLUE}🚀 Triggering Merge to Main Workflow${NC}"
echo ""
echo "Repository: ${REPO_OWNER}/${REPO_NAME}"
echo "Source Branch: ${SOURCE_BRANCH}"
echo "Version Bump: ${VERSION_BUMP}"
echo "Create Release: true"
echo ""

# Check if GITHUB_TOKEN is set
if [ -z "$GITHUB_TOKEN" ]; then
    echo -e "${YELLOW}⚠️  GITHUB_TOKEN not set${NC}"
    echo ""
    echo "To trigger workflow via API, you need a GitHub Personal Access Token."
    echo ""
    echo "Steps:"
    echo "1. Go to: https://github.com/settings/tokens"
    echo "2. Generate new token (classic)"
    echo "3. Select scopes: repo, workflow"
    echo "4. Copy token"
    echo "5. Export: export GITHUB_TOKEN=your_token_here"
    echo ""
    echo -e "${BLUE}Alternative: Use GitHub UI${NC}"
    echo "1. Go to: https://github.com/${REPO_OWNER}/${REPO_NAME}/actions"
    echo "2. Select 'Merge to Main' workflow"
    echo "3. Click 'Run workflow'"
    echo "4. Configure options:"
    echo "   - Source branch: ${SOURCE_BRANCH}"
    echo "   - Create release: ✅ Yes"
    echo "   - Version bump: ${VERSION_BUMP}"
    echo "5. Click 'Run workflow'"
    echo ""
    exit 1
fi

# Trigger workflow
echo -e "${GREEN}Triggering workflow...${NC}"

RESPONSE=$(curl -s -X POST \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/actions/workflows/${WORKFLOW_FILE}/dispatches" \
  -d "{\"ref\":\"${SOURCE_BRANCH}\",\"inputs\":{\"source_branch\":\"${SOURCE_BRANCH}\",\"create_release\":\"true\",\"version_bump\":\"${VERSION_BUMP}\"}}")

if [ $? -eq 0 ]; then
    echo -e "${GREEN}✅ Workflow triggered successfully!${NC}"
    echo ""
    echo "View workflow runs:"
    echo "https://github.com/${REPO_OWNER}/${REPO_NAME}/actions"
    echo ""
    echo "This will:"
    echo "1. Merge '${SOURCE_BRANCH}' to 'main'"
    echo "2. Bump version (${VERSION_BUMP})"
    echo "3. Create git tag"
    echo "4. Trigger release workflow"
    echo ""
    echo "Expected time: ~2-3 minutes"
else
    echo -e "${YELLOW}❌ Failed to trigger workflow${NC}"
    echo "Response: $RESPONSE"
    exit 1
fi
