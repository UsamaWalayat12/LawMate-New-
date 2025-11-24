# Vercel Deployment Guide for Pakistani Legal RAG Assistant

This guide will help you deploy your Python FastAPI backend to Vercel.

## 1. Prerequisites

- **Vercel Account**: [Sign up here](https://vercel.com/signup).
- **Vercel CLI** (Optional but recommended): Install via `npm i -g vercel`.
- **GitHub Repository**: Push your code to a GitHub repository.

## 2. Configuration Files (Already Created)

We have already configured the necessary files for you:
- `vercel.json`: Tells Vercel how to build and route your Python app.
- `.vercelignore`: Tells Vercel which files to ignore to keep the deployment small.
- `requirements.txt`: Lists all Python dependencies.
- `backend_api.py`: The main entry point for your API.

## 3. Deployment Steps

### Option A: Deploy via Vercel Dashboard (Recommended)

1.  **Push to GitHub**: Ensure your latest code is pushed to your GitHub repository.
2.  **Import Project**:
    - Go to your [Vercel Dashboard](https://vercel.com/dashboard).
    - Click **"Add New..."** -> **"Project"**.
    - Select your GitHub repository.
3.  **Configure Project**:
    - **Framework Preset**: Select **"Other"** (or leave as default, Vercel usually detects Python).
    - **Root Directory**: `./` (default).
4.  **Environment Variables**:
    - Expand the **"Environment Variables"** section.
    - Add the following variables:
        - `GEMINI_API_KEY`: Your Google Gemini API Key.
        - `GEMINI_MODEL`: `models/gemini-2.5-flash` (or your preferred model).
        - `CHROMA_DB_DIR`: `ChromaDB` (if you are uploading the DB folder).
5.  **Deploy**: Click **"Deploy"**.

### Option B: Deploy via CLI

1.  Open your terminal in the project folder.
2.  Run:
    ```bash
    vercel
    ```
3.  Follow the prompts:
    - Set up and deploy? **Y**
    - Which scope? (Select your account)
    - Link to existing project? **N**
    - Project name? (Press Enter)
    - In which directory? `./`
    - Want to modify settings? **N**
4.  **Set Environment Variables**:
    - Go to the Vercel Dashboard for your new project -> Settings -> Environment Variables.
    - Add `GEMINI_API_KEY` and `GEMINI_MODEL`.
    - Redeploy if needed.

## 4. Important Notes

### ⚠️ ChromaDB Limitations on Vercel
Vercel is a **Serverless** platform with strict size limits (max 250MB for the function bundle).
- **If your `ChromaDB` folder is large**, the deployment will FAIL.
- **Solution**:
    1.  **Use an external Vector DB**: Move to Pinecone, Weaviate, or Chroma Cloud.
    2.  **Reduce DB size**: Only include essential documents.
    3.  **Deploy elsewhere**: Use **Railway** or **Render** (Docker-based) if you need the full local DB.

### ⚠️ Read-Only Filesystem
Vercel functions are read-only (except `/tmp`).
- The API cannot *save* new chat history permanently to `chat_history.json`.
- It cannot *add* new documents to ChromaDB at runtime.
- **PDF Generation**: The API generates PDFs to `/tmp` and serves them. This works fine for immediate download, but files won't persist after the function finishes.

## 5. Verification
After deployment, visit your Vercel URL (e.g., `https://your-project.vercel.app`).
- Go to `/docs` to see the Swagger UI.
- Test the `/health` endpoint.
