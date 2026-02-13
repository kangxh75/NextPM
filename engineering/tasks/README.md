# Task Breakdowns

This folder contains **task breakdowns for NextPM features**.

## Purpose

Convert specifications into actionable tasks that can be assigned to AI coding assistants (GitHub Copilot, Cursor, Claude Code) or tracked manually.

## When to Create Task Breakdowns

After writing a spec in `/specs/`, break it down into:
- Specific, actionable tasks
- Logical implementation order
- Clear acceptance criteria

## Task Breakdown Template

```markdown
# [Feature Name] - Tasks

**Spec:** Link to `/specs/[feature-name].md`

## Task List

### 1. [Task Name]
**Description:** What needs to be done

**Acceptance Criteria:**
- [ ] Criterion 1
- [ ] Criterion 2

**Files to Modify:**
- `path/to/file.py`

**AI Assistant:** GitHub Copilot / Cursor / Claude Code

**Status:** Not Started / In Progress / Done

---

### 2. [Next Task]
...
```

## Task Granularity

**Good task size:**
- Can be completed in one focused session
- Has clear start and end points
- Can be validated independently

**Too large:** "Implement dark mode" → Break into smaller tasks
**Too small:** "Add comma to line 42" → Combine with related work

## Workflow

1. **Write spec** → `/specs/`
2. **Break down tasks** → `/tasks/` (this folder)
3. **Assign to AI** → Use AI coding assistants
4. **Track progress** → Update task status
5. **Validate** → Document in `/validations/`

## Using AI for Task Breakdown

AI can help break down specs into tasks:

```
I have this spec: [paste spec]

Break this into specific, actionable tasks for implementation.
For each task, include:
- What needs to be done
- Which files will be affected
- Acceptance criteria
```

## Naming Convention

Match the related spec:
- Spec: `dark-mode-feature.md`
- Tasks: `dark-mode-tasks.md`

## Task Status Tracking

Use simple status markers:
- ⏳ Not Started
- 🚧 In Progress
- ✅ Done
- ❌ Blocked

Or GitHub-style checkboxes:
- [ ] Not done
- [x] Done

---

**Tip**: Good task breakdowns make AI coding assistants 10x more effective. Be specific!
