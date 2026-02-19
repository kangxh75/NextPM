# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

NextPM is a **Spec-Driven Development Showcase** - a living laboratory demonstrating AI-era product management and development workflows. The repository showcases how AI assistants can enhance spec-driven development with visual timelines, automated commit tracking, and real-time search capabilities.

**Website**: https://kangxh.com
**Repository**: https://github.com/kangxh75/NextPM

This project uses itself as the development target, creating a self-referential demonstration of AI-assisted spec-driven development practices.

## Common Commands

```bash
# Install dependencies (first time setup)
pip install -r requirements.txt

# Serve documentation locally (with automated spec processing)
python mkdocs-scripts/serve.py

# Alternative: Manual approach
python mkdocs-scripts/build-specs.py && mkdocs serve

# Default port: http://localhost:8002
# Use different port if needed: python mkdocs-scripts/serve.py -a localhost:8001

# Build static site (with automated spec processing)
python mkdocs-scripts/build.py

# Build with strict mode (fails on warnings - used in CI/CD)
python mkdocs-scripts/build.py --strict

# Clean build directory
rm -rf mkdocs-site/

# Build only specifications (for testing)
python mkdocs-scripts/build-specs.py
```

## Code Architecture

### High-Level Structure

```
NextPM/
├── mkdocs-docs/          # Website content (markdown files)
│   └── engineering/      # Engineering documentation
│       ├── specs/        # Auto-published specifications with visual timelines
│       └── dev-workflows/ # Implementation summaries
├── mkdocs-static/        # Static assets (CSS, JS, search index)
├── engineering/          # Working artifacts (source of truth)
│   ├── specs/           # PM specifications (auto-published to website)
│   ├── tasks/           # Task breakdowns for features
│   ├── validations/     # Test reports and validation docs
│   └── templates/       # Templates for specs and commit summaries
├── meta/                # Architecture Decision Records (ADRs)
├── mkdocs-scripts/      # Build automation and enhancement scripts
├── mkdocs.yml           # MkDocs configuration (navigation, theme)
├── requirements.txt     # Python dependencies
└── .github/workflows/   # CI/CD pipelines
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

4. **Spec-Driven Development Showcase**:
   - All specifications demonstrate visual state management with animated timelines
   - Git integration automatically tracks commits and links them to specs
   - Real-time search and filtering across all specifications
   - Interactive dashboard showing development progress and statistics

5. **Enhanced Build System** (Feature #2026-02-13-01):
   - `mkdocs-scripts/build-specs.py` processes specs with visual enhancements
   - Automated generation of search index and dashboard statistics
   - Git commit timeline integration with spec references
   - CSS3 animations and interactive features without heavy frameworks

### Navigation Structure

The site uses nested navigation under "Engineering":
- Engineering
  - Dashboard (interactive search and statistics)
  - Specs (auto-published from engineering/specs/ with visual enhancements)
  - Implementation Summaries (development tracking and commit summaries)

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
   - Link back to published spec (auto-published from engineering/specs/)
   - Use template from `/engineering/templates/dev-workflow-commit-summary-template.md`

**What's Automated:**
- Specs are automatically copied from `engineering/specs/` to website during build
- Navigation entries are automatically generated based on available specs
- Internal links are processed for website compatibility
- Visual timelines and state badges are automatically generated
- Search index and dashboard statistics are updated on every build

**Key Features:**
The enhanced system provides visual state management, git integration, real-time search, and interactive dashboards that showcase the complete spec-driven development workflow.

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
python mkdocs-scripts/serve.py

# Build static site (auto-builds specs first)
python mkdocs-scripts/build.py

# Build with strict mode (fails on warnings - used in CI/CD)
python mkdocs-scripts/build.py --strict

# Build only specifications (for testing)
python mkdocs-scripts/build-specs.py
```

### CI/CD Pipeline

The GitHub Actions workflow automatically:
1. Runs `python mkdocs-scripts/build-specs.py` to process specifications
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
   python mkdocs-scripts/serve.py
   # Visit http://localhost:8002
   # Test navigation, links, and formatting
   # Specs are auto-built and included
   ```

2. **Strict Mode Build** (CI/CD uses this):
   ```bash
   python mkdocs-scripts/build.py --strict
   # Fails on any warnings (broken links, missing files)
   ```

3. **Specification Processing**:
   ```bash
   python mkdocs-scripts/build-specs.py
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
- Maintain navigation hierarchy (Engineering > Dashboard/Specs/Implementation Summaries)
- **Note**: Spec navigation is auto-generated - manual editing will be overwritten during build
- Keep navigation order consistent for non-auto-generated sections
- Test with `python mkdocs-scripts/build.py --strict` after changes

### When Creating New Pages
1. **For Specifications**: Create directly in `/engineering/specs/` using proper naming convention
   - File will be automatically included in website during next build
   - No manual navigation updates required
2. **For Other Pages**: Create in appropriate `/mkdocs-docs/` subdirectory
3. Update `mkdocs.yml` navigation for non-spec pages
4. Test locally with `python mkdocs-scripts/serve.py` before committing

## Spec-Driven Development Philosophy

This repository demonstrates "building in public" principles with automated publishing:
- Every feature has a PM spec (planning phase) - automatically published to website
- Every commit has implementation tracking (development phase)
- Complete traceability from idea → spec → code → deployment with visual timelines
- Documentation created as byproduct of regular development, not separate manual process
- Single-source-of-truth approach eliminates duplication and sync issues
- AI assistance is explicitly acknowledged in Dev Workflows

## CI/CD Pipeline

Located in `.github/workflows/`:
- Runs `mkdocs build --strict` on every push
- Deploys to Azure Static Web Apps on successful build
- Ensures no broken links or missing files in production

## Getting Help

- **Documentation Issues**: Run `python mkdocs-scripts/serve.py` and check http://localhost:8000
- **Build Failures**: Run `python mkdocs-scripts/build.py --strict` to see specific errors
- **Spec Processing Issues**: Run `python mkdocs-scripts/build-specs.py` to test spec automation
- **Navigation Issues**: Check `mkdocs.yml` navigation structure (specs are auto-generated)
- **Link Errors**: Use strict mode to identify broken links

---

**Last Updated**: 2026-02-11
**NextPM Version**: Phase 1 - Static Knowledge Hub
**AI Assistant**: Updated by Claude Sonnet 4
