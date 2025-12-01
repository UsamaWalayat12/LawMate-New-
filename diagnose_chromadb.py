"""
Diagnostic script to check ChromaDB contents and retrieval
"""
import chromadb
from sentence_transformers import SentenceTransformer

# Configuration
DB_PATH = "ChromaDB"
COLLECTION = "pakistan_law"
MODEL_NAME = "all-mpnet-base-v2"

print("=" * 60)
print("ChromaDB Diagnostic Tool")
print("=" * 60)

# Initialize ChromaDB
try:
    print("\n1. Connecting to ChromaDB...")
    client_chroma = chromadb.PersistentClient(path=DB_PATH)
    print(f"   ✓ Connected to {DB_PATH}")
except Exception as e:
    print(f"   ✗ Failed to connect: {e}")
    exit(1)

# Get collection
try:
    print(f"\n2. Loading collection '{COLLECTION}'...")
    col = client_chroma.get_collection(name=COLLECTION)
    print(f"   ✓ Collection loaded")
except Exception as e:
    print(f"   ✗ Failed to load collection: {e}")
    exit(1)

# Get collection stats
try:
    print("\n3. Collection Statistics:")
    count = col.count()
    print(f"   Total documents: {count}")
    
    if count == 0:
        print("\n   ⚠️  WARNING: Collection is empty!")
        print("   You need to populate the database first.")
        exit(1)
        
except Exception as e:
    print(f"   ✗ Failed to get stats: {e}")

# Sample some documents
try:
    print("\n4. Sampling documents...")
    sample = col.get(limit=5, include=['documents', 'metadatas'])
    
    if sample and 'documents' in sample:
        docs = sample['documents']
        metas = sample.get('metadatas', [])
        
        print(f"   Found {len(docs)} sample documents:")
        for i, (doc, meta) in enumerate(zip(docs, metas), 1):
            print(f"\n   Document {i}:")
            print(f"   - Length: {len(doc)} characters")
            print(f"   - Language: {meta.get('lang', 'unknown')}")
            print(f"   - Source: {meta.get('source', 'unknown')}")
            print(f"   - Preview: {doc[:200]}...")
    else:
        print("   ✗ No documents found in sample")
        
except Exception as e:
    print(f"   ✗ Failed to sample: {e}")

# Test retrieval
try:
    print("\n5. Testing retrieval with sample queries...")
    
    # Load embedding model
    print("   Loading embedding model...")
    model = SentenceTransformer(MODEL_NAME)
    print("   ✓ Model loaded")
    
    test_queries = [
        "legal notice for breach of contract",
        "property transfer process",
        "employment law",
        "contract law"
    ]
    
    for query in test_queries:
        print(f"\n   Query: '{query}'")
        
        # Encode query
        q_emb = model.encode(query, convert_to_numpy=True).tolist()
        
        # Query collection
        res = col.query(
            query_embeddings=[q_emb],
            n_results=10,
            include=['documents', 'metadatas', 'distances']
        )
        
        if res and 'documents' in res and len(res['documents']) > 0:
            docs = res['documents'][0]
            metas = res['metadatas'][0]
            dists = res['distances'][0]
            
            print(f"   Found {len(docs)} results:")
            
            # Check filtering criteria
            filtered_count = 0
            for doc, meta, dist in zip(docs, metas, dists):
                doc_len = len(doc)
                lang = str(meta.get('lang', 'en')).lower()
                
                # Apply same filters as retrieve_and_filter
                if doc_len < 200:
                    print(f"   - FILTERED OUT (too short): {doc_len} chars, lang={lang}")
                    continue
                    
                if lang and not lang.startswith('en') and lang != 'unknown':
                    print(f"   - FILTERED OUT (non-English): {doc_len} chars, lang={lang}")
                    continue
                
                filtered_count += 1
                print(f"   - ✓ KEPT: {doc_len} chars, lang={lang}, distance={dist:.4f}")
                print(f"     Preview: {doc[:150]}...")
            
            print(f"\n   Summary: {filtered_count}/{len(docs)} documents passed filters")
            
            if filtered_count == 0:
                print("\n   ⚠️  WARNING: All documents were filtered out!")
                print("   This explains why you're getting 'no evidence' responses.")
        else:
            print("   ✗ No results returned")
            
except Exception as e:
    print(f"   ✗ Retrieval test failed: {e}")
    import traceback
    traceback.print_exc()

print("\n" + "=" * 60)
print("Diagnostic Complete")
print("=" * 60)
