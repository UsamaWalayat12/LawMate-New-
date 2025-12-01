"""
Test if chroma_test.py can be imported without sentence_transformers
"""
import os

# Set Chroma Cloud env vars to simulate Railway environment
os.environ['CHROMA_API_KEY'] = 'ck-WN7siQucBorxSYYta76sUbAzMbnFCuk8GiMXcdYgsnd'
os.environ['CHROMA_TENANT'] = '632db25e-e86a-4b90-808a-a221877d15d1'
os.environ['CHROMA_DATABASE'] = 'Law-Mate'

print("Testing chroma_test import without sentence_transformers...")
print("=" * 60)

try:
    import chroma_test
    print("✓ SUCCESS: chroma_test imported without errors!")
    print(f"  Model: {chroma_test.model}")
    print(f"  Collection: {chroma_test.col}")
    
    # Test a query
    if chroma_test.col:
        print("\nTesting query...")
        results = chroma_test.retrieve_and_filter("contract law", top_k=5, return_top=3)
        print(f"✓ Query returned {len(results)} results")
        if results:
            print(f"  First result preview: {results[0]['text'][:100]}...")
    
except ImportError as e:
    print(f"✗ FAILED: Import error: {e}")
    import traceback
    traceback.print_exc()
except Exception as e:
    print(f"✗ FAILED: {e}")
    import traceback
    traceback.print_exc()

print("=" * 60)
