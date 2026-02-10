# ADR 004: Authentication Strategy

**Status:** Superseded (see Amendment below)
**Date:** 2026-02-10
**Author:** Kang (with AI assistance from Claude Code)

## Context

NextPM contains two types of content:
- **Public content:** Engineering documentation, examples, about pages (portfolio/teaching material)
- **Protected content:** Prompt library (intellectual property)

The site needs authentication to protect the prompt library while keeping all other content publicly accessible for portfolio and teaching purposes.

**Problem:** How should we implement authentication for selective content protection on a static MkDocs site hosted on Azure Static Web Apps?

## Decision

We will implement **dual authentication** with **section-based access control** using:
- **Azure AD (Microsoft Entra ID)** for enterprise/OAuth-based authentication
- **Basic Auth via Azure Functions** for simple username/password access
- **staticwebapp.config.json** for route-based access control

**Protected Sections:**
- `/prompts/*` - Requires authentication

**Public Sections:**
- `/` (Home)
- `/engineering/*` (PM/Dev Workflows)
- `/examples/*` (Case studies)
- `/about/*` (About pages)

**User Storage:**
- Azure AD users: Managed in Microsoft Entra ID
- Basic Auth users: Stored in environment variables (JSON format, 1-5 users)

## Rationale

### Why Dual Authentication?

**Azure AD:**
- Enterprise-grade OAuth 2.0 security
- Zero-cost built-in support in Azure Static Web Apps
- No password management needed
- Suitable for professional users with Microsoft accounts

**Basic Auth:**
- Simple username/password for users without Microsoft accounts
- Easy to add/remove users via environment variables
- Sufficient for small user base (1-5 users)
- Implemented via Azure Functions (already planned for Phase 2)

### Why Section-Based (Not Full Site) Protection?

1. **Portfolio value:** Engineering documentation demonstrates skills and project history publicly
2. **Teaching value:** PM/Dev workflows serve as educational content
3. **SEO benefits:** Public content can be indexed by search engines
4. **Selective protection:** Only prompt library contains IP worth protecting
5. **Fallback safety:** If authentication breaks, public documentation remains accessible

### Why Environment Variables (Not Database)?

**For 1-5 users:**
- No database infrastructure needed (saves cost and complexity)
- Environment variables in Azure configuration are secure
- Python script simplifies user management
- Fast access (no database query overhead)
- Sufficient for Phase 1 scope

**When to migrate to database:**
- User count grows beyond 10
- Need user profiles or metadata
- Require audit logs
- Phase 2 Cosmos DB is implemented

## Alternatives Considered

### Alternative 1: Azure AD Only

**Approach:** Single authentication mode using only Azure AD.

**Pros:**
- Simplest implementation (built-in, zero code)
- Enterprise-grade security
- No password management
- Zero cost

**Cons:**
- All users must have Microsoft accounts
- External collaborators need guest invitations
- Less flexible for non-enterprise users

**Decision:** Rejected - want flexibility for users without Microsoft accounts

### Alternative 2: Basic Auth Only

**Approach:** Single authentication mode using only username/password.

**Pros:**
- Simple username/password
- No dependency on Microsoft ecosystem
- Full control over user management

**Cons:**
- Less secure than OAuth
- Manual password management
- No enterprise SSO
- Requires custom implementation

**Decision:** Rejected - want enterprise-grade option for professional users

### Alternative 3: Full Site Protection

**Approach:** Require authentication for entire site including engineering docs.

**Pros:**
- Simpler configuration (one rule: everything protected)
- Maximum content protection

**Cons:**
- Loses portfolio/teaching value
- No public visibility of engineering work
- No SEO benefits
- Defeats "building in public" philosophy

**Decision:** Rejected - engineering documentation has value as public portfolio content

### Alternative 4: Database-Backed User Storage

**Approach:** Store Basic Auth users in Cosmos DB from the start.

**Pros:**
- Scalable to many users
- Can store user profiles and metadata
- Supports audit logs

**Cons:**
- Adds complexity for 1-5 users
- Requires Cosmos DB setup (not needed yet)
- Increases cost ($0.01/GB storage, $0.25/RU)
- Over-engineering for current needs

**Decision:** Rejected - defer to Phase 2 when database is needed for other features

## Consequences

### Positive

1. **Flexibility:** Users can choose authentication method (Azure AD or Basic Auth)
2. **Portfolio value preserved:** Engineering docs remain public for teaching/portfolio
3. **Zero infrastructure cost:** Uses existing Azure resources only
4. **Simple user management:** Environment variables sufficient for 1-5 users
5. **Future-proof:** Can add more providers (GitHub, Google) later
6. **Security balance:** Enterprise auth where appropriate, simple auth where sufficient

### Negative

1. **Two systems to maintain:** Azure AD and Basic Auth both need management
2. **Cold start delay:** Azure Functions may have 2-5 second delay on first request
3. **Limited scalability:** Environment variable storage doesn't scale beyond 10-20 users
4. **Manual user management:** No self-service registration or password reset
5. **SHA-256 hashing:** Less secure than bcrypt/Argon2 (acceptable for low-risk use case)

### Neutral

1. **Implementation effort:** Medium complexity (3-5 hours total)
2. **User experience:** Login adds friction but only for prompt library access
3. **Testing overhead:** Need to test both authentication paths

## Migration Path

If needs change:

**Scale Users (>10 users):**
1. Create Cosmos DB users table
2. Migrate environment variables to database
3. Update user_store.py to query database
4. Add user management API endpoints

**Add Authentication Providers:**
1. Register provider in Azure Static Web Apps
2. Add provider to staticwebapp.config.json
3. Update login page UI with new option

**Protect Additional Sections:**
1. Update routes in staticwebapp.config.json
2. Add route rules for new protected sections
3. Test access control

**Upgrade Password Security:**
1. Install bcrypt or Argon2 library
2. Update password_utils.py with new hashing
3. Reset all Basic Auth user passwords

## Implementation Details

**Configuration File:** `staticwebapp.config.json`
- Routes for access control
- Azure AD provider configuration
- Redirect rules for unauthorized access

**Azure Functions:** `api/auth/`
- Basic Auth endpoint
- User credential verification
- Environment variable-based user store

**User Management:** `scripts/add_user.py`
- Generate SHA-256 password hashes
- Update environment variable JSON

**Login UI:** `mkdocs-static/auth-choice.html`
- Choice between Azure AD and Basic Auth
- Mobile-friendly design
- Clear error messages

## References

- [Azure Static Web Apps Authentication](https://learn.microsoft.com/en-us/azure/static-web-apps/authentication-authorization)
- [ADR 003: Azure Static Web Apps](003-azure-static-web-apps.md) - Hosting decision
- [Spec: 2026-02-10-01 Authentication](../../project/specs/2026-02-10-01-authentication.md) - Full specification

## Status History

- **2026-02-10:** Proposed and Accepted (Dual Authentication)
- **2026-02-10:** Superseded by Amendment 1 (Azure AD-only)

---

## Amendment 1: Changed to Azure AD-Only Authentication

**Status:** Accepted
**Date:** 2026-02-10
**Reason:** Technical incompatibility discovered during implementation

### What Changed

**Original Decision:** Dual authentication (Azure AD + Basic Auth)
**Revised Decision:** Azure AD-only authentication

### Why the Change?

During implementation, we discovered a fundamental platform limitation:

**Technical Constraint:**

Azure Static Web Apps' route-based access control (`allowedRoles: ["authenticated"]` in staticwebapp.config.json) only recognizes authentication from **built-in OAuth providers** (Azure AD, GitHub, Twitter). Custom username/password authentication cannot integrate with this route protection mechanism.

**Attempted Solutions:**

1. **Basic Auth with Authorization header** → Browser showed infinite popup loop due to WWW-Authenticate header
2. **JSON POST with custom session cookie** → Cookie not recognized by Azure Static Web Apps for route enforcement
3. **Azure Function authentication** → Session doesn't persist across pages

**Root Cause:**

Azure Static Web Apps manages authentication sessions internally and only trusts sessions from its built-in identity providers. Custom authentication endpoints (via Azure Functions) cannot create sessions that Azure Static Web Apps will honor for route protection.

### Revised Implementation

**What Was Removed:**

- api/auth/ directory (Azure Functions for Basic Auth)
- scripts/add_user.py (user management script)
- mkdocs-static/auth-choice.html (dual auth login page)
- Basic Auth routes in staticwebapp.config.json
- api_location in GitHub Actions workflow

**What Remains:**

- staticwebapp.config.json with Azure AD provider only
- Direct redirect to Microsoft OAuth login
- Route protection for /prompts/\*
- Guest user invitation support

### Benefits of Azure AD-Only

1. **Proper Route Protection:** Full integration with Azure Static Web Apps authentication
2. **Enterprise Security:** OAuth 2.0 with zero custom credential management
3. **Simpler Architecture:** No Azure Functions, no session management code
4. **Zero Maintenance:** Microsoft handles user management, MFA, password policies
5. **Guest User Support:** External collaborators can be invited via email

### Addressing Original Concerns

**Original Concern:** "All users must have Microsoft accounts"
**Resolution:** Azure AD guest user invitations allow external users with any email address

**Original Concern:** "Less flexible for non-enterprise users"
**Resolution:** Guest invitations work with Gmail, Yahoo, corporate emails - anyone can be invited

### Updated Alternatives Analysis

#### Alternative 1: Azure AD Only (NOW CHOSEN)

**Pros:**

- ✅ Proper integration with Azure Static Web Apps
- ✅ Enterprise-grade security
- ✅ No custom code or session management
- ✅ Guest user invitation support
- ✅ Zero maintenance overhead

**Cons:**

- Users must accept guest invitation (one-time process)
- Requires Azure AD app registration (one-time setup)

**Decision:** ACCEPTED - only viable option for route-based protection

#### Alternative 2: Basic Auth Only (NOW TECHNICALLY IMPOSSIBLE)

**Decision:** Rejected - cannot integrate with Azure Static Web Apps route protection

#### Alternative 3: Move to Full Backend Architecture

To support username/password authentication, would require:

- Migrate from static site to server-rendered app
- Custom authentication middleware
- Session management infrastructure
- Database for user credentials

**Decision:** Rejected - massive architecture change not justified for this use case

### Consequences

**Positive:**

- Simpler implementation (removed ~500 lines of code)
- More secure (OAuth 2.0 vs custom password management)
- Zero maintenance (no password resets, no user database)
- Proper session management by platform

**Negative:**

- Lost flexibility of username/password option
- Users must have or create Microsoft account for guest access
- Single authentication method (no user choice)

**Mitigations:**

- Guest user invitations are straightforward (just an email)
- Most professional users already have Microsoft accounts
- Authentication still only required for /prompts/\* (rest of site is public)

### Implementation Status

- [x] Removed all Basic Auth code
- [x] Updated staticwebapp.config.json to Azure AD-only
- [x] Removed auth-choice.html
- [x] Updated GitHub Actions workflow
- [x] Updated specification document
- [x] Updated this ADR
- [ ] Update PM and Dev workflow documentation
- [ ] Deploy changes

---

**Next Review:** If Azure Static Web Apps adds custom authentication provider support
