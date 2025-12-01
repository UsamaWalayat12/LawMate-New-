"""
Test script for Pakistani Legal RAG Assistant API
Run this to verify the API is working correctly
"""

import requests
import json
import time

BASE_URL = "http://localhost:8000"

def print_section(title):
    print("\n" + "=" * 60)
    print(f"  {title}")
    print("=" * 60)

def test_health():
    """Test health check endpoint"""
    print_section("Testing Health Check")
    try:
        response = requests.get(f"{BASE_URL}/health")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_status():
    """Test status endpoint"""
    print_section("Testing Status Endpoint")
    try:
        response = requests.get(f"{BASE_URL}/api/status")
        print(f"Status Code: {response.status_code}")
        data = response.json()
        print(json.dumps(data, indent=2))
        return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_chat():
    """Test chat endpoint"""
    print_section("Testing Chat Endpoint")
    try:
        query = "What is breach of contract in Pakistani law?"
        print(f"Query: {query}")
        print("Sending request...")
        
        response = requests.post(
            f"{BASE_URL}/api/chat",
            json={"query": query},
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"\n✓ Success!")
            print(f"Answer (first 200 chars): {data['answer'][:200]}...")
            print(f"Timestamp: {data['timestamp']}")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_history():
    """Test history endpoint"""
    print_section("Testing History Endpoint")
    try:
        response = requests.get(f"{BASE_URL}/api/history")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Success!")
            print(f"Total messages: {data['total_messages']}")
            print(f"History entries: {len(data['history'])}")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_generate_pdf():
    """Test PDF generation endpoint"""
    print_section("Testing PDF Generation")
    try:
        print("Generating PDF (template mode)...")
        
        response = requests.post(
            f"{BASE_URL}/api/generate-pdf",
            json={"mode": "template"},
            headers={"Content-Type": "application/json"}
        )
        
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Success!")
            print(f"PDF URL: {data['pdf_url']}")
            print(f"Filename: {data['filename']}")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def test_list_pdfs():
    """Test list PDFs endpoint"""
    print_section("Testing List PDFs")
    try:
        response = requests.get(f"{BASE_URL}/api/pdfs")
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            data = response.json()
            print(f"✓ Success!")
            print(f"Total PDFs: {data['count']}")
            if data['pdfs']:
                print("PDF files:")
                for pdf in data['pdfs'][:5]:  # Show first 5
                    print(f"  - {pdf}")
            return True
        else:
            print(f"❌ Error: {response.text}")
            return False
            
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    """Run all tests"""
    print("\n" + "=" * 60)
    print("  Pakistani Legal RAG Assistant - API Tests")
    print("=" * 60)
    print("\nMake sure the server is running (start_server.bat)")
    print("Press Enter to start tests...")
    input()
    
    results = []
    
    # Run tests
    results.append(("Health Check", test_health()))
    time.sleep(1)
    
    results.append(("Status", test_status()))
    time.sleep(1)
    
    results.append(("Chat", test_chat()))
    time.sleep(2)
    
    results.append(("History", test_history()))
    time.sleep(1)
    
    results.append(("Generate PDF", test_generate_pdf()))
    time.sleep(2)
    
    results.append(("List PDFs", test_list_pdfs()))
    
    # Summary
    print_section("Test Summary")
    passed = sum(1 for _, result in results if result)
    total = len(results)
    
    for test_name, result in results:
        status = "✓ PASS" if result else "✗ FAIL"
        print(f"{status} - {test_name}")
    
    print(f"\nTotal: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 All tests passed! API is working correctly.")
    else:
        print(f"\n⚠️  {total - passed} test(s) failed. Check the errors above.")
    
    print("\n" + "=" * 60)

if __name__ == "__main__":
    main()
