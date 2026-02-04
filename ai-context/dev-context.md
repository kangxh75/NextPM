# Dev Context for AI Assistants

This file provides the **technical/development perspective** on NextPM. Read this to understand the tech stack, patterns, and architectural decisions.

## 🛠️ Tech Stack

### Phase 1: Static Site (Current)

**Frontend/Site Generator:**
- **MkDocs Material** (v9.5+)
  - Python-based static site generator
  - Material Design theme
  - Markdown for all content
  - Built-in search, navigation, code highlighting

**Hosting:**
- **Azure Static Web Apps** (Free tier)
  - Integrated with GitHub Actions
  - Custom domain: kangxh.com
  - SSL included
  - CDN for global performance

**CI/CD:**
- **GitHub Actions**
  - Auto-deploy on push to main
  - Build validation on PRs
  - Python linting (future)

**Development:**
- **Python 3.9+**
- **pip** for dependency management
- **Git** for version control

### Phase 2: Dynamic Site (Future)

**Backend:**
- **FastAPI** (modern, async Python framework)
  - RESTful API endpoints
  - Auto-generated OpenAPI docs
  - Pydantic for data validation

**Frontend Enhancement:**
- **HTMX** (progressive enhancement)
  - Add interactivity without SPA complexity
  - Server-side rendering maintained
  - Minimal JavaScript

**Database:**
- **Azure Cosmos DB** (Free tier: 1000 RU/s, 25GB)
  - NoSQL document store
  - Python SDK
  - Use cases: user accounts, saved prompts, usage tracking

**Infrastructure:**
- **Azure Static Web Apps** (frontend) + **Azure Functions** (API routes)
- Or **Azure Container Apps** (if more complex backend needed)

## 📁 Repository Structure

```
NextPM/
├── docs/                       # MkDocs source (Markdown)
│   ├── index.md               # Homepage
│   ├── pm-workflows/          # PM workflow guides
│   ├── dev-workflows/         # Dev guides for PMs
│   ├── prompts/               # Prompt library pages
│   └── examples/              # Case studies, specs
│
├── prompts/                   # Actual prompt templates (not docs)
│   ├── pm/
│   │   ├── spec-writing/     # Spec prompts
│   │   ├── user-research/    # Research prompts
│   │   └── evaluation/       # Evaluation prompts
│   └── dev/
│       ├── feature-implementation/
│       └── debugging/
│
├── examples/                  # Real PM artifacts
│   ├── pm-specs/             # Example specifications
│   │   └── nextpm-project-spec.md
│   ├── prototypes/           # Working demos (Phase 2)
│   └── evaluations/          # Product evaluation docs
│
├── ai-context/               # Context for AI assistants
│   ├── README.md
│   ├── pm-context.md        # Product perspective
│   ├── dev-context.md       # This file
│   ├── conventions.md       # Standards
│   └── architecture.md      # Design decisions
│
├── meta/                     # Project meta-documentation
│   ├── adr/                 # Architecture Decision Records
│   │   └── template.md
│   ├── roadmap.md
│   └── retrospectives/
│
├── scripts/                  # Utility scripts
│   ├── azure-setup.sh       # Azure deployment script
│   └── new-prompt.py        # Template for new prompts
│
├── static/                   # Static assets
│   ├── css/
│   ├── js/
│   └── images/
│
├── .github/
│   ├── workflows/
│   │   └── azure-static-web-apps.yml
│   └── copilot-instructions.md
│
├── .gitignore
├── .cursorrules             # Cursor AI rules
├── mkdocs.yml              # MkDocs configuration
├── requirements.txt        # Python dependencies
├── README.md
├── AI-NATIVE.md
└── LICENSE
```

## 🏗️ Architecture Patterns

### Content Architecture

**Separation of Concerns:**
- `/docs/` = User-facing documentation (rendered by MkDocs)
- `/prompts/` = Actual prompt templates (referenced by docs)
- `/examples/` = Real artifacts (specs, prototypes)
- `/ai-context/` = Context for AI assistants (not user-facing)
- `/meta/` = Project decisions (user-facing via site)

**Why this structure?**
- Clear separation makes it easier for AI to navigate
- Prompts are version-controlled like code
- Examples provide concrete references
- Meta documentation maintains decision history

### Documentation Pattern

**Every feature needs:**
1. **Spec** in `/examples/pm-specs/` (written BEFORE implementation)
2. **ADR** in `/meta/adr/` (for architectural decisions)
3. **Guide** in `/docs/` (user-facing documentation)
4. **Prompt** in `/prompts/` (if applicable)

### Code Style (Phase 2)

**Python (FastAPI backend):**
- Type hints everywhere
- Pydantic models for data
- Async/await for I/O
- Clear function names over comments

**HTMX (frontend enhancement):**
- Progressive enhancement
- Server-side rendering primary
- HTMX for interactive components
- Minimal custom JavaScript

## 🔧 Development Workflow

### Local Development

```bash
# Setup (first time)
cd C:\Projects\NextPM
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# Run local server
mkdocs serve
# Visit http://localhost:8000

# Build static site
mkdocs build
# Output in site/
```

### Content Creation

```bash
# Create new doc
# Add to docs/ folder
# Reference in mkdocs.yml nav

# Create new prompt template
# Add to prompts/ folder
# Document in docs/prompts/

# Test locally
mkdocs serve
```

### Deployment

**Phase 1 (Automated via GitHub Actions):**
```yaml
# .github/workflows/azure-static-web-apps.yml
# Triggers on push to main
# Builds MkDocs site
# Deploys to Azure Static Web Apps
```

**Manual deployment (if needed):**
```bash
# Build site
mkdocs build

# Deploy with Azure CLI
az staticwebapp deploy --app-name nextpm --source ./site
```

## 🎨 Design System

### MkDocs Material Theme Configuration

**Colors:**
- Primary: Indigo (#3F51B5)
- Accent: Indigo
- Light/Dark mode support

**Typography:**
- System fonts for performance
- Code: Monospace (JetBrains Mono preferred)

**Components:**
- Admonitions for callouts (tip, warning, example)
- Code blocks with copy button
- Mermaid diagrams for architecture
- Tabbed content for alternatives

### Content Conventions

**Markdown Extensions:**
- `pymdownx.highlight` for code blocks
- `pymdownx.superfences` for fenced code with features
- `pymdownx.emoji` for emoji support
- `admonition` for callout boxes
- `toc` for table of contents

**Front Matter (if needed in future):**
```yaml
---
title: Page Title
description: SEO description
tags: [ai, pm, productivity]
---
```

## 🔐 Security & Best Practices

### Phase 1 (Static Site)
- No backend = minimal attack surface
- HTTPS enforced (Azure Static Web Apps)
- No sensitive data in repo
- Content Security Policy headers

### Phase 2 (Dynamic Site)
- Environment variables for secrets (.env, never committed)
- Azure Key Vault for production secrets
- API rate limiting
- Input validation (Pydantic)
- CORS configuration
- Authentication via Azure AD B2C (if needed)

## 🚀 Performance

### Targets
- Lighthouse Score: 95+ (all categories)
- First Contentful Paint: < 1.5s
- Time to Interactive: < 3s
- Bundle size: Minimal (MkDocs Material is optimized)

### Optimizations
- Static site = fast by default
- Azure CDN for global distribution
- Image optimization (WebP, lazy loading)
- Minified CSS/JS (via mkdocs-minify-plugin)
- No client-side framework overhead

## 📦 Dependencies

### Core
- `mkdocs-material` - Theme and site generator
- `pymdown-extensions` - Enhanced Markdown features

### Plugins
- `mkdocs-minify-plugin` - Minify HTML
- `mkdocs-redirects` - Handle URL redirects

### Optional (for image optimization)
- `pillow` - Image processing
- `cairosvg` - SVG to PNG conversion

### Future (Phase 2)
- `fastapi` - Backend framework
- `uvicorn` - ASGI server
- `pydantic` - Data validation
- `azure-cosmos` - Cosmos DB SDK
- `python-dotenv` - Environment variables

## 🧪 Testing Strategy

### Phase 1
- Manual review of content
- Link checking (future)
- Build validation in CI

### Phase 2
- `pytest` for unit tests
- `httpx` for API testing
- Integration tests for key workflows
- Lighthouse CI for performance regression

## 📊 Monitoring & Analytics

### Phase 1
- Google Analytics (privacy-respecting)
- Azure Static Web Apps analytics
- GitHub traffic insights

### Phase 2
- Application Insights (Azure)
- Error tracking
- API usage metrics
- User behavior analytics

## 🔄 Migration Path (Static → Dynamic)

### Strategy
1. **Phase 1**: Pure static site, all content
2. **Phase 1.5**: Add static contact form (Azure Functions)
3. **Phase 2**: Add user accounts, saved prompts
4. **Phase 2.5**: Add interactive tools (spec generator, etc.)
5. **Phase 3**: Full dynamic features

### Technical Approach
- Keep `/docs` as static site
- Add `/api` for backend endpoints
- HTMX for progressive enhancement
- No client-side framework migration (avoid rewrite)

## 🛠️ Tools & IDE Setup

### Recommended
- **VS Code** with extensions:
  - Python
  - Markdown All in One
  - MkDocs Material
  - GitHub Copilot
- **Cursor** for AI-assisted editing
- **Git** with GitHub CLI (`gh`)

### Author's Setup
- Windows 11
- Python 3.9+
- VS Code + Cursor
- GitHub Copilot via enterprise account
- Azure CLI for deployment

## 📝 Code Review Standards

### What to Check
- ✅ Follows conventions.md
- ✅ Has corresponding spec/ADR
- ✅ Documentation updated
- ✅ Builds locally without errors
- ✅ PM-friendly language (for docs)
- ✅ No secrets committed

### What AI Reviewers Should Note
- Keep complexity low (author is learning)
- Explain non-obvious patterns
- Suggest improvements with reasoning
- Link to relevant docs/conventions

## 🎓 Learning Resources

### For Author (PM Learning Dev)
- [MkDocs Material Docs](https://squidfunk.github.io/mkdocs-material/)
- [FastAPI Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Azure Static Web Apps Docs](https://learn.microsoft.com/azure/static-web-apps/)
- [HTMX Examples](https://htmx.org/examples/)

### For Contributors
- [AI-NATIVE.md](../AI-NATIVE.md) - AI-native principles
- [pm-context.md](pm-context.md) - Product perspective
- [conventions.md](conventions.md) - Standards

---

**For AI Assistants**: This context helps you make technically sound decisions while keeping the author's learning goals in mind. Balance best practices with simplicity and clear explanations.
