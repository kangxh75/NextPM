# Conventions - Coding and Writing Standards

This file defines the standards for code, documentation, and prompts in the NextPM repository.

## 📝 Writing Conventions

### Documentation (Markdown)

**File Naming:**
- Use lowercase with hyphens: `spec-writing.md`, `cursor-for-pm.md`
- Be descriptive: `ai-native-pm.md` not `pm.md`
- Date-based for retrospectives: `2025-01-retro.md`

**Document Structure:**
```markdown
# Title (H1 - only one per document)

Brief introduction (2-3 sentences).

## Section (H2)

Content with clear paragraphs.

### Subsection (H3)

More specific content.

## Key Takeaways (at end)

- Bulleted summary
- 3-5 key points
```

**Voice and Tone:**
- **Active voice**: "Use Claude to write specs" not "Specs can be written using Claude"
- **Second person**: "You can..." not "One can..." or "We can..."
- **Conversational but professional**: Like talking to a colleague
- **Avoid jargon**: Or explain it when necessary
- **Be specific**: "30% time savings" not "significant savings"

**PM-Friendly Language:**
- ❌ "Instantiate a FastAPI route handler"
- ✅ "Create an API endpoint"

- ❌ "Leverage the LLM's context window"
- ✅ "Use Claude's conversation memory"

**Code Examples:**
Always include:
- Language identifier: ` ```python ` not just ` ``` `
- Comments explaining key parts
- Context before the code block

```python
# Example: Basic FastAPI endpoint
# This creates a simple API route that returns JSON

from fastapi import FastAPI

app = FastAPI()

@app.get("/hello")
async def hello():
    return {"message": "Hello, NextPM!"}
```

**Admonitions (Callouts):**
```markdown
!!! tip "Pro Tip"
    Use this pattern to highlight helpful shortcuts.

!!! warning "Watch Out"
    Use this for common pitfalls.

!!! example "Real Example"
    Use this for concrete examples.

!!! note
    Use this for additional context.
```

### Prompt Templates

**File Naming:**
- Descriptive: `prd-template.md`, `user-story-generator.md`
- Location: `/prompts/{pm|dev}/{category}/`

**Structure:**
````markdown
# [Prompt Name]

## Purpose
What this prompt helps you accomplish.

## When to Use
Specific scenarios where this prompt is useful.

## Context Required
What information you need before using this prompt.

## The Prompt

```
[The actual prompt template with {placeholders}]
```

## Example Usage

**Input:**
[Show what you'd fill in]

**Output:**
[Show expected result]

## Tips
- Tip 1
- Tip 2

## Variations
- How to adapt for different scenarios
````

### Case Studies

**Structure:**
```markdown
# [Feature/Task Name]: AI-Assisted Approach

## Context
- What was the task?
- Why was it needed?
- What was the starting point?

## Traditional Approach
- How this would typically be done
- Estimated time
- Pain points

## AI-Assisted Approach
- Tools used (Claude, Cursor, etc.)
- Workflow steps
- Actual time taken
- Prompts used (link to /prompts/)

## Results
- **Time Saved**: X hours (X% reduction)
- **Quality**: [Improvements or trade-offs]
- **Learnings**: What worked, what didn't

## Would I Do It Again?
Honest reflection on whether this approach is worth it.
```

## 💻 Code Conventions

### Python Style

**General:**
- Follow PEP 8
- Use type hints
- Max line length: 100 characters
- Use f-strings for formatting

```python
# Good
def calculate_time_saved(original: int, optimized: int) -> float:
    """Calculate percentage of time saved."""
    return ((original - optimized) / original) * 100

# Avoid
def calc(o, n):
    return ((o - n) / o) * 100  # What does this do?
```

**Naming:**
- Functions/variables: `snake_case`
- Classes: `PascalCase`
- Constants: `UPPER_SNAKE_CASE`
- Private: `_leading_underscore`

```python
# Good
MAX_PROMPTS = 50

class PromptTemplate:
    def __init__(self, name: str):
        self._name = name

    def generate_output(self) -> str:
        return f"Template: {self._name}"

# Avoid
maxPrompts = 50

class prompt_template:
    def __init__(self, n):
        self.n = n
```

**Documentation:**
```python
def write_spec_with_ai(
    feature_name: str,
    context: str,
    template: str = "default"
) -> str:
    """
    Generate a product spec using AI assistance.

    Args:
        feature_name: Name of the feature to spec
        context: Background information and requirements
        template: Prompt template to use (default: "default")

    Returns:
        Generated specification as markdown string

    Example:
        >>> spec = write_spec_with_ai(
        ...     "Dark Mode",
        ...     "Users want dark mode for night usage",
        ...     "feature-spec"
        ... )
    """
    pass
```

**Imports:**
```python
# Order: stdlib, third-party, local
import os
from typing import Dict, List

from fastapi import FastAPI
from pydantic import BaseModel

from .models import User
from .utils import format_prompt
```

### YAML (Configuration)

**MkDocs Configuration:**
```yaml
# Group related settings
site_name: NextPM
site_description: Brief description
site_author: Kang

# Theme configuration
theme:
  name: material
  palette:
    primary: indigo
  features:
    - navigation.tabs
    - search.suggest

# Keep alphabetically sorted within groups
plugins:
  - minify
  - search
```

### Git Conventions

**Commit Messages:**
```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types:**
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting (not code style)
- `refactor`: Code restructuring
- `test`: Adding tests
- `chore`: Maintenance tasks

**Examples:**
```
feat(prompts): add PRD template for new features

Added comprehensive PRD template in /prompts/pm/spec-writing/.
Includes sections for goals, success metrics, and user stories.

Closes #12

---

docs(workflows): update spec-writing guide with Claude examples

Added real examples of using Claude for spec writing.
Includes before/after comparison and time savings data.

---

chore: update mkdocs-material to v9.5.3
```

**Branch Naming:**
- `feat/add-prd-template`
- `fix/broken-link-in-docs`
- `docs/update-readme`

### File Organization

**Keep Related Files Together:**
```
prompts/pm/spec-writing/
├── README.md              # Overview of spec-writing prompts
├── prd-template.md        # Full PRD template
├── user-story.md          # User story generator
└── one-pager.md           # Executive summary template
```

**READMEs Everywhere:**
Every directory should have a README explaining:
- What's in this directory
- How files are organized
- How to add new content

## 🤖 AI-Specific Conventions

### .cursorrules

```markdown
# NextPM - Cursor AI Rules

## Project Context
- PM knowledge hub for AI workflows
- Author is PM learning dev with AI
- Keep code simple and well-explained

## Code Style
- Python: PEP 8, type hints, docstrings
- Markdown: PM-friendly language
- Comments: Explain "why", not "what"

## Workflow
1. Check /ai-context/ for project context
2. Follow /ai-context/conventions.md
3. Create spec before implementation
4. Document decisions in /meta/adr/

## Common Tasks
- **New prompt**: Use /prompts/ structure
- **New guide**: Use /docs/ structure
- **New feature**: Spec first in /examples/pm-specs/
```

### GitHub Copilot Instructions

```markdown
# NextPM - GitHub Copilot Instructions

Keep suggestions:
- Simple (author is learning)
- Well-commented
- Following PEP 8
- Using type hints

Prefer:
- Readable over clever
- Explicit over implicit
- Standard library over dependencies
```

## 📐 Prompt Engineering Standards

### Prompt Structure

```markdown
You are a [role] helping a Product Manager [task].

Context:
- [Relevant background]
- [Project details]
- [Constraints]

Task:
[Clear, specific instructions]

Format:
[Expected output format]

Example:
[Show desired output style]
```

### Prompt Variables

Use clear placeholders:
- `{feature_name}` not `{f}`
- `{user_problem}` not `{problem}`
- `{success_metrics}` not `{metrics}`

### Prompt Documentation

Every prompt template needs:
1. **Purpose**: What it accomplishes
2. **When to Use**: Scenarios
3. **Inputs Required**: What context to provide
4. **Expected Output**: What you'll get
5. **Example**: Real usage
6. **Variations**: How to adapt

## ✅ Quality Checklist

### Before Committing Content

- [ ] Follows naming conventions
- [ ] Has clear structure (H1, H2, H3)
- [ ] Uses PM-friendly language
- [ ] Includes examples where relevant
- [ ] Links to related content
- [ ] No typos (use spell check)
- [ ] Tests locally (`mkdocs serve`)

### Before Committing Code

- [ ] Follows Python/YAML conventions
- [ ] Has type hints (Python)
- [ ] Has docstrings
- [ ] Runs without errors
- [ ] Has corresponding spec/ADR
- [ ] Updated relevant docs

### Before Committing Prompts

- [ ] Has complete documentation
- [ ] Includes real example
- [ ] Uses clear placeholders
- [ ] Tested and works
- [ ] Referenced in relevant guide

## 🎯 Exceptions

**When to Break Rules:**
- **User request**: If explicitly asked for different style
- **Better pattern**: If you have a compelling reason, document in ADR
- **External content**: When quoting or including third-party content

**How to Break Rules:**
- Document why in commit message or ADR
- Discuss in PR (when contributions open)
- Update conventions if pattern should be adopted

---

**Remember**: Conventions exist to make collaboration (human-human and human-AI) smoother. They're guidelines, not laws. Use judgment, and document exceptions.
