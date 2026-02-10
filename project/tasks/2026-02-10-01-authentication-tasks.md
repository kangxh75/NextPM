# 2026-02-10-01 Authentication Tasks

**Feature:** Site Authentication (Dual Auth)
**Spec:** [2026-02-10-01-authentication.md](../specs/2026-02-10-01-authentication.md)
**Date:** 2026-02-10

## Task Breakdown

### Phase 1: Configuration & Setup

#### Task 1.1: Create staticwebapp.config.json
- Create root-level configuration file
- Define routes for /prompts/* protection
- Configure Azure AD provider
- Set up redirect rules for unauthorized access
- Add security headers
- **Estimated effort:** 30 minutes

#### Task 1.2: Update .gitignore
- Add api/__pycache__/ pattern
- Add scripts/users.json (local only)
- Ensure Azure Functions cache excluded
- **Estimated effort:** 5 minutes

#### Task 1.3: Update GitHub Actions workflow
- Modify .github/workflows/azure-deploy.yml
- Add api_location: "api" parameter
- No other changes needed
- **Estimated effort:** 5 minutes

### Phase 2: Azure Functions for Basic Auth

#### Task 2.1: Create Azure Functions structure
- Create api/ folder
- Create api/auth/ subfolder
- Create api/host.json runtime config
- Create api/requirements.txt dependencies
- Create api/.funcignore
- **Estimated effort:** 10 minutes

#### Task 2.2: Implement Basic Auth endpoint
- Create api/auth/__init__.py
- Implement credential parsing from Authorization header
- Implement verification logic
- Return Azure Static Web Apps compatible response
- Handle error cases with clear messages
- **Estimated effort:** 45 minutes

#### Task 2.3: Implement user store
- Create api/auth/user_store.py
- Load users from BASIC_AUTH_USERS environment variable
- Verify username/password with SHA-256 hashing
- Return boolean verification result
- **Estimated effort:** 20 minutes

### Phase 3: User Management

#### Task 3.1: Create user management script
- Create scripts/add_user.py
- Generate SHA-256 password hashes
- Accumulate users in local JSON file
- Output formatted JSON for Azure configuration
- Add usage instructions
- **Estimated effort:** 30 minutes

#### Task 3.2: Create scripts folder structure
- Ensure scripts/ folder exists
- Create README if needed
- Document user management workflow
- **Estimated effort:** 10 minutes

### Phase 4: Authentication UI

#### Task 4.1: Create login page
- Create mkdocs-static/auth-choice.html
- Design mobile-friendly layout
- Add Azure AD login button
- Add Basic Auth form with username/password fields
- Implement client-side login logic
- Add error message handling
- Style with gradient background and clean design
- **Estimated effort:** 60 minutes

#### Task 4.2: Test login page locally
- Open in browser
- Test responsive design
- Verify form validation
- Check error message display
- **Estimated effort:** 15 minutes

### Phase 5: Testing & Validation

#### Task 5.1: Validate JSON configuration
- Run python -m json.tool on staticwebapp.config.json
- Ensure valid JSON format
- **Estimated effort:** 2 minutes

#### Task 5.2: Test MkDocs build
- Run mkdocs build --strict
- Ensure no warnings or errors
- Verify all links still work
- **Estimated effort:** 5 minutes

#### Task 5.3: Test user script
- Run scripts/add_user.py with test user
- Verify JSON output format
- Ensure hash generation works
- **Estimated effort:** 5 minutes

#### Task 5.4: Commit implementation
- Add all new files
- Create descriptive commit message with spec ID
- Push to trigger deployment
- **Estimated effort:** 10 minutes

### Phase 6: Azure Configuration (Manual)

#### Task 6.1: Azure AD App Registration
- Navigate to Microsoft Entra ID in Azure Portal
- Create new app registration "NextPM Authentication"
- Configure redirect URI
- Create client secret
- Copy client ID and tenant ID
- **Estimated effort:** 15 minutes

#### Task 6.2: Configure Azure Static Web Apps
- Navigate to Static Web App "web" resource
- Add AZURE_AD_CLIENT_ID environment variable
- Add AZURE_AD_CLIENT_SECRET environment variable
- Add BASIC_AUTH_USERS={} environment variable
- **Estimated effort:** 10 minutes

#### Task 6.3: Update staticwebapp.config.json with tenant ID
- Replace <TENANT_ID> placeholder
- Commit and push update
- **Estimated effort:** 5 minutes

#### Task 6.4: Add initial users
- Add Azure AD users (existing accounts work immediately)
- Or invite guest users via Azure Portal
- For Basic Auth: run add_user.py script
- Update BASIC_AUTH_USERS in Azure configuration
- **Estimated effort:** 10 minutes per user

### Phase 7: Post-Deployment Testing

#### Task 7.1: Test public access
- Visit www.kangxh.com in incognito
- Verify home page loads without auth
- Verify /engineering/ loads without auth
- Verify /examples/ loads without auth
- Verify /about/ loads without auth
- **Estimated effort:** 5 minutes

#### Task 7.2: Test protected access
- Visit www.kangxh.com/prompts/
- Verify redirect to login page
- **Estimated effort:** 2 minutes

#### Task 7.3: Test Azure AD login
- Click "Sign in with Microsoft"
- Complete OAuth flow
- Verify access to /prompts/
- Test logout
- **Estimated effort:** 10 minutes

#### Task 7.4: Test Basic Auth login
- Click "Sign in with Username/Password"
- Enter valid credentials
- Verify access to /prompts/
- Test logout
- **Estimated effort:** 10 minutes

#### Task 7.5: Test invalid credentials
- Try wrong password for Basic Auth
- Verify error message displays
- Verify no access granted
- **Estimated effort:** 5 minutes

#### Task 7.6: Cross-browser testing
- Test in Chrome
- Test in Firefox
- Test in Edge
- Test on mobile
- **Estimated effort:** 15 minutes

### Phase 8: Documentation

#### Task 8.1: Create PM Workflow summary
- Create mkdocs-docs/engineering/pm-workflows/2026-02-10-01-authentication.md
- Link to full spec on GitHub
- Document what was planned
- **Estimated effort:** 20 minutes

#### Task 8.2: Create Dev Workflow summary
- Create mkdocs-docs/engineering/dev-workflows/2026-02-10-HHMM-authentication-implementation.md
- Document commit hash
- List all files changed
- Document Azure configuration steps
- Link to PM spec
- **Estimated effort:** 30 minutes

#### Task 8.3: Update mkdocs.yml navigation
- Add PM Workflow entry
- Add Dev Workflow entry
- Maintain chronological order
- **Estimated effort:** 5 minutes

#### Task 8.4: Update CLAUDE.md
- Add authentication configuration notes
- Document user management procedures
- Add environment variable list
- **Estimated effort:** 15 minutes

#### Task 8.5: Update spec with lessons learned
- Document what worked well
- Document challenges encountered
- Update spec status to ✅ Completed
- **Estimated effort:** 15 minutes

## Dependencies

```
Task 1.1 → Task 5.1 (validate JSON)
Task 2.1 → Task 2.2, 2.3 (structure first)
Task 2.2, 2.3 → Task 5.3 (test functions)
Task 3.1 → Task 5.3 (test script)
Task 1.1, 2.1-2.3, 3.1, 4.1 → Task 5.2 (build test)
Task 5.1, 5.2, 5.3 → Task 5.4 (commit)
Task 5.4 → Phase 6 (deployment first)
Phase 6 → Phase 7 (Azure config required)
Phase 7 → Phase 8 (testing before docs)
```

## Risk Items

**High Risk:**
- Task 6.1-6.3: Azure Portal configuration (manual, error-prone)
- Task 7.3-7.4: Authentication testing (depends on correct Azure setup)

**Medium Risk:**
- Task 2.2: Basic Auth implementation (custom logic, needs testing)
- Task 4.1: Login page (client-side JavaScript, browser compatibility)

**Low Risk:**
- Task 1.1: staticwebapp.config.json (well-documented format)
- Task 3.1: User script (simple Python, easy to test)

## Success Criteria

- [ ] All automated tasks (Phase 1-5) completed
- [ ] MkDocs build --strict passes
- [ ] JSON configuration validated
- [ ] User script generates correct output
- [ ] Azure configuration completed (manual)
- [ ] All 7 test scenarios pass
- [ ] Documentation updated (PM/Dev Workflows)
- [ ] CLAUDE.md includes auth notes
- [ ] Lessons learned documented in spec

## Total Estimated Effort

**Automated (Claude Code):** ~4-5 hours
**Manual (Azure Portal):** ~40 minutes
**Testing:** ~1 hour
**Documentation:** ~1.5 hours

**Total:** ~7 hours

---

**Status:** Ready for implementation
**Next Step:** Begin Phase 1 automated tasks
