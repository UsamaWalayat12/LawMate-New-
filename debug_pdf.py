#!/usr/bin/env python3
"""
Debug PDF generation issue
"""

import os
import json

def test_simple_pdf():
    """Test basic PDF generation"""
    
    # Test reportlab directly
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate, Paragraph
        from reportlab.lib.styles import getSampleStyleSheet
        
        print("✓ ReportLab imports successful")
        
        # Create simple PDF
        filename = "test_simple.pdf"
        doc = SimpleDocTemplate(filename, pagesize=A4)
        styles = getSampleStyleSheet()
        
        story = [Paragraph("Test PDF Generation", styles['Title'])]
        doc.build(story)
        
        if os.path.exists(filename):
            print(f"✓ Simple PDF created: {filename}")
            return True
        else:
            print("❌ Simple PDF not created")
            return False
            
    except Exception as e:
        print(f"❌ ReportLab error: {e}")
        return False

def test_chroma_pdf():
    """Test the chroma_test PDF generation"""
    
    # Create test history
    test_history = [
        {"role": "user", "content": "Test message for PDF generation"},
        {"role": "assistant", "content": "Test response"}
    ]
    
    # Save as history file
    with open("chat_history.json", "w") as f:
        json.dump(test_history, f)
    
    print("✓ Test history created")
    
    try:
        from chroma_test import generate_pdf_from_history
        
        print("🤖 Testing PDF generation...")
        result = generate_pdf_from_history(test_history, mode="template")
        
        if result:
            print(f"✓ PDF generation returned: {result}")
            if os.path.exists(result):
                print(f"✓ PDF file exists: {result}")
                return True
            else:
                print(f"❌ PDF file not found: {result}")
                return False
        else:
            print("❌ PDF generation returned None")
            return False
            
    except Exception as e:
        print(f"❌ PDF generation error: {e}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    print("🔍 Debugging PDF Generation")
    print("=" * 40)
    
    print("\n1. Testing ReportLab directly...")
    simple_ok = test_simple_pdf()
    
    print("\n2. Testing chroma_test PDF generation...")
    chroma_ok = test_chroma_pdf()
    
    print("\n" + "=" * 40)
    print("📊 Results:")
    print(f"  ReportLab: {'✓' if simple_ok else '❌'}")
    print(f"  Chroma PDF: {'✓' if chroma_ok else '❌'}")
    
    if simple_ok and chroma_ok:
        print("\n🎉 PDF generation is working!")
    elif simple_ok:
        print("\n⚠️ ReportLab works, but chroma_test has issues")
    else:
        print("\n❌ ReportLab has issues")