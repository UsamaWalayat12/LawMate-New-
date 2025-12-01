# Migration from Render to Railway

## Overview
This document outlines the migration from Render to Railway deployment platform.

## Why Railway?
- **Better Performance**: Faster deployments and better resource allocation
- **Cost-Effective**: $5/month credit (vs Render's $7/month minimum)
- **Simpler Setup**: GitHub integration with automatic deployments
- **Better Monitoring**: Real-time logs and metrics
- **Flexible Scaling**: Easy to scale up/down as needed

## Current Status

### ✅ Already Configured
- Dockerfile is production-ready
- requirements.txt has all dependencies
- backend_api.py is properly configured
- railway.json is set up
- Environment variables documented in .env.example
- Chroma Cloud integration working

### ❌ To Remove
- render.yaml (no longer needed)
- Render-specific documentation

## Migration Steps

### Step 1: Prepare Code
```bash
# Ensure all code is committed and pushed to GitHub
git add .
git commit -m "Prepare for Railway migration"
git push origin main
```

### Step 2: Create Railway Project
1. Go to https://railway.app
2. Sign in or create account
3. Click "New Project"
4. Select "Deploy from GitHub"
5. Connect your GitHub account
6. Select your repository
7. Click "Deploy"

### Step 3: Configure Environment Variables
In Railway Dashboard:
1. Go to your project
2. Click on the service
3. Go to "Variables" tab
4. Add these variables:

```
GOOGLE_API_KEY=your_google_api_key_here
CHROMA_API_KEY=ck-78FYpMeYchrNdWQyvPadg4HXfWXygWCBtCiyUiZz9X6t
CHROMA_TENANT_ID=632db25e-e86a-4b90-808a-a221877d15d1
CHROMA_COLLECTION=pakistan_law
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=production
```

### Step 4: Monitor Deployment
1. Go to "Logs" tab
2. Watch for build completion
3. Verify "Deployment successful" message
4. Note the service URL

### Step 5: Test Deployment
```bash
# Replace YOUR_RAILWAY_URL with your actual URL
curl https://YOUR_RAILWAY_URL/health
curl https://YOUR_RAILWAY_URL/api/status
```

### Step 6: Update Documentation
- Update README.md to reference Railway
- Remove Render references
- Update API documentation with new URL

### Step 7: Cleanup (Optional)
- Delete Render project if no longer needed
- Remove render.yaml from repository
- Archive Render-related documentation

## File Structure

### Keep These Files
```
Dockerfile                          # Used by Railway
railway.json                        # Railway configuration
requirements.txt                    # Python dependencies
backend_api.py                      # Main application
chroma_test.py                      # RAG functionality
.env.example                        # Environment template
```

### Remove These Files (Optional)
```
render.yaml                         # Render configuration
RENDER_DEPLOYMENT.md               # Render documentation
RENDER_ENV_SETUP.md                # Render setup guide
RENDER_CHROMADB_FIX.md            # Render-specific fixes
```

## Configuration Comparison

| Aspect | Render | Railway |
|--------|--------|---------|
| Config File | render.yaml | railway.json |
| Build | YAML-based | Dockerfile |
| Deployment | Webhook | GitHub integration |
| Environment | render.yaml | Dashboard |
| Logs | Web UI | Web UI |
| Health Check | Configured in YAML | Configured in JSON |
| Restart Policy | Limited | Configurable |

## Environment Variables

### Required
- `GOOGLE_API_KEY` - Google Gemini API key
- `CHROMA_API_KEY` - Chroma Cloud API key
- `CHROMA_TENANT_ID` - Chroma Cloud tenant ID
- `CHROMA_COLLECTION` - Collection name (pakistan_law)

### Optional
- `PORT` - Server port (default: 8000)
- `HOST` - Server host (default: 0.0.0.0)
- `ENVIRONMENT` - Environment name (production/development)

## Deployment Process

### Automatic (Recommended)
1. Push code to GitHub
2. Railway automatically detects changes
3. Builds and deploys automatically
4. No manual intervention needed

### Manual
```bash
# Using Railway CLI
railway login
railway up
```

## Monitoring & Logs

### View Logs
- Go to Railway Dashboard
- Click on your service
- Go to "Logs" tab
- View real-time logs

### View Metrics
- Go to Railway Dashboard
- Click on your service
- Go to "Metrics" tab
- Monitor CPU, Memory, Network

### Set Alerts
- Go to "Settings" tab
- Configure alerts for errors
- Get notified of deployment issues

## Troubleshooting

### Build Fails
**Problem**: Deployment fails during build
**Solution**: 
- Check Dockerfile syntax
- Verify all dependencies in requirements.txt
- Check logs for specific errors

### Service Won't Start
**Problem**: Build succeeds but service won't start
**Solution**:
- Verify PORT environment variable is set
- Check GOOGLE_API_KEY is valid
- Verify backend_api.py runs locally

### ChromaDB Connection Error
**Problem**: Service starts but can't connect to Chroma Cloud
**Solution**:
- Verify CHROMA_API_KEY is correct
- Check CHROMA_TENANT_ID
- Ensure collection exists in Chroma Cloud
- Check network connectivity

### Slow Response Times
**Problem**: API responses are slow
**Solution**:
- Check CPU/Memory metrics
- Review logs for bottlenecks
- Consider upgrading Railway plan
- Optimize database queries

## Performance Tips

1. **Use Connection Pooling**: Reuse database connections
2. **Cache Results**: Cache frequent queries
3. **Optimize Queries**: Use indexes in Chroma
4. **Monitor Metrics**: Watch CPU and memory
5. **Scale Vertically**: Upgrade plan if needed

## Cost Analysis

### Render
- Minimum: $7/month
- Includes: 0.5 CPU, 512MB RAM
- Overage: $0.25/hour per additional resource

### Railway
- Free tier: $5/month credit
- Paid: Pay-as-you-go after credit
- Includes: Generous free tier
- Overage: Charged only for usage

## Rollback Procedure

If something goes wrong:

1. Go to Railway Dashboard
2. Click on your service
3. Go to "Deployments" tab
4. Find previous working deployment
5. Click "Rollback"
6. Service will revert to previous version

## Next Steps

1. ✅ Prepare code (push to GitHub)
2. ✅ Create Railway project
3. ✅ Configure environment variables
4. ✅ Monitor deployment
5. ✅ Test endpoints
6. ✅ Update documentation
7. ✅ Cleanup old Render setup

## Support

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- GitHub Issues: Report issues in repository

## Conclusion

Your LawMate application is now ready for Railway deployment. The migration is straightforward with automatic GitHub integration and better monitoring capabilities.

**Key Benefits**:
- ✅ Automatic deployments on GitHub push
- ✅ Better performance and reliability
- ✅ Lower cost ($5/month vs $7/month)
- ✅ Easier monitoring and logs
- ✅ Flexible scaling options
