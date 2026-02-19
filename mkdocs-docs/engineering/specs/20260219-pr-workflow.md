
# 20260219-pr-workflow

<span class="spec-state-badge spec-state-completed" data-status="completed" data-priority="high">
    🔥 Completed
</span>

<div class="spec-timeline" data-timeline="{&quot;spec_id&quot;: &quot;20260219-pr-workflow&quot;, &quot;status&quot;: &quot;completed&quot;, &quot;state_history&quot;: [{&quot;state&quot;: &quot;draft&quot;, &quot;date&quot;: &quot;2026-02-19&quot;, &quot;author&quot;: &quot;Kang&quot;, &quot;notes&quot;: &quot;Initial spec creation for documenting PR workflow&quot;}, {&quot;state&quot;: &quot;completed&quot;, &quot;date&quot;: &quot;2026-02-19&quot;, &quot;author&quot;: &quot;Kang&quot;, &quot;notes&quot;: &quot;Workflow documented with examples and CI/CD integration&quot;}], &quot;estimated_hours&quot;: 2, &quot;actual_hours&quot;: 2, &quot;priority&quot;: &quot;high&quot;, &quot;category&quot;: &quot;nextpm-feature&quot;, &quot;demonstrates&quot;: [&quot;spec-driven-development&quot;, &quot;pr-workflow&quot;, &quot;team-collaboration&quot;, &quot;git-best-practices&quot;]}"></div>

<div class="commit-timeline">
    <h4>📝 Development Timeline</h4>
    <div class="timeline-container">
        <div class="timeline-item latest">
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

> **Related:** See [20260219-pr-tracking](20260219-pr-tracking.md) for the technical implementation of PR tracking and timeline visualization.

## Overview

Establish a Pull Request-based development workflow for NextPM that separates PM specification work from implementation work, enabling clear role separation, code review, and professional Git practices. This workflow supports both team collaboration and solo development with AI coding assistants.

## Problem

**Current State:**
- Direct commits to master branch
- No code review process
- Specs and implementation mixed together
- No formal approval workflow
- Missing demonstration of professional Git practices

**Pain Points:**
- Solo developers using AI tools (Claude Code, GitHub Copilot) need to manage multiple features in parallel
- No clear separation between PM work (specs) and engineering work (implementation)
- Direct master commits don't demonstrate professional workflow for portfolio
- Team collaboration patterns not established
- PR template created but workflow not documented

## User Impact

**Primary Users:**
- **Product Managers** - Need clear process for spec creation and approval
- **Developers** - Need structured workflow for implementing features
- **Solo Developers** - Working like a team with multiple AI coding assistants
- **Teams** - Clear roles and responsibilities for collaboration

**User Benefits:**
- Structured workflow with clear phases (spec → review → implementation → review)
- CI/CD automatically tests PRs before merge
- Complete audit trail of decisions and changes
- Professional Git practices demonstrated in portfolio
- AI assistants can work on multiple features simultaneously

## Proposed Solution

### High-Level Approach

Implement a two-phase PR workflow where:
1. **Phase 1: Spec PR** - PM creates spec, dev team reviews requirements
2. **Phase 2: Implementation PR** - Dev creates code, team reviews implementation

Both phases use the same PR template, CI/CD, and timeline tracking system.

### Workflow Diagrams

#### **For Teams:**
```
PM (You)                          Developer (Teammate)
    |                                    |
    | 1. Create spec branch              |
    | feat/YYYYMMDD-feature-name         |
    |                                    |
    | 2. Write spec.md                   |
    |                                    |
    | 3. Push + Create PR                |
    |                                    |
    | 4. Assign dev for review     ----> | 5. Review spec
    |                                    |    - Check feasibility
    | 6. Discuss/update spec       <---- |    - Estimate hours
    |                                    |    - Suggest changes
    | 7. Merge spec PR                   |
    |                                    |
    |                              ----> | 8. Create impl branch
    |                                    |    feat/YYYYMMDD-feature-name-impl
    |                                    |
    |                                    | 9. Write code
    |                                    |
    |                                    | 10. Push + Create PR
    |                                    |
    | 11. Code review            <------ | 12. Assign PM/tech lead
    |                                    |
    | 13. Approve & merge                |
    |                                    |
    | 14. Both PRs appear in timeline!   |
```

#### **For Solo Developer (AI-Assisted):**
```
You as PM                         You as Developer
    |                                    |
    | 1. Write spec                      |
    | feat/YYYYMMDD-feature              |
    |                                    |
    | 2. Create PR, self-review          |
    |                                    |
    | 3. Merge spec                      |
    |                                    |
    | 4. Switch to dev role        ----> | 5. Create impl branch
    |                                    |    feat/YYYYMMDD-feature-impl
    |                                    |
    |                              (AI generates code with Claude Code/Copilot)
    |                                    |
    |                                    | 6. Create PR, self-review
    |                                    |
    | 7. Approve & merge                 |
    |                                    |
    | 8. Both PRs in timeline!           |
```

### Detailed Workflow Steps

#### **Phase 1: Spec Creation & Review**

**Step 1: PM Creates Feature Branch**
```bash
git checkout master
git pull origin master

# Create branch for spec (no -spec suffix needed)
git checkout -b feat/YYYYMMDD-feature-name
```

**Step 2: PM Writes Specification**
```bash
# Create spec file
engineering/specs/YYYYMMDD-feature-name.md

# Use PM spec template
engineering/templates/pm-workflow-spec-template.md

# Commit
git add engineering/specs/YYYYMMDD-feature-name.md
git commit -m "docs: add spec for feature name (#YYYYMMDD)

Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

# Push
git push origin feat/YYYYMMDD-feature-name
```

**Step 3: Create Spec PR on GitHub**
1. Visit GitHub repository
2. Click "Compare & pull request" (or create from pushed branch)
3. **PR template auto-fills** - Fill in:
   ```
   **Spec ID**: YYYYMMDD
   ```
4. Title: "docs: add spec for [feature name]"
5. Assign reviewer (for teams) or self-review (solo)
6. **CI/CD automatically runs** build-and-test.yml
7. Wait for tests to pass (green checkmark)

**Step 4: Spec Review Process**
- Developer reviews feasibility, estimates, approach
- Comments on PR with questions/suggestions
- PM updates spec based on feedback
- Reviewer approves when satisfied

**Step 5: Merge Spec PR**
- Click "Merge pull request" on GitHub
- Delete feature branch (GitHub offers this option)
- **Spec is now official and published**

---

#### **Phase 2: Implementation & Code Review**

**Step 6: Developer Creates Implementation Branch**
```bash
git checkout master
git pull origin master  # Get merged spec

# Create implementation branch
git checkout -b feat/YYYYMMDD-feature-name-impl
```

**Step 7: Developer Implements Feature**
```bash
# Write code (use AI assistants!)
# - Claude Code for complex logic
# - GitHub Copilot for boilerplate
# - Cursor for refactoring

# Commit frequently
git commit -m "feat: add component X (#YYYYMMDD)"
git commit -m "feat: add tests for X (#YYYYMMDD)"
git commit -m "feat: update documentation (#YYYYMMDD)"

# Push when ready
git push origin feat/YYYYMMDD-feature-name-impl
```

**Step 8: Create Implementation PR on GitHub**
1. Visit GitHub repository
2. Click "Compare & pull request"
3. **PR template auto-fills** - Fill in:
   ```
   **Spec ID**: YYYYMMDD
   ```
4. Title: "feat: implement [feature name]"
5. Assign reviewer or self-review
6. **CI/CD automatically runs** tests
7. Wait for tests to pass

**Step 9: Code Review Process**
- Reviewer checks:
  - Code quality and style
  - Tests passing
  - Matches spec requirements
  - No security vulnerabilities
  - Performance considerations
- Developer addresses feedback
- Reviewer approves when satisfied

**Step 10: Merge Implementation PR**
- Click "Merge pull request"
- Delete implementation branch
- **azure-deploy.yml triggers** - Website deploys
- **Both PRs appear in spec timeline!**

**Step 11: Cleanup Local Branches**
```bash
git checkout master
git pull origin master  # Get merged changes

# Delete local branches
git branch -d feat/YYYYMMDD-feature-name
git branch -d feat/YYYYMMDD-feature-name-impl
```

---

### Branch Naming Conventions

**For PM Work (Specs):**
```bash
feat/YYYYMMDD-feature-name      # Feature spec
fix/YYYYMMDD-bug-name           # Bug fix spec
docs/YYYYMMDD-doc-name          # Documentation spec
```

**For Developer Work (Implementation):**
```bash
feat/YYYYMMDD-feature-name-impl # Feature implementation
fix/YYYYMMDD-bug-name-impl      # Bug fix implementation
refactor/YYYYMMDD-cleanup       # Refactoring work
```

**Conventions:**
- Always start with type prefix: `feat/`, `fix/`, `docs/`, `refactor/`
- Always include spec date: `YYYYMMDD`
- Use kebab-case for descriptions: `user-authentication` not `userAuthentication`
- Keep branch names short but descriptive
- Add `-impl` suffix for implementation branches (optional but recommended)

---

### CI/CD Integration

**GitHub Actions Workflows:**

**1. build-and-test.yml (Runs on ALL PRs)**
```yaml
on:
  push:
    branches: [ master, main ]
  pull_request:
    branches: [ master, main ]
```

**What it does:**
- Installs dependencies
- Runs `build-specs.py` (processes specs)
- Builds MkDocs site with `--strict` mode
- Verifies no broken links
- Uploads build artifacts
- **Blocks merge if tests fail**

**2. azure-deploy.yml (Runs ONLY on master/main push)**
```yaml
on:
  push:
    branches: [ master, main ]
```

**What it does:**
- Only triggers after PR merge
- Builds complete site
- Deploys to Azure Static Web Apps
- Updates live website at kangxh.com

**Result:**
- Every PR is tested before merge
- Only merged code reaches production
- Broken code never reaches website

---

### Solo Developer Workflow with AI Assistants

**Scenario: Working on 3 Features Simultaneously**

```bash
# Feature 1: Claude Code generates authentication
git checkout -b feat/20260219-auth
# ... spec work ...
git push origin feat/20260219-auth
# Create PR #1 (spec), merge

git checkout master && git pull
git checkout -b feat/20260219-auth-impl
# ... AI generates auth code ...
git push origin feat/20260219-auth-impl
# Create PR #2 (impl), merge

# Feature 2: GitHub Copilot generates dashboard UI
git checkout master && git pull
git checkout -b feat/20260219-dashboard
# ... spec work ...
git push origin feat/20260219-dashboard
# Create PR #3 (spec), merge

git checkout master && git pull
git checkout -b feat/20260219-dashboard-impl
# ... AI generates dashboard ...
git push origin feat/20260219-dashboard-impl
# Create PR #4 (impl), merge

# Feature 3: Cursor AI refactors API
git checkout master && git pull
git checkout -b feat/20260219-api-refactor
# ... spec + impl in one branch ...
git push origin feat/20260219-api-refactor
# Create PR #5 (combined), merge
```

**Result:** Managing multiple features like a team, with AI as your "teammates"

---

### PR Template Usage

**Location:** `.github/pull_request_template.md`

**Template Structure:**
```markdown
## Spec Reference
**Spec ID**: <!-- Enter spec ID here, e.g., 20260219 -->

## Summary
Brief description of changes made in this PR.

## Changes
- [ ] Change 1
- [ ] Change 2

## Testing
Describe how you tested these changes.
```

**How to Fill:**
1. **Spec ID**: Required - Links PR to spec timeline
2. **Summary**: What was done (spec written or feature implemented)
3. **Changes**: Checklist of specific changes
4. **Testing**: How you verified it works

**Examples:**

*Spec PR:*
```markdown
**Spec ID**: 20260219

## Summary
Added specification for PR-based workflow documentation feature.

## Changes
- [x] Created 20260219-pr-workflow.md spec
- [x] Documented two-phase PR process
- [x] Added workflow diagrams
- [x] Included CI/CD integration details

## Testing
- Reviewed spec template compliance
- Verified YAML frontmatter is valid
- Checked all examples are accurate
```

*Implementation PR:*
```markdown
**Spec ID**: 20260219

## Summary
Implemented PR tracking system per spec 20260219.

## Changes
- [x] Added collect_pr_data() function
- [x] Enhanced timeline visualization
- [x] Added purple PR badges
- [x] Updated dashboard statistics

## Testing
- Created mock merge commit for PR detection
- Verified PRs appear in timeline
- Tested search index updates
- Confirmed CI/CD passes
```

---

### Verification Checklist

**Before Creating Spec PR:**
- [ ] Spec file created in `engineering/specs/YYYYMMDD-feature.md`
- [ ] YAML frontmatter is complete and valid
- [ ] Problem, solution, and success metrics are clear
- [ ] Spec follows template structure
- [ ] Branch name follows convention `feat/YYYYMMDD-feature`
- [ ] Commit message includes spec ID `(#YYYYMMDD)`

**Before Creating Implementation PR:**
- [ ] Spec has been merged to master
- [ ] Implementation branch created from updated master
- [ ] Code follows spec requirements
- [ ] Tests are written and passing locally
- [ ] Branch name follows convention `feat/YYYYMMDD-feature-impl`
- [ ] Commit messages include spec ID `(#YYYYMMDD)`

**Before Merging Any PR:**
- [ ] CI/CD tests are passing (green checkmark)
- [ ] All review comments addressed
- [ ] PR template is filled out completely
- [ ] Spec ID is correct

---

## Success Metrics

**Quantitative:**
- ✅ All new features use PR workflow
- ✅ CI/CD runs on 100% of PRs before merge
- ✅ Both spec and implementation PRs appear in timelines
- ✅ Zero direct commits to master (except emergency fixes)
- ✅ PR template filled out in all PRs

**Qualitative:**
- ✅ Clear separation between PM and dev work
- ✅ Code review process is consistent
- ✅ Professional Git practices demonstrated
- ✅ AI assistants can work in parallel on features
- ✅ Complete audit trail of all decisions

## Benefits

**For Solo Developers:**
- Work on multiple features simultaneously with AI assistants
- Maintain professional Git practices for portfolio
- Clear mental separation between PM and dev roles
- Self-review process catches issues early

**For Teams:**
- Clear handoff between PM and engineering
- Formal review and approval process
- Better communication through PR discussions
- Complete history of requirements and implementation

**For Portfolio/Job Search:**
- Demonstrates professional Git workflow
- Shows understanding of team collaboration
- PR history shows code quality standards
- Spec-driven approach shows PM skills

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Extra overhead for solo dev | Low | Worth it for portfolio and learning |
| Forgetting to fill PR template | Medium | CI/CD reminder step added |
| Confusion about which branch | Low | Clear naming conventions documented |
| Merge conflicts from parallel work | Medium | Regular syncs with master, small PRs |

## Future Enhancements

1. **Automated PR Validation** - Check PR description for spec ID
2. **Branch Protection Rules** - Require PR reviews in GitHub settings
3. **PR Status Badges** - Show open/closed/draft state in timeline
4. **Automated Branch Cleanup** - Auto-delete merged branches
5. **PR Templates by Type** - Different templates for specs vs implementations

## References

- GitHub Flow: https://guides.github.com/introduction/flow/
- PR Best Practices: https://github.com/features/code-review
- Git Branch Naming: https://www.conventionalcommits.org/
- NextPM PR Template: `.github/pull_request_template.md`

---

**Implementation Status:** ✅ Documented and Ready for Use
**Effective Date:** 2026-02-19 - All new specs use this workflow
