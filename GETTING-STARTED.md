# Getting Started with NextPM

Welcome! Your NextPM project is now set up and ready to use. Here's everything you need to know to start working on it.

## 📁 Project Location

```
C:\Projects\NextPM
```

## ✅ What's Been Set Up

### Project Structure
- ✅ Complete AI-native repository structure
- ✅ MkDocs Material configuration
- ✅ AI context documentation for assistants
- ✅ Sample prompt template (PRD)
- ✅ Initial homepage and workflow docs
- ✅ Git repository initialized with first commit

### Files Created

**Core Configuration:**
- `README.md` - Project overview
- `AI-NATIVE.md` - AI-native philosophy and approach
- `mkdocs.yml` - Site configuration
- `requirements.txt` - Python dependencies
- `.gitignore` - Git ignore patterns

**AI Context (`/ai-context/`):**
- `README.md` - Quick start for AI assistants
- `pm-context.md` - Product perspective (goals, users, metrics)
- `dev-context.md` - Technical perspective (stack, architecture)
- `conventions.md` - Coding and writing standards

**Content (`/docs/`):**
- `index.md` - Homepage
- `pm-workflows/index.md` - PM workflows overview

**Prompts (`/prompts/`):**
- `pm/spec-writing/prd-template.md` - PRD prompt template (example)

## 🚀 Next Steps

### 1. View the Site Locally

```bash
cd C:\Projects\NextPM
mkdocs serve
```

Then open http://localhost:8000 in your browser.

**To stop the server:** Press `Ctrl+C` in the terminal

### 2. Create Content

You now have a working foundation! Here are suggested next steps:

#### Week 1: Core Content
- [ ] Write first workflow guide: `docs/pm-workflows/spec-writing.md`
- [ ] Create 2-3 more prompt templates in `/prompts/pm/spec-writing/`
- [ ] Write your first case study (use NextPM itself as example!)

#### Week 2: Expand Library
- [ ] Add user research prompts
- [ ] Add evaluation prompts
- [ ] Create dev workflows for PMs content

#### Week 3: Polish & Deploy
- [ ] Complete all placeholder content
- [ ] Test all links
- [ ] Set up GitHub repository (when personal account ready)
- [ ] Deploy to Azure Static Web Apps

### 3. Daily Workflow

**Creating New Content:**

```bash
# 1. Navigate to project
cd C:\Projects\NextPM

# 2. Create your markdown file
# docs/pm-workflows/new-guide.md
# prompts/pm/category/new-prompt.md

# 3. Add to mkdocs.yml navigation (if needed)

# 4. Preview locally
mkdocs serve

# 5. Commit when satisfied
git add .
git commit -m "feat(docs): add new workflow guide"
```

**Working with AI Assistants:**

When asking Claude/ChatGPT/Cursor for help:
1. Point them to `/ai-context/README.md` first
2. Reference specific context files as needed
3. Ask them to follow `/ai-context/conventions.md`

Example prompt:
```
I'm working on the NextPM project at C:\Projects\NextPM.
Please read /ai-context/README.md for project context.

I want to create a new workflow guide for user research synthesis.
Follow the conventions in /ai-context/conventions.md.
```

## 📝 Content Creation Templates

### New Workflow Guide

Create in `/docs/pm-workflows/[name].md`:

```markdown
# [Workflow Name]

Brief description of what this workflow accomplishes.

## Overview
- What this workflow solves
- When to use it
- Expected time savings

## Traditional Approach
How you currently do this, pain points

## AI-Assisted Approach
Step-by-step with prompts

## Real Example
Actual usage with results

## Key Takeaways
- Bullet points
- Lessons learned
```

### New Prompt Template

Create in `/prompts/[pm|dev]/[category]/[name].md`:

````markdown
# [Prompt Name]

## Purpose
What this prompt helps accomplish

## When to Use
Specific scenarios

## Context Required
What info you need first

## The Prompt
```
[The actual prompt with {placeholders}]
```

## Example Usage
Input and expected output

## Tips
Helpful hints

## Variations
How to adapt
````

## 🛠️ Common Tasks

### Build the Site

```bash
cd C:\Projects\NextPM
mkdocs build
# Output in /site directory
```

### Check for Broken Links

```bash
# Install linkchecker (once)
pip install linkchecker

# Check links
linkchecker http://localhost:8000
```

### Update Dependencies

```bash
pip install --upgrade -r requirements.txt
```

## 📤 When Your GitHub Account is Ready

### 1. Create Remote Repository

```bash
# Authenticate with personal account
gh auth login

# Create repository
gh repo create NextPM --public --description "AI-Native PM Knowledge Hub"

# Add remote
git remote add origin https://github.com/YOUR_USERNAME/NextPM.git

# Push
git push -u origin master
```

### 2. Update Configuration

Update these files with your GitHub username:
- `mkdocs.yml` - Replace `YOUR_USERNAME` in `repo_url`
- `docs/index.md` - Update GitHub links

### 3. Set Up Azure Deployment

(Full guide will be created later, but you'll need:)
1. Azure Static Web Apps resource
2. GitHub Actions workflow
3. Azure deployment token as GitHub secret

## 🎓 Learning Resources

### MkDocs Material
- [Official Docs](https://squidfunk.github.io/mkdocs-material/)
- [Getting Started](https://squidfunk.github.io/mkdocs-material/getting-started/)
- [Reference](https://squidfunk.github.io/mkdocs-material/reference/)

### Markdown Guide
- [Basic Syntax](https://www.markdownguide.org/basic-syntax/)
- [Extended Syntax](https://www.markdownguide.org/extended-syntax/)
- [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/)

### Git Basics
- [Git Handbook](https://guides.github.com/introduction/git-handbook/)
- [Commit Message Conventions](https://www.conventionalcommits.org/)

## 🤝 Getting Help

### From AI Assistants
Point them to:
1. `/ai-context/README.md` - Project overview
2. `/ai-context/pm-context.md` - Product goals
3. `/ai-context/dev-context.md` - Technical details
4. `/ai-context/conventions.md` - Standards

### From Documentation
- This file for getting started
- `README.md` for project overview
- `AI-NATIVE.md` for philosophy
- `/ai-context/` for detailed context

## 📊 Project Status

**Phase:** Phase 1 - Foundation Complete ✅

**Next Milestones:**
1. Create 3 workflow guides
2. Build prompt library (10+ templates)
3. Write first case study
4. Deploy to GitHub
5. Deploy to Azure + kangxh.com

**Current Git Status:**
- Branch: `master`
- Commits: 1 (initial commit)
- Remote: Not yet configured (waiting for personal GitHub account)

## 🎯 Your First Task

Suggested first task to practice the workflow:

**Create a case study of building NextPM itself!**

1. Create `examples/pm-specs/nextpm-project-spec.md`
2. Write the spec for this project (dogfooding!)
3. Use the PRD template you already have in `/prompts/`
4. Document: goals, users, success metrics, approach
5. This becomes your first real example!

This demonstrates:
- ✅ Using AI to write specs
- ✅ Following your own templates
- ✅ Creating real examples
- ✅ Practicing what you preach

## ✨ Tips for Success

1. **Commit Often**: Small, focused commits are better than big ones
2. **Use the Templates**: Follow the conventions you've set up
3. **Test Locally**: Always preview with `mkdocs serve` before committing
4. **Document Decisions**: Add ADRs (Architecture Decision Records) for important choices
5. **Start Small**: One workflow at a time, build momentum

## 🎉 You're Ready!

Everything is set up. The foundation is solid. Now it's time to create content and practice AI-augmented PM workflows.

Start with `mkdocs serve` and begin writing! 🚀

---

**Questions?** All the context is in `/ai-context/`. Ask your AI assistant for help, and point them there first.
