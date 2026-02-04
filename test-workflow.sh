#!/bin/bash

# Simple test: Push to dev branch to trigger test workflow

set -e

echo "🧪 Testing GitHub Actions Workflow"
echo ""
echo "This will:"
echo "1. Create a test commit"
echo "2. Push to dev branch"
echo "3. Trigger test workflow automatically"
echo ""

# Create a test file
echo "Test run at $(date)" > .workflow-test

# Commit and push
git add .workflow-test
git commit -m "test: trigger workflow test"
git push origin dev

echo ""
echo "✅ Pushed to dev branch"
echo ""
echo "View workflow run:"
echo "https://github.com/nguyennamkkb/ios-spec-driven-claude/actions"
echo ""
echo "The test workflow will:"
echo "- Test installation on Ubuntu and macOS"
echo "- Test with Python 3.8 and 3.12"
echo "- Run all CLI commands"
echo "- Build package"
echo ""
echo "Expected time: ~5-10 minutes"
