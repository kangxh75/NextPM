# Feature Specifications

This folder contains **actual specifications for NextPM features**.

## Purpose

Document what we're building before we build it. Each spec should answer:
- **What** are we building?
- **Why** does it matter?
- **Who** is it for?
- **How** will we know it's successful?

## When to Create a Spec

Create a spec for:
- New features (any size)
- Significant refactors
- Architecture changes
- User-facing changes

Even small features benefit from 10 minutes of structured thinking.

## Spec Template

Use this basic structure:

```markdown
# [Feature Name]

## Overview
Brief 2-3 sentence summary.

## Problem
What problem does this solve? Why now?

## User Impact
Who benefits? How?

## Proposed Solution
High-level approach. What will we build?

## Success Metrics
How will we measure success?

## Implementation Notes
Technical considerations, dependencies, risks.

## Out of Scope
What we're explicitly NOT doing (for now).

## References
- Related specs
- Similar examples
- Useful resources
```

## Using AI to Write Specs

1. **Start with context** - Describe the problem and user need
2. **Use prompt templates** - Check `/prompts/pm/spec-writing/`
3. **Iterate** - Refine with AI assistance
4. **Validate** - Does it answer the key questions above?

## Example Specs

See `/examples/pm-specs/` for sanitized teaching examples.

## Naming Convention

- `feature-name-spec.md` or `feature-name.md`
- Use descriptive, hyphenated names
- Date prefix if needed: `2025-02-dark-mode-spec.md`

---

**Tip**: A good spec takes 15-30 minutes to write but saves hours of confusion later.
