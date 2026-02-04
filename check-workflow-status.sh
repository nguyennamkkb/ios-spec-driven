#!/bin/bash

# Check workflow status via GitHub API

set -e

REPO_OWNER="nguyennamkkb"
REPO_NAME="ios-spec-driven-claude"

echo "🔍 Checking workflow status..."
echo ""

if [ -z "$GITHUB_TOKEN" ]; then
    echo "⚠️  GITHUB_TOKEN not set"
    echo ""
    echo "View workflows manually:"
    echo "https://github.com/${REPO_OWNER}/${REPO_NAME}/actions"
    echo ""
    exit 0
fi

# Get latest workflow runs
echo "Latest workflow runs:"
echo ""

curl -s \
  -H "Accept: application/vnd.github+json" \
  -H "Authorization: Bearer $GITHUB_TOKEN" \
  -H "X-GitHub-Api-Version: 2022-11-28" \
  "https://api.github.com/repos/${REPO_OWNER}/${REPO_NAME}/actions/runs?per_page=5" \
  | jq -r '.workflow_runs[] | "\(.name) - \(.status) - \(.conclusion // "running") - \(.html_url)"'

echo ""
echo "View all runs:"
echo "https://github.com/${REPO_OWNER}/${REPO_NAME}/actions"
