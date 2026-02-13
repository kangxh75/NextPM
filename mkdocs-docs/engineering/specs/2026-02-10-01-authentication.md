# 2026-02-10-01 Site Authentication

<span class="spec-state-badge spec-state-draft" data-status="draft" data-priority="medium">
    📋 Draft
</span>

<div class="spec-timeline" data-timeline="{&quot;spec_id&quot;: &quot;2026-02-10-01&quot;, &quot;status&quot;: &quot;draft&quot;, &quot;state_history&quot;: [], &quot;estimated_hours&quot;: 0, &quot;actual_hours&quot;: 0, &quot;priority&quot;: &quot;medium&quot;, &quot;category&quot;: &quot;nextpm-feature&quot;, &quot;demonstrates&quot;: []}"></div>

<div class="commit-timeline">
    <h4>📝 Development Timeline</h4>
    <div class="timeline-container">
        <div class="timeline-item latest">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#c8df1fba</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">refactor: remove Basic Auth, finalize Azure AD-only authentication (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 14 files changed</span>
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#4090ea9c</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">fix: remove WWW-Authenticate header causing browser popup (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 2 files changed</span>
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#d9ee6d21</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">fix: add function.json for Azure Functions Basic Auth endpoint (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 1 files changed</span>
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#1e8cf07b</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">fix: copy auth config and static files to build output (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 1 files changed</span>
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#e0b544bc</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">config: add Azure AD tenant ID to authentication config (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 1 files changed</span>
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#33b8ed15</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">docs: add PM and Dev Workflow summaries for authentication (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 3 files changed</span>
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#71bcc049</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">feat: implement dual authentication system (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 11 files changed</span>
                </div>
            </div>
        </div>
        <div class="timeline-item">
            <div class="timeline-marker"></div>
            <div class="timeline-content">
                <div class="commit-header">
                    <span class="commit-hash">#18d2e4c6</span>
                    <span class="commit-date">2026-02-10</span>
                </div>
                <div class="commit-message">docs: add authentication feature spec and ADR (#2026-02-10-01)</div>
                <div class="commit-meta">
                    <span class="commit-author">👤 Allen Kang (from Dev Box)</span>
                    <span class="files-changed">📁 2 files changed</span>
                </div>
            </div>
        </div>
    </div>
</div>



**Status:** ✅ Implemented
**Date:** 2026-02-10
**Version:** 2.0
**Priority:** High

## Overview

Implement authentication for the NextPM website to protect the Prompt Library while keeping all other content public including engineering documentation. The solution uses Azure AD (Microsoft Entra ID) OAuth-based authentication for secure, enterprise-grade access control.

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
- **Authorized Viewers** - Need secure access to prompt library using their Microsoft account
- **Public Visitors** - Should be able to access all content except prompt library (home, engineering, examples, about pages)

**User Benefits:**

- Protect valuable prompt library intellectual property
- Maintain full public visibility for engineering documentation, examples, and portfolio
- Enterprise-grade Azure AD OAuth authentication
- Guest user invitation support for external collaborators
- No manual user management overhead (handled by Microsoft Entra ID)
- No impact on public pages - only /prompts/\* requires authentication

## Proposed Solution

### High-Level Approach

Implement section-based authentication using Azure Static Web Apps' built-in Azure AD (Microsoft Entra ID) OAuth capabilities. Only /prompts/\* section requires authentication; all other sections (/, /engineering/\*, /examples/\*, /about/\*) remain public.

### Key Features

1. **Azure AD Authentication**
   - Microsoft account OAuth 2.0 integration
   - Supports internal Azure AD users and external guest users
   - Enterprise-grade security with no custom credential management
   - Automatic session management by Azure Static Web Apps

2. **Section-Based Access Control**
   - /prompts/\* - **Protected** (Prompt Library only)
   - /, /engineering/\*, /examples/\*, /about/\* - **Public** (no authentication required)
   - Configured via static web app config file with route rules

3. **User Management**
   - Azure AD users: Managed in Azure Portal (Microsoft Entra ID)
   - Guest user invitations for external collaborators
   - No manual user database or password management required

4. **Authentication UI**
   - Automatic redirect to Microsoft login page
   - Seamless redirect back to requested page after login
   - Built-in Microsoft OAuth UI (no custom login page needed)

### Technical Design

**Architecture:**

- Azure Static Web Apps built-in authentication for Azure AD
- staticwebapp.config.json for route-based access control
- Microsoft Entra ID for user management
- MkDocs static site remains unchanged

**Authentication Flow:**

```text
User → Access /prompts/* → Redirect to /login
      ↓
Microsoft OAuth Login Page
      ↓
User authenticates with Microsoft account
      ↓
OAuth callback to Azure Static Web Apps
      ↓
Session cookie set by Azure Static Web Apps
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

- User accounts: Microsoft Entra ID (Azure cloud)
- Session: Azure Static Web Apps managed (8-hour default)
- No custom password storage or session management required

**Files Created:**

- staticwebapp.config.json - Core authentication configuration

**Files Modified:**

- .github/workflows/azure-deploy.yml - No changes needed (authentication is built-in)

## Success Metrics

### Completion Criteria

- [x] staticwebapp.config.json created with route-based access control
- [x] Azure AD app registration completed and configured
- [x] Azure Static Web Apps configuration includes all required secrets
- [x] /prompts/* section requires authentication
- [x] All other sections (/, /engineering/*, /examples/*, /about/*) remain public
- [x] Azure AD authentication successfully grants access
- [x] Logout functionality works correctly
- [x] Zero downtime during deployment

### Quality Indicators

- Login completes in under 5 seconds (Azure AD OAuth)
- Microsoft login page works on all major browsers and mobile devices
- Clear error messages for invalid credentials (handled by Microsoft)
- No broken links after authentication is added
- MkDocs build --strict passes
- GitHub Actions deployment succeeds

### User Acceptance

- Prompt library is inaccessible without authentication
- All other content (engineering, examples, about) remains freely accessible
- Login experience is intuitive using familiar Microsoft login
- Guest users can be invited for external collaborators
- No impact on site performance or load times

## Implementation Notes

### Implementation Steps

1. Create Azure AD app registration in Microsoft Entra ID
2. Configure redirect URIs and client secrets
3. Create staticwebapp.config.json with Azure AD provider configuration
4. Add Azure AD secrets to Static Web App configuration (AZURE_AD_CLIENT_ID, AZURE_AD_CLIENT_SECRET)
5. Deploy and test Azure AD login flow
6. Document user management process for Azure AD (including guest user invitations)
7. Create PM and Dev Workflow summaries
8. Update CLAUDE.md with authentication notes

### Technical Constraints

- Azure Static Web Apps Free Tier (100 GB bandwidth/month, 250 MB app size)
- Session duration fixed at 8 hours (Azure Static Web Apps default)
- Requires Azure AD app registration (one-time setup)
- Guest users require email invitation for external collaborators

### Why Azure AD Only?

**Initial Approach:**

Originally planned to support dual authentication (Azure AD + Basic Auth with username/password) to provide flexibility for users without Microsoft accounts.

**Technical Limitation Discovered:**

Azure Static Web Apps' route-based access control (`allowedRoles: ["authenticated"]`) only recognizes authentication from built-in OAuth providers (Azure AD, GitHub, Twitter). Custom username/password authentication cannot integrate with this route protection mechanism, even when using Azure Functions to validate credentials and set session cookies.

**Attempted Solutions:**

1. Basic Auth with Authorization header → Browser showed infinite popup loop
2. JSON POST with custom session cookie → Cookie not recognized by Azure Static Web Apps route protection
3. Azure Function custom authentication → Session doesn't persist across pages

**Final Decision:**

Azure AD-only authentication provides:

- ✅ Enterprise-grade security with OAuth 2.0
- ✅ Proper integration with Azure Static Web Apps route protection
- ✅ No custom credential or session management complexity
- ✅ Guest user invitation support for external collaborators
- ✅ Zero maintenance overhead for user management

## Out of Scope

**For v1.0 (this feature):**

- ❌ Role-based access control (admin, editor, viewer roles)
- ❌ User profile management or self-service password reset
- ❌ Social login (GitHub, Google, Twitter)
- ❌ Multi-factor authentication (MFA) - relies on Azure AD tenant MFA settings
- ❌ Audit logs or access tracking
- ❌ API authentication (for Phase 2 backend features)
- ❌ Custom session duration or remember-me functionality
- ❌ Basic Auth or username/password authentication (not supported by Azure Static Web Apps route protection)
- ❌ Protecting engineering documentation (explicitly kept public for portfolio/teaching)

**Explicitly Deferred:**

- Database-backed user storage (not needed - Azure AD handles user management)
- Admin UI for user management (Azure Portal provides this functionality)

## Risks & Mitigations

| Risk | Impact | Mitigation |
|------|--------|-----------|
| Azure AD tenant access | Low | Document guest user invitation process; owner can invite external users as needed |
| Accidental lockout | Medium | Always test in incognito before final deployment; maintain rollback plan; engineering docs remain public as fallback |
| OAuth redirect misconfiguration | Medium | Carefully document redirect URI setup; test thoroughly before production deployment |
| Session expiration during use | Low | 8-hour session is sufficient for typical usage patterns; users can re-authenticate easily |

## References

### Internal Documents

- [Engineering History Tracking Spec](2026-02-09-01-engineering-history-tracking.md) - Established workflow documentation process
- [Project Start Spec](0.00-project-start.md) - Initial Azure Static Web Apps decision
- [ADR 003: Azure Static Web Apps](https://github.com/kangxh75/NextPM/blob/master/meta/adr/003-azure-static-web-apps.md) - Architecture decision rationale
- [ADR 004: Authentication Strategy](https://github.com/kangxh75/NextPM/blob/master/../../meta/adr/004-authentication-strategy.md) - Authentication approach and final decision

### External Resources

- [Azure Static Web Apps Authentication](https://learn.microsoft.com/en-us/azure/static-web-apps/authentication-authorization)
- [Microsoft Entra ID App Registration](https://learn.microsoft.com/en-us/entra/identity-platform/quickstart-register-app)
- [Azure AD Guest User Access](https://learn.microsoft.com/en-us/entra/external-id/what-is-b2b)

### Related Artifacts

- **Tasks:** `/project/tasks/2026-02-10-01-authentication-tasks.md`
- **PM Workflow:** `/mkdocs-docs/engineering/pm-workflows/2026-02-10-01-authentication.md`
- **Dev Workflow:** `/mkdocs-docs/engineering/dev-workflows/2026-02-10-1528-authentication-implementation.md`

## Next Steps

1. ~~Review and approve this specification~~
2. ~~Create task breakdown in `/project/tasks/`~~
3. ~~Begin Phase 1: Azure AD app registration~~
4. ~~Implement staticwebapp.config.json configuration~~
5. ~~Deploy and test Azure AD authentication~~
6. ~~Create PM and Dev Workflow summaries~~
7. Update CLAUDE.md with authentication notes
8. Invite guest users as needed for external collaborators

## Lessons Learned

**What Worked Well:**

- Azure Static Web Apps built-in authentication is powerful and requires minimal configuration
- OAuth flow with Azure AD provides enterprise-grade security without custom implementation
- Route-based access control is simple and effective
- Guest user invitation system works well for external collaborators

**Technical Insights:**

- Azure Static Web Apps only supports OAuth providers (Azure AD, GitHub, Twitter) for route protection
- Custom username/password authentication cannot integrate with `allowedRoles` in staticwebapp.config.json
- Session cookies from Azure Functions are not recognized by Azure Static Web Apps authentication framework
- Attempting to build custom Basic Auth results in session management complexity without proper route enforcement

**Process Improvements:**

- Always validate authentication approach against platform limitations before implementation
- Test authentication integration early to discover compatibility issues
- Consider OAuth-first for modern web applications on managed platforms

## Change History

### Version 2.0 - 2026-02-10

- **Changed to Azure AD-only authentication** (removed Basic Auth)
- Reason: Azure Static Web Apps route protection only supports built-in OAuth providers
- Basic Auth implementation removed after discovering technical incompatibility
- Simplified authentication flow with direct redirect to Microsoft login
- Removed custom login page and Azure Functions
- Updated all documentation to reflect final implementation

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
