# 🤖 AI-Native Repository

## What Makes NextPM AI-Native?

NextPM is designed from the ground up for **human-AI collaboration**. This isn't just a repository with some AI tools bolted on—it's architected specifically to maximize productivity when humans and AI work together.

## Core Principles

### 1. **Rich Context for AI Assistants**

All context AI needs to be productive is organized in [`/ai-context/`](ai-context/):
- **Architecture**: System design and technical decisions
- **Conventions**: Coding and writing standards
- **PM Context**: Product goals, users, success metrics
- **Dev Context**: Tech stack, patterns, dependencies

**Why**: AI assistants work best with clear, structured context. Instead of repeatedly explaining the project, all context is pre-documented.

### 2. **Dual Documentation Philosophy**

NextPM documents from **two perspectives**:

#### PM View (`/docs/pm-workflows/`)
- Product thinking and strategy
- Spec writing with AI
- User research synthesis
- Feature evaluation

#### Dev View (`/docs/dev-workflows/`)
- How PMs can code with AI
- Cursor and GitHub Copilot for non-devs
- Understanding codebases
- Prototyping workflows

**Why**: As a PM learning to code with AI, I need both perspectives. Other PMs can learn from the PM view; AI assistants benefit from the dev view.

### 3. **Prompts as First-Class Artifacts**

The [`/prompts/`](prompts/) directory contains reusable prompt templates:
- Organized by PM workflow (spec writing, research, evaluation)
- Include context, examples, and expected outputs
- Version-controlled like code
- Searchable and forkable

**Why**: In AI-native work, prompts are as valuable as code. They're reusable tools that compound in value.

### 4. **Specifications Drive Development**

Every feature starts with a spec in [`/examples/pm-specs/`](examples/pm-specs/):
- **Before coding**: Write the spec with AI assistance
- **During coding**: AI uses spec as context
- **After shipping**: Spec becomes documentation

**Why**: Specs provide clear requirements for AI assistants and create alignment before writing code.

### 5. **Decision Documentation**

Architecture decisions are recorded in [`/meta/adr/`](meta/adr/) (Architecture Decision Records):
- **What** was decided
- **Why** this choice vs alternatives
- **Consequences** and trade-offs

**Why**: AI assistants can understand past decisions and maintain consistency. Future contributors (human or AI) understand the reasoning.

## AI Collaboration Patterns

### For AI Assistants Reading This

When working in this repository:

1. **Start with context**: Read [`/ai-context/README.md`](ai-context/README.md) first
2. **Check conventions**: Follow [`/ai-context/conventions.md`](ai-context/conventions.md)
3. **Understand goals**: Review [`/ai-context/pm-context.md`](ai-context/pm-context.md)
4. **Use prompts**: Reference [`/prompts/`](prompts/) for templates
5. **Document decisions**: Create ADRs in [`/meta/adr/`](meta/adr/) for significant choices

### For Human Developers/PMs

When working with AI on this project:

1. **Provide context**: Point AI to relevant `/ai-context/` files
2. **Use prompts**: Start with templates in `/prompts/` and customize
3. **Spec first**: Write specs before implementation
4. **Document decisions**: Create ADRs for architectural choices
5. **Update context**: Keep `/ai-context/` current as project evolves

## What AI-Native Looks Like in Practice

### Traditional Repo
```
"Write a spec for dark mode feature"
→ AI has no context
→ Generic, doesn't fit your style
→ Doesn't know your architecture
→ You spend time editing
```

### AI-Native Repo (NextPM)
```
"Write a spec using /prompts/pm/spec-writing/feature-spec.md
template for dark mode feature"
→ AI uses your template
→ Follows your conventions
→ Knows your tech stack from /ai-context/
→ Matches your style
→ 80% done on first try
```

## Measurable Benefits

| Aspect | Traditional | AI-Native (NextPM) |
|--------|-------------|-------------------|
| **AI context gathering** | 5-10 min per task | < 1 min (pre-documented) |
| **Prompt iteration** | 3-5 rounds | 1-2 rounds |
| **Consistency** | Varies per session | Maintained via conventions |
| **Onboarding** | AI starts from zero | AI reads `/ai-context/` |
| **Knowledge retention** | Lost between sessions | Persisted in repo |

## Evolution of AI-Native

This repository will evolve as I learn:

- **Phase 1** (Current): Basic AI-native structure
- **Phase 2**: Refined based on real usage patterns
- **Phase 3**: Advanced patterns (agents, automated workflows)

Each phase will be documented in [`/meta/retrospectives/`](meta/retrospectives/).

## Inspiration & Resources

- [Cursor Rules Collection](https://github.com/PatrickJS/awesome-cursorrules)
- [Simon Willison's AI-Assisted Development](https://simonwillison.net/tags/ai-assisted-programming/)
- [Anthropic Claude Prompt Engineering](https://docs.anthropic.com/claude/docs/prompt-engineering)

## Questions?

- **"Isn't this over-engineered?"**: Maybe! This is an experiment. I'll document what works and what doesn't.
- **"Do I need all this for my project?"**: No. Start simple. This repo shows the full spectrum of AI-native patterns.
- **"Is this just for PMs?"**: The dual-documentation approach is PM-focused, but principles apply to any role learning with AI.

---

**This document itself was written with AI assistance**, demonstrating the collaborative approach NextPM promotes. 🤖🤝👤
