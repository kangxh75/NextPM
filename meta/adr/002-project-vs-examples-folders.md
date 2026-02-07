# ADR 002: Project vs Examples Folder Structure

**Status:** Accepted
**Date:** 2026-02-04
**Author:** Kang (with AI assistance from Claude Code)

## Context

NextPM serves dual purposes:
1. **Working repository** for building the NextPM product itself
2. **Teaching resource** demonstrating AI-augmented PM workflows

This creates a unique requirement: we need to track our own development process (specs, tasks, validations) while also providing sanitized examples for educational purposes.

**Problem:** Where should we store NextPM's own development artifacts vs. teaching materials for users?

## Decision

We will use **two separate top-level folders** with distinct purposes:

**`/project/`** - NextPM's own development artifacts
- `project/specs/` - Real feature specifications for NextPM
- `project/tasks/` - Task breakdowns for actual work
- `project/validations/` - Validation documentation for completed work

**`/examples/`** - Teaching materials for users
- `examples/pm-specs/` - Sanitized example specifications (teaching)
- `examples/evaluations/` - Example product evaluations
- `examples/prototypes/` - Working demo projects

## Rationale

### Pros
1. **Clear separation**: Working files vs teaching materials are distinct
2. **Clean documentation**: Users see polished examples, not messy reality
3. **Authentic development**: We can document real work without cleanup
4. **Dual value**: Repository is both product AND case study
5. **Meta-documentation**: Process itself becomes learning material
6. **Flexibility**: Can iterate on real work without affecting examples

### Cons
1. **Duplication risk**: Might need to sanitize project/ content for examples/
2. **Maintenance overhead**: Two sets of similar content to maintain
3. **Confusion potential**: Contributors might not know which folder to use
4. **Extra structure**: Adds complexity to repository organization

### Alternatives Considered

#### Alternative 1: Single `/specs/` folder for everything
- **Pros**: Simpler structure, no duplication
- **Cons**: Mixes working files with teaching materials, harder to keep examples clean
- **Rejected because**: Conflates two distinct purposes

#### Alternative 2: Put everything in `/project/`, curate `/examples/` from it
- **Pros**: Single source of truth, examples derived from real work
- **Cons**: Still need separation, `/project/` could get messy
- **Rejected because**: Doesn't solve the core separation problem

#### Alternative 3: Use `/work/` instead of `/project/`
- **Pros**: Shorter name, clear purpose
- **Cons**: Less descriptive than "project," could be confused with temporary work
- **Rejected because**: "project" better conveys "this project's artifacts"

#### Alternative 4: No `/project/` folder, use `/meta/` for development docs
- **Pros**: Leverages existing `/meta/` folder
- **Cons**: `/meta/` is for strategic decisions (ADRs, retrospectives), not tactical work
- **Rejected because**: Specs and tasks aren't meta-level documentation

## Implementation

### Folder Structure

```
NextPM/
├── project/              # NextPM's development artifacts
│   ├── specs/           # Real feature specs
│   │   ├── README.md
│   │   └── 0.00-project-start.md
│   ├── tasks/           # Task breakdowns
│   │   └── README.md
│   └── validations/     # Validation docs
│       └── README.md
│
├── examples/            # Teaching materials
│   ├── pm-specs/       # Example specifications
│   ├── evaluations/    # Example evaluations
│   └── prototypes/     # Demo projects
│
└── meta/                # Strategic documentation
    ├── adr/            # Architecture decisions
    └── retrospectives/ # Process reflections
```

### Usage Guidelines

**When to use `/project/`:**
- Writing specs for NextPM features
- Breaking down tasks for implementation
- Documenting validation of completed work
- Real, messy, in-progress work

**When to use `/examples/`:**
- Creating teaching materials for users
- Sanitizing real specs for educational use
- Building demo projects
- Polished, curated content

**When to use `/meta/`:**
- Architecture Decision Records (ADRs)
- Sprint/phase retrospectives
- High-level project reflections
- Strategic thinking documents

### Workflow

1. **Do real work** in `/project/`
   - Write spec → `project/specs/feature-name.md`
   - Break into tasks → `project/tasks/feature-name-tasks.md`
   - Implement using AI assistants
   - Validate → `project/validations/feature-name-validation.md`

2. **Extract learnings** to `/examples/`
   - Sanitize successful specs
   - Create generalized templates
   - Build reusable examples
   - Remove project-specific details

3. **Document decisions** in `/meta/`
   - Create ADRs for architectural choices
   - Write retrospectives on process
   - Reflect on what worked/didn't

## Consequences

### Positive
- ✅ Clear mental model: working files vs teaching materials
- ✅ Authentic development process documented
- ✅ Clean examples for users without clutter
- ✅ Repository demonstrates its own principles
- ✅ Easy to explain to AI assistants and collaborators

### Negative
- ⚠️ Need to maintain two sets of content
- ⚠️ Risk of letting examples become stale
- ⚠️ Requires discipline to sanitize project/ content for examples/

### Neutral
- May need periodic "cleanup" to move polished project/ items to examples/
- Good candidates for examples/ can emerge organically from project/ work

## Compliance

This decision is documented in:
- `/ai-context/conventions.md` - Project folders section
- `/project/README.md` - Folder structure explanation
- `/examples/README.md` - Purpose and usage (to be created)
- This ADR

## Related Decisions

- Complements ADR 001 (folder prefix strategy)
- `/meta/` remains separate for strategic documentation
- May inform future Phase 2 folder organization

## Review Date

**Next review:** End of Phase 1 (estimated March 2026)

**Review criteria:**
- Has separation been maintained effectively?
- Is `/examples/` being populated from `/project/`?
- Has the dual-folder approach caused confusion?

## Notes

- Implementation completed 2026-02-04
- First spec created: `project/specs/0.00-project-start.md`
- README files added to all subfolders for guidance
- AI context updated to reflect structure

---

**Status History:**
- 2026-02-04: Proposed and Accepted
- Implementation: Completed 2026-02-04
