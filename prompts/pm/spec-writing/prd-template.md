# PRD Template - Product Requirements Document

## Purpose
Generate a comprehensive Product Requirements Document (PRD) for a new feature or product using AI assistance.

## When to Use
- Starting a new feature initiative
- Need to document requirements before development
- Want to ensure alignment across stakeholders
- Building case for resource allocation

## Context Required

Before using this prompt, gather:
- **Feature name and brief description**
- **Problem you're solving** (user pain point)
- **Target users** (who benefits)
- **Success metrics** (how you'll measure success)
- **Technical constraints** (if any)
- **Timeline / priority** level

## The Prompt

```
You are a senior product manager helping me write a comprehensive PRD (Product Requirements Document).

Context about the feature:
- Feature name: {feature_name}
- Problem: {user_problem}
- Target users: {target_users}
- Success metrics: {success_metrics}
- Constraints: {any_constraints}

Please create a PRD with the following structure:

1. **Executive Summary**
   - One paragraph overview
   - Key value proposition

2. **Problem Statement**
   - What problem are we solving?
   - Why is it important?
   - Current user pain points

3. **Goals and Success Metrics**
   - Primary goals (3-5)
   - Success metrics (quantifiable)
   - Success criteria for launch

4. **Target Users**
   - Primary user personas
   - Use cases
   - User journey considerations

5. **Proposed Solution**
   - High-level description
   - Key features and functionality
   - User experience flow

6. **Requirements**
   - Functional requirements (prioritized: Must-have, Should-have, Nice-to-have)
   - Non-functional requirements (performance, security, accessibility)
   - Technical considerations

7. **Out of Scope**
   - What we're NOT doing (and why)
   - Future considerations

8. **Open Questions**
   - Technical unknowns
   - Decisions needed
   - Risks and dependencies

9. **Timeline and Milestones**
   - Suggested phases
   - Key milestones
   - Launch criteria

Use clear, concise language. Be specific about requirements. Include examples where helpful.
```

## Example Usage

### Input:

```
Feature name: Dark Mode
Problem: Users report eye strain and battery drain when using app at night
Target users: Power users who use app >2 hours/day, especially in evening
Success metrics: 30% adoption rate, 10% increase in evening session duration
Constraints: Must work on both web and mobile, maintain brand consistency
```

### Output:

(AI generates complete PRD following the template structure)

```markdown
# PRD: Dark Mode Support

## Executive Summary
We will implement a dark mode theme option to reduce eye strain and improve battery
 life for users who engage with our app during evening hours...

## Problem Statement
Our power users, who spend 2+ hours daily in the app, report significant eye strain
 during evening usage. Current light theme causes discomfort in low-light environments...

[... continues with full PRD structure ...]
```

## Tips

### 1. Provide Rich Context
The more context you provide, the better the output:
- Include relevant data (user complaints, survey results)
- Reference similar features in other products
- Mention your product's specific constraints

### 2. Iterate on Structure
First pass generates the structure. Then:
- Ask AI to expand specific sections
- Request more technical detail if needed
- Add user stories based on requirements

Example follow-up:
```
Can you expand the "Requirements" section with specific user stories in the format:
"As a [user], I want to [action] so that [benefit]"
```

### 3. Use for Alignment
Share AI draft with stakeholders to:
- Get early feedback on scope
- Identify missing requirements
- Surface concerns before development

### 4. Customize Template
Adapt sections based on your company's PRD format:
- Add/remove sections as needed
- Include company-specific fields
- Match terminology to your organization

## Variations

### Lean PRD (Startups)
Remove sections 7-9, focus on:
- Problem
- Solution
- Must-have requirements

```
Create a lean PRD focusing only on:
1. Problem statement with user pain points
2. Proposed solution (1-2 paragraphs)
3. Must-have requirements only
4. Success metrics

Keep it under 2 pages.
```

### Technical PRD (Engineering-Heavy)
Expand section 6 with technical details:

```
Please focus on section 6 (Requirements) and include:
- API endpoints needed
- Database schema changes
- Third-party integrations
- Performance requirements (latency, throughput)
- Security considerations
```

### Executive PRD (Leadership)
Focus on business case:

```
Create an executive-focused PRD emphasizing:
1. Business problem and opportunity size
2. Strategic alignment with company goals
3. ROI and success metrics
4. High-level solution overview
5. Resource requirements and timeline
```

## Common Pitfalls

❌ **Too Vague**: "Users want better experience"
✅ **Specific**: "Users report 45% task completion rate vs 80% industry benchmark"

❌ **Solution Jumping**: Starting with "Build a dashboard"
✅ **Problem First**: "Users can't track progress, leading to confusion"

❌ **Missing Metrics**: "Users will love it"
✅ **Measurable**: "30% adoption rate, NPS increase from 40 to 50"

## Time Savings

| Traditional Approach | With AI | Savings |
|---------------------|---------|---------|
| 6-8 hours | 2-3 hours | **60-70%** |

**Breakdown:**
- First draft: 4 hours → 30 minutes (AI generates structure)
- Research/details: 2 hours → 1 hour (AI synthesizes, you validate)
- Editing/refinement: 2 hours → 1 hour (Focus on accuracy, not writing)

## Next Steps After PRD

1. **User Stories**: Use [User Story Generator](user-story.md) to break down requirements
2. **Technical Spec**: Share PRD with engineering for technical design
3. **Roadmap**: Add to product roadmap with timeline
4. **Kickoff**: Use PRD for project kickoff meeting

## Related Prompts

- **[User Story Generator](user-story.md)** - Convert requirements to user stories
- **[One-Pager Template](one-pager.md)** - Executive summary version
- **[Feature Evaluation](../evaluation/feature-scoring.md)** - Prioritize against other features

---

**Pro Tip**: Save your customized version of this prompt with your company's specific sections and terminology. Reuse it for every new feature!
