# NextPM 🤖

**AI-Native PM Knowledge Hub** - Next-generation product management workflows and practices

[![AI-Native](https://img.shields.io/badge/AI-Native-blue.svg)](AI-NATIVE.md)
[![MkDocs Material](https://img.shields.io/badge/MkDocs-Material-526CFE.svg)](https://squidfunk.github.io/mkdocs-material/)
[![Azure Static Web Apps](https://img.shields.io/badge/Azure-Static%20Web%20Apps-0078D4.svg)](https://azure.microsoft.com/services/app-service/static/)

## 🎯 What is NextPM?

NextPM is a living laboratory for **AI-augmented Product Management**. This repository serves three purposes:

1. **Knowledge Hub**: Documenting how PMs can 10x productivity with AI tools
2. **Prompt Library**: Reusable templates for specs, research, evaluation, and prototyping
3. **Living Example**: This project itself demonstrates AI-native PM practices

## 🤖 AI-Native Repository

This is an **AI-native repository** designed for human-AI collaboration. See [AI-NATIVE.md](AI-NATIVE.md) for details on:
- How AI assistants should work with this codebase
- Dual documentation philosophy (PM + Dev perspectives)
- AI collaboration principles

**For AI Assistants**: Start with [`/ai-context/README.md`](ai-context/README.md)

## 📚 Content Structure

```
NextPM/
├── docs/               # MkDocs site content
│   ├── pm-workflows/  # PM practices with AI
│   └── dev-workflows/ # Dev practices for PMs
├── prompts/           # Prompt library (PM artifacts)
│   ├── pm/           # PM-specific prompts
│   └── dev/          # Dev prompts for PMs
├── examples/          # Real PM artifacts
│   ├── pm-specs/     # Example specifications
│   ├── prototypes/   # Working demos
│   └── evaluations/  # Product evaluations
├── ai-context/        # Context for AI assistants
└── meta/             # Project meta-documentation
    └── adr/          # Architecture Decision Records
```

## 🚀 Quick Start

### Prerequisites

- Python 3.9+
- pip or Poetry

### Local Development

```bash
# Install dependencies
pip install -r requirements.txt

# Serve documentation locally
mkdocs serve

# Visit http://localhost:8000
```

## 🎓 Who is This For?

- **Mid-Senior PMs** curious about AI-augmented workflows
- **Non-technical PMs** wanting to prototype and "speak dev"
- **AI-curious PMs** looking for practical, actionable guidance
- **Product teams** exploring AI integration in their workflow

## 🌟 Key Features

### For Product Managers
- ✅ Real PM workflows with AI tools (Claude, ChatGPT, Cursor)
- ✅ Copy-paste prompt templates for common PM tasks
- ✅ Case studies with measurable outcomes
- ✅ From PM perspective, not dev-heavy

### For AI Assistants
- ✅ Rich context in `/ai-context/` directory
- ✅ Dual documentation (PM + Dev views)
- ✅ Every feature has a spec
- ✅ Decisions documented in ADRs

## 📖 Documentation

- **Live Site**: Coming soon to kangxh.com
- **Local Docs**: Run `mkdocs serve`
- **AI Context**: See [ai-context/README.md](ai-context/README.md)

## 🛠️ Tech Stack

- **Static Site**: MkDocs Material (Phase 1)
- **Backend**: FastAPI + HTMX (Phase 2)
- **Database**: Cosmos DB (Free tier)
- **Hosting**: Azure Static Web Apps
- **CI/CD**: GitHub Actions

## 🗺️ Roadmap

**Phase 1: Static Knowledge Hub** (Current)
- [x] AI-native repository structure
- [ ] Core PM workflow documentation
- [ ] Prompt library with 10+ templates
- [ ] 3 real case studies
- [ ] Deploy to kangxh.com

**Phase 2: Dynamic Features**
- [ ] Interactive PM tools
- [ ] User authentication
- [ ] Tool usage tracking
- [ ] Community contributions

See [meta/roadmap.md](meta/roadmap.md) for details.

## 🤝 Contributing

This is a personal learning project, but ideas and feedback are welcome! Once the personal GitHub account is set up, contribution guidelines will be added.

## 📄 License

MIT License - See [LICENSE](LICENSE) for details

## 👤 Author

**Kang** - Product Manager exploring AI-native workflows

- Website: [kangxh.com](https://kangxh.com) (coming soon)
- Focus: AI-augmented PM practices

---

**Built with AI assistance** - This project practices what it preaches! 🚀
