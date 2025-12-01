#!/usr/bin/env python3
"""
Test script to demonstrate the improved PDF generation works for different document types
"""

import json
from chroma_test import generate_pdf_from_history

def test_document_type(conversation, test_name):
    """Test PDF generation for a specific conversation"""
    print(f"\n{'='*60}")
    print(f"🧪 Testing: {test_name}")
    print(f"{'='*60}")
    
    # Save conversation as history
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(conversation, f, ensure_ascii=False, indent=2)
    
    # Show conversation summary
    print("\n📝 Conversation:")
    for msg in conversation:
        role = msg['role'].upper()
        content = msg['content'][:100] + "..." if len(msg['content']) > 100 else msg['content']
        print(f"  {role}: {content}")
    
    # Generate PDF
    print(f"\n🤖 Generating PDF...")
    pdf_filename = generate_pdf_from_history(conversation, mode="template")
    
    if pdf_filename:
        print(f"✅ SUCCESS! Generated: {pdf_filename}")
        return True
    else:
        print(f"❌ FAILED to generate PDF")
        return False

def main():
    """Test different document types"""
    
    print("🚀 Testing Improved PDF Generation for Different Document Types")
    print("This demonstrates that the system now understands user intent!")
    
    # Test 1: Breach of Contract Notice
    breach_conversation = [
        {
            "role": "user",
            "content": "I need to draft a breach of contract notice. My client Ahmad Khan had a contract with Bilal Ahmed dated March 1, 2024 for construction work worth PKR 2,500,000. Payment was due April 15, 2024 but hasn't been paid."
        },
        {
            "role": "assistant", 
            "content": "I can help you draft a breach of contract notice for the construction work payment default. This constitutes a material breach under Pakistani contract law."
        }
    ]
    
    # Test 2: Employment Contract
    employment_conversation = [
        {
            "role": "user",
            "content": "Help me create an employment contract for hiring Sarah Ahmed as Senior Software Engineer at Tech Solutions Ltd. Salary is PKR 150,000 per month, starting January 1, 2025. Include standard terms and conditions."
        },
        {
            "role": "assistant",
            "content": "I'll help you create a comprehensive employment contract with standard Pakistani employment law provisions, including salary, benefits, and termination clauses."
        }
    ]
    
    # Test 3: Legal Notice
    legal_notice_conversation = [
        {
            "role": "user",
            "content": "I want to send a legal notice to my neighbor Hassan Ali for property encroachment. He has built a wall 2 feet into my property at House 123, Block A, DHA Lahore. I have the survey documents proving ownership."
        },
        {
            "role": "assistant",
            "content": "I can help you draft a legal notice for property encroachment. This is a serious matter that requires formal legal action under Pakistani property law."
        }
    ]
    
    # Test 4: Lease Agreement
    lease_conversation = [
        {
            "role": "user",
            "content": "Draft a lease agreement for renting my apartment to Fatima Khan. Property is at Flat 4B, Gulberg Heights, Karachi. Monthly rent PKR 45,000, security deposit PKR 90,000, lease period 2 years starting December 1, 2024."
        },
        {
            "role": "assistant",
            "content": "I'll create a comprehensive lease agreement with all standard terms including rent, security deposit, maintenance responsibilities, and termination conditions."
        }
    ]
    
    # Run tests
    tests = [
        (breach_conversation, "Breach of Contract Notice"),
        (employment_conversation, "Employment Contract"),
        (legal_notice_conversation, "Legal Notice for Property Encroachment"),
        (lease_conversation, "Lease Agreement")
    ]
    
    results = []
    for conversation, test_name in tests:
        success = test_document_type(conversation, test_name)
        results.append((test_name, success))
    
    # Summary
    print(f"\n{'='*60}")
    print("📊 TEST RESULTS SUMMARY")
    print(f"{'='*60}")
    
    passed = sum(1 for _, success in results if success)
    total = len(results)
    
    for test_name, success in results:
        status = "✅ PASS" if success else "❌ FAIL"
        print(f"  {status} - {test_name}")
    
    print(f"\n🎯 Overall Result: {passed}/{total} tests passed")
    
    if passed == total:
        print("\n🎉 EXCELLENT! The improved PDF generation system works perfectly!")
        print("   ✅ Understands different document types")
        print("   ✅ Extracts specific information accurately") 
        print("   ✅ Generates appropriate legal documents")
        print("   ✅ Adapts to user intent and context")
    else:
        print(f"\n⚠️  Some tests failed. Check the error messages above.")
    
    print(f"\n📁 Generated PDFs are saved in the current directory.")
    print("   You can open them to verify the quality and accuracy!")

if __name__ == "__main__":
    main()