# Document Retrieval Fix - "No Documents Found" Issue

## Problem
Every query was returning:
```
I apologize, but I couldn't find specific legal documents matching your query in the database...
```

This meant the `retrieve_and_filter()` function was returning an empty list for all queries.

## Root Cause
Two issues were preventing document retrieval:

1. **Embedding Model Not Loaded**: The code was skipping the embedding model initialization when using Chroma Cloud, but Chroma Cloud still requires embeddings for queries
2. **Wrong Query Method**: The code was using `query_texts` (text-based query) instead of `query_embeddings` (embedding-based query)

## Solution

### Issue 1: Always Load Embedding Model

**Before:**
```python
USING_CHROMA_CLOUD = bool(os.environ.get("CHROMA_API_KEY"))

if USING_CHROMA_CLOUD:
    print("Using Chroma Cloud - skipping local embedding model")
    model = None  # ❌ Model not loaded!
else:
    model = SentenceTransformer(MODEL_NAME)
```

**After:**
```python
# Always load embedding model (needed for both local and cloud)
print("Loading embedding model:", MODEL_NAME)
model = SentenceTransformer(MODEL_NAME)  # ✓ Always load!
```

### Issue 2: Use Embeddings for Chroma Cloud Queries

**Before:**
```python
if using_cloud:
    # ❌ Wrong: text-based query
    res = col.query(
        query_texts=[query],
        n_results=top_k,
        include=['documents', 'metadatas', 'distances']
    )
```

**After:**
```python
if using_cloud:
    # ✓ Correct: embedding-based query
    q_emb = model.encode(query, convert_to_numpy=True).tolist()
    res = col.query(
        query_embeddings=[q_emb],
        n_results=top_k,
        include=['documents', 'metadatas', 'distances']
    )
```

## Changes Made

**File: `chroma_test.py`**

1. **Lines 56-64**: Always load embedding model regardless of Chroma Cloud usage
2. **Lines 198-209**: Use `query_embeddings` for Chroma Cloud queries instead of `query_texts`

## How It Works Now

1. **Embedding Model Loads**: SentenceTransformer loads on startup
2. **Query Comes In**: User asks a question
3. **Embedding Generated**: Query is converted to embeddings using the model
4. **Chroma Cloud Searches**: Embeddings are sent to Chroma Cloud for similarity search
5. **Documents Retrieved**: Matching documents are returned
6. **RAG Pipeline**: Documents are used to generate AI response

## Testing

After Render redeploys, test with:

```bash
curl -X POST https://lawmate-new.onrender.com/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is contract law?"}'
```

Expected response:
```json
{
  "success": true,
  "answer": "Based on the legal documents in our database, contract law is...",
  "timestamp": "2025-11-26T...",
  "message_id": "msg_1"
}
```

## Deployment Status

✅ Code fixed and pushed to GitHub
⏳ Render will auto-deploy
⏳ Check logs for: `✓ Loaded embedding model: all-mpnet-base-v2`

## Expected Log Output

```
Loading embedding model: all-mpnet-base-v2
✓ Loaded embedding model: all-mpnet-base-v2
============================================================
CHROMA CONNECTION DIAGNOSTIC
============================================================
✓ All Chroma Cloud env vars found!
✓ CloudClient created successfully (v1.3.5 API)
✓ Collection 'pakistan_law' connected (cloud)
✓ Chroma Cloud connected! Documents: [count]

[API] Processing query: What is contract law?
[DEBUG] Using Chroma Cloud with embeddings: What is contract law?
[API] Retrieved 5 evidence documents
[API] Calling Gemini AI...
[API] Received AI response (1234 chars)
```

## Key Points

- **Embedding Model**: `all-mpnet-base-v2` (same as used during data ingestion)
- **Query Method**: Vector similarity search using embeddings
- **Chroma Cloud**: Handles the vector database and similarity matching
- **Gemini AI**: Uses retrieved documents to generate answers

## Troubleshooting

If still getting "no documents found":

1. **Check embedding model loaded**: Look for `✓ Loaded embedding model` in logs
2. **Check Chroma Cloud connection**: Look for `✓ Chroma Cloud connected!` in logs
3. **Check document count**: Should show `Documents: [number > 0]`
4. **Check query debug output**: Should show `[DEBUG] Using Chroma Cloud with embeddings`

If documents still not found:
- Verify data was uploaded to Chroma Cloud
- Check database has "pakistan_law" collection
- Verify collection has documents
