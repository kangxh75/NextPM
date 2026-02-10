# Git Hooks for NextPM

These git hooks help track which design spec your changes relate to and remind you to update documentation.

## Installation

From the project root directory, run:

```bash
./scripts/install-git-hooks.sh
```

This will copy the hooks from `scripts/git-hooks/` to `.git/hooks/` and make them executable.

## Hooks

### pre-push

Runs before `git push` and prompts you to specify which design spec the changes relate to.

**Behavior:**

1. Displays a numbered list of the 5 most recent specs
2. Press ENTER to use default (newest spec, marked with green)
3. Type a number (1-5) to select a spec from the list
4. Type the full spec ID if it's not in the list
5. Type 'no' or 'none' to skip spec tracking
6. Validates that the spec file exists (with option to continue anyway)

**Example:**

```
═══════════════════════════════════════════════════════
        Git Push - Spec Tracking
═══════════════════════════════════════════════════════

Which design spec are these changes related to?

Recent specs:
  [1] 2026-02-10-01-authentication (default)
  [2] 2026-02-09-01-engineering-history-tracking
  [3] 0.00-project-start

Options:
  - Press ENTER to use default (newest spec)
  - Type a number (1-3) to select from list
  - Type full spec ID if not in list above
  - Type 'no' or 'none' to skip spec tracking

Your choice:
```

### post-push

Runs after a successful `git push` and reminds you to update the related documentation.

**Behavior:**
1. Shows which spec the changes were tagged with
2. Lists the documentation files that should be updated:
   - PM Workflow summary
   - Dev Workflow summary
   - Spec file (if needed)

**Example:**

```
═══════════════════════════════════════════════════════
✓ Push successful!
═══════════════════════════════════════════════════════

📝 Documentation Reminder:

Related spec: 2026-02-10-01-authentication

Please ensure the following are updated:

  1. PM Workflow:
     mkdocs-docs/engineering/pm-workflows/2026-02-10-01-authentication.md

  2. Dev Workflow:
     mkdocs-docs/engineering/dev-workflows/[timestamp]-*.md

  3. Spec file (if needed):
     project/specs/2026-02-10-01-authentication.md

═══════════════════════════════════════════════════════
```

## Workflow Integration

These hooks integrate with the NextPM documentation workflow:

1. **Before Push**: Specify which spec your changes relate to
2. **After Push**: Get reminded to update PM and Dev workflow documentation
3. This ensures all changes are properly tracked and documented

## Customization

To modify the hooks:

1. Edit files in `scripts/git-hooks/`
2. Run `./scripts/install-git-hooks.sh` to reinstall
3. Or manually edit files in `.git/hooks/` for testing

## Why Git Hooks?

Git hooks are **not committed** to the repository (they live in `.git/hooks/`), so they must be installed locally by each developer. This is why we:

1. Store templates in `scripts/git-hooks/` (committed to repo)
2. Provide `install-git-hooks.sh` script for easy installation
3. Document installation in CLAUDE.md and this README

## Troubleshooting

**Hook not running:**
- Ensure hooks are executable: `chmod +x .git/hooks/pre-push .git/hooks/post-push`
- Check if hooks exist: `ls -la .git/hooks/`

**Hook fails with error:**
- Verify you're in the project root directory
- Check that `project/specs/` directory exists
- Ensure bash is available on your system

**Skip hook temporarily:**
- Use `git push --no-verify` to bypass pre-push hook
- Use with caution - you'll miss spec tracking for that push

---

**Created**: 2026-02-10
**Last Updated**: 2026-02-10
**Related Spec**: Workflow improvement (not tracked under specific spec)
