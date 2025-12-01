# PDF Legal Document Generation - User Guide

## 🎉 New Features Added

Your Pakistani Legal RAG Assistant now has **automatic PDF generation** with smart data extraction from chat history!

## 📋 Installation

First, install the required PDF library:

```bash
pip install reportlab
```

## 🚀 How to Use

### 1. Have a Conversation
Ask your legal questions as usual:

```bash
python chroma_test.py "How to draft a notice for breach of contract for payment overdue?"
```

### 2. Generate PDF Document
After your conversation, generate a professional PDF:

```bash
python chroma_test.py --generate-pdf
```

The system will:
- ✅ Automatically extract relevant information from your chat history
- ✅ Detect the document type you need
- ✅ Fill in the template with extracted data
- ✅ Generate a professional PDF document

## 📝 Available Commands

| Command | Description |
|---------|-------------|
| `python chroma_test.py "your question"` | Ask a legal question |
| `python chroma_test.py --generate-pdf` | Generate template-based PDF |
| `python chroma_test.py --generate-pdf full` | Generate PDF with FULL AI content |
| `python chroma_test.py --generate-pdf breach_notice` | Generate specific document type |
| `python chroma_test.py --show-history` | View COMPLETE chat history (not truncated) |
| `python chroma_test.py --clear-history` | Clear chat history |
| `python chroma_test.py --help` | Show help menu |

## 📄 PDF Generation Modes

### **1. Template Mode (Default)**
- Professional legal document template
- Auto-fills: names, dates, amounts from chat
- Quick and consistent format
- Command: `--generate-pdf` or `--generate-pdf template`

### **2. Full Content Mode (NEW!)**
- Complete AI-generated analysis
- Includes all evidence and citations
- Full reasoning and legal grounds
- Unique content for each case
- Command: `--generate-pdf full`

## 📄 Supported Document Types (Template Mode)

1. **breach_notice** (default) - Notice for Breach of Contract
2. **legal_notice** - General Legal Notice
3. **agreement** - Contract/Agreement Draft

## 🤖 Smart Data Extraction

The system automatically extracts from your conversation:

- 👥 **Party Names** - Sender and recipient
- 💰 **Amounts** - Payment amounts (PKR, Rs, rupees)
- 📅 **Dates** - Contract dates, due dates
- 📍 **Addresses** - Party addresses
- 📋 **Breach Details** - Description of breach
- ⏰ **Deadlines** - Payment deadlines

## 💡 Example Workflows

### **Workflow 1: Template-Based (Quick Standard Notice)**
```bash
# Step 1: Ask about drafting a notice
python chroma_test.py "I need to draft a breach of contract notice. The contract was dated January 15, 2024. Payment of PKR 500,000 was due on February 1, 2024 but remains unpaid."

# Step 2: Generate template-based PDF
python chroma_test.py --generate-pdf

# Output: legal_document_breach_notice_20241121_143022.pdf
```

### **Workflow 2: Full AI Content (Detailed Analysis)**
```bash
# Step 1: Ask a complex legal question
python chroma_test.py "What are the legal grounds for breach of contract in Pakistani law with evidence and case citations?"

# Step 2: Generate PDF with FULL AI answer
python chroma_test.py --generate-pdf full

# Output: legal_analysis_full_20241121_143022.pdf
# Contains: Complete AI analysis with all evidence, citations, and reasoning
```

### **Workflow 3: View Complete History**
```bash
# View FULL chat history (not truncated)
python chroma_test.py --show-history

# You'll see complete answers, not just summaries!
```

## 📋 PDF Output Features

Your generated PDF includes:

- ✅ Professional legal document formatting
- ✅ Proper Pakistani legal notice structure
- ✅ Auto-filled data from conversation
- ✅ Placeholders for missing information
- ✅ Ready-to-use template
- ✅ Signature section
- ✅ Date and reference numbers

## 🔧 Customization

You can manually edit the extracted data before PDF generation by:

1. Viewing extracted data (shown during generation)
2. Modifying the chat history if needed
3. Re-generating the PDF

## 📌 Tips for Best Results

1. **Be Specific**: Mention dates, amounts, and names in your questions
2. **Use Standard Formats**: 
   - Dates: "January 15, 2024" or "15/01/2024"
   - Amounts: "PKR 500,000" or "Rs. 500,000"
3. **Multiple Conversations**: The system uses the last 5 exchanges for context
4. **Review Before Use**: Always review the generated PDF and fill in any placeholders

## 🎯 What's NOT Changed

- ✅ All existing RAG functionality works exactly the same
- ✅ Chat history feature works as before
- ✅ Evidence retrieval unchanged
- ✅ Gemini API integration unchanged

Only **NEW features added** - nothing broken!

## 🐛 Troubleshooting

**Error: "reportlab not installed"**
```bash
pip install reportlab
```

**No data extracted?**
- Make sure you mentioned relevant details in your conversation
- The system will use placeholders like [AMOUNT] for missing data
- You can manually fill these in the PDF

**PDF not generating?**
- Check if you have write permissions in the directory
- Ensure reportlab is properly installed
- Check for error messages in the console

## 📞 Support

If you encounter issues:
1. Check the console output for error messages
2. Use `--help` to see all available commands
3. Use `--show-history` to verify your conversation was saved

---

**Enjoy your automated legal document generation!** 🎉
