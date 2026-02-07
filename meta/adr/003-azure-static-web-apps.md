# ADR 003: Azure Static Web Apps for Hosting

**Status:** Accepted
**Date:** 2026-02-04
**Author:** Kang (with AI assistance from Claude Code)

## Context

NextPM requires hosting for:
- **Phase 1:** Static documentation site (MkDocs Material)
- **Phase 2:** Dynamic features (APIs, authentication, database integration)

The solution needs to:
- Support static site generation
- Allow future expansion to serverless APIs
- Integrate with GitHub for CI/CD
- Be cost-effective (MSDN subscription with $150/month credit)
- Support custom domains with SSL
- Have good global CDN performance

**Problem:** Which hosting platform should we use for NextPM?

## Decision

We will use **Azure Static Web Apps (Free Tier)** for hosting NextPM.

**Resource Details:**
- Resource Group: `myweb`
- Resource Name: `web`
- Domain: `www.kangxh.com`
- Default URL: `yellow-grass-0e9681800.6.azurestaticapps.net`

## Rationale

### Pros
1. **Free tier perfect for Phase 1**
   - 100 GB bandwidth/month
   - Custom domains + SSL included
   - $0 cost (saves MSDN credits)

2. **Future-proof for Phase 2**
   - Built-in Azure Functions support
   - Native authentication providers
   - Seamless API integration
   - Database connectivity (Cosmos DB)

3. **Excellent developer experience**
   - GitHub Actions integration
   - Automatic deployments
   - Preview environments for PRs
   - Easy rollbacks

4. **Azure ecosystem advantages**
   - Already using Azure (MSDN subscription)
   - Easy integration with other Azure services
   - Familiar Azure Portal interface
   - Good documentation and support

5. **No platform migration needed**
   - Phase 1 → Phase 2 is additive (just add `/api` folder)
   - No rehosting or reconfiguration
   - Single deployment pipeline

### Cons
1. **Azure lock-in**
   - Harder to migrate to other platforms later
   - Azure-specific configurations

2. **Cold start latency**
   - Azure Functions have cold start delays
   - Less critical for Phase 1 (static only)

3. **Limited customization**
   - Less control than VMs or containers
   - Constrained by platform capabilities

4. **Regional limitations**
   - Not all regions support all features
   - May have latency for some global users

### Alternatives Considered

#### Alternative 1: Netlify
- **Pros**: Popular, great DX, generous free tier, excellent docs
- **Cons**: Not Azure ecosystem, would need separate backend later, less integration
- **Rejected because**: Phase 2 requires Azure Functions/Cosmos DB anyway

#### Alternative 2: Vercel
- **Pros**: Excellent performance, great for Next.js/React, good free tier
- **Cons**: Not Azure ecosystem, optimized for Vercel's stack, separate backend needed
- **Rejected because**: Doesn't leverage MSDN Azure subscription

#### Alternative 3: GitHub Pages
- **Pros**: Free, simple, GitHub-native
- **Cons**: No serverless APIs, no authentication, no Phase 2 path, Jekyll-focused
- **Rejected because**: Can't support Phase 2 dynamic features

#### Alternative 4: Azure App Service
- **Pros**: Full control, supports any framework, Azure-native
- **Cons**: Expensive (~$70/month for P0v3), overkill for static site, no free tier
- **Rejected because**: Too expensive for Phase 1, Static Web Apps better fit

#### Alternative 5: Azure Blob Storage + CDN
- **Pros**: Very cheap, simple for static hosting
- **Cons**: No built-in CI/CD, no API support, manual SSL setup, no Phase 2 path
- **Rejected because**: More setup, no serverless API path

#### Alternative 6: Self-hosted (VPS/VM)
- **Pros**: Full control, any technology
- **Cons**: Maintenance burden, security updates, manual scaling, costs time
- **Rejected because**: Solo developer, want to focus on content not infrastructure

## Implementation

### Phase 1: Static Site (Current)

**Architecture:**
```
GitHub Repository
  ↓ (push to master)
GitHub Actions
  ↓ (build MkDocs)
Azure Static Web Apps
  ↓ (serve via CDN)
Users (www.kangxh.com)
```

**Setup:**
1. ✅ Created resource: `myweb/web`
2. ✅ Configured custom domain: `www.kangxh.com`
3. ✅ DNS configured in GoDaddy
4. ⏳ GitHub deployment (pending account)

### Phase 2: Dynamic Features (Future)

**Architecture:**
```
GitHub Repository
  ├── mkdocs-docs/ (static)
  └── api/ (Azure Functions)
       ↓
Azure Static Web Apps
  ├── Static site
  └── Serverless APIs
       ↓
Cosmos DB (user data, tracking)
```

**Migration:**
- Add `/api` folder with Azure Functions
- Update GitHub Actions workflow
- Add Cosmos DB connection
- No redeployment of static site needed

### Cost Projection

**Phase 1 (Free Tier):**
- Static Web Apps: $0/month
- Bandwidth: 100 GB free
- Custom domain + SSL: $0
- **Total: $0/month**

**Phase 2 (Still Mostly Free):**
- Static Web Apps: $0/month
- Azure Functions: 1M requests/month free
- Cosmos DB: Free tier (1000 RU/s, 25 GB)
- **Estimated: $0-5/month** (only if exceed free tiers)

**Remaining MSDN Credit:**
- Current: ~$75-85/month used (Container Registry + App Service)
- After NextPM: ~$75-90/month used
- **Budget remaining: $60-75/month for other projects**

## Consequences

### Positive
- ✅ Zero cost for Phase 1
- ✅ Seamless path to Phase 2 without migration
- ✅ Professional hosting with global CDN
- ✅ Automatic SSL certificate management
- ✅ GitHub Actions integration
- ✅ Preview deployments for testing

### Negative
- ⚠️ Locked into Azure ecosystem
- ⚠️ Learning curve for Azure-specific features
- ⚠️ Cold start delays for APIs (Phase 2)

### Neutral
- Can evaluate alternatives if requirements change significantly
- Free tier sufficient for foreseeable traffic
- Upgrade path available if needed (Standard tier $9/month)

## Compliance

This decision is documented in:
- `/meta/deployment.md` - Deployment guide
- `/project/specs/0.00-project-start.md` - Tech stack section
- `.github/workflows/azure-deploy.yml` - Deployment workflow
- This ADR

## Related Decisions

- Complements MkDocs Material choice (ADR not yet written)
- Informs Phase 2 architecture planning
- Supports FastAPI + HTMX approach for Phase 2

## Review Date

**Next review:** When starting Phase 2 implementation (estimated April-May 2026)

**Review criteria:**
- Is Free tier still sufficient for traffic?
- Has Azure Static Web Apps met expectations?
- Are there better alternatives for Phase 2 needs?
- Cost still within MSDN budget?

## Success Metrics

**Phase 1:**
- [ ] Successful deployment via GitHub Actions
- [ ] Custom domain working with SSL
- [ ] Site loads in <2 seconds globally
- [ ] Zero downtime in first 3 months

**Phase 2:**
- [ ] API endpoints respond in <1 second (warm)
- [ ] Cosmos DB integration working
- [ ] Authentication functional
- [ ] Still within free/low-cost tiers

## Notes

- Resource created: 2026-02-04
- DNS configured: 2026-02-04
- Deployment pending GitHub account setup
- Default URL: `yellow-grass-0e9681800.6.azurestaticapps.net`
- Custom domain: `www.kangxh.com`

## References

- [Azure Static Web Apps Documentation](https://docs.microsoft.com/en-us/azure/static-web-apps/)
- [Azure Static Web Apps Pricing](https://azure.microsoft.com/en-us/pricing/details/app-service/static/)
- [Azure Functions Pricing](https://azure.microsoft.com/en-us/pricing/details/functions/)

---

**Status History:**
- 2026-02-04: Proposed and Accepted
- Implementation: In Progress (resource created, deployment pending)
