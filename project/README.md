# Project Development Artifacts

This folder contains **NextPM's own development process documentation**. Unlike `/examples/` (which contains teaching materials for users), this folder tracks the **actual work** of building NextPM itself.

## Purpose

Document the AI-augmented PM workflow in action:
- **Spec** → **Task Breakdown** → **Implementation** → **Validation**

This folder serves dual purposes:
1. **Working directory** for active development
2. **Case study** demonstrating AI-native PM practices

## Folder Structure

```
project/
├── specs/          # Feature specifications (WHAT we're building)
├── tasks/          # Task breakdowns (HOW we break down work)
└── validations/    # Test results and validation docs (PROOF it works)
```

## Workflow

### 1. Start with a Spec
Create a specification in `/specs/` using AI assistance (Claude, ChatGPT, etc.)

**Example:** `specs/dark-mode-feature.md`

### 2. Break Down into Tasks
Convert the spec into actionable tasks in `/tasks/`

**Example:** `tasks/dark-mode-tasks.md`

### 3. Implement
Assign tasks to AI coding assistants (GitHub Copilot, Cursor, Claude Code)

### 4. Validate
Document testing and validation in `/validations/`

**Example:** `validations/dark-mode-test-results.md`

## Naming Conventions

**Use descriptive, hyphenated names:**
- ✅ `dark-mode-feature.md`
- ✅ `search-functionality-spec.md`
- ❌ `feature1.md`
- ❌ `spec.md`

**Keep related files linked:**
```
specs/dark-mode-feature.md
tasks/dark-mode-tasks.md
validations/dark-mode-validation.md
```

## Relationship to Other Folders

- **`/meta/`** - Strategic decisions and retrospectives (WHY and HOW we work)
- **`/project/`** - Tactical feature work (WHAT we're building)
- **`/examples/`** - Teaching materials for users (sanitized examples)
- **`/ai-context/`** - Context for AI assistants

## Tips

1. **Write specs before coding** - Even simple features benefit from structured thinking
2. **Link between documents** - Reference related specs, tasks, and validations
3. **Use AI at every step** - Spec writing, task breakdown, validation planning
4. **Reflect on outcomes** - Note what worked and what didn't
5. **Sanitize for examples** - Good specs/workflows can be adapted into `/examples/`

---

**Remember**: This folder is both a working directory AND documentation of your AI-augmented PM process. Write as if teaching others while doing real work.
