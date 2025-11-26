# Render Deployment - ChromaDB '_type' Error Fix

## Problem
When deploying to Render, the application was failing with:
```
KeyError: '_type'
File "chromadb/api/configuration.py", line 209, in from_json
```

## Root Cause
The ChromaDB HttpClient was not properly formatting the authentication credentials for v1.3.4. The `auth_credentials` parameter expects a specific `AuthToken` object, not a plain string.

## Solution
Updated the ChromaDB connection code to use the correct authentication format for v1.3.5:

### Before (Broken):
```python
client_chroma = chromadb.HttpClient(
    host="api.trychroma.com",
    port=443,
    ssl=True,
    tenant_name=CHROMA_TENANT,
    database_name=CHROMA_DATABASE,
    auth_credentials=chromadb.auth.AuthToken(token=CHROMA_API_KEY)  # ❌ AuthToken doesn't exist in v1.3.5
)
```

### After (Fixed):
```python
client_chroma = chromadb.HttpClient(
    host="api.trychroma.com",
    port=443,
    ssl=True,
    tenant_name=CHROMA_TENANT,
    database_name=CHROMA_DATABASE,
    headers={"Authorization": f"Bearer {CHROMA_API_KEY}"}  # ✓ Correct format for v1.3.5
)
```

## Changes Made

**File: `chroma_test.py` (lines 93-104)**
- Changed authentication from `auth_credentials` to `headers` with Bearer token
- Added proper error handling for cloud connection failures
- Changed fallback to use `get_or_create_collection()` instead of `get_collection()`
- Prevents fallback to corrupted local DB when cloud vars are set

## Deployment Steps

1. **Push the fix** (already done):
   ```bash
   git add chroma_test.py requirements.txt
   git commit -m "Fix ChromaDB v1.3.4 connection with proper AuthToken format"
   git push origin main
   ```

2. **Render will auto-deploy** when you push to main branch

3. **Monitor the logs** in Render Dashboard to verify:
   ```
   ✓ All Chroma Cloud env vars found!
   ✓ HttpClient created successfully (v1.3.4 API)
   ✓ Collection 'pakistan_law' connected (cloud)
   ✓ Chroma Cloud connected! Documents: [count]
   ```

## Verification

After deployment, test the API:

```bash
# Check health
curl https://lawmate-new.onrender.com/health

# Test chat endpoint
curl -X POST https://lawmate-new.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is contract law?"}'
```

## Environment Variables Required on Render

Ensure these are set in Render Dashboard → Environment:
- `CHROMA_API_KEY` - Your Chroma Cloud API key
- `CHROMA_TENANT` - Your Chroma Cloud tenant ID
- `CHROMA_DATABASE` - Your Chroma Cloud database name
- `GEMINI_API_KEY` - Your Google Gemini API key
- `PORT` - 8000 (or your preferred port)
- `PYTHONUNBUFFERED` - true

## ChromaDB Version Info

- **Installed Version**: 1.3.5
- **API Used**: HttpClient with Bearer token in headers
- **Connection Type**: Cloud (api.trychroma.com)
- **Port**: 443 (SSL/TLS)
- **Authentication**: Bearer token passed in Authorization header

## Troubleshooting

If you still see errors:

1. **Check Render logs** for the exact error message
2. **Verify environment variables** are correctly set
3. **Test locally** with same env vars:
   ```bash
   set CHROMA_API_KEY=your_key
   set CHROMA_TENANT=your_tenant
   set CHROMA_DATABASE=your_db
   set GEMINI_API_KEY=your_gemini_key
   python chroma_test.py
   ```
4. **Check Chroma Cloud dashboard** to ensure database exists and is accessible

## Next Steps

- Monitor Render logs for any new errors
- Test all API endpoints
- Set up error monitoring/alerts
- Consider upgrading Render plan if needed for production
