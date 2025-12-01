# Chroma Cloud Deployment Guide

## What We Did

✅ Updated `chroma_test.py` to connect to Chroma Cloud
✅ Code now uses environment variables for cloud credentials

## Next Steps

### 1. Set Environment Variables on Railway

You need to add these 3 variables to Railway:

```
CHROMA_API_KEY=ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd
CHROMA_TENANT=632db25e-e86a-4b90-808a-a221877d15d1
CHROMA_DATABASE=Law-Mate
```

**Option A: Use Railway Dashboard (Easiest)**
1. Go to: https://railway.app/dashboard
2. Select your project "adorable-endurance"
3. Click "Variables" tab
4. Add the 3 variables above
5. Click "Deploy" to redeploy

**Option B: Use Script**
Double-click: `deploy-chroma-cloud.bat`

### 2. Upload Your Data to Chroma Cloud

**IMPORTANT:** You need to upload your local ChromaDB data to Chroma Cloud!

Your local database has 872MB of legal documents, but Chroma Cloud is currently empty.

**Upload Script:**
```python
import chromadb
from chromadb.config import Settings

# Connect to local ChromaDB
local_client = chromadb.PersistentClient(path="ChromaDB")
local_collection = local_client.get_collection("pakistan_law")

# Connect to Chroma Cloud
cloud_client = chromadb.CloudClient(
    api_key='ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd',
    tenant='632db25e-e86a-4b90-808a-a221877d15d1',
    database='Law-Mate'
)

# Create collection in cloud
cloud_collection = cloud_client.create_collection("pakistan_law")

# Get all data from local
all_data = local_collection.get()

# Upload to cloud in batches
batch_size = 100
total = len(all_data['ids'])

for i in range(0, total, batch_size):
    end = min(i + batch_size, total)
    cloud_collection.add(
        ids=all_data['ids'][i:end],
        documents=all_data['documents'][i:end],
        metadatas=all_data['metadatas'][i:end] if all_data['metadatas'] else None,
        embeddings=all_data['embeddings'][i:end] if all_data['embeddings'] else None
    )
    print(f"Uploaded {end}/{total} documents...")

print("Upload complete!")
```

### 3. Deploy to Railway

After setting variables and uploading data:

```bash
railway up
```

### 4. Test

Once deployed:
1. Open your Flutter app
2. Ask: "Contract law and breach of contract"
3. Should get detailed legal answers! ✅

---

## Troubleshooting

**If you get "no evidence" errors:**
- Check Railway logs to see if cloud connection succeeded
- Verify all 3 environment variables are set correctly
- Make sure you uploaded data to Chroma Cloud

**Check Railway Logs:**
```bash
railway logs
```

Look for: "✓ Chroma Cloud connected successfully"
