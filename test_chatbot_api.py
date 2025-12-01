"""
Quick test to verify the API chatbot endpoint works with the fixes
"""
import requests
import json

API_URL = "http://localhost:8000"

def test_chat_endpoint():
    """Test the /api/chat endpoint with sample queries"""
    
    print("=" * 60)
    print("Testing Chatbot API")
    print("=" * 60)
    
    # Check if API is running
    try:
        response = requests.get(f"{API_URL}/health", timeout=5)
        if response.status_code == 200:
            print("\n✓ API is running")
        else:
            print(f"\n✗ API health check failed: {response.status_code}")
            return
    except Exception as e:
        print(f"\n✗ Cannot connect to API: {e}")
        print("\nPlease start the backend server first:")
        print("  python backend_api.py")
        return
    
    # Test queries
    test_queries = [
        "What is a legal notice?",
        "How to draft a breach of contract notice?",
        "Property transfer process in Pakistan",
        "Employment law basics"
    ]
    
    print("\nTesting chat endpoint with sample queries:")
    print("-" * 60)
    
    for i, query in enumerate(test_queries, 1):
        print(f"\n{i}. Query: '{query}'")
        
        try:
            response = requests.post(
                f"{API_URL}/api/chat",
                json={"query": query},
                timeout=30
            )
            
            if response.status_code == 200:
                data = response.json()
                answer = data.get("answer", "")
                
                # Check if we got a real answer or the "no evidence" error
                if "couldn't find" in answer.lower() or "couldn't find specific" in answer.lower():
                    print("  ⚠️  WARNING: Still getting 'no evidence' response")
                    print(f"  Response preview: {answer[:200]}...")
                else:
                    print("  ✓ SUCCESS: Got legal content response")
                    print(f"  Response length: {len(answer)} characters")
                    print(f"  Preview: {answer[:150]}...")
            else:
                print(f"  ✗ ERROR: HTTP {response.status_code}")
                print(f"  {response.text[:200]}")
                
        except Exception as e:
            print(f"  ✗ ERROR: {e}")
    
    print("\n" + "=" * 60)
    print("Test Complete")
    print("=" * 60)

if __name__ == "__main__":
    test_chat_endpoint()
