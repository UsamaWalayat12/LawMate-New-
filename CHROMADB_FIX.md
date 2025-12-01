# ChromaDB Connection Error Fix - '_type' Error

## Problem
The error `ERROR connecting to ChromaDB: '_type'` was occurring when trying to connect to Chroma Cloud. This is a known issue with ChromaDB API compatibility.

## Root Cause
The code was using `chromadb.HttpClient()` with unsupported parameters:
- The `headers` parameter with `'X-Chroma-Token'` is not properly supported in the HttpClient API
- This caused ChromaDB to fail with a `'_type'` validation error

## Solution
Changed from `HttpClient` to `CloudClient` which is the proper API for Chroma Cloud connections.

### Changes Made

**File: `chroma_test.py` (lines 86-114)**

**Before:**
```python
client_chroma = chromadb.HttpClient(
    host='api.trychroma.com',
    ssl=True,
    tenant=CHROMA_TENANT,
    database=CHROMA_DATABASE,
    headers={'X-Chroma-Token': CHROMA_API_KEY}
)
```

**After:**
```python
client_chroma = chromadb.CloudClient(
    api_key=CHROMA_API_KEY,
    tenant=CHROMA_TENANT,
    database=CHROMA_DATABASE
)
```

### Why This Works
- `CloudClient` is the official ChromaDB API for cloud connections
- It properly handles authentication via `api_key` parameter
- It automatically manages tenant and database routing
- No need for manual header configuration

## Testing
To verify the fix works:

```bash
# Set your environment variables
set CHROMA_API_KEY=your_api_key
set CHROMA_TENANT=your_tenant_id
set CHROMA_DATABASE=your_database_name
set GEMINI_API_KEY=your_gemini_key

# Run the test
python chroma_test.py
```

Expected output:
```
✓ All Chroma Cloud env vars found!
  Tenant: [your_tenant_id]
  Database: [your_database_name]
  Attempting cloud connection...
  ✓ CloudClient created successfully
  ✓ Collection 'pakistan_law' connected (cloud)
  ✓ Chroma Cloud connected! Documents: [count]
```

## Additional Changes
- Updated `requirements.txt` to use `chromadb>=0.4.0` for better version compatibility
- Fixed exception handling to properly capture exception variable in line 113

## Deployment
After applying these fixes:
1. Update your environment variables on Railway/Vercel/your deployment platform
2. Reinstall dependencies: `pip install -r requirements.txt`
3. Restart your application
