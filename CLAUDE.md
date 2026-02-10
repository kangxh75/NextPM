# CLAUDE.md - AI Assistant Context for NextPM

This file provides context for AI assistants (Claude Code, Cursor, etc.) working with the NextPM repository.

## Project Overview

NextPM is an **AI-Native PM Knowledge Hub** - a living laboratory for AI-augmented Product Management. The repository serves as both a teaching resource and a working example of AI-native PM practices.

**Website**: https://kangxh.com
**Repository**: https://github.com/kangxh75/NextPM

## Common Commands

```bash
# Install dependencies (first time setup)
pip install -r requirements.txt

# Serve documentation locally
mkdocs serve

# Default port: http://localhost:8000
# Use different port if needed: mkdocs serve -a localhost:8001

# Build static site (outputs to mkdocs-site/)
mkdocs build

# Build with strict mode (fails on warnings - used in CI/CD)
mkdocs build --strict

# Clean build directory
rm -rf mkdocs-site/
```

## Code Architecture

### High-Level Structure

```
NextPM/
├── mkdocs-docs/          # Website content (markdown files)
│   ├── engineering/      # Engineering documentation (NEW structure as of 2026-02-09)
│   │   ├── pm-workflows/     # PM spec summaries (what to build)
│   │   └── dev-workflows/    # Dev commit summaries (what was built)
│   ├── prompts/          # Prompt library for PM tasks
│   ├── examples/         # Real PM artifacts and case studies
│   └── about/            # About pages
├── mkdocs-static/        # Static assets (CSS, images, etc.)
├── project/              # Working artifacts (NOT published to website)
│   ├── specs/            # Full PM specifications (source of truth)
│   ├── tasks/            # Task breakdowns for features
│   ├── validations/      # Test reports and validation docs
│   └── templates/        # Templates for specs and commits
├── mkdocs.yml            # MkDocs configuration (navigation, theme)
├── requirements.txt      # Python dependencies
├── venv/                 # Python virtual environment
└── .github/workflows/    # CI/CD pipelines
```

### Key Design Decisions

1. **mkdocs- Prefix**: All MkDocs-related folders use `mkdocs-` prefix for clarity and root folder hygiene.

2. **Two-Folder Strategy**:
   - `/project/`: Working artifacts (specs, tasks, templates) - Git-tracked but not published
   - `/mkdocs-docs/`: Website content (summaries) - Published to kangxh.com
   - Specs live in `/project/specs/` with summaries in `/mkdocs-docs/engineering/pm-workflows/`

3. **Engineering History Tracking** (Feature #2026-02-09-01):
   - Navigation reorganized under "Engineering" parent section
   - PM Workflows: What to build (specifications)
   - Dev Workflows: What was built (commit summaries)
   - Bidirectional linking between specs and commits using spec IDs

### Navigation Structure

The site uses nested navigation under "Engineering":
- Engineering
  - PM Workflows (specifications)
  - Dev Workflows (implementation summaries)
- Prompt Library
- Examples
- About

All navigation is defined in `mkdocs.yml`.

## Important Patterns and Conventions

### Spec Naming Convention

**Format**: `YYYY-MM-DD-nn-descriptive-name.md`

Examples:
- `2026-02-09-01-engineering-history-tracking.md`
- `2026-02-09-02-feature-name.md`

**Exception**: `0.00-project-start.md` (grandfathered first spec)

**Spec ID in Commits**: Use `(#YYYY-MM-DD-nn)` format in commit messages for linking:
```bash
git commit -m "feat: implement feature X (#2026-02-09-01)"
```

### Dev Workflow Naming Convention

**Format**: `YYYY-MM-DD-HHMM-descriptive-name.md`

The HHMM timestamp supports multiple commits per day.

Examples:
- `2026-02-09-1200-engineering-history-implementation.md`
- `2026-02-09-1530-bugfix-navigation.md`

### Documentation Workflow

When implementing a feature:

1. **Create PM Spec** in `/project/specs/YYYY-MM-DD-nn-feature-name.md`
   - Use template from `/project/templates/pm-workflow-spec-template.md`
   - Include version number and Change History section

2. **Create Task Breakdown** in `/project/tasks/YYYY-MM-DD-nn-feature-name-tasks.md`

3. **Implement Feature** and commit with spec ID reference:
   ```bash
   git commit -m "feat: implement feature (#2026-02-09-01)"
   ```

4. **Create PM Workflow Summary** in `/mkdocs-docs/engineering/pm-workflows/YYYY-MM-DD-nn-feature-name.md`
   - Brief overview linking to full spec on GitHub
   - Use template from `/project/templates/pm-workflow-spec-template.md`

5. **Create Dev Workflow Summary** in `/mkdocs-docs/engineering/dev-workflows/YYYY-MM-DD-HHMM-implementation-name.md`
   - Document commit hash, files changed, key decisions
   - Link back to PM Workflow spec
   - Use template from `/project/templates/dev-workflow-commit-summary-template.md`

6. **Update mkdocs.yml** navigation to include new pages

### Version Tracking

Specs use **Change History** section for version tracking:

```markdown
## Change History

### Version 1.1 - 2026-02-09
- Clarified HHMM timestamp format for Dev Workflows
- Added bidirectional linking workflow details

### Version 1.0 - 2026-02-09
- Initial spec creation
```

### Git Workflow

- Main branch: `main`
- Current branch: `master` (should be synced with main)
- Always use conventional commits: `feat:`, `fix:`, `docs:`, `refactor:`, etc.
- Reference spec ID in commit message: `(#YYYY-MM-DD-nn)`

**Git Hooks** (Spec Tracking):

The repository includes git hooks to track which spec changes relate to:

1. **Install hooks** (first time setup):
   ```bash
   ./scripts/install-git-hooks.sh
   ```

2. **Pre-push hook**: Prompts before each push to specify related spec
   - Default: Most recent spec file
   - Options: Enter spec ID, or type 'no' if not related to any spec
   - Helps maintain proper documentation tracking

3. **Post-push hook**: Reminds you to update workflow documentation
   - PM Workflow: `/mkdocs-docs/engineering/pm-workflows/[spec-id].md`
   - Dev Workflow: `/mkdocs-docs/engineering/dev-workflows/[timestamp]-*.md`

**Hook Location**: Hooks are stored in `scripts/git-hooks/` and installed to `.git/hooks/`

## Tech Stack

- **Static Site Generator**: MkDocs Material 9.5.0+
- **Language**: Python 3.9+
- **Deployment**: Azure Static Web Apps
- **CI/CD**: GitHub Actions
- **Theme**: Material for MkDocs with custom color scheme (indigo)

## Testing and Validation

1. **Local Testing**:
   ```bash
   mkdocs serve
   # Visit http://localhost:8000
   # Test navigation, links, and formatting
   ```

2. **Strict Mode Build** (CI/CD uses this):
   ```bash
   mkdocs build --strict
   # Fails on any warnings (broken links, missing files)
   ```

3. **Link Validation**:
   - All internal links must work in strict mode
   - Use relative paths for internal links
   - Website links to full specs use GitHub URLs

## File Editing Guidelines

### DO NOT Create Files Unless Necessary
- Always prefer editing existing files over creating new ones
- Check for existing placeholders before creating new pages

### When Editing mkdocs.yml
- Maintain navigation hierarchy (Engineering > PM/Dev Workflows)
- Keep navigation order consistent (oldest to newest specs)
- Test with `mkdocs build --strict` after changes

### When Creating New Pages
1. Create full spec in `/project/specs/` first
2. Create summary in `/mkdocs-docs/engineering/pm-workflows/` or `dev-workflows/`
3. Update `mkdocs.yml` navigation
4. Test locally before committing

## AI-Native Philosophy

This repository demonstrates "building in public" principles:
- Every feature has a PM spec (planning phase)
- Every commit has a Dev Workflow summary (implementation phase)
- Complete traceability from idea → spec → code → deployment
- Documentation created as byproduct of regular development
- AI assistance is explicitly acknowledged in Dev Workflows

## CI/CD Pipeline

Located in `.github/workflows/`:
- Runs `mkdocs build --strict` on every push
- Deploys to Azure Static Web Apps on successful build
- Ensures no broken links or missing files in production

## Getting Help

- **Documentation Issues**: Run `mkdocs serve` and check http://localhost:8000
- **Build Failures**: Run `mkdocs build --strict` to see specific errors
- **Navigation Issues**: Check `mkdocs.yml` navigation structure
- **Link Errors**: Use strict mode to identify broken links

---

**Last Updated**: 2026-02-09
**NextPM Version**: Phase 1 - Static Knowledge Hub
**AI Assistant**: This file was created by Claude Sonnet 4.5
