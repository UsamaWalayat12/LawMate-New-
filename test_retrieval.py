"""
Simple test script to verify ChromaDB retrieval is working
"""
import sys
import os

# Test ChromaDB connection
print("Testing ChromaDB Retrieval")
print("=" * 60)

try:
    from chroma_test import retrieve_and_filter, col, model
    
    if col is None or model is None:
        print("ERROR: ChromaDB or model not initialized")
        sys.exit(1)
    
    print("SUCCESS: ChromaDB and model initialized")
    
    # Get collection stats
    count = col.count()
    print(f"Total documents in collection: {count}")
    
    if count == 0:
        print("ERROR: Collection is empty!")
        sys.exit(1)
    
    # Test queries
    test_queries = [
        "legal notice for breach of contract",
        "property transfer process",
        "employment law",
        "how to draft a contract"
    ]
    
    print("\nTesting retrieval with sample queries:")
    print("-" * 60)
    
    for query in test_queries:
        print(f"\nQuery: '{query}'")
        
        # Call retrieve_and_filter
        evidences = retrieve_and_filter(query, top_k=10, return_top=5)
        
        print(f"  Results: {len(evidences)} documents")
        
        if len(evidences) == 0:
            print("  WARNING: No documents returned after filtering!")
            
            # Try to get raw results to see what's being filtered
            q_emb = model.encode(query, convert_to_numpy=True).tolist()
            raw_res = col.query(
                query_embeddings=[q_emb],
                n_results=10,
                include=['documents', 'metadatas', 'distances']
            )
            
            if raw_res and 'documents' in raw_res:
                docs = raw_res['documents'][0] if raw_res['documents'] else []
                metas = raw_res['metadatas'][0] if raw_res['metadatas'] else []
                
                print(f"  Raw retrieval returned: {len(docs)} documents")
                
                # Check why they were filtered
                for i, (doc, meta) in enumerate(zip(docs[:3], metas[:3])):
                    doc_len = len(doc)
                    lang = meta.get('lang', 'unknown')
                    print(f"    Doc {i+1}: length={doc_len}, lang={lang}")
                    
                    if doc_len < 200:
                        print(f"      -> FILTERED: too short (< 200 chars)")
                    if lang and not lang.startswith('en') and lang != 'unknown':
                        print(f"      -> FILTERED: non-English (lang={lang})")
        else:
            print("  SUCCESS: Documents retrieved")
            for i, ev in enumerate(evidences[:2], 1):
                print(f"    {i}. Length: {ev['len']}, Distance: {ev['dist']:.4f}")
                print(f"       Preview: {ev['text'][:100]}...")
    
    print("\n" + "=" * 60)
    print("Test Complete")
    
except ImportError as e:
    print(f"ERROR: Failed to import chroma_test: {e}")
    sys.exit(1)
except Exception as e:
    print(f"ERROR: {e}")
    import traceback
    traceback.print_exc()
    sys.exit(1)
