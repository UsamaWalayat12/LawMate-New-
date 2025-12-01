"""
Test if Railway can connect to Chroma Cloud
Run this locally to verify the connection works
"""
import os
import chromadb

# Set the environment variables (same as Railway)
os.environ['CHROMA_API_KEY'] = 'ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd'
os.environ['CHROMA_TENANT'] = '632db25e-e86a-4b90-808a-a221877d15d1'
os.environ['CHROMA_DATABASE'] = 'Law-Mate'

print("Testing Chroma Cloud Connection...")
print("=" * 60)

try:
    # Connect to Chroma Cloud
    print("\n1. Connecting to Chroma Cloud...")
    client = chromadb.CloudClient(
        api_key=os.environ['CHROMA_API_KEY'],
        tenant=os.environ['CHROMA_TENANT'],
        database=os.environ['CHROMA_DATABASE']
    )
    print("   ✓ Connected to Chroma Cloud")
    
    # Get collection
    print("\n2. Getting collection 'pakistan_law'...")
    collection = client.get_collection("pakistan_law")
    print("   ✓ Collection found")
    
    # Count documents
    print("\n3. Counting documents...")
    count = collection.count()
    print(f"   ✓ Found {count} documents")
    
    # Test query
    print("\n4. Testing query...")
    from sentence_transformers import SentenceTransformer
    model = SentenceTransformer("all-mpnet-base-v2")
    
    query = "contract law and breach of contract"
    q_emb = model.encode(query, convert_to_numpy=True).tolist()
    
    results = collection.query(
        query_embeddings=[q_emb],
        n_results=5,
        include=['documents', 'metadatas', 'distances']
    )
    
    if results and 'documents' in results and len(results['documents'][0]) > 0:
        print(f"   ✓ Query returned {len(results['documents'][0])} results")
        print(f"\n   First result preview:")
        print(f"   {results['documents'][0][0][:200]}...")
    else:
        print("   ✗ Query returned no results")
    
    print("\n" + "=" * 60)
    print("SUCCESS: Chroma Cloud connection works!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ ERROR: {e}")
    import traceback
    traceback.print_exc()
    print("\n" + "=" * 60)
    print("FAILED: Could not connect to Chroma Cloud")
    print("=" * 60)
