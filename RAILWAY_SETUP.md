# Railway Deployment Setup Guide

## Overview
This guide walks through deploying LawMate to Railway instead of Render.

## Prerequisites
1. Railway account (https://railway.app)
2. GitHub repository with your code
3. Environment variables configured

## Step 1: Create Railway Project

1. Go to https://railway.app
2. Click "New Project"
3. Select "Deploy from GitHub"
4. Connect your GitHub account
5. Select your repository
6. Railway will automatically detect the Dockerfile

## Step 2: Configure Environment Variables

In Railway Dashboard:
1. Go to your project
2. Click on the service
3. Go to "Variables" tab
4. Add these environment variables:

```
GOOGLE_API_KEY=your_google_api_key_here
CHROMA_API_KEY=ck-78FYpMeYchrNdWQyvPadg4HXfWXygWCBtCiyUiZz9X6t
CHROMA_TENANT_ID=632db25e-e86a-4b90-808a-a221877d15d1
CHROMA_COLLECTION=pakistan_law
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=production
```

## Step 3: Configure Build & Deploy Settings

In Railway Dashboard:
1. Go to "Settings" tab
2. Build Command: Leave empty (uses Dockerfile)
3. Start Command: Leave empty (uses Dockerfile CMD)
4. Root Directory: `/` (or your project root)

## Step 4: Deploy

1. Click "Deploy" button
2. Railway will build and deploy automatically
3. Monitor logs in the "Logs" tab

## Step 5: Get Your Service URL

1. Go to "Settings" tab
2. Look for "Domains" section
3. Your service URL will be: `https://lawmate-new.up.railway.app` (or similar)

## Monitoring

- **Logs**: View real-time logs in the Logs tab
- **Metrics**: Check CPU, Memory, Network usage
- **Health**: Endpoint `/health` is monitored automatically

## Troubleshooting

### Service won't start
- Check logs for errors
- Verify all environment variables are set
- Ensure PORT is set to 8000

### ChromaDB connection fails
- Verify CHROMA_API_KEY is correct
- Check CHROMA_TENANT_ID
- Ensure collection exists in Chroma Cloud

### Port binding error
- Railway automatically assigns PORT
- Ensure backend_api.py uses `os.getenv('PORT', 8000)`

## Redeployment

To redeploy after code changes:
1. Push changes to GitHub
2. Railway automatically redeploys
3. Or manually trigger in Dashboard > Deploy

## Rollback

To rollback to previous deployment:
1. Go to "Deployments" tab
2. Click on previous deployment
3. Click "Rollback"

## Cost Considerations

- Railway free tier: $5/month credit
- Paid plans start at $5/month
- See pricing at https://railway.app/pricing

## Key Differences from Render

| Feature | Render | Railway |
|---------|--------|---------|
| Deployment | YAML config | Dockerfile |
| Auto-deploy | GitHub webhook | GitHub integration |
| Environment | render.yaml | Railway Dashboard |
| Logs | Web UI | Web UI |
| Pricing | $7/month minimum | $5/month credit |

## Next Steps

1. Push code to GitHub
2. Create Railway project
3. Set environment variables
4. Deploy
5. Test endpoints at your Railway URL
