#!/usr/bin/env python3
"""
Test script for improved AI-powered PDF generation
"""

import json
from chroma_test import (
    generate_pdf_from_history,
    load_history,
    save_history
)

# Create a test conversation that should generate a proper legal document
test_conversation = [
    {
        "role": "user",
        "content": "I need to draft a legal notice for breach of contract. The contract was between Ahmad Khan (my client) and Bilal Ahmed. The contract was dated January 15, 2024 for supply of textile goods worth PKR 750,000. Payment was due on March 1, 2024 but Bilal Ahmed has not paid despite multiple reminders."
    },
    {
        "role": "assistant", 
        "content": "I can help you draft a legal notice for breach of contract. Based on the information provided, this involves non-payment for textile goods supply. Under Pakistani contract law, this constitutes a material breach. The notice should demand payment and specify consequences for continued non-compliance."
    },
    {
        "role": "user",
        "content": "Please include that Ahmad Khan is a textile manufacturer based in Karachi and Bilal Ahmed runs a retail business in Lahore. The breach has caused significant financial hardship and we want to give him 15 days to pay or face legal action."
    },
    {
        "role": "assistant",
        "content": "Understood. I'll include the business details and locations. The 15-day deadline is reasonable for a payment demand notice. The notice should mention the financial hardship caused and clearly state the legal consequences of continued non-payment, including potential court proceedings for recovery of the amount plus damages and costs."
    }
]

def test_pdf_generation():
    """Test the improved PDF generation system"""
    
    print("🧪 Testing Improved AI-Powered PDF Generation")
    print("=" * 60)
    
    # Save test conversation as history
    with open("chat_history.json", "w", encoding="utf-8") as f:
        json.dump(test_conversation, f, ensure_ascii=False, indent=2)
    
    print("✓ Test conversation created")
    print("\nConversation Summary:")
    print("- Contract between Ahmad Khan and Bilal Ahmed")
    print("- Textile goods worth PKR 750,000")
    print("- Payment overdue since March 1, 2024")
    print("- 15-day deadline for payment")
    
    # Test different PDF generation modes
    print("\n" + "=" * 60)
    print("🤖 Testing AI-Powered Template Mode")
    print("=" * 60)
    
    # Load history and generate PDF
    history = load_history()
    
    if history:
        # Generate intelligent PDF
        pdf_filename = generate_pdf_from_history(history, mode="template")
        
        if pdf_filename:
            print(f"\n✅ SUCCESS! PDF generated: {pdf_filename}")
            print("\nThe PDF should contain:")
            print("- Proper legal notice format")
            print("- All extracted details (names, amounts, dates)")
            print("- Professional Pakistani legal language")
            print("- Specific demands and consequences")
        else:
            print("\n❌ PDF generation failed")
    else:
        print("❌ No conversation history found")
    
    print("\n" + "=" * 60)
    print("📄 Testing Full Content Mode")
    print("=" * 60)
    
    # Test full content mode
    if history:
        pdf_filename_full = generate_pdf_from_history(history, mode="full")
        
        if pdf_filename_full:
            print(f"\n✅ SUCCESS! Full content PDF generated: {pdf_filename_full}")
        else:
            print("\n❌ Full content PDF generation failed")
    
    print("\n" + "=" * 60)
    print("🎯 Test Complete!")
    print("=" * 60)
    print("\nYou should now have:")
    print("1. An intelligent legal notice PDF with extracted data")
    print("2. A full content PDF with complete AI analysis")
    print("\nBoth PDFs should be much more accurate and professional!")

if __name__ == "__main__":
    test_pdf_generation()