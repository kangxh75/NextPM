# [2026-02-10 15:28] Authentication System Implementation

**Date:** 2026-02-10 15:28
**Commits:** [18d2e4c](https://github.com/kangxh75/NextPM/commit/18d2e4c), [71bcc04](https://github.com/kangxh75/NextPM/commit/71bcc04)
**Related Spec:** [#2026-02-10-01 Site Authentication](../pm-workflows/2026-02-10-01-authentication.md)

## Changes Summary

Implemented complete dual authentication system (Azure AD + Basic Auth) to protect /prompts/* section while keeping all other content public. System uses Azure Static Web Apps built-in authentication combined with custom Azure Functions for flexible access control.

## Files Changed

### Files Created

**Core Configuration:**
- `staticwebapp.config.json` - Route-based access control, Azure AD provider, security headers
- `project/tasks/2026-02-10-01-authentication-tasks.md` - Implementation task breakdown

**Azure Functions (Basic Auth):**
- `api/auth/__init__.py` - Basic Auth endpoint handler with credential verification
- `api/auth/user_store.py` - User verification against environment variables
- `api/requirements.txt` - Azure Functions Python dependencies
- `api/host.json` - Azure Functions runtime configuration
- `api/.funcignore` - Build exclusions for Azure Functions

**User Management:**
- `scripts/add_user.py` - User credential generator with SHA-256 hashing

**Authentication UI:**
- `mkdocs-static/auth-choice.html` - Login page with dual auth options (Azure AD + Basic Auth)

**Documentation:**
- `meta/adr/004-authentication-strategy.md` - Architecture decision record
- `project/specs/2026-02-10-01-authentication.md` - Feature specification

### Files Modified

**Infrastructure:**
- `.github/workflows/azure-deploy.yml` - Added `api_location: "api"` for Azure Functions deployment
- `.gitignore` - Added exclusions for api cache and local user files

## Key Decisions

### Protected vs Public Content
- **Protected:** `/prompts/*` only (Prompt Library)
- **Public:** Home, engineering docs, examples, about pages
- **Rationale:** Engineering documentation provides portfolio/teaching value

### Dual Authentication
- **Azure AD:** Enterprise OAuth for Microsoft account users
- **Basic Auth:** Username/password via Azure Functions for non-Microsoft users
- **Storage:** Environment variables (sufficient for 1-5 users)

### Section-Based Access Control
- Route-based protection using staticwebapp.config.json
- Unauthorized access redirects to /login
- No authentication required for public sections

## Technical Details

### Authentication Flow

**Azure AD Path:**
```
User → /prompts/* → Redirect to /login
     → Click "Sign in with Microsoft"
     → OAuth flow via /.auth/login/aad
     → Callback to site
     → Access granted
```

**Basic Auth Path:**
```
User → /prompts/* → Redirect to /login
     → Click "Sign in with Username/Password"
     → Enter credentials
     → POST to /api/auth (Azure Function)
     → Verify against BASIC_AUTH_USERS env var
     → Access granted
```

### Access Control Rules

```json
Routes:
- /prompts/* → authenticated only
- /* → anonymous or authenticated (public)
```

### User Management

**Add Basic Auth User:**
```bash
python scripts/add_user.py username password
# Outputs JSON for Azure configuration
```

**Add Azure AD User:**
- Existing Microsoft account users work immediately
- External users: Invite as guest in Azure Portal

## Testing

### Local Testing Performed
- ✅ JSON configuration validated
- ✅ MkDocs build --strict passes
- ✅ User management script tested successfully
- ✅ Login page UI displays correctly

### Azure Testing Required
- ⏳ Azure AD OAuth flow (requires Azure deployment)
- ⏳ Basic Auth via Azure Functions (requires Azure deployment)
- ⏳ Access control enforcement
- ⏳ Logout functionality
- ⏳ Cross-browser testing

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
   - `BASIC_AUTH_USERS` = [JSON from add_user.py]

### Step 4: Add Users
**Basic Auth users added:**
- `admin` - Test admin account
- `Kangxh` - Personal account

## Security Notes

- **Password Hashing:** SHA-256 (acceptable for low-risk, 1-5 users)
- **HTTPS:** Enforced by Azure Static Web Apps
- **Session Duration:** 8 hours (Azure default)
- **Security Headers:** X-Frame-Options, X-Content-Type-Options, X-XSS-Protection
- **Secrets:** Stored in Azure configuration, never in Git

## Next Steps

- [ ] Push commits to GitHub
- [ ] Complete Azure Portal configuration (Steps 1-3 above)
- [ ] Test Azure AD authentication
- [ ] Test Basic Auth authentication
- [ ] Verify access control works correctly
- [ ] Test logout functionality
- [ ] Cross-browser testing
- [ ] Update CLAUDE.md with authentication notes
- [ ] Update spec with lessons learned

## AI Assistance

**Tools used:** Claude Code (Claude Sonnet 4.5)
**Time saved estimate:** ~4-5 hours

**AI contribution:**
- Designed complete dual authentication architecture
- Implemented all code automatically without manual intervention
- Created Azure Functions for Basic Auth endpoint
- Designed mobile-friendly login UI
- Generated user management script with hash generation
- Created comprehensive documentation (spec, ADR, tasks)
- Configured deployment pipeline for API functions

---

**GitHub Commits:**
- [18d2e4c](https://github.com/kangxh75/NextPM/commit/18d2e4c) - docs: add authentication feature spec and ADR (#2026-02-10-01)
- [71bcc04](https://github.com/kangxh75/NextPM/commit/71bcc04) - feat: implement dual authentication system (#2026-02-10-01)

---

*This change is part of the [#2026-02-10-01 Site Authentication](../pm-workflows/2026-02-10-01-authentication.md) feature.*
