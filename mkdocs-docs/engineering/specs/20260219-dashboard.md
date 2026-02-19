
# 20260219-dashboard

<span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>

<div class="spec-timeline" data-timeline="{&quot;spec_id&quot;: &quot;20260219-dashboard&quot;, &quot;status&quot;: &quot;draft&quot;, &quot;state_history&quot;: [], &quot;estimated_hours&quot;: 0, &quot;actual_hours&quot;: 0, &quot;priority&quot;: &quot;medium&quot;, &quot;category&quot;: &quot;nextpm-feature&quot;, &quot;demonstrates&quot;: []}"></div>

<div class="commit-timeline">
    <h4>📝 Development Timeline</h4>
    <div class="timeline-container">
        <div class="timeline-item latest">
            <div class="timeline-marker timeline-marker-pr"></div>
            <div class="timeline-content">
                <div class="timeline-type-badge pr-badge">🔀 Pull Request #7</div>
                <div class="pr-header">
                    <a href="https://github.com/kangxh75/NextPM/pull/7" target="_blank" class="pr-link">
                        <span class="pr-title">Merge pull request #7 from kangxh75/feat/20260219-dashboard-impl</span>
                    </a>
                    <span class="pr-date">2026-02-19</span>
                </div>
                <div class="pr-meta">
                    <span class="pr-author">👤 kangxh</span>
                    <span class="pr-branch">🌿 kangxh75/feat/20260219-dashboard-impl</span>
                    
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker timeline-marker-pr"></div>
            <div class="timeline-content">
                <div class="timeline-type-badge pr-badge">🔀 Pull Request #2</div>
                <div class="pr-header">
                    <a href="https://github.com/kangxh75/NextPM/pull/2" target="_blank" class="pr-link">
                        <span class="pr-title">Merge pull request #2 from kangxh75/feat/20260219-pr-tracking</span>
                    </a>
                    <span class="pr-date">2026-02-19</span>
                </div>
                <div class="pr-meta">
                    <span class="pr-author">👤 kangxh</span>
                    <span class="pr-branch">🌿 kangxh75/feat/20260219-pr-tracking</span>
                    
                </div>
            </div>
        </div>
    </div>
</div>



**Date:** 2026-02-19
**Version:** 1.0

> **Related:** See [20260219-pr-tracking](20260219-pr-tracking.md) for PR tracking implementation and [20260213-spec-showcase](20260213-spec-showcase.md) for visual timeline features.

## Overview

Transform the NextPM dashboard into a comprehensive project management interface featuring a sortable/filterable table view of all specifications and a gitflow-style activity graph showing the complete development history (specs → commits → PRs → merges) in a visual timeline similar to Git branching workflows.

## Problem

**Current State:**
- Dashboard shows basic statistics (total specs, commits, PRs) with simple stat cards
- No table view for browsing and comparing specs at a glance
- No visual representation of development activity flow
- Cannot see the relationship between specs, branches, commits, and PRs
- Difficult to understand the development timeline across multiple features

**Pain Points:**
- **No Quick Overview**: Cannot quickly scan all specs with their key attributes (status, priority, hours, activity)
- **No Filtering/Sorting**: Cannot find specs by status, priority, or date without reading each one
- **No Activity Visualization**: Cannot see how development flows from spec → branch → commits → PR → merge
- **Limited Project Insights**: No visual way to see which specs are active, completed, or stalled
- **Missing Git Workflow Context**: Cannot see the branching and merging patterns that demonstrate PR workflow

## User Impact

**Primary Users:**
- **Product Managers** - Need table view to track spec status, priorities, and progress at a glance
- **Developers** - Need activity graph to understand development flow and see which specs are actively being worked on
- **Portfolio Viewers** - Want to see professional project management and Git workflow visualization

**User Benefits:**
- Quick filtering/sorting of specs by status, priority, date, or hours
- Visual gitflow-style graph showing complete development timeline
- Clear understanding of which specs are in progress vs completed
- Professional demonstration of spec-driven development with Git workflows
- Easy identification of active development streams and merge patterns

## Proposed Solution

### High-Level Approach

Enhance the existing dashboard with two major sections:

1. **Table View** - Interactive, sortable/filterable table showing all specs with key metadata
2. **Activity Graph** - Gitflow-style visualization showing specs, branches, commits, PRs, and merges over time

### Key Features

#### 1. **Spec Table View**

**Columns:**
- **Spec ID** (linked to spec page) - e.g., `20260219-dashboard`
- **Title** - Short description
- **Status** - Badge with color coding (draft/in-progress/completed/archived)
- **Priority** - Badge (low/medium/high/critical)
- **Estimated Hours** - Planned effort
- **Actual Hours** - Time spent
- **Commits** - Count of linked commits
- **PRs** - Count of linked PRs
- **Last Updated** - Most recent activity date
- **Author** - Spec creator

**Interactions:**
- Click column headers to sort (ascending/descending)
- Filter by status using dropdown or buttons
- Filter by priority using dropdown or buttons
- Search by spec ID or title
- Click row to navigate to spec page

**Visual Design:**
- Clean, modern table with hover effects
- Color-coded status badges (draft=gray, in-progress=blue, completed=green, archived=purple)
- Priority badges with icons (low=▽, medium=◇, high=△, critical=⚠️)
- Responsive layout for mobile/tablet

#### 2. **Activity Graph (Gitflow Style)**

**Graph Structure:**
```
Timeline (horizontal, newest on right) →

Master Branch (main horizontal line)
    ├─ Spec 20260210 created
    │   └─ feat/20260210-auth branch
    │       ├─ commit A
    │       ├─ commit B
    │       └─ PR #1 → merge to master
    │
    ├─ Spec 20260213 created
    │   ├─ feat/20260213-spec branch
    │   │   ├─ commit C
    │   │   └─ PR #2 → merge to master
    │   │
    │   └─ feat/20260213-impl branch
    │       ├─ commit D
    │       ├─ commit E
    │       └─ PR #3 → merge to master
    │
    └─ Current state
```

**Visual Elements:**
- **Master branch line** - Horizontal line representing main branch
- **Feature branch lines** - Branches extending from master, showing parallel work
- **Spec nodes** - Diamond shapes for spec creation events
- **Commit nodes** - Circles showing individual commits
- **PR nodes** - Rounded rectangles showing pull requests
- **Merge arrows** - Curved lines showing PR merges back to master
- **Color coding** - Different colors for specs, commits, PRs (matching timeline badges)

**Interactions:**
- Hover over nodes to see details (commit message, PR title, author, date)
- Click nodes to navigate to commit, PR, or spec page
- Zoom in/out to see more/less detail
- Pan left/right to navigate timeline
- Toggle to show/hide completed specs

**Time Scale:**
- X-axis shows dates (day/week/month granularity)
- Auto-adjust scale based on activity density
- Show relative time labels ("2 days ago", "1 week ago")

## Success Metrics

### Completion Criteria

**Table View:**
- [x] Table displays all specs with 10 columns (ID, title, status, priority, hours, commits, PRs, date, author)
- [x] Click column headers to sort ascending/descending
- [x] Filter by status (draft/in-progress/completed/archived)
- [x] Filter by priority (low/medium/high/critical)
- [x] Search by spec ID or title
- [x] Click row to navigate to spec page
- [x] Responsive layout works on mobile/tablet/desktop
- [x] Status and priority badges show correct colors and icons

**Activity Graph:**
- [x] Graph shows horizontal timeline with master branch
- [x] Feature branches display for each spec with PR workflow
- [x] Commit nodes show individual commits with author and date
- [x] PR nodes show pull request info with merge status
- [x] Merge arrows connect PRs back to master
- [x] Hover tooltips show details for each node
- [x] Click nodes to navigate to spec/commit/PR pages
- [x] Zoom in/out controls work smoothly
- [x] Pan left/right to navigate timeline
- [x] Color coding matches existing timeline badges (commits=gray, PRs=purple, specs=blue)

**Build Process:**
- [x] `python mkdocs-scripts/build-specs.py` generates table and graph data
- [x] Dashboard page includes embedded JSON data
- [x] JavaScript loads and renders both components
- [x] Build completes without errors in strict mode
- [x] Dashboard loads in under 2 seconds with 50 specs

### Quality Indicators

**User Experience:**
- Table sorting responds instantly (< 100ms)
- Graph renders smoothly without jank
- Hover tooltips appear within 200ms
- All interactions feel responsive and smooth
- Mobile layout is usable without horizontal scrolling

**Visual Quality:**
- Graph resembles professional gitflow diagrams from Atlassian/GitHub
- Colors are consistent with existing NextPM theme (indigo/purple scheme)
- Typography is clear and readable at all zoom levels
- Animations are smooth (60fps)

**Code Quality:**
- JavaScript follows ES6+ best practices
- No console errors or warnings
- D3.js code is modular and maintainable
- Performance profiling shows no bottlenecks

### User Acceptance

- Product managers can quickly find specs by status or priority
- Developers can see active development branches and recent merges
- Portfolio viewers can understand the project's Git workflow at a glance
- Graph clearly shows parallel development streams
- Table provides quick overview without needing to read individual specs

## Out of Scope

**For v1.0 (this feature):**
- ❌ Real-time updates (dashboard requires rebuild to show new data)
- ❌ Export table to CSV/Excel
- ❌ Custom chart/graph types (bar charts, pie charts)
- ❌ Filtering by date range or author
- ❌ Advanced search with regex or multiple criteria
- ❌ GitHub API integration for live PR status
- ❌ Commit diff viewer in dashboard
- ❌ Branch comparison tool
- ❌ Animated graph transitions showing how timeline evolves
- ❌ Multi-user collaboration features (comments, reviews)

**Explicitly Deferred to v2.0:**
- Gantt chart view for project planning
- Burndown charts for sprint tracking
- Custom dashboard widgets (configurable by user)
- Dashboard customization (show/hide sections, reorder)

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| D3.js learning curve steep | High | Start with Mermaid prototype, migrate to D3.js incrementally; use D3 tutorials and examples |
| Large graph with 100+ specs becomes slow | Medium | Implement virtual scrolling, limit visible nodes, add pagination or date range filtering |
| Complex git history with many branches hard to visualize | Medium | Simplify graph by grouping commits, showing only PR-related branches, hide merged branches |
| Mobile/tablet graph interaction challenging | Low | Provide pinch-to-zoom, swipe-to-pan gestures; add fallback table view for small screens |
| Browser compatibility issues with D3.js | Low | Test on Chrome, Firefox, Safari, Edge; provide fallback message for unsupported browsers |

## References

### Internal Documents

- [20260219-pr-tracking](20260219-pr-tracking.md) - PR tracking system that provides data for activity graph
- [20260213-spec-showcase](20260213-spec-showcase.md) - Visual timeline features and state management

### External Resources

- [Atlassian Gitflow Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow) - Inspiration for activity graph visualization
- [D3.js Graph Gallery](https://d3-graph-gallery.com/) - D3.js examples and tutorials
- [GitHub Network Graph](https://github.com/kangxh75/NextPM/network) - GitHub's built-in graph visualization
- [Mermaid Git Graphs](https://mermaid.js.org/syntax/gitgraph.html) - Mermaid diagram syntax for git graphs

## Next Steps

1. Review and approve this specification
2. Create task breakdown in `/project/tasks/20260219-dashboard-tasks.md`
3. Begin Phase 1: Spec table view implementation
4. Prototype activity graph with Mermaid to validate layout
5. Implement D3.js activity graph
6. Test and polish interactions
7. Create PR for implementation review

## Change History

### Version 1.0 - 2026-02-19

- Initial spec creation
- Defined two-part dashboard: table view + activity graph
- Specified gitflow-style visualization inspired by Atlassian
- Established D3.js as primary technology with Mermaid fallback
- Scoped to build-time data generation (no real-time updates)
- Set success criteria for table sorting/filtering and graph interactions

---

**Document Metadata:**
- **Spec Version:** 1.0
- **Created:** 2026-02-19
- **Author:** Kang (with AI assistance from Claude Sonnet 4.5)
- **Last Updated:** 2026-02-19
- **Related Specs:** 20260219-pr-tracking, 20260213-spec-showcase
- **Status:** Living document
