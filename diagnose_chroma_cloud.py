"""
Diagnostic script to check Chroma Cloud database and collection status
"""
import os
import chromadb

print("=" * 70)
print("CHROMA CLOUD DIAGNOSTIC")
print("=" * 70)

# Get credentials
CHROMA_API_KEY = os.environ.get("CHROMA_API_KEY")
CHROMA_TENANT = os.environ.get("CHROMA_TENANT")
CHROMA_DATABASE = os.environ.get("CHROMA_DATABASE")

print("\n1. Checking environment variables...")
print(f"   CHROMA_API_KEY: {'SET' if CHROMA_API_KEY else 'NOT SET'}")
print(f"   CHROMA_TENANT: {'SET' if CHROMA_TENANT else 'NOT SET'}")
print(f"   CHROMA_DATABASE: {'SET' if CHROMA_DATABASE else 'NOT SET'}")

if not all([CHROMA_API_KEY, CHROMA_TENANT, CHROMA_DATABASE]):
    print("\n❌ ERROR: Missing environment variables!")
    exit(1)

try:
    print("\n2. Connecting to Chroma Cloud...")
    client = chromadb.CloudClient(
        api_key=CHROMA_API_KEY,
        tenant=CHROMA_TENANT,
        database=CHROMA_DATABASE
    )
    print("   ✓ Connected to Chroma Cloud")
    
    print("\n3. Listing all collections...")
    collections = client.list_collections()
    print(f"   Found {len(collections)} collections:")
    for col in collections:
        print(f"     - {col.name}")
    
    if len(collections) == 0:
        print("   ❌ ERROR: No collections found in database!")
        print("   You need to upload documents to Chroma Cloud first.")
        exit(1)
    
    print("\n4. Checking 'pakistan_law' collection...")
    try:
        col = client.get_collection(name="pakistan_law")
        print("   ✓ Collection 'pakistan_law' found")
        
        # Count documents
        count = col.count()
        print(f"   ✓ Collection has {count} documents")
        
        if count == 0:
            print("   ❌ ERROR: Collection is EMPTY!")
            print("   You need to upload documents to this collection.")
            exit(1)
        
        # Get a sample document
        print("\n5. Checking sample documents...")
        results = col.query(
            query_texts=["contract law"],
            n_results=1,
            include=['documents', 'metadatas']
        )
        
        if results and results['documents'] and len(results['documents'][0]) > 0:
            doc = results['documents'][0][0]
            print(f"   ✓ Sample document retrieved")
            print(f"   Length: {len(doc)} characters")
            print(f"   Preview: {doc[:200]}...")
        else:
            print("   ❌ ERROR: Could not retrieve sample documents!")
            exit(1)
        
        print("\n" + "=" * 70)
        print("✅ SUCCESS: Chroma Cloud is properly configured!")
        print(f"   Database: {CHROMA_DATABASE}")
        print(f"   Collection: pakistan_law")
        print(f"   Documents: {count}")
        print("=" * 70)
        
    except Exception as e:
        print(f"   ❌ ERROR: Collection 'pakistan_law' not found: {e}")
        print("\n   Available collections:")
        for col in collections:
            print(f"     - {col.name}")
        exit(1)
        
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    exit(1)
