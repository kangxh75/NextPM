# 2026-02-10-01: Site Authentication

**Status:** 🚧 In Progress
**Full Spec:** [View on GitHub](https://github.com/kangxh75/NextPM/blob/master/project/specs/2026-02-10-01-authentication.md)

## What This Feature Does

Implements dual authentication (Azure AD + Basic Auth) to protect the Prompt Library while keeping all other content public. Users can choose between Microsoft account login or username/password authentication.

## Why It Matters

Protects valuable prompt library intellectual property while maintaining public visibility of engineering documentation for portfolio and teaching purposes. Provides flexible authentication options for both enterprise and individual users.

## Implementation Timeline

- **Started:** 2026-02-10
- **Completed:** In Progress (code complete, Azure configuration pending)

## Related Changes

- [2026-02-10 15:28 Authentication Implementation](../dev-workflows/2026-02-10-1528-authentication-implementation.md)

## Key Outcomes

**Protected Content:**
- `/prompts/*` - Prompt Library (authentication required)

**Public Content:**
- `/` - Home page
- `/engineering/*` - PM and Dev Workflows
- `/examples/*` - Examples and case studies
- `/about/*` - About pages

**Authentication Methods:**
- Azure AD (OAuth 2.0) for Microsoft account users
- Basic Auth (username/password) via Azure Functions

**User Management:**
- Azure AD users: Managed in Microsoft Entra ID
- Basic Auth users: Environment variable storage (1-5 users)
- Python script for credential generation

**Technical Implementation:**
- staticwebapp.config.json for route-based access control
- Azure Functions custom authentication endpoint
- Mobile-friendly login page with dual auth options

## Lessons Learned

*To be filled after deployment and testing*

---

**Want the full technical details?** [Read the complete spec on GitHub](https://github.com/kangxh75/NextPM/blob/master/project/specs/2026-02-10-01-authentication.md)
