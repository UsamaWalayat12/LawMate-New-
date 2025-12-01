@echo off
REM Quick Railway Deployment Script
REM This script helps you deploy to Railway

echo.
echo ========================================
echo Railway Deployment Quick Start
echo ========================================
echo.

echo Prerequisites:
echo - Railway CLI installed (npm install -g @railway/cli)
echo - GitHub repository with code pushed
echo - Railway account at https://railway.app
echo.

echo Step 1: Install Railway CLI
echo Command: npm install -g @railway/cli
echo.

echo Step 2: Login to Railway
echo Command: railway login
echo.

echo Step 3: Create Railway Project
echo Go to https://railway.app and create new project
echo Select "Deploy from GitHub"
echo.

echo Step 4: Set Environment Variables
echo In Railway Dashboard, go to Variables and add:
echo   - GOOGLE_API_KEY
echo   - CHROMA_API_KEY
echo   - CHROMA_TENANT_ID
echo   - CHROMA_COLLECTION
echo   - PORT (8000)
echo   - HOST (0.0.0.0)
echo.

echo Step 5: Deploy
echo Option A - Automatic (GitHub integration):
echo   Push to GitHub, Railway auto-deploys
echo.
echo Option B - Manual (using Railway CLI):
echo   railway up
echo.

echo Step 6: Monitor
echo   railway logs
echo.

echo For more info, see RAILWAY_SETUP.md
echo.
pause
