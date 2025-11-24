"""
Pakistani Legal RAG Assistant - REST API
FastAPI backend that wraps the existing RAG functionality
Optimized for Vercel serverless deployment
"""

from fastapi import FastAPI, HTTPException, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse, JSONResponse
from pydantic import BaseModel
from typing import Optional, List, Dict, Any
from datetime import datetime
import os
import sys
import json

# Import existing RAG functions
try:
    from chroma_test import (
        retrieve_and_filter,
        call_gemini_chat,
        build_strict_rag_prompt,
        load_history,
        save_history,
        add_to_history,
        generate_pdf_from_history,
        extract_case_metadata,
        GEMINI_MODEL,
        TOP_K,
        RETURN_TOP
    )
except ImportError as e:
    print(f"Warning: Could not import chroma_test: {e}")
    # Fallback values for serverless environment
    GEMINI_MODEL = "models/gemini-2.5-flash"
    TOP_K = 10
    RETURN_TOP = 5

# Create FastAPI app
app = FastAPI(
    title="Pakistani Legal RAG Assistant API",
    description="REST API for Pakistani legal document analysis and generation",
    version="1.0.0"
)

# Enable CORS for Flutter app
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (Flutter app can connect)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Request/Response Models
class ChatRequest(BaseModel):
    query: str
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    success: bool
    answer: str
    timestamp: str
    message_id: Optional[str] = None
    conversation_id: Optional[str] = None

class HistoryResponse(BaseModel):
    success: bool
    history: List[Dict[str, Any]]
    total_messages: int

class GeneratePDFRequest(BaseModel):
    mode: str = "template"  # "template" or "full"
    doc_type: Optional[str] = None

class GeneratePDFResponse(BaseModel):
    success: bool
    pdf_url: str
    filename: str

class StatusResponse(BaseModel):
    status: str
    version: str
    model: str
    endpoints: List[str]

# Root endpoint
@app.get("/")
async def root():
    """API root - health check"""
    return {
        "message": "Pakistani Legal RAG Assistant API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs"
    }

# Health check
@app.get("/health")
async def health_check():
    """Check if API is running"""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}

# Status endpoint
@app.get("/api/status", response_model=StatusResponse)
async def get_status():
    """Get API status and configuration"""
    return {
        "status": "running",
        "version": "1.0.0",
        "model": GEMINI_MODEL,
        "endpoints": [
            "/api/chat",
            "/api/history",
            "/api/generate-pdf",
            "/api/pdf/{filename}",
            "/api/clear-history"
        ]
    }

# Chat endpoint
@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    """
    Send a legal query and get AI-generated answer
    
    Args:
        request: ChatRequest with query string
        
    Returns:
        ChatResponse with AI answer
    """
    try:
        query = request.query.strip()
        
        if not query:
            raise HTTPException(status_code=400, detail="Query cannot be empty")
        
        # Load history
        history = load_history()
        
        # Add user query to history
        add_to_history(history, "user", query)
        
        # Retrieve evidence
        evidences = retrieve_and_filter(query, top_k=TOP_K, return_top=RETURN_TOP)
        
        if len(evidences) == 0:
            answer = "I couldn't find relevant evidence in the legal database for your query. Please try rephrasing your question or ask about Pakistani legal topics."
        else:
            # Build prompt
            prompt = build_strict_rag_prompt(query, evidences)
            
            # Get AI response
            answer = call_gemini_chat(prompt, model=GEMINI_MODEL, temperature=0.0, max_tokens=2000)
        
        # Add assistant response to history
        add_to_history(history, "assistant", answer)
        
        # Generate message ID
        message_id = f"msg_{len(history)}"
        
        return {
            "success": True,
            "answer": answer,
            "timestamp": datetime.now().isoformat(),
            "message_id": message_id,
            "conversation_id": request.conversation_id
        }
        
    except Exception as e:
        print(f"Error in chat endpoint: {e}")
        raise HTTPException(status_code=500, detail=f"Error processing query: {str(e)}")

# Get history endpoint
@app.get("/api/history", response_model=HistoryResponse)
async def get_history():
    """
    Get complete chat history
    
    Returns:
        HistoryResponse with all messages
    """
    try:
        history = load_history()
        
        return {
            "success": True,
            "history": history,
            "total_messages": len(history)
        }
        
    except Exception as e:
        print(f"Error getting history: {e}")
        raise HTTPException(status_code=500, detail=f"Error retrieving history: {str(e)}")

# Clear history endpoint
@app.delete("/api/history/clear")
async def clear_history():
    """Clear all chat history"""
    try:
        history_file = "chat_history.json"
        if os.path.exists(history_file):
            os.remove(history_file)
        
        return {
            "success": True,
            "message": "Chat history cleared successfully"
        }
        
    except Exception as e:
        print(f"Error clearing history: {e}")
        raise HTTPException(status_code=500, detail=f"Error clearing history: {str(e)}")

# Generate PDF endpoint
@app.post("/api/generate-pdf", response_model=GeneratePDFResponse)
async def generate_pdf(request: GeneratePDFRequest):
    """
    Generate PDF document from chat history
    
    Args:
        request: GeneratePDFRequest with mode and doc_type
        
    Returns:
        GeneratePDFResponse with PDF URL and filename
    """
    try:
        history = load_history()
        
        if not history:
            raise HTTPException(status_code=400, detail="No chat history found. Have a conversation first.")
        
        # Generate PDF
        pdf_filename = generate_pdf_from_history(
            history, 
            doc_type=request.doc_type,
            mode=request.mode
        )
        
        if not pdf_filename:
            raise HTTPException(status_code=500, detail="Failed to generate PDF")
        
        # Return URL to download PDF
        pdf_url = f"/api/pdf/{pdf_filename}"
        
        return {
            "success": True,
            "pdf_url": pdf_url,
            "filename": pdf_filename
        }
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error generating PDF: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating PDF: {str(e)}")

# Download PDF endpoint
@app.get("/api/pdf/{filename}")
async def download_pdf(filename: str):
    """
    Download generated PDF file
    
    Args:
        filename: Name of the PDF file
        
    Returns:
        FileResponse with PDF file
    """
    try:
        # Check if file exists
        if not os.path.exists(filename):
            raise HTTPException(status_code=404, detail="PDF file not found")
        
        # Return file
        return FileResponse(
            filename,
            media_type="application/pdf",
            filename=filename
        )
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error downloading PDF: {e}")
        raise HTTPException(status_code=500, detail=f"Error downloading PDF: {str(e)}")

# List PDFs endpoint
@app.get("/api/pdfs")
async def list_pdfs():
    """List all generated PDF files"""
    try:
        pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]
        
        return {
            "success": True,
            "pdfs": pdf_files,
            "count": len(pdf_files)
        }
        
    except Exception as e:
        print(f"Error listing PDFs: {e}")
        raise HTTPException(status_code=500, detail=f"Error listing PDFs: {str(e)}")

# Configuration endpoint
@app.get("/api/config")
async def get_config():
    """Get current configuration"""
    return {
        "success": True,
        "config": {
            "model": GEMINI_MODEL,
            "top_k": TOP_K,
            "return_top": RETURN_TOP,
            "db_path": "ChromaDB",
            "collection": "pakistan_law"
        }
    }

# Error handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler"""
    return JSONResponse(
        status_code=500,
        content={
            "success": False,
            "error": str(exc),
            "message": "An unexpected error occurred"
        }
    )

# Run server
if __name__ == "__main__":
    import uvicorn
    import os
    
    # Get port from environment (Railway sets this automatically)
    port = int(os.getenv("PORT", 8000))
    host = os.getenv("HOST", "0.0.0.0")
    
    print("=" * 60)
    print("🚀 Pakistani Legal RAG Assistant API")
    print("=" * 60)
    print(f"📡 Server starting at: http://{host}:{port}")
    print(f"📚 API Documentation: http://{host}:{port}/docs")
    print(f"🤖 AI Model: {GEMINI_MODEL}")
    print(f"🌍 Environment: {os.getenv('ENVIRONMENT', 'development')}")
    print("=" * 60)
    print("\n✅ Server is ready! You can now connect your Flutter app.\n")
    
    uvicorn.run(
        app,
        host=host,
        port=port,
        log_level="info"
    )
