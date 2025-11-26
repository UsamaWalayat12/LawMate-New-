# ChromaDB "Permission Denied" Error - Troubleshooting Guide

## Problem
When deploying to Render, getting:
```
chromadb.errors.ChromaError: Permission denied.
```

This means the API key doesn't have access to the specified tenant/database.

## Root Causes

1. **Invalid API Key** - Key is expired, revoked, or incorrect
2. **Wrong Tenant ID** - Doesn't match the API key's tenant
3. **Wrong Database Name** - Database doesn't exist or name is misspelled
4. **API Key Permissions** - Key doesn't have access to this database
5. **Network/Firewall** - Render can't reach Chroma Cloud API

## Solution Steps

### Step 1: Verify Credentials Locally

Run the test script to verify your credentials:

```bash
# Set your environment variables
set CHROMA_API_KEY=your_api_key
set CHROMA_TENANT=your_tenant_id
set CHROMA_DATABASE=your_database_name
set GEMINI_API_KEY=your_gemini_key

# Run the test
python test_chroma_credentials.py
```

Expected output:
```
✓ HttpClient created
✓ Authenticated as: UserIdentity(...)
✓ Collection 'test_collection' accessed
✓ Collection has X documents

✅ SUCCESS: Chroma Cloud credentials are valid!
```

### Step 2: Get Correct Credentials from Chroma Cloud

1. Go to https://console.trychroma.com
2. Log in to your account
3. Navigate to your project/database
4. Find these values:
   - **API Key**: Usually in Settings → API Keys
   - **Tenant ID**: Usually in Settings → Organization
   - **Database Name**: The name of your database (e.g., "Law-Mate")

### Step 3: Update Render Environment Variables

1. Go to Render Dashboard
2. Select your service (lawmate-new)
3. Go to **Environment** tab
4. Update these variables:
   ```
   CHROMA_API_KEY=<your_actual_api_key>
   CHROMA_TENANT=<your_actual_tenant_id>
   CHROMA_DATABASE=<your_actual_database_name>
   GEMINI_API_KEY=<your_gemini_key>
   ```
5. Click **Save** (this will trigger a redeploy)

### Step 4: Verify in Render Logs

After redeploy, check logs for:
```
✓ All Chroma Cloud env vars found!
✓ HttpClient created successfully (v1.3.5 API)
✓ Collection 'pakistan_law' connected (cloud)
✓ Chroma Cloud connected! Documents: [count]
```

## Common Issues & Solutions

| Issue | Solution |
|-------|----------|
| `Permission denied` | Check API key is correct and not expired |
| `Collection not found` | Verify database name matches exactly (case-sensitive) |
| `Tenant not found` | Verify tenant ID is correct |
| `Connection timeout` | Check Render can reach api.trychroma.com (network issue) |
| `Invalid credentials` | Regenerate API key in Chroma Cloud dashboard |

## How to Regenerate API Key

1. Go to https://console.trychroma.com
2. Settings → API Keys
3. Delete the old key
4. Create a new key
5. Copy the new key
6. Update `CHROMA_API_KEY` in Render environment variables
7. Redeploy

## Verify Chroma Cloud Database

Make sure your database exists and has data:

1. Go to https://console.trychroma.com
2. Select your database
3. Check:
   - Database name matches `CHROMA_DATABASE` env var
   - Collections exist (should have "pakistan_law" collection)
   - Documents are present

## Testing Endpoints After Fix

Once deployment succeeds, test the API:

```bash
# Health check
curl https://lawmate-new.onrender.com/health

# API status
curl https://lawmate-new.onrender.com/api/status

# Test chat (should work if Chroma Cloud is connected)
curl -X POST https://lawmate-new.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is contract law?"}'
```

## Debug Mode

To enable more detailed logging, add this to `chroma_test.py`:

```python
DEBUG = True  # Set to True for verbose logging
```

Then redeploy to see more detailed error messages.

## Still Having Issues?

1. **Check Chroma Cloud Status**: https://status.trychroma.com
2. **Verify Network**: Render should be able to reach api.trychroma.com:443
3. **Check API Key Format**: Should be a long string (not a URL or ID)
4. **Contact Chroma Support**: If credentials are correct but still failing

## Quick Checklist

- [ ] API key is valid and not expired
- [ ] Tenant ID matches the API key's tenant
- [ ] Database name exists in Chroma Cloud
- [ ] Environment variables are set correctly in Render
- [ ] No typos in credentials
- [ ] API key has permission to access the database
- [ ] Render can reach api.trychroma.com (no firewall blocking)
