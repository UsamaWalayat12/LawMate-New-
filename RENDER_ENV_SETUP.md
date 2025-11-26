# Render Environment Variables Setup

## Your Chroma Cloud Credentials

Use these values to set up your Render environment variables:

```
CHROMA_API_KEY: ck-78FYpMeYchrNdWQyvPadg4HXfWXygWCBtCiyUiZz9X6t
CHROMA_TENANT: 632db25e-e86a-4b90-808a-a221877d15d1
CHROMA_DATABASE: Law-Mate
```

## Steps to Update Render

1. Go to https://dashboard.render.com
2. Select your service: **lawmate-new**
3. Click on **Environment** tab
4. Add/Update these environment variables:

| Key | Value |
|-----|-------|
| `CHROMA_API_KEY` | `ck-78FYpMeYchrNdWQyvPadg4HXfWXygWCBtCiyUiZz9X6t` |
| `CHROMA_TENANT` | `632db25e-e86a-4b90-808a-a221877d15d1` |
| `CHROMA_DATABASE` | `Law-Mate` |
| `GEMINI_API_KEY` | Your Google Gemini API key |
| `PORT` | `8000` |
| `PYTHONUNBUFFERED` | `true` |

5. Click **Save** (this will trigger an automatic redeploy)

## What Happens Next

1. Render will automatically redeploy your service
2. Check the logs to verify connection:
   ```
   ✓ All Chroma Cloud env vars found!
   ✓ CloudClient created successfully (v1.3.5 API)
   ✓ Collection 'pakistan_law' connected (cloud)
   ✓ Chroma Cloud connected! Documents: [count]
   ```

## Test the API

Once deployment completes, test:

```bash
# Health check
curl https://lawmate-new.onrender.com/health

# API status
curl https://lawmate-new.onrender.com/api/status

# Test chat endpoint
curl -X POST https://lawmate-new.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is contract law?"}'
```

## Code Changes

The code has been updated to use `CloudClient` instead of `HttpClient`:

```python
client_chroma = chromadb.CloudClient(
    api_key=CHROMA_API_KEY,
    tenant=CHROMA_TENANT,
    database=CHROMA_DATABASE
)
```

This is the correct API for ChromaDB 1.3.5 with Chroma Cloud.

## Status

✅ Code updated and pushed to GitHub
⏳ Waiting for you to update Render environment variables
⏳ Render will auto-deploy once env vars are saved
