# 📡 Pakistani Legal RAG Assistant - API Documentation

## 🚀 Quick Start

### 1. Install Dependencies
```bash
# Double-click or run:
install_api.bat

# Or manually:
pip install -r api_requirements.txt
```

### 2. Start Server
```bash
# Double-click or run:
start_server.bat

# Server starts at: http://localhost:8000
```

### 3. Test API
```bash
# Run test script:
python test_api.py

# Or check status:
check_server.bat
```

---

## 📋 API Endpoints

### Base URL
```
http://localhost:8000
```

---

## 🔍 Endpoints

### 1. Health Check
**GET** `/health`

Check if API is running.

**Response:**
```json
{
  "status": "healthy",
  "timestamp": "2024-11-21T14:30:00"
}
```

---

### 2. Get Status
**GET** `/api/status`

Get API configuration and available endpoints.

**Response:**
```json
{
  "status": "running",
  "version": "1.0.0",
  "model": "models/gemini-2.5-flash",
  "endpoints": [
    "/api/chat",
    "/api/history",
    "/api/generate-pdf",
    "/api/pdf/{filename}",
    "/api/clear-history"
  ]
}
```

---

### 3. Chat (Send Query)
**POST** `/api/chat`

Send a legal query and get AI-generated answer.

**Request Body:**
```json
{
  "query": "How to draft a breach of contract notice?",
  "conversation_id": "optional-id"
}
```

**Response:**
```json
{
  "success": true,
  "answer": "1) SHORT ANSWER\n...",
  "timestamp": "2024-11-21T14:30:00",
  "message_id": "msg_123",
  "conversation_id": "optional-id"
}
```

**Example (curl):**
```bash
curl -X POST http://localhost:8000/api/chat \
  -H "Content-Type: application/json" \
  -d '{"query": "What is breach of contract?"}'
```

**Example (Python):**
```python
import requests

response = requests.post(
    "http://localhost:8000/api/chat",
    json={"query": "What is breach of contract?"}
)
print(response.json()['answer'])
```

---

### 4. Get History
**GET** `/api/history`

Get complete chat history.

**Response:**
```json
{
  "success": true,
  "history": [
    {
      "role": "user",
      "content": "How to draft breach notice?",
      "timestamp": "2024-11-21T14:30:00"
    },
    {
      "role": "assistant",
      "content": "1) SHORT ANSWER...",
      "timestamp": "2024-11-21T14:30:15"
    }
  ],
  "total_messages": 2
}
```

**Example (curl):**
```bash
curl http://localhost:8000/api/history
```

---

### 5. Clear History
**DELETE** `/api/history/clear`

Clear all chat history.

**Response:**
```json
{
  "success": true,
  "message": "Chat history cleared successfully"
}
```

**Example (curl):**
```bash
curl -X DELETE http://localhost:8000/api/history/clear
```

---

### 6. Generate PDF
**POST** `/api/generate-pdf`

Generate PDF document from chat history.

**Request Body:**
```json
{
  "mode": "template",
  "doc_type": "breach_notice"
}
```

**Parameters:**
- `mode`: "template" (default) or "full"
  - `template`: Professional template with extracted data
  - `full`: Complete AI-generated analysis
- `doc_type`: "breach_notice", "legal_notice", or "agreement" (optional)

**Response:**
```json
{
  "success": true,
  "pdf_url": "/api/pdf/legal_document_breach_notice_20241121.pdf",
  "filename": "legal_document_breach_notice_20241121.pdf"
}
```

**Example (curl):**
```bash
curl -X POST http://localhost:8000/api/generate-pdf \
  -H "Content-Type: application/json" \
  -d '{"mode": "full"}'
```

---

### 7. Download PDF
**GET** `/api/pdf/{filename}`

Download generated PDF file.

**Response:**
PDF file download

**Example:**
```
http://localhost:8000/api/pdf/legal_document_breach_notice_20241121.pdf
```

---

### 8. List PDFs
**GET** `/api/pdfs`

List all generated PDF files.

**Response:**
```json
{
  "success": true,
  "pdfs": [
    "legal_document_breach_notice_20241121.pdf",
    "legal_analysis_full_20241121.pdf"
  ],
  "count": 2
}
```

---

### 9. Get Configuration
**GET** `/api/config`

Get current API configuration.

**Response:**
```json
{
  "success": true,
  "config": {
    "model": "models/gemini-2.5-flash",
    "top_k": 20,
    "return_top": 5,
    "db_path": "ChromaDB",
    "collection": "pakistan_law"
  }
}
```

---

## 🔧 Error Handling

All endpoints return errors in this format:

```json
{
  "success": false,
  "error": "Error message",
  "message": "Detailed description"
}
```

**Common HTTP Status Codes:**
- `200` - Success
- `400` - Bad Request (invalid input)
- `404` - Not Found (resource doesn't exist)
- `500` - Internal Server Error

---

## 💡 Usage Examples

### Complete Workflow Example

```python
import requests

BASE_URL = "http://localhost:8000"

# 1. Send a query
response = requests.post(
    f"{BASE_URL}/api/chat",
    json={"query": "How to draft breach notice for PKR 500,000?"}
)
answer = response.json()['answer']
print(f"AI Answer: {answer[:200]}...")

# 2. Get history
response = requests.get(f"{BASE_URL}/api/history")
history = response.json()['history']
print(f"Total messages: {len(history)}")

# 3. Generate PDF
response = requests.post(
    f"{BASE_URL}/api/generate-pdf",
    json={"mode": "full"}
)
pdf_url = response.json()['pdf_url']
print(f"PDF generated: {pdf_url}")

# 4. Download PDF
pdf_response = requests.get(f"{BASE_URL}{pdf_url}")
with open("my_legal_document.pdf", "wb") as f:
    f.write(pdf_response.content)
print("PDF downloaded!")
```

---

## 🔒 CORS Configuration

The API allows all origins by default for development. For production, update `backend_api.py`:

```python
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://your-flutter-app-domain.com"],  # Specific domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
```

---

## 📊 Interactive API Documentation

FastAPI provides automatic interactive documentation:

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

You can test all endpoints directly from the browser!

---

## 🐛 Troubleshooting

### Server won't start
```bash
# Check if port 8000 is already in use
netstat -ano | findstr :8000

# Kill the process if needed
taskkill /PID <process_id> /F
```

### Connection refused
- Make sure server is running: `check_server.bat`
- Check firewall settings
- Verify port 8000 is not blocked

### Import errors
```bash
# Reinstall dependencies
pip install -r api_requirements.txt
```

### GEMINI_API_KEY not set
```bash
# Set environment variable
set GEMINI_API_KEY=your_api_key_here
```

---

## 📝 Notes

- Server runs on `http://localhost:8000` by default
- All chat history is saved to `chat_history.json`
- Generated PDFs are saved in the current directory
- The API uses your existing RAG logic from `chroma_test.py`

---

## 🎯 Next Steps

1. ✅ API is running
2. ✅ Test with `test_api.py`
3. ➡️ Integrate with Flutter app (see FLUTTER_INTEGRATION.md)

---

**API Version:** 1.0.0  
**Last Updated:** November 21, 2024
