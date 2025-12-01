# Render Deployment Guide for LawMate API

## Prerequisites
1. Render account (https://render.com)
2. GitHub repository with your code
3. Environment variables configured

## Step 1: Prepare Your Repository

Ensure these files are in your repo:
- `requirements.txt` - Python dependencies
- `backend_api.py` - FastAPI application
- `chroma_test.py` - RAG functions
- `Dockerfile` - Container configuration
- `render.yaml` - Render configuration (optional but recommended)

## Step 2: Create Render Service

1. Go to https://dashboard.render.com
2. Click "New +" → "Web Service"
3. Connect your GitHub repository
4. Fill in the details:
   - **Name**: `lawmate-api`
   - **Runtime**: `Python 3.11`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `python backend_api.py`
   - **Instance Type**: Free (or Starter for production)

## Step 3: Configure Environment Variables

In Render Dashboard, go to your service → Environment:

```
CHROMA_API_KEY=your_chroma_api_key
CHROMA_TENANT=your_tenant_id
CHROMA_DATABASE=your_database_name
GEMINI_API_KEY=your_gemini_api_key
PORT=8000
PYTHONUNBUFFERED=true
```

## Step 4: Deploy

1. Push your code to GitHub
2. Render will automatically deploy when you push to main branch
3. Monitor logs in Render Dashboard

## Troubleshooting

### Error: '_type' in ChromaDB
**Solution**: Ensure `chroma_test.py` uses the correct HttpClient parameters for v1.3.4:
```python
client_chroma = chromadb.HttpClient(
    host="api.trychroma.com",
    port=443,
    ssl=True,
    tenant_name=CHROMA_TENANT,
    database_name=CHROMA_DATABASE,
    auth_credentials=CHROMA_API_KEY
)
```

### Error: Module not found
**Solution**: Check `requirements.txt` includes all dependencies:
```
fastapi==0.104.1
uvicorn[standard]==0.24.0
google-genai
chromadb>=0.4.0
sentence-transformers>=2.2.0
python-multipart==0.0.6
python-dotenv==1.0.0
reportlab>=4.0.0
pydantic==2.5.0
numpy<2.0.0
```

### Error: Connection timeout
**Solution**: 
- Increase health check timeout in Render settings
- Ensure Chroma Cloud credentials are correct
- Check network connectivity from Render region

### Error: Out of memory
**Solution**: 
- Use Starter plan instead of Free
- Optimize embedding model loading
- Consider using Chroma Cloud instead of local DB

## Testing Deployment

After deployment, test the API:

```bash
# Health check
curl https://your-service.onrender.com/health

# API status
curl https://your-service.onrender.com/api/status

# Chat endpoint
curl -X POST https://your-service.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is contract law?"}'
```

## Monitoring

1. View logs: Dashboard → Logs
2. Check metrics: Dashboard → Metrics
3. Set up alerts: Dashboard → Alerts

## Common Issues

| Issue | Solution |
|-------|----------|
| Deployment fails | Check build logs, ensure all dependencies in requirements.txt |
| API returns 500 | Check application logs, verify env vars are set |
| ChromaDB connection fails | Verify API key, tenant, database name are correct |
| Slow responses | Upgrade instance type, optimize queries |

## Production Recommendations

1. Use Starter plan or higher (Free tier has limitations)
2. Enable auto-deploy from GitHub
3. Set up error monitoring (Sentry, etc.)
4. Use environment-specific configs
5. Enable HTTPS (Render provides free SSL)
6. Set up backup for Chroma Cloud data
