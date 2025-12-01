"""
Test Railway API directly to see the actual error
"""
import requests
import json

# Your Railway URL - UPDATE THIS with your actual Railway URL
RAILWAY_URL = "https://adorable-endurance-production.up.railway.app"  # CHANGE THIS!

print("=" * 60)
print("Testing Railway API Directly")
print("=" * 60)

# Test health endpoint
print("\n1. Testing health endpoint...")
try:
    response = requests.get(f"{RAILWAY_URL}/health", timeout=10)
    print(f"   Status: {response.status_code}")
    print(f"   Response: {response.json()}")
except Exception as e:
    print(f"   Error: {e}")

# Test chat endpoint
print("\n2. Testing chat endpoint...")
try:
    response = requests.post(
        f"{RAILWAY_URL}/api/chat",
        json={"query": "contract law and breach of contract"},
        timeout=30
    )
    print(f"   Status: {response.status_code}")
    result = response.json()
    print(f"   Success: {result.get('success')}")
    print(f"   Answer preview: {result.get('answer', '')[:200]}...")
    
    if not result.get('success') or "couldn't find" in result.get('answer', '').lower():
        print("\n   ❌ STILL GETTING 'NO EVIDENCE' ERROR")
        print(f"   Full response: {json.dumps(result, indent=2)}")
    else:
        print("\n   ✅ SUCCESS! Got real answer!")
        
except Exception as e:
    print(f"   Error: {e}")

print("\n" + "=" * 60)
