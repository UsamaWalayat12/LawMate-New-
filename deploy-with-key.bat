@echo off
echo ================================================
echo Deploying AI Assistant to Railway (Auto-Key)
echo ================================================
echo.

echo Step 1: Checking if Railway CLI is installed...
railway --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Railway CLI not found!
    echo Please install it: npm install -g @railway/cli
    pause
    exit /b 1
)

echo ✅ Railway CLI found
echo.

echo Step 2: Login to Railway...
:: railway login
echo (Skipping login - already done)
echo.

echo Step 3: Initialize Railway project...
:: railway init
echo (Skipping init - already done)
echo.

echo Step 4: Setting up environment variables...
echo Using provided API Key...
set api_key=AIzaSyBO7g1SWj-fxSsWIxslHsK7zrjfSPfhoG8

railway variables set GEMINI_API_KEY=%api_key%
railway variables set PORT=8000
railway variables set HOST=0.0.0.0
railway variables set ENVIRONMENT=production

echo.
echo Step 5: Deploying to Railway...
echo This may take a few minutes...
railway up

echo.
echo ================================================
echo 🎉 Deployment Complete!
echo ================================================
echo.
echo Visit Railway dashboard to get your URL:
echo https://railway.app/dashboard
echo.
pause
