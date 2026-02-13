# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NextPM is an **AI-Native PM Knowledge Hub** - a living laboratory for AI-augmented Product Management. The repository serves as both a teaching resource and a working example of AI-native PM practices.

**Website**: https://kangxh.com
**Repository**: https://github.com/kangxh75/NextPM

## Common Commands

```bash
# Install dependencies (first time setup)
pip install -r requirements.txt

# Serve documentation locally (with automated spec processing)
python scripts/serve.py

# Alternative: Manual approach
python scripts/build-specs.py && mkdocs serve

# Default port: http://localhost:8002
# Use different port if needed: python scripts/serve.py -a localhost:8001

# Build static site (with automated spec processing)
python scripts/build.py

# Build with strict mode (fails on warnings - used in CI/CD)
python scripts/build.py --strict

# Clean build directory
rm -rf mkdocs-site/

# Build only specifications (for testing)
python scripts/build-specs.py
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
├── engineering/          # Working artifacts (NOT published to website)
│   ├── specs/            # Full PM specifications (source of truth)
│   ├── tasks/            # Task breakdowns for features
│   ├── validations/      # Test reports and validation docs
│   └── templates/        # Templates for specs and commits
├── ai-context/           # AI assistant context and instructions
├── examples/             # Real PM artifacts (root level)
├── prompts/              # Prompt library (root level)
├── meta/                 # Project meta-documentation
├── scripts/              # Git hooks and utility scripts
├── mkdocs.yml            # MkDocs configuration (navigation, theme)
├── requirements.txt      # Python dependencies
├── venv/                 # Python virtual environment
└── .github/workflows/    # CI/CD pipelines
```

### Key Design Decisions

1. **mkdocs- Prefix**: All MkDocs-related folders use `mkdocs-` prefix for clarity and root folder hygiene.

2. **Single-Source-of-Truth Strategy**:
   - `/engineering/specs/`: Single source of truth for all specifications - published directly to website
   - `/mkdocs-docs/`: Website content (generated specs + handwritten pages) - Published to kangxh.com
   - Specs are automatically copied and processed during build - no manual duplication required

3. **Automated Publishing**:
   - Build process automatically copies specs from `/engineering/specs/` to `/mkdocs-docs/engineering/specs/`
   - Navigation is auto-generated based on available spec files
   - Internal links are processed to work correctly in website context
   - No manual website summary creation required

4. **Dual Content Structure**:
   - Content exists in both root level (`/examples/`, `/prompts/`) and under `/mkdocs-docs/`
   - Root level folders contain actual working content
   - `/mkdocs-docs/` folders contain website-optimized versions
   - AI context lives in `/ai-context/` for assistant onboarding

5. **Engineering History Tracking** (Feature #2026-02-09-01):
   - Navigation reorganized under "Engineering" parent section
   - PM Workflows: What to build (specifications)
   - Dev Workflows: What was built (commit summaries)
   - Bidirectional linking between specs and commits using spec IDs

### Navigation Structure

The site uses nested navigation under "Engineering":
- Engineering
  - Specs (auto-published from project/specs/)
  - PM Workflows (Legacy) (manually created summaries - deprecated)
  - Dev Workflows (implementation summaries)
- Prompt Library
- Examples
- About

All navigation is defined in `mkdocs.yml` and specs navigation is auto-generated during build.

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

### Documentation Workflow (Simplified)

**Single-Source-of-Truth Workflow** - Specs are automatically published to website:

1. **Create PM Spec** in `/engineering/specs/YYYY-MM-DD-nn-feature-name.md`
   - Use template from `/engineering/templates/pm-workflow-spec-template.md`
   - Include version number and Change History section
   - **Spec is automatically published to website during build**

2. **Create Task Breakdown** in `/engineering/tasks/YYYY-MM-DD-nn-feature-name-tasks.md`

3. **Implement Feature** and commit with spec ID reference:
   ```bash
   git commit -m "feat: implement feature (#2026-02-09-01)"
   ```

4. **Create Dev Workflow Summary** in `/mkdocs-docs/engineering/dev-workflows/YYYY-MM-DD-HHMM-implementation-name.md`
   - Document commit hash, files changed, key decisions
   - Link back to published spec (auto-published from project/specs/)
   - Use template from `/engineering/templates/dev-workflow-commit-summary-template.md`

**What's Automated:**
- Specs are automatically copied from `engineering/specs/` to website during build
- Navigation entries are automatically generated based on available specs
- Internal links are processed for website compatibility
- No manual website summary creation required

**Legacy Workflow (Deprecated):**
The previous workflow required manual creation of website summaries in `/mkdocs-docs/engineering/pm-workflows/`. These remain visible as "PM Workflows (Legacy)" but new specs should only be created in `engineering/specs/`.

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

## Build Process

### Local Development

Use the provided wrapper scripts for automated spec processing:

```bash
# Serve documentation locally (auto-builds specs first)
python scripts/serve.py

# Build static site (auto-builds specs first)
python scripts/build.py

# Build with strict mode (fails on warnings - used in CI/CD)
python scripts/build.py --strict

# Build only specifications (for testing)
python scripts/build-specs.py
```

### CI/CD Pipeline

The GitHub Actions workflow automatically:
1. Runs `python scripts/build-specs.py` to process specifications
2. Runs `mkdocs build --strict` to build the site
3. Deploys to Azure Static Web Apps on successful build

## Tech Stack

- **Static Site Generator**: MkDocs Material 9.5.0+
- **Language**: Python 3.x (see requirements.txt for exact dependencies)
- **Deployment**: Azure Static Web Apps
- **CI/CD**: GitHub Actions
- **Theme**: Material for MkDocs with custom color scheme (indigo)

## Testing and Validation

1. **Local Testing**:
   ```bash
   python scripts/serve.py
   # Visit http://localhost:8002
   # Test navigation, links, and formatting
   # Specs are auto-built and included
   ```

2. **Strict Mode Build** (CI/CD uses this):
   ```bash
   python scripts/build.py --strict
   # Fails on any warnings (broken links, missing files)
   ```

3. **Specification Processing**:
   ```bash
   python scripts/build-specs.py
   # Tests spec copying, link processing, and navigation generation
   ```

4. **Link Validation**:
   - All internal links must work in strict mode
   - Spec internal links are auto-processed for website compatibility
   - Website links to external resources (GitHub) are preserved

## File Editing Guidelines

### DO NOT Create Files Unless Necessary
- Always prefer editing existing files over creating new ones
- Check for existing placeholders before creating new pages

### When Editing mkdocs.yml
- Maintain navigation hierarchy (Engineering > Specs/PM Workflows (Legacy)/Dev Workflows)
- **Note**: Spec navigation is auto-generated - manual editing will be overwritten during build
- Keep navigation order consistent for non-auto-generated sections
- Test with `python scripts/build.py --strict` after changes

### When Creating New Pages
1. **For Specifications**: Create directly in `/engineering/specs/` using proper naming convention
   - File will be automatically included in website during next build
   - No manual navigation updates required
2. **For Other Pages**: Create in appropriate `/mkdocs-docs/` subdirectory
3. Update `mkdocs.yml` navigation for non-spec pages
4. Test locally with `python scripts/serve.py` before committing

## AI-Native Philosophy

This repository demonstrates "building in public" principles with automated publishing:
- Every feature has a PM spec (planning phase) - automatically published to website
- Every commit has a Dev Workflow summary (implementation phase)
- Complete traceability from idea → spec → code → deployment
- Documentation created as byproduct of regular development, not separate manual process
- Single-source-of-truth approach eliminates duplication and sync issues
- AI assistance is explicitly acknowledged in Dev Workflows

## CI/CD Pipeline

Located in `.github/workflows/`:
- Runs `mkdocs build --strict` on every push
- Deploys to Azure Static Web Apps on successful build
- Ensures no broken links or missing files in production

## Getting Help

- **Documentation Issues**: Run `python scripts/serve.py` and check http://localhost:8000
- **Build Failures**: Run `python scripts/build.py --strict` to see specific errors
- **Spec Processing Issues**: Run `python scripts/build-specs.py` to test spec automation
- **Navigation Issues**: Check `mkdocs.yml` navigation structure (specs are auto-generated)
- **Link Errors**: Use strict mode to identify broken links

---

**Last Updated**: 2026-02-11
**NextPM Version**: Phase 1 - Static Knowledge Hub
**AI Assistant**: Updated by Claude Sonnet 4
