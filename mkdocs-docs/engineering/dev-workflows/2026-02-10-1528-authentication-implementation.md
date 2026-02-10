# [2026-02-10 15:28] Authentication System Implementation

**Date:** 2026-02-10 15:28
**Commits:** [18d2e4c](https://github.com/kangxh75/NextPM/commit/18d2e4c), [71bcc04](https://github.com/kangxh75/NextPM/commit/71bcc04)
**Related Spec:** [#2026-02-10-01 Site Authentication](../pm-workflows/2026-02-10-01-authentication.md)

## Changes Summary

Implemented Azure AD OAuth authentication system to protect /prompts/* section while keeping all other content public. System uses Azure Static Web Apps built-in authentication for enterprise-grade security with zero custom credential management.

**UPDATE 2026-02-10:** Removed Basic Auth implementation after discovering technical incompatibility with Azure Static Web Apps route protection. Final implementation is Azure AD-only.

## Files Changed

### Files Created

**Core Configuration:**

- `staticwebapp.config.json` - Route-based access control, Azure AD provider, security headers
- `project/tasks/2026-02-10-01-authentication-tasks.md` - Implementation task breakdown

**Documentation:**

- `meta/adr/004-authentication-strategy.md` - Architecture decision record (with amendment for Azure AD-only)
- `project/specs/2026-02-10-01-authentication.md` - Feature specification (updated to version 2.0)

### Files Modified

**Infrastructure:**

- `.github/workflows/azure-deploy.yml` - Updated deployment workflow (removed api_location after removing Basic Auth)

### Files Deleted

**Basic Auth Implementation (Removed 2026-02-10):**

- `api/auth/__init__.py` - Basic Auth endpoint (removed - incompatible with platform)
- `api/auth/user_store.py` - User verification (removed)
- `api/requirements.txt` - Azure Functions dependencies (removed)
- `api/host.json` - Azure Functions runtime config (removed)
- `api/.funcignore` - Build exclusions (removed)
- `scripts/add_user.py` - User management script (removed)
- `mkdocs-static/auth-choice.html` - Dual auth login page (removed - direct redirect to Azure AD)

## Key Decisions

### Protected vs Public Content

- **Protected:** `/prompts/*` only (Prompt Library)
- **Public:** Home, engineering docs, examples, about pages
- **Rationale:** Engineering documentation provides portfolio/teaching value

### Azure AD-Only Authentication

- **Azure AD:** Enterprise OAuth for Microsoft account users
- **Guest Users:** Email invitations for external collaborators
- **No Custom Auth:** Zero credential or session management code

### Why Not Dual Authentication?

**Original Plan:** Azure AD + Basic Auth (username/password)

**Technical Limitation Discovered:**

Azure Static Web Apps' route protection (`allowedRoles: ["authenticated"]`) only recognizes built-in OAuth providers (Azure AD, GitHub, Twitter). Custom authentication via Azure Functions cannot create sessions that Azure Static Web Apps will honor for route enforcement.

**Attempted Solutions:**

1. Basic Auth with Authorization header → Infinite browser popup loop
2. JSON POST with session cookie → Cookie not recognized for route protection
3. Azure Function authentication → Session doesn't persist

**Final Decision:** Azure AD-only provides proper platform integration and better security

### Section-Based Access Control

- Route-based protection using staticwebapp.config.json
- Unauthorized access redirects to /login (Microsoft OAuth)
- No authentication required for public sections

## Technical Details

### Authentication Flow

**Azure AD OAuth:**

```text
User → /prompts/* → Redirect to /login
     → Redirect to Microsoft OAuth
     → User authenticates with Microsoft account
     → OAuth callback to Azure Static Web Apps
     → Session cookie set
     → Access granted
```

### Access Control Rules

```json
Routes:
- /prompts/* → authenticated only
- /* → anonymous or authenticated (public)
```

### User Management

**Add Azure AD User:**

- Existing Microsoft account users work immediately
- External users: Invite as guest in Azure Portal → Users → Invite external user
- Guest receives email invitation with setup instructions

## Testing

### Local Testing Performed

- ✅ JSON configuration validated
- ✅ MkDocs build --strict passes
- ✅ Login redirect configured correctly

### Azure Testing Completed

- ✅ Azure AD OAuth flow works correctly
- ✅ Access control enforcement functional
- ✅ Logout functionality working
- ✅ Cross-browser testing passed

## Azure Configuration Steps (Manual)

### Step 1: Azure AD App Registration
1. Azure Portal → Microsoft Entra ID → App registrations
2. New registration: "NextPM Authentication"
3. Redirect URI: `https://www.kangxh.com/.auth/login/aad/callback`
4. Copy Application (client) ID and Directory (tenant) ID
5. Create client secret and copy value

### Step 2: Update Configuration

1. Replace `<TENANT_ID>` in staticwebapp.config.json with Directory ID
2. Commit and push

### Step 3: Configure Azure Static Web Apps

1. Azure Portal → Static Web App "web" → Configuration
2. Add application settings:
   - `AZURE_AD_CLIENT_ID` = [client ID]
   - `AZURE_AD_CLIENT_SECRET` = [secret]

## Security Notes

- **Authentication:** OAuth 2.0 via Microsoft Entra ID
- **HTTPS:** Enforced by Azure Static Web Apps
- **Session Duration:** 8 hours (Azure default)
- **Security Headers:** X-Frame-Options, X-Content-Type-Options, X-XSS-Protection
- **Secrets:** Stored in Azure configuration, never in Git
- **Password Management:** None required (handled by Microsoft)

## Next Steps

- [x] Push commits to GitHub
- [x] Complete Azure Portal configuration (Steps 1-3 above)
- [x] Test Azure AD authentication
- [x] Verify access control works correctly
- [x] Test logout functionality
- [x] Cross-browser testing
- [x] Remove Basic Auth implementation (incompatible with platform)
- [x] Update documentation to reflect Azure AD-only approach
- [ ] Update CLAUDE.md with authentication notes
- [ ] Invite guest users as needed

## AI Assistance

**Tools used:** Claude Code (Claude Sonnet 4.5)
**Time saved estimate:** ~4-5 hours

**AI contribution:**

- Designed complete authentication architecture
- Implemented initial dual authentication system
- Discovered platform limitation with Basic Auth during testing
- Redesigned to Azure AD-only after discovering incompatibility
- Removed all Basic Auth code systematically
- Updated all documentation to reflect final implementation
- Created comprehensive documentation (spec, ADR with amendment, tasks)
- Configured deployment pipeline

**Key Technical Discovery:**

AI identified that Azure Static Web Apps only supports OAuth providers for route protection, leading to the decision to remove Basic Auth implementation rather than continue with a solution that couldn't properly enforce access control.

---

**GitHub Commits:**
- [18d2e4c](https://github.com/kangxh75/NextPM/commit/18d2e4c) - docs: add authentication feature spec and ADR (#2026-02-10-01)
- [71bcc04](https://github.com/kangxh75/NextPM/commit/71bcc04) - feat: implement dual authentication system (#2026-02-10-01)

---

*This change is part of the [#2026-02-10-01 Site Authentication](../pm-workflows/2026-02-10-01-authentication.md) feature.*
