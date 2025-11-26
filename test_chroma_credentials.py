"""
Test script to verify Chroma Cloud credentials
Run this locally to diagnose authentication issues
"""
import os
import chromadb

# Load environment variables
CHROMA_API_KEY = os.environ.get("CHROMA_API_KEY")
CHROMA_TENANT = os.environ.get("CHROMA_TENANT")
CHROMA_DATABASE = os.environ.get("CHROMA_DATABASE")

print("=" * 60)
print("CHROMA CLOUD CREDENTIALS TEST")
print("=" * 60)

# Check if credentials are set
print("\n1. Checking environment variables...")
print(f"   CHROMA_API_KEY: {'SET' if CHROMA_API_KEY else 'NOT SET'}")
print(f"   CHROMA_TENANT: {'SET' if CHROMA_TENANT else 'NOT SET'}")
print(f"   CHROMA_DATABASE: {'SET' if CHROMA_DATABASE else 'NOT SET'}")

if not all([CHROMA_API_KEY, CHROMA_TENANT, CHROMA_DATABASE]):
    print("\n❌ ERROR: Missing environment variables!")
    print("   Set these before running:")
    print("   - CHROMA_API_KEY")
    print("   - CHROMA_TENANT")
    print("   - CHROMA_DATABASE")
    exit(1)

print(f"\n   API Key (first 10 chars): {CHROMA_API_KEY[:10]}...")
print(f"   Tenant: {CHROMA_TENANT}")
print(f"   Database: {CHROMA_DATABASE}")

# Test connection
print("\n2. Testing Chroma Cloud connection...")
try:
    client = chromadb.HttpClient(
        host="api.trychroma.com",
        port=443,
        ssl=True,
        headers={"Authorization": f"Bearer {CHROMA_API_KEY}"}
    )
    print("   ✓ HttpClient created")
    
    # Try to get user identity
    print("\n3. Verifying authentication...")
    identity = client.get_user_identity()
    print(f"   ✓ Authenticated as: {identity}")
    
    # Try to get collection
    print("\n4. Accessing collection...")
    col = client.get_or_create_collection(name="test_collection")
    print(f"   ✓ Collection 'test_collection' accessed")
    
    # Count documents
    count = col.count()
    print(f"   ✓ Collection has {count} documents")
    
    print("\n" + "=" * 60)
    print("✅ SUCCESS: Chroma Cloud credentials are valid!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n❌ ERROR: {e}")
    import traceback
    traceback.print_exc()
    print("\n" + "=" * 60)
    print("TROUBLESHOOTING:")
    print("=" * 60)
    print("1. Verify API key is correct (check Chroma Cloud dashboard)")
    print("2. Verify tenant ID is correct")
    print("3. Verify database name is correct")
    print("4. Check if API key has expired")
    print("5. Try regenerating the API key in Chroma Cloud dashboard")
    print("=" * 60)
