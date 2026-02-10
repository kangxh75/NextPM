# ADR 004: Dual Authentication Strategy

**Status:** Accepted
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

- **2026-02-10:** Proposed and Accepted

---

**Next Review:** After Phase 2 implementation or when user count exceeds 10
