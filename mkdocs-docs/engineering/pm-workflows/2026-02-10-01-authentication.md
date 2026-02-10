# 2026-02-10-01: Site Authentication

**Status:** ✅ Implemented
**Full Spec:** [View on GitHub](https://github.com/kangxh75/NextPM/blob/master/project/specs/2026-02-10-01-authentication.md)

## What This Feature Does

Implements Azure AD (Microsoft Entra ID) OAuth authentication to protect the Prompt Library while keeping all other content public. Users authenticate with their Microsoft account to access protected sections.

## Why It Matters

Protects valuable prompt library intellectual property while maintaining public visibility of engineering documentation for portfolio and teaching purposes. Uses enterprise-grade OAuth 2.0 authentication with zero custom credential management.

## Implementation Timeline

- **Started:** 2026-02-10
- **Completed:** 2026-02-10 (Azure AD-only implementation)

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

**Authentication Method:**

- Azure AD (OAuth 2.0) for Microsoft account users
- Guest user invitation support for external collaborators

**User Management:**

- Azure AD users: Managed in Microsoft Entra ID (Azure Portal)
- Guest invitations: Send email invitations to external users
- No manual password management required

**Technical Implementation:**

- staticwebapp.config.json for route-based access control
- Direct redirect to Microsoft OAuth login
- Zero custom authentication code
- Built-in session management by Azure Static Web Apps

## Lessons Learned

**What Worked Well:**

- Azure Static Web Apps built-in authentication is powerful and simple
- OAuth flow provides enterprise-grade security without custom implementation
- Route-based protection is straightforward and effective

**Key Technical Discovery:**

- Azure Static Web Apps only supports OAuth providers (Azure AD, GitHub, Twitter) for route protection
- Custom username/password authentication cannot integrate with staticwebapp.config.json route enforcement
- Initially planned dual authentication (Azure AD + Basic Auth) but discovered Basic Auth is technically incompatible
- Removed Basic Auth implementation after discovering platform limitation

**Decision Evolution:**

1. **Initial Plan:** Dual authentication (Azure AD + Basic Auth) for flexibility
2. **Implementation:** Built both authentication methods
3. **Discovery:** Basic Auth sessions not recognized by Azure Static Web Apps route protection
4. **Final Decision:** Azure AD-only provides proper integration and better security

**Process Insight:**

- Always validate authentication approach against platform capabilities early
- Testing authentication integration revealed incompatibility before production deployment
- Guest user invitations address the original concern about requiring Microsoft accounts

---

**Want the full technical details?** [Read the complete spec on GitHub](https://github.com/kangxh75/NextPM/blob/master/project/specs/2026-02-10-01-authentication.md)
