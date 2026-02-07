# ADR 001: MkDocs Folder Prefix Strategy

**Status:** Accepted
**Date:** 2026-02-04
**Author:** Kang (with AI assistance from Claude Code)

## Context

NextPM uses MkDocs Material for static site generation. By default, MkDocs uses generic folder names (`docs/`, `static/`, `site/`) that don't clearly indicate their purpose when viewing the root directory. As the project grows with multiple top-level folders (`prompts/`, `examples/`, `project/`, `meta/`, `ai-context/`), maintaining a clean and organized root folder structure becomes important.

**Problem:** How should we name MkDocs-related folders to keep the root directory clean and identifiable?

## Decision

We will **prefix all MkDocs-related folders with `mkdocs-`**:

- `docs/` → `mkdocs-docs/` (source content)
- `static/` → `mkdocs-static/` (static assets)
- `site/` → `mkdocs-site/` (build output)

This requires updating:
- `mkdocs.yml` configuration (`docs_dir`, `site_dir`)
- `.gitignore` (exclude `mkdocs-site/`)
- `.vscode/settings.json` (exclude from search/explorer)
- GitHub Actions workflows (reference correct paths)
- AI context documentation

## Rationale

### Pros
1. **Clarity**: Immediately obvious which folders are MkDocs-related
2. **Root folder hygiene**: Keeps root clean by grouping related items with consistent naming
3. **Discoverability**: New contributors (human or AI) can quickly identify purpose
4. **Consistency**: Aligns with root folder organization principle (group related files)
5. **No conflicts**: Avoids confusion with other `docs/` or `static/` folders that might be added later
6. **Searchability**: Easy to find all MkDocs-related files with glob patterns (`mkdocs-*`)

### Cons
1. **Non-standard**: Most MkDocs projects use default folder names
2. **Documentation updates**: Need to update references in docs and tutorials
3. **Configuration overhead**: Requires explicit `docs_dir` and `site_dir` configuration
4. **Team learning curve**: New contributors need to understand the naming convention
5. **Tool compatibility**: Some MkDocs plugins might assume default folder names (rare)

### Alternatives Considered

#### Alternative 1: Keep default names (`docs/`, `site/`, `static/`)
- **Pros**: Standard, no configuration needed, familiar to MkDocs users
- **Cons**: Generic names clutter root, unclear purpose, potential conflicts
- **Rejected because**: Doesn't align with root folder organization principle

#### Alternative 2: Move all MkDocs files into single `mkdocs/` folder
```
mkdocs/
  ├── docs/
  ├── static/
  └── site/
```
- **Pros**: All MkDocs files in one place, very clean root
- **Cons**: Breaks MkDocs conventions, requires complex configuration, harder to navigate
- **Rejected because**: Too much deviation from MkDocs norms, reduces usability

#### Alternative 3: Use underscore prefix (`_docs/`, `_site/`)
- **Pros**: Convention from Jekyll/other static generators
- **Cons**: Less descriptive than `mkdocs-`, underscore has special meaning in some contexts
- **Rejected because**: Less clear about purpose, `mkdocs-` is more explicit

## Implementation

### Configuration Changes

**mkdocs.yml:**
```yaml
docs_dir: mkdocs-docs
site_dir: mkdocs-site
```

**.gitignore:**
```
site/
mkdocs-site/
```

**.vscode/settings.json:**
```json
{
  "files.exclude": {
    "mkdocs-site/": true
  },
  "search.exclude": {
    "mkdocs-site/": true
  }
}
```

**GitHub Actions workflows:**
Update all references to use `mkdocs-site/` for build output.

### Migration Steps

1. Rename folders:
   - `mv docs mkdocs-docs`
   - `mv static mkdocs-static` (if exists)
2. Update `mkdocs.yml` with new paths
3. Update `.gitignore` and `.vscode/settings.json`
4. Update AI context documentation
5. Test build: `mkdocs build --strict`
6. Commit all changes with descriptive message

## Consequences

### Positive
- ✅ Root folder is cleaner and more organized
- ✅ Purpose of folders is immediately clear
- ✅ Aligns with documented conventions in `ai-context/conventions.md`
- ✅ Sets precedent for other tool-specific folder prefixes if needed
- ✅ Easy to enforce via documentation and AI context

### Negative
- ⚠️ Deviates from MkDocs community norms
- ⚠️ Requires explaining to collaborators
- ⚠️ Need to update external documentation/tutorials that reference default paths

### Neutral
- Future tools/frameworks can follow same pattern (e.g., `fastapi-app/`, `react-frontend/`)
- Can be documented as a project convention in README and contributing guidelines

## Compliance

This decision is documented in:
- `/ai-context/conventions.md` - Root folder structure principle
- `/project/specs/0.00-project-start.md` - Implementation notes
- This ADR

## Related Decisions

- Will inform future decisions about folder organization
- May establish pattern for other tool-specific folders (Phase 2)

## Review Date

**Next review:** When adding Phase 2 dynamic features (estimated February 2026)

**Review criteria:**
- Has this caused significant confusion or friction?
- Have we needed to revert or modify the approach?
- Do benefits outweigh the non-standard nature?

## Notes

- Initial implementation completed 2026-02-04
- No issues encountered during implementation
- MkDocs build works correctly with new paths
- AI assistants (Claude Code) adapted immediately with updated context

---

**Status History:**
- 2026-02-04: Proposed and Accepted
- Implementation: Completed 2026-02-04
