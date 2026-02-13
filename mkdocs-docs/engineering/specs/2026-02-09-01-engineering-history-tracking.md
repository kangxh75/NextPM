# 2026-02-09-01 Engineering History Tracking System

<span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>

<div class="spec-timeline" data-timeline="{&quot;spec_id&quot;: &quot;2026-02-09-01&quot;, &quot;status&quot;: &quot;draft&quot;, &quot;state_history&quot;: [], &quot;estimated_hours&quot;: 0, &quot;actual_hours&quot;: 0, &quot;priority&quot;: &quot;medium&quot;, &quot;category&quot;: &quot;nextpm-feature&quot;, &quot;demonstrates&quot;: []}"></div>


**Status:** 📝 Draft
**Date:** 2026-02-09
**Version:** 1.1
**Priority:** High

## Overview

Create a comprehensive engineering history tracking system that links PM specs with code changes, providing a complete audit trail of NextPM's evolution. This feature will reorganize navigation under "Engineering" to showcase the development process and create templates for consistent change documentation.

## Problem

**Current State:**
- PM Workflows and Dev Workflows are separate top-level menu items
- No formal tracking of how specs relate to actual code changes
- No standardized format for documenting commits/changes
- Difficult to see the connection between "what we planned" (specs) and "what we built" (commits)
- Missing the meta-narrative of building NextPM itself

**Pain Points:**
- Can't easily trace a feature from spec → implementation → deployment
- No audit trail for future reference or case studies
- Navigation doesn't reflect the "building in public" philosophy
- Inconsistent commit documentation format

## User Impact

**Primary Users:**
- **You (Kang)** - Track your own development process
- **Future PMs** - Learn from real development examples
- **AI Assistants** - Better context about project history

**User Benefits:**
- Complete visibility into development process
- Real examples of AI-augmented PM workflows
- Teaching material created as byproduct of work
- Professional development documentation

## Proposed Solution

### 1. Navigation Restructuring

**New Structure:**
```
Home
Engineering (NEW!)
  ├── PM Workflows (moved here)
  │   ├── Overview
  │   ├── 0.00 Project Start ← Existing (grandfathered)
  │   ├── 2026-02-09-01 Engineering History ← NEW (this feature)
  │   └── [Future specs with YYYY-MM-DD-nn format...]
  │
  └── Dev Workflows (moved here)
      ├── Overview
      ├── 2026-02-09 Initial Setup ← NEW (commit summary)
      ├── 2026-02-09 Placeholder Pages ← NEW (commit summary)
      └── [Future commit summaries...]

Prompt Library
Examples
About
```

**Rationale:**
- Groups related content under "Engineering"
- Shows PM → Dev flow clearly
- Makes the building process transparent
- Easier to navigate development timeline

### 2. PM Workflow Specs

**Two-Folder Approach:**
- **Working Specs:** `/project/specs/` - Full detailed specifications (not exposed to external users)
- **Website Summaries:** `/mkdocs-docs/engineering/pm-workflows/` - User-friendly summaries with links to GitHub

**Content Strategy:**
- Full specs remain in `/project/specs/` as comprehensive working documents
- Website pages provide digestible summaries for external visitors
- Summaries link to full specs on GitHub for those wanting details
- This keeps website clean while maintaining complete documentation

**Website Summary Template:**
```markdown
# [Feature Number]: [Feature Name]

**Status:** [Draft/In Progress/Completed]
**Full Spec:** [View on GitHub](https://github.com/kangxh75/NextPM/blob/master/project/specs/YYYY-MM-DD-nn-spec-name.md)

## What This Feature Does

2-3 sentence overview of the feature in plain language.

## Why It Matters

Brief explanation of the problem it solves and user benefits.

## Implementation Timeline

- **Started:** YYYY-MM-DD
- **Completed:** YYYY-MM-DD (or "In Progress")

## Related Changes

- [2026-02-09 Commit Title](../dev-workflows/2026-02-09-commit-title.md)
- [2026-02-10 Commit Title](../dev-workflows/2026-02-10-commit-title.md)

## Key Outcomes

- Outcome 1
- Outcome 2
- Outcome 3

## Lessons Learned

1-2 key takeaways from implementing this feature.

---

**Want the full technical details?** [Read the complete spec on GitHub](link)
```

### 3. Dev Workflow Commit Summaries

**Location:** `/mkdocs-docs/engineering/dev-workflows/`

**Naming Convention:** `YYYY-MM-DD-HHMM-brief-title.md`
- One entry per commit/push
- Timestamp (24-hour format) allows multiple commits per day
- Examples:
  - `2026-02-09-1430-add-navigation.md`
  - `2026-02-09-1645-fix-links.md`
  - `2026-02-09-2120-update-styles.md`

**Linking to Specs:**
- Use spec ID in commit messages: `feat: add feature (#2026-02-09-01)`
- Format: `(#YYYY-MM-DD-nn)` where nn is the sequential number
- When creating Dev Workflow summary, link to the related PM Workflow page
- PM Workflow summaries manually add links to Dev Workflow entries as work progresses

**Template Structure:**
```markdown
# [YYYY-MM-DD HH:MM] [Brief Title]

**Date:** YYYY-MM-DD HH:MM
**Commits:** [Commit hash(es)]
**Related Spec:** [#2026-02-09-01 Engineering History](../pm-workflows/2026-02-09-01-engineering-history.md)

## Changes Summary

Brief description of what changed.

## Files Changed

- `path/to/file1.ext` - Description of change
- `path/to/file2.ext` - Description of change

## Key Decisions

- Decision 1
- Decision 2

## Technical Details

### What Was Added
- Feature/file 1
- Feature/file 2

### What Was Modified
- Change 1
- Change 2

### What Was Removed
- Removal 1 (if any)

## Testing

How changes were validated.

## Next Steps

- [ ] Follow-up task 1
- [ ] Follow-up task 2

## AI Assistance

Tools used: [Claude Code, GitHub Copilot, etc.]
Time saved estimate: [X hours]

---

**GitHub Commits:**
- [Commit hash](link to GitHub commit)
```

### 4. Linking Workflow

**How Specs and Dev Summaries Connect:**

1. **When starting work on a spec:**
   - PM creates spec: `/project/specs/2026-02-09-01-feature-name.md`
   - PM creates summary: `/mkdocs-docs/engineering/pm-workflows/2026-02-09-01-feature-name.md`
   - Summary includes "Related Changes" section (initially empty)

2. **When making a commit:**
   - Include spec ID in commit message: `feat: add navigation (#2026-02-09-01)`
   - Commit message format: `type: description (#YYYY-MM-DD-nn)`
   - Push to GitHub

3. **After pushing:**
   - Create Dev Workflow summary: `/mkdocs-docs/engineering/dev-workflows/YYYY-MM-DD-HHMM-brief-title.md`
   - Link to related spec using spec ID from commit message
   - Example: `**Related Spec:** [#2026-02-09-01 Engineering History](../pm-workflows/2026-02-09-01-engineering-history.md)`

4. **Update PM Workflow summary:**
   - Add link to new Dev Workflow entry in "Related Changes" section
   - Example: `- [2026-02-09 14:30 Add Navigation](../dev-workflows/2026-02-09-1430-add-navigation.md)`

**Benefits:**
- Commit messages show which spec the work relates to
- Dev summaries link back to specs
- PM summaries accumulate links to all related commits
- Complete bidirectional traceability

### 5. Automation Considerations (Future)

**Manual for now, can automate later:**
- Manual: Write commit summary after pushing
- Future: GitHub Action to generate template from commits
- Future: Auto-link specs to commit summaries

## Success Metrics

### Completion Criteria
- [x] Navigation restructured with "Dev History" parent
- [ ] Template created for PM Workflow specs
- [ ] Template created for Dev Workflow commit summaries
- [ ] First two entries created (0.00 and 0.01 specs)
- [ ] First commit summary created (today's work)
- [ ] Documentation updated in conventions.md
- [ ] Site builds and deploys successfully

### Quality Indicators
- All links work (no 404s)
- Templates are clear and easy to follow
- Navigation makes logical sense
- Content is consistent with NextPM's voice

### User Acceptance
- Easy to find development history
- Clear connection between specs and implementations
- Professional appearance
- Mobile-friendly navigation

## Implementation Notes

### Phase 1: Structure (This PR)

1. **Reorganize folders:**
   ```
   mkdocs-docs/
   ├── engineering/              (NEW)
   │   ├── index.md             (overview)
   │   ├── pm-workflows/        (moved from root)
   │   │   ├── index.md
   │   │   ├── 0.00-project-start.md  (existing)
   │   │   └── 2026-02-09-01-engineering-history.md  (NEW - this feature)
   │   └── dev-workflows/       (moved from root)
   │       ├── index.md
   │       └── 2026-02-09-initial-setup.md  (NEW)
   ```

2. **Update mkdocs.yml navigation:**
   ```yaml
   nav:
     - Home: index.md
     - Engineering:
         - Overview: engineering/index.md
         - PM Workflows:
             - Overview: engineering/pm-workflows/index.md
             - 0.00 Project Start: engineering/pm-workflows/0.00-project-start.md
             - 2026-02-09-01 Engineering History: engineering/pm-workflows/2026-02-09-01-engineering-history.md
         - Dev Workflows:
             - Overview: engineering/dev-workflows/index.md
             - 2026-02-09 Initial Setup: engineering/dev-workflows/2026-02-09-initial-setup.md
     - Prompt Library: ...
     - Examples: ...
     - About: ...
   ```

3. **Create templates:**
   - `/project/templates/pm-workflow-spec-template.md`
   - `/project/templates/dev-workflow-commit-summary-template.md`

4. **Create initial entries:**
   - PM Workflow: 0.00 Project Start (from existing spec, grandfathered)
   - PM Workflow: 2026-02-09-01 Engineering History (this feature)
   - Dev Workflow: Today's work summary

### Phase 2: Content (Next)

5. **Backfill existing work:**
   - Create commit summaries for previous commits
   - Link them to today's PM workflow specs

6. **Update conventions:**
   - Document process in `/ai-context/conventions.md`
   - Add to feature development flow

### Technical Constraints

- Must maintain backward compatibility with existing links
- Navigation depth limited (keep it simple)
- File naming must be consistent for sorting
- Templates must work in MkDocs Material

## Out of Scope

**For v0.1 (this feature):**
- ❌ Automated commit summary generation
- ❌ GitHub Action integration
- ❌ Linking from GitHub commits back to site
- ❌ Search/filter functionality
- ❌ Timeline visualization
- ❌ RSS feed of changes
- ❌ Email notifications

**Explicitly Deferred:**
- Automation can be added in future iteration
- Advanced features after validating manual process
- Integration with GitHub API (Phase 2)

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Navigation too complex | High | Keep max 2 levels deep, clear labels |
| Too much manual work | Medium | Start simple, automate later if needed |
| Links break during restructure | High | Test thoroughly, use relative links |
| Inconsistent documentation | Medium | Provide clear templates and examples |
| Cluttered navigation | Medium | Archive old entries periodically |

## References

### Internal Documents
- [project/specs/0.00-project-start.md](../specs/0.00-project-start.md) - Foundation spec
- [ai-context/conventions.md](https://github.com/kangxh75/NextPM/blob/master/ai-context/conventions.md) - Documentation standards
- [meta/adr/002-project-vs-examples-folders.md](https://github.com/kangxh75/NextPM/blob/master/../../meta/adr/002-project-vs-examples-folders.md) - Folder strategy

### Inspiration
- [Keep a Changelog](https://keepachangelog.com/) - Changelog format
- [Conventional Commits](https://www.conventionalcommits.org/) - Commit message standard
- [ADR](https://adr.github.io/) - Architecture Decision Records

### Related Artifacts
- **Tasks:** To be created in `/project/tasks/2026-02-09-01-engineering-history-tasks.md`
- **Validation:** To be created in `/project/validations/2026-02-09-01-engineering-history-validation.md`

## Next Steps

1. Create task breakdown
2. Implement navigation restructure
3. Create template files
4. Create initial content entries
5. Test all links
6. Deploy and validate
7. Document in validation file

## Lessons Learned

**To be filled after implementation**

## Change History

### Version 1.1 - 2026-02-09
- Added clarification on multiple commits per day (HHMM timestamp format)
- Added "Linking Workflow" section explaining bidirectional traceability
- Clarified spec modification approach (modify original vs create new)
- Added version tracking strategy (Option B with Change History section)
- Updated templates with spec ID linking format

### Version 1.0 - 2026-02-09
- Initial spec creation
- Defined navigation structure under "Engineering"
- Created templates for PM Workflow specs and Dev Workflow summaries
- Established two-folder approach (working specs vs website summaries)

---

**Document Metadata:**
- **Spec Version:** 1.1
- **Created:** 2026-02-09
- **Author:** Kang (with AI assistance from Claude Code)
- **Last Updated:** 2026-02-09
- **Related Specs:** 0.00-project-start.md
- **Status:** Living document
