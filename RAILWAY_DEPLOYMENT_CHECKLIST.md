# Railway Deployment Checklist

## Pre-Deployment ✓

- [x] Dockerfile exists and is configured
- [x] requirements.txt has all dependencies
- [x] backend_api.py is the entry point
- [x] railway.json is configured
- [x] .env.example documents all required variables
- [x] Code is pushed to GitHub

## Railway Setup Steps

### 1. Create Railway Project
- [ ] Go to https://railway.app
- [ ] Sign in or create account
- [ ] Click "New Project"
- [ ] Select "Deploy from GitHub"
- [ ] Connect GitHub and select repository
- [ ] Click "Deploy"

### 2. Configure Environment Variables
In Railway Dashboard > Variables tab, add:

```
GOOGLE_API_KEY=your_google_api_key_here
CHROMA_API_KEY=ck-78FYpMeYchrNdWQyvPadg4HXfWXygWCBtCiyUiZz9X6t
CHROMA_TENANT_ID=632db25e-e86a-4b90-808a-a221877d15d1
CHROMA_COLLECTION=pakistan_law
PORT=8000
HOST=0.0.0.0
ENVIRONMENT=production
```

- [ ] GOOGLE_API_KEY set
- [ ] CHROMA_API_KEY set
- [ ] CHROMA_TENANT_ID set
- [ ] CHROMA_COLLECTION set
- [ ] PORT set to 8000
- [ ] HOST set to 0.0.0.0

### 3. Monitor Deployment
- [ ] Check Logs tab for build progress
- [ ] Verify no build errors
- [ ] Wait for "Deployment successful" message
- [ ] Note the service URL

### 4. Test Deployment
- [ ] Visit `/health` endpoint
- [ ] Test `/api/status` endpoint
- [ ] Test `/api/chat` with a sample query
- [ ] Verify ChromaDB connection works

## Post-Deployment

### Verify Service
```bash
# Test health endpoint
curl https://your-railway-url/health

# Test status endpoint
curl https://your-railway-url/api/status

# Test chat endpoint
curl -X POST https://your-railway-url/api/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What is the Pakistani Constitution?"}'
```

### Monitor Logs
- [ ] Check Logs tab regularly
- [ ] Set up alerts for errors
- [ ] Monitor CPU and memory usage

### Cleanup (Optional)
- [ ] Remove Render deployment if no longer needed
- [ ] Delete render.yaml if not using Render
- [ ] Update documentation to reference Railway

## Troubleshooting

### Build Fails
- Check Dockerfile syntax
- Verify all dependencies in requirements.txt
- Check logs for specific errors

### Service Won't Start
- Verify PORT environment variable
- Check GOOGLE_API_KEY is valid
- Verify Chroma Cloud credentials

### ChromaDB Connection Error
- Verify CHROMA_API_KEY
- Check CHROMA_TENANT_ID
- Ensure collection exists in Chroma Cloud

### Slow Response Times
- Check CPU/Memory metrics
- Review logs for bottlenecks
- Consider upgrading Railway plan

## Support

- Railway Docs: https://docs.railway.app
- Railway Discord: https://discord.gg/railway
- GitHub Issues: Check project repository
