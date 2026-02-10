# 2026-02-10-01 Site Authentication

**Status:** 📝 Draft
**Date:** 2026-02-10
**Version:** 1.0
**Priority:** High

## Overview

Implement authentication for the NextPM website to protect the Prompt Library while keeping all other content public including engineering documentation. The solution supports two authentication methods: Azure AD (modern OAuth-based) for enterprise users and Basic Auth (username/password) for simple access control.

## Problem

**Current State:**
- NextPM website is completely public and accessible to anyone
- Prompt library represents valuable intellectual property with no protection
- No authentication or access control exists
- Azure Static Web Apps resource is deployed but has no authentication configured

**Pain Points:**
- Cannot protect prompt library templates and examples
- Prompts represent curated intellectual property that should be restricted
- No way to track who is accessing the prompt library
- Public content (home, engineering, examples, about pages) should remain open for teaching and portfolio purposes
- No way to differentiate access levels between public and protected content

## User Impact

**Primary Users:**
- **Site Owner (PM)** - Needs to protect prompt library while keeping other content public
- **Authorized Viewers** - Need easy, secure access to prompt library without complicated setup
- **Public Visitors** - Should be able to access all content except prompt library (home, engineering, examples, about pages)

**User Benefits:**
- Protect valuable prompt library intellectual property
- Maintain full public visibility for engineering documentation, examples, and portfolio
- Support both enterprise (Azure AD) and simple (username/password) authentication methods
- Simple user management (1-5 total users expected)
- No impact on public pages - only /prompts/* requires authentication

## Proposed Solution

### High-Level Approach

Implement section-based authentication using Azure Static Web Apps' built-in capabilities combined with custom Azure Functions for flexible auth options. Only /prompts/* section requires authentication; all other sections (/, /engineering/*, /examples/*, /about/*) remain public.

### Key Features

1. **Dual Authentication Modes**
   - Azure AD integration for Microsoft account users (OAuth 2.0)
   - Basic Auth via Azure Functions for username/password access
   - User chooses authentication method on login page
   - Both methods provide the same access level

2. **Section-Based Access Control**
   - /prompts/* - **Protected** (Prompt Library only)
   - /, /engineering/*, /examples/*, /about/* - **Public** (no authentication required)
   - Configured via static web app config file with route rules

3. **User Management**
   - Azure AD users: Managed in Azure Portal (Microsoft Entra ID)
   - Basic Auth users: Managed via environment variables (1-5 users)
   - Simple Python script to generate user credentials
   - No database required for Phase 1

4. **Authentication UI**
   - Custom login page with choice between Azure AD and Basic Auth
   - Clean, mobile-friendly interface
   - Clear error messages for failed login attempts
   - Seamless redirect back to requested page after login

### Technical Design

**Architecture:**
- Azure Static Web Apps built-in authentication for Azure AD
- Azure Functions custom authentication endpoint for Basic Auth
- staticwebapp.config.json for route-based access control
- Environment variables for secrets management
- MkDocs static site remains unchanged

**Authentication Flow:**

```
User → Access /prompts/* → Redirect to /login
      ↓
Login Page → Choose Auth Method
      ↓
Azure AD Path:                Basic Auth Path:
- Redirect to Microsoft       - Enter username/password
- OAuth flow                  - POST to /api/auth
- Callback to site            - Azure Function validates
- Set session cookie          - Set session cookie
      ↓
Access Granted → Redirect to Originally Requested Page
```

**Access Control Rules:**
```json
Routes:
- /prompts/* → Requires: ["authenticated"]
- /* → Requires: ["anonymous", "authenticated"] (public)
```

**Storage:**
- Azure AD users: Microsoft Entra ID (Azure cloud)
- Basic Auth users: Azure Static Web Apps environment variables (JSON)
- Passwords: SHA-256 hashed
- Session: Azure Static Web Apps managed (8-hour default)

**Files Created:**
- staticwebapp.config.json - Core authentication configuration
- api/auth/__init__.py - Basic Auth Azure Function endpoint
- api/auth/user_store.py - User credential verification
- api/requirements.txt - Azure Functions dependencies
- api/host.json - Azure Functions runtime config
- mkdocs-static/auth-choice.html - Login page UI
- scripts/add_user.py - User management script

**Files Modified:**
- .github/workflows/azure-deploy.yml - Add API deployment
- .gitignore - Exclude local user files and cache

## Success Metrics

### Completion Criteria
- [ ] staticwebapp.config.json created with route-based access control
- [ ] Azure AD app registration completed and configured
- [ ] Basic Auth Azure Functions endpoint implemented and deployed
- [ ] Login page created with both authentication options
- [ ] Azure Static Web Apps configuration includes all required secrets
- [ ] /prompts/* section requires authentication
- [ ] All other sections (/, /engineering/*, /examples/*, /about/*) remain public
- [ ] Both Azure AD and Basic Auth successfully grant access
- [ ] Logout functionality works correctly
- [ ] User management script operational for Basic Auth users
- [ ] All tests pass (7 test scenarios)
- [ ] Zero downtime during deployment

### Quality Indicators
- Login completes in under 5 seconds (Azure AD and Basic Auth)
- Mobile-friendly login page works on all major browsers
- Clear error messages for invalid credentials
- No broken links after authentication is added
- MkDocs build --strict passes
- GitHub Actions deployment succeeds

### User Acceptance
- Site owner can successfully add new users (both auth methods)
- Prompt library is inaccessible without authentication
- All other content (engineering, examples, about) remains freely accessible
- Login experience is intuitive and straightforward
- No impact on site performance or load times

## Implementation Notes

### Phase 1: Azure AD Authentication
1. Create Azure AD app registration
2. Configure redirect URIs and secrets
3. Create staticwebapp.config.json with Azure AD provider
4. Add Azure secrets to Static Web App configuration
5. Test Azure AD login flow
6. Document user management for Azure AD

### Phase 2: Basic Auth Integration
1. Create Azure Functions for Basic Auth endpoint
2. Implement user store with environment variable storage
3. Create login page with authentication choice UI
4. Update staticwebapp.config.json with Basic Auth route
5. Create user management script
6. Test both authentication methods
7. Verify logout and session management

### Phase 3: Testing & Documentation
1. Run all 7 test scenarios
2. Test cross-browser compatibility
3. Create PM Workflow summary
4. After deployment, create Dev Workflow summary
5. Update CLAUDE.md with authentication notes
6. Document user management procedures

### Technical Constraints
- Azure Static Web Apps Free Tier (100 GB bandwidth/month, 250 MB app size)
- 1-5 total users expected (influences storage choice)
- No database available in Phase 1 (environment variables only)
- Azure Functions cold start delay (2-5 seconds on first request)
- Session duration fixed at 8 hours (Azure Static Web Apps default)
- SHA-256 password hashing (sufficient for low-risk, small user base)

## Out of Scope

**For v1.0 (this feature):**
- ❌ Role-based access control (admin, editor, viewer roles)
- ❌ User profile management or self-service password reset
- ❌ Social login (GitHub, Google, Twitter)
- ❌ Multi-factor authentication (MFA)
- ❌ Audit logs or access tracking
- ❌ API authentication (for Phase 2 backend features)
- ❌ Custom session duration or remember-me functionality
- ❌ User registration or invitation system (manual user addition only)
- ❌ Protecting engineering documentation (explicitly kept public for portfolio/teaching)

**Explicitly Deferred:**
- Database-backed user storage (wait for Phase 2 Cosmos DB)
- Advanced password policies (complexity requirements, expiration)
- Stronger password hashing (bcrypt, Argon2) - upgrade when user count grows
- Admin UI for user management - using scripts is sufficient for 1-5 users

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Azure Functions cold start delay | Medium | Accept 2-5 second delay on first login; uncommon for low-traffic site |
| Complex authentication debugging | Medium | Comprehensive logging; clear error messages; fallback to Azure AD if Basic Auth fails |
| User management overhead | Low | Python script simplifies user addition; limit to 5 users to keep manual process manageable |
| SHA-256 password security | Low | Sufficient for low-risk site with 1-5 users; plan upgrade to bcrypt if user count grows |
| Accidental lockout | Medium | Always test in incognito before final deployment; maintain rollback plan; engineering docs remain public as fallback |
| Azure AD tenant access | Low | Document guest user invitation process; owner can invite external users as needed |

## References

### Internal Documents
- [Engineering History Tracking Spec](2026-02-09-01-engineering-history-tracking.md) - Established workflow documentation process
- [Project Start Spec](0.00-project-start.md) - Initial Azure Static Web Apps decision
- [ADR 003: Azure Static Web Apps](../meta/adr/003-azure-static-web-apps.md) - Architecture decision rationale

### External Resources
- [Azure Static Web Apps Authentication](https://learn.microsoft.com/en-us/azure/static-web-apps/authentication-authorization)
- [Azure Functions Python Guide](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python)
- [Microsoft Entra ID App Registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)

### Related Artifacts
- **Tasks:** `/project/tasks/2026-02-10-01-authentication-tasks.md`
- **Validation:** `/project/validations/2026-02-10-01-authentication-validation.md`
- **Implementation Plan:** `C:\Users\allenk\.claude\plans\breezy-baking-beacon.md`

## Next Steps

1. Review and approve this specification
2. Create task breakdown in `/project/tasks/`
3. Begin Phase 1: Azure AD app registration
4. Implement staticwebapp.config.json configuration
5. Phase 2: Build Basic Auth Azure Functions
6. Create and test login UI
7. Deploy and run test scenarios
8. Create PM and Dev Workflow summaries
9. Update CLAUDE.md

## Lessons Learned

**To be filled after implementation**

## Change History

### Version 1.0 - 2026-02-10
- Initial spec creation
- Defined dual authentication approach (Azure AD + Basic Auth)
- Scoped to /prompts/* protection only (engineering docs remain public)
- Configuration file storage for Basic Auth users (1-5 users)
- Both authentication phases to be implemented together
- Established success criteria and test scenarios

---

**Document Metadata:**
- **Spec Version:** 1.0
- **Created:** 2026-02-10
- **Author:** Kang (with AI assistance from Claude Sonnet 4.5)
- **Last Updated:** 2026-02-10
- **Related Specs:** 2026-02-09-01 (Engineering History Tracking)
- **Status:** Living document
