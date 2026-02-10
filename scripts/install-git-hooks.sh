#!/bin/bash
# Setup git hooks for NextPM project

echo "Installing NextPM git hooks..."

# Copy pre-push hook
cp scripts/git-hooks/pre-push .git/hooks/pre-push
chmod +x .git/hooks/pre-push
echo "✓ Installed pre-push hook (spec tracking)"

# Copy post-push hook
cp scripts/git-hooks/post-push .git/hooks/post-push
chmod +x .git/hooks/post-push
echo "✓ Installed post-push hook (documentation reminder)"

echo ""
echo "Git hooks installed successfully!"
echo ""
echo "What these hooks do:"
echo "  - pre-push:  Prompts for which spec the changes relate to"
echo "  - post-push: Reminds you to update PM/Dev workflow documentation"
echo ""
