---
status: "completed"
priority: "high"
estimated_hours: 4
actual_hours: 4
assignee: "Kang"
category: "nextpm-feature"
demonstrates: ["spec-driven-development", "pr-workflow", "git-integration", "visual-timeline"]
state_history:
  - state: "draft"
    date: "2026-02-19"
    author: "Kang"
    notes: "Initial spec creation for PR tracking feature"
  - state: "completed"
    date: "2026-02-19"
    author: "Kang"
    notes: "Feature implemented with PR template, detection system, and timeline visualization"
---

# 20260219-pr-tracking

**Date:** 2026-02-19
**Version:** 1.0

## Overview

Extend NextPM's commit tracking system to also track and display Pull Requests in spec timelines. This enables complete visibility into the development journey from spec → commits → PR → merge, showcasing professional GitHub workflows and team collaboration patterns.

## Problem

**Current State:**
- NextPM automatically tracks commits linked to specs via `(#YYYYMMDD)` references
- Commits appear in visual timelines with author, date, and files changed
- No visibility into Pull Requests or code review process
- Missing demonstration of professional PR-based workflows

**Pain Points:**
- Solo developers working with AI tools (GitHub Copilot, Claude Code) create multiple feature branches
- PR workflow is industry standard but not demonstrated in NextPM
- No way to see which PRs implemented which specs
- Code review process not visible in development timeline
- Team collaboration patterns not showcased

## User Impact

**Primary Users:**
- **Solo Developers** - Working with AI tools to manage multiple features in parallel
- **Hiring Managers** - Evaluating portfolio projects for professional Git practices
- **Students** - Learning PR-based workflows and best practices
- **Teams** - Understanding how to link PRs to specifications

**User Benefits:**
- See complete development history: spec → feature branch → PR → merge
- Demonstrate professional GitHub workflow in portfolio
- Visual timeline shows both individual commits and PR merge events
- Clickable GitHub links to view actual PRs
- PR metadata (author, reviewers, branch name) displayed

## Proposed Solution

### High-Level Approach

Implement PR tracking that integrates seamlessly with existing commit tracking infrastructure, using git merge commits to detect PRs and display them in the visual timeline.

### Key Features

1. **PR Template**
   - Manual spec ID entry field
   - Clear instructions for developers
   - GitHub automatically shows template on PR creation
   - Parseable format for future automation

2. **Automatic PR Detection**
   - Detect PR merge commits via git log
   - Extract PR number from merge commit message pattern
   - Parse PR metadata: title, author, reviewers, branch
   - Support both full spec IDs (20260219-pr-tracking) and short form (20260219)

3. **Enhanced Timeline Visualization**
   - Unified timeline showing commits AND PRs chronologically
   - Purple gradient badges for PRs (vs gray for commits)
   - Clickable GitHub PR links
   - Display PR number, title, merge date, author, reviewers, branch

4. **Dashboard Integration**
   - Total PR count across all specs
   - Total commit count for comparison
   - Search index includes PR counts per spec

5. **CSS Styling System**
   - Purple theme for PR items
   - Hover effects on PR links
   - Responsive design for timeline items
   - Visual distinction between commits and PRs

### Technical Design

**Architecture:**
- Extend existing `collect_git_data()` to also call `collect_pr_data()`
- Use git log with `--merges` flag to find PR merge commits
- Regex parsing for GitHub merge commit patterns
- Merge commits and PRs into unified timeline sorted by date

**Key Components:**

1. **PR Detection** (`collect_pr_data()` function):
   ```python
   # Search for merge commits referencing spec ID
   git log --grep #{spec_id} --merges

   # Parse merge commit pattern
   "Merge pull request #123 from branch"

   # Extract: PR number, title, author, reviewers, branch
   ```

2. **Timeline Generation** (enhanced `generate_commit_timeline_html()`):
   - Merge commits and PRs into single array
   - Sort by date (most recent first)
   - Generate HTML for each item type
   - Helper functions: `generate_commit_item_html()`, `generate_pr_item_html()`

3. **Search Index** (add PR count field):
   ```json
   {
     "git_commits": 5,
     "pull_requests": 2
   }
   ```

**File Changes:**
- `.github/pull_request_template.md` - New PR template
- `mkdocs-scripts/build-specs.py` - PR detection and timeline logic
- `mkdocs-static/css/custom.css` - PR styling
- Dashboard stats calculation

### Implementation Details

**PR Merge Commit Pattern Recognition:**
```
Merge pull request #999 from branch-name
Title of the PR (#20260219)
Co-authored-by: Reviewer <email>
```

**Timeline HTML Structure:**
```html
<div class="timeline-item">
  <div class="timeline-marker timeline-marker-pr"></div>
  <div class="timeline-content">
    <div class="timeline-type-badge pr-badge">🔀 Pull Request #999</div>
    <a href="github.com/...">PR Title</a>
    <div class="pr-meta">
      👤 Author | 🌿 Branch | 👥 Reviewers
    </div>
  </div>
</div>
```

## Success Metrics

**Quantitative:**
- ✅ PR template appears on GitHub PR creation
- ✅ System detects and displays PRs in spec timelines
- ✅ Search index includes PR counts
- ✅ Dashboard shows total PR statistics
- ✅ CI/CD runs on PRs before merge

**Qualitative:**
- ✅ Visual distinction between commits and PRs is clear
- ✅ PR links successfully open GitHub PR pages
- ✅ Timeline chronology is accurate
- ✅ Professional GitHub workflow demonstrated in portfolio

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| PR template not followed | Medium | System gracefully handles missing spec IDs |
| Merge commit format varies | Medium | Regex patterns handle multiple GitHub formats |
| Shortened spec IDs cause mismatches | High | Search for both full (20260219-pr-tracking) and short (20260219) formats |
| Timeline becomes cluttered | Low | Clear visual distinction with color coding |

## Implementation Phases

### Phase 1: PR Detection (Completed ✅)
- Create PR template
- Implement `collect_pr_data()` function
- Integrate into `collect_git_data()`

### Phase 2: Timeline Visualization (Completed ✅)
- Refactor timeline generation
- Add helper functions for commit/PR items
- Merge and sort timeline items

### Phase 3: Styling & Polish (Completed ✅)
- Add PR CSS with purple theme
- Implement hover effects
- Test responsive design

### Phase 4: Dashboard Integration (Completed ✅)
- Add PR count to search index
- Update dashboard statistics
- Display total PRs

## Testing Strategy

**Local Testing:**
- Create mock merge commit with PR pattern
- Verify PR detection and parsing
- Check timeline HTML generation
- Validate search index updates

**Integration Testing:**
- Create real PR with spec reference
- Merge PR via GitHub
- Verify CI/CD runs successfully
- Confirm PR appears in timeline

## Future Enhancements (Out of Scope)

1. **GitHub API Integration** - Real-time PR status updates
2. **Review Comments** - Show approval/change requests in timeline
3. **Linked Issues** - Detect and link GitHub issues
4. **PR Status Badges** - Show draft/open/merged/closed states
5. **Timeline Filtering** - Toggle commits-only or PRs-only view

## References

- GitHub PR Template Docs: https://docs.github.com/en/communities/using-templates-to-encourage-useful-issues-and-pull-requests
- Git Log Documentation: https://git-scm.com/docs/git-log
- GitHub Merge Commit Patterns: Standard across all GitHub repositories
- Material Design PR Colors: Purple represents code review/collaboration

---

**Implementation Status:** ✅ Completed
**Live Demo:** Available after PR merge at kangxh.com
