"""
Vercel serverless function entry point
"""
import sys
import os

# Add the parent directory to the path so we can import our modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Import the FastAPI app from backend_api.py
from backend_api import app

# Vercel expects the app to be available as 'app'
# This is the entry point for Vercel serverless functions