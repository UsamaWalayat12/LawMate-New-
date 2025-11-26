# Setting Up Chroma Cloud Credentials

## Step 1: Get Your Credentials from Chroma Cloud

1. Go to https://console.trychroma.com
2. Log in to your account
3. Navigate to your project/database
4. Find and copy these values:

### Finding Your API Key
- Go to **Settings** → **API Keys**
- Copy your API key (looks like: `ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd`)

### Finding Your Tenant ID
- Go to **Settings** → **Organization**
- Copy your Tenant ID (looks like: `632db25e-e86a-4b90-808a-a221877d15d1`)

### Finding Your Database Name
- Go to **Databases**
- Find your database name (e.g., `Law-Mate`)

## Step 2: Set Environment Variables Locally

### On Windows (PowerShell):

```powershell
# Set the environment variables
$env:CHROMA_API_KEY = "your_api_key_here"
$env:CHROMA_TENANT = "your_tenant_id_here"
$env:CHROMA_DATABASE = "your_database_name_here"
$env:GEMINI_API_KEY = "your_gemini_api_key_here"

# Verify they are set
echo $env:CHROMA_API_KEY
echo $env:CHROMA_TENANT
echo $env:CHROMA_DATABASE
echo $env:GEMINI_API_KEY
```

### On Windows (Command Prompt):

```cmd
set CHROMA_API_KEY=your_api_key_here
set CHROMA_TENANT=your_tenant_id_here
set CHROMA_DATABASE=your_database_name_here
set GEMINI_API_KEY=your_gemini_api_key_here

# Verify they are set
echo %CHROMA_API_KEY%
echo %CHROMA_TENANT%
echo %CHROMA_DATABASE%
echo %GEMINI_API_KEY%
```

### On Mac/Linux:

```bash
export CHROMA_API_KEY="your_api_key_here"
export CHROMA_TENANT="your_tenant_id_here"
export CHROMA_DATABASE="your_database_name_here"
export GEMINI_API_KEY="your_gemini_api_key_here"

# Verify they are set
echo $CHROMA_API_KEY
echo $CHROMA_TENANT
echo $CHROMA_DATABASE
echo $GEMINI_API_KEY
```

## Step 3: Test Your Credentials

After setting the environment variables, run:

```bash
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

## Step 4: Update Render Environment Variables

Once you've verified credentials locally:

1. Go to https://dashboard.render.com
2. Select your service: **lawmate-new**
3. Click on **Environment** tab
4. Add/Update these variables:
   ```
   CHROMA_API_KEY=your_api_key_here
   CHROMA_TENANT=your_tenant_id_here
   CHROMA_DATABASE=your_database_name_here
   GEMINI_API_KEY=your_gemini_api_key_here
   ```
5. Click **Save** (this triggers a redeploy)

## Step 5: Verify Deployment

After Render redeploys, check the logs:

1. Go to Render Dashboard → lawmate-new → Logs
2. Look for these success messages:
   ```
   ✓ All Chroma Cloud env vars found!
   ✓ HttpClient created successfully (v1.3.5 API)
   ✓ Collection 'pakistan_law' connected (cloud)
   ✓ Chroma Cloud connected! Documents: [count]
   ```

## Troubleshooting

### If you get "Permission denied":
- Check API key is correct (copy-paste from Chroma Cloud dashboard)
- Verify API key hasn't expired
- Try regenerating the API key

### If you get "Collection not found":
- Verify database name matches exactly (case-sensitive)
- Check database exists in Chroma Cloud dashboard

### If you get "Tenant not found":
- Verify tenant ID is correct
- Check it matches your organization ID

## Security Notes

⚠️ **IMPORTANT**: 
- Never commit `.env` file to git (it's already in `.gitignore`)
- Never share your API key publicly
- Regenerate API key if it's been exposed
- Use environment variables for all sensitive data

## Example Credentials Format

```
CHROMA_API_KEY: ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd
CHROMA_TENANT: 632db25e-e86a-4b90-808a-a221877d15d1
CHROMA_DATABASE: Law-Mate
GEMINI_API_KEY: AIzaSyD...
```

(These are examples - use your actual credentials)
