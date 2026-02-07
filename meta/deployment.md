# Deployment Guide

This document explains how to deploy NextPM to Azure Static Web Apps using GitHub Actions.

## Prerequisites

Before deploying, ensure you have:

- [x] GitHub account (personal account ready)
- [x] Repository pushed to GitHub
- [ ] Azure subscription (MSDN or other)
- [ ] Azure Static Web Apps resource created

## CI/CD Pipelines

### 1. Build and Test Workflow

**File:** `.github/workflows/build-and-test.yml`

**Triggers:**
- Push to `master` or `main` branch
- Pull requests to `master` or `main` branch

**What it does:**
- Checks out code
- Sets up Python 3.12
- Installs dependencies from `requirements.txt`
- Builds MkDocs site with `--strict` flag (fails on warnings)
- Uploads build artifacts for review

**Status:** Ready to run when repository is on GitHub

### 2. Azure Deployment Workflow

**File:** `.github/workflows/azure-deploy.yml`

**Triggers:**
- Push to `master` or `main` branch
- Manual workflow dispatch

**What it does:**
- Builds MkDocs site
- Deploys to Azure Static Web Apps
- Uses deployment token from GitHub secrets

**Status:** Requires Azure setup (see below)

## Azure Setup (When Ready)

### Step 1: Create Azure Static Web Apps Resource

1. Go to [Azure Portal](https://portal.azure.com)
2. Click "Create a resource"
3. Search for "Static Web Apps"
4. Click "Create"

**Configuration:**
- **Subscription:** Your MSDN subscription
- **Resource Group:** Create new `rg-nextpm` or use existing
- **Name:** `nextpm-prod` (or your preference)
- **Plan type:** Free (perfect for Phase 1)
- **Region:** Choose closest to your users (e.g., East Asia, East US)
- **Deployment source:** GitHub (will configure later)

5. Click "Review + Create"
6. Click "Create"

### Step 2: Get Deployment Token

After the resource is created:

1. Go to your Static Web Apps resource
2. Click "Manage deployment token" in the Overview page
3. Copy the deployment token (keep it secure!)

### Step 3: Add GitHub Secret

1. Go to your GitHub repository
2. Settings → Secrets and variables → Actions
3. Click "New repository secret"
4. Name: `AZURE_STATIC_WEB_APPS_API_TOKEN`
5. Value: Paste the deployment token from Step 2
6. Click "Add secret"

### Step 4: Configure Custom Domain (Optional)

After deployment is successful:

1. Go to your Static Web Apps resource
2. Click "Custom domains"
3. Click "Add"
4. Choose "Custom domain on other DNS"
5. Enter: `kangxh.com` or `nextpm.kangxh.com`
6. Follow DNS configuration instructions

**DNS Records Needed:**
- **Type:** CNAME or ALIAS
- **Name:** `@` (for root) or `nextpm` (for subdomain)
- **Value:** Your Azure Static Web Apps URL

### Step 5: Trigger First Deployment

Once secrets are configured:

1. Push a commit to `master` or `main` branch, OR
2. Go to Actions → Azure Deploy → Run workflow

The deployment will:
- Build your MkDocs site
- Deploy to Azure Static Web Apps
- Show deployment URL in the workflow logs

## Post-Deployment Checklist

After first successful deployment:

- [ ] Visit the Azure Static Web Apps URL
- [ ] Verify site loads correctly
- [ ] Test all navigation links
- [ ] Configure custom domain (if desired)
- [ ] Set up Google Analytics (update `mkdocs.yml`)
- [ ] Update `mkdocs.yml` with actual GitHub username and repo URL

## Monitoring and Maintenance

### View Deployment Logs

- **GitHub Actions:** Repository → Actions tab
- **Azure Portal:** Static Web Apps resource → Deployment history

### Deployment URL

Your site will be available at:
- **Azure default URL:** `https://nextpm-prod.azurestaticapps.net` (example)
- **Custom domain:** `https://kangxh.com` (when configured)

### Automatic Deployments

Every push to `master` or `main` will trigger:
1. Build and test workflow (validates build)
2. Azure deployment workflow (deploys if build succeeds)

### Manual Deployment

You can manually trigger deployment:
1. Go to repository → Actions
2. Select "Deploy to Azure Static Web Apps"
3. Click "Run workflow"
4. Choose branch and click "Run workflow"

## Troubleshooting

### Build Fails

**Check:**
- MkDocs configuration in `mkdocs.yml`
- All referenced files exist in `mkdocs-docs/`
- Python dependencies in `requirements.txt`
- Build logs in GitHub Actions

**Fix:**
- Test locally first: `mkdocs build --strict`
- Fix any warnings or errors
- Push the fix

### Deployment Fails

**Check:**
- Azure deployment token is correctly set in GitHub secrets
- Azure Static Web Apps resource is running
- Deployment logs in GitHub Actions

**Fix:**
- Regenerate deployment token in Azure Portal
- Update GitHub secret
- Re-run workflow

### Site Doesn't Update

**Check:**
- Workflow ran successfully (green checkmark)
- CDN cache may take a few minutes to update

**Fix:**
- Wait 2-5 minutes for CDN propagation
- Hard refresh browser (Ctrl+Shift+R / Cmd+Shift+R)
- Check Azure deployment history

### Custom Domain Issues

**Check:**
- DNS records are correctly configured
- DNS propagation can take 24-48 hours
- Use [DNS Checker](https://dnschecker.org) to verify

## Cost Considerations

**Azure Static Web Apps Free Tier:**
- 100 GB bandwidth/month
- 0.5 GB storage
- Custom domains included
- SSL certificates included (auto-renewed)

**Should be sufficient for:**
- Phase 1 (static site)
- Moderate traffic (thousands of monthly visitors)

**Upgrade needed when:**
- Traffic exceeds free tier limits
- Need custom authentication providers
- Need staging environments

## Security Notes

**GitHub Secrets:**
- Never commit deployment tokens to git
- Rotate tokens periodically (every 6-12 months)
- Use least privilege (repo-specific tokens)

**Azure:**
- Static Web Apps are secure by default
- HTTPS is enforced automatically
- No server-side code execution in Phase 1

## Next Steps After Deployment

1. **Test thoroughly:** Verify all functionality works
2. **Set up monitoring:** Configure Azure Application Insights (optional)
3. **Enable analytics:** Update Google Analytics ID in `mkdocs.yml`
4. **Share the site:** Announce on LinkedIn, Twitter, etc.
5. **Gather feedback:** Use analytics and direct feedback

## References

- [Azure Static Web Apps Documentation](https://docs.microsoft.com/en-us/azure/static-web-apps/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [MkDocs Deployment Guide](https://www.mkdocs.org/user-guide/deploying-your-docs/)

---

**Questions?** Check the AI context files or ask your AI assistant, pointing them to this document.
