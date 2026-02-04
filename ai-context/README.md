# AI Context - Quick Start for AI Assistants

Welcome! This directory contains all the context you need to effectively work on the NextPM project.

## 🎯 Project Overview

**NextPM** is an AI-native knowledge hub for Product Managers learning to 10x their productivity with AI tools. The author (Kang) is a PM, not a developer, using this project to practice AI-augmented PM workflows.

## 📋 Read These Files First

1. **[pm-context.md](pm-context.md)** - Product perspective: goals, users, success metrics
2. **[dev-context.md](dev-context.md)** - Technical perspective: stack, patterns, architecture
3. **[conventions.md](conventions.md)** - Coding and writing standards
4. **[architecture.md](architecture.md)** - System design and technical decisions

## 🚀 Quick Context

### What is This Project?

- **Type**: Static documentation site (MkDocs Material) → Dynamic site (FastAPI + HTMX in Phase 2)
- **Purpose**: Document AI PM workflows, provide reusable prompt templates, showcase real examples
- **Audience**: Mid-senior PMs curious about AI tools
- **Unique Angle**: Dual documentation from PM AND dev perspectives

### Project Structure

```
NextPM/
├── mkdocs-docs/       # MkDocs site content
│   ├── pm-workflows/  # How PMs use AI (target audience)
│   └── dev-workflows/ # How PMs learn dev with AI (meta)
├── prompts/           # Reusable prompt templates (core value)
├── examples/          # Teaching materials (sanitized examples)
├── project/           # NextPM's own development artifacts
│   ├── specs/        # Feature specifications
│   ├── tasks/        # Task breakdowns
│   └── validations/  # Test results and validation
├── meta/             # Architecture decisions and retrospectives
└── ai-context/       # YOU ARE HERE - Context for AI
```

### Current Phase

**Phase 1: Static Knowledge Hub**
- Building MkDocs Material site
- Creating prompt library
- Writing workflow documentation
- Preparing for deploy to Azure Static Web Apps at kangxh.com

### Author's Context

- **Role**: Product Manager
- **Dev Experience**: Learning to code with AI assistance
- **AI Tools Used**: Claude (primary), ChatGPT, Cursor, GitHub Copilot
- **Goal**: Practice AI-augmented PM work and share learnings

## 🤖 How to Help

### When Coding
- Keep code simple - author is learning
- Explain technical decisions
- Prefer well-documented patterns over clever solutions
- Python style: readable > performant (unless critical)

### When Writing
- PM-friendly language (avoid unnecessary jargon)
- Include practical examples
- Show before/after comparisons
- Emphasize outcomes and time saved

### When Making Decisions
- Document in `/meta/adr/` (Architecture Decision Records)
- Consider both PM and dev perspectives
- Prefer maintainable over cutting-edge
- Azure-friendly (MSDN subscription available)

## 📚 Key Files to Reference

- **Prompts**: Check `/prompts/` for existing templates before creating new ones
- **Conventions**: Follow `/ai-context/conventions.md` for consistency
- **Specs**: Every feature should have a spec in `/examples/pm-specs/`
- **ADRs**: Check `/meta/adr/` for past architectural decisions

## 🎯 Success Criteria

You're being helpful when:
- ✅ Solutions are simple and well-explained
- ✅ Decisions are documented
- ✅ Patterns are consistent with existing code
- ✅ Documentation is PM-friendly
- ✅ Changes align with project goals (see pm-context.md)

## 🔗 Related Files

- [../AI-NATIVE.md](../AI-NATIVE.md) - AI-native philosophy and principles
- [../README.md](../README.md) - Project overview for humans
- [conventions.md](conventions.md) - Detailed coding/writing standards

---

**Remember**: This project is both a learning journey AND a product. Help the author learn while building something valuable for other PMs. 🚀
