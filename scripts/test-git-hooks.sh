#!/bin/bash
# Test script for git hooks

echo "Testing pre-push hook..."
echo ""

# Run the pre-push hook
bash .git/hooks/pre-push

echo ""
echo "════════════════════════════════════════════════════════"
echo "Test completed!"
echo ""
echo "To test with different inputs:"
echo "  1. Run: bash .git/hooks/pre-push"
echo "  2. Try different options:"
echo "     - Press ENTER (default)"
echo "     - Type a number (1, 2, 3)"
echo "     - Type a full spec ID"
echo "     - Type 'no' or 'none'"
echo ""
