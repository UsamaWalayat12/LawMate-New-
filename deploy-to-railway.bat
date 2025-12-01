@echo off
echo ================================================
echo Deploying AI Assistant to Railway
echo ================================================
echo.

echo Step 1: Checking if Railway CLI is installed...
railway --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ Railway CLI not found!
    echo.
    echo Please install Railway CLI first:
    echo 1. Visit: https://railway.app/cli
    echo 2. Download and install Railway CLI
    echo 3. Run this script again
    echo.
    pause
    exit /b 1
)

echo ✅ Railway CLI found

echo.
echo Step 2: Login to Railway...
railway login

echo.
echo Step 3: Initialize Railway project...
railway init

echo.
echo Step 4: Setting up environment variables...
echo.
echo ⚠️  IMPORTANT: You need to set your Google API key
echo.
set /p api_key="Enter your Google Gemini API key: "

if "%api_key%"=="" (
    echo ❌ API key is required!
    pause
    exit /b 1
)

echo.
echo Optional: Chroma Cloud Credentials (press Enter to skip if using local DB)
set /p chroma_key="Enter Chroma API Key: "
set /p chroma_tenant="Enter Chroma Tenant ID: "
set /p chroma_db="Enter Chroma Database Name: "

railway variables set GEMINI_API_KEY=%api_key%
if not "%chroma_key%"=="" railway variables set CHROMA_API_KEY=%chroma_key%
if not "%chroma_tenant%"=="" railway variables set CHROMA_TENANT=%chroma_tenant%
if not "%chroma_db%"=="" railway variables set CHROMA_DATABASE=%chroma_db%

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
echo Your AI Assistant is now live 24/7!
echo.
echo Next steps:
echo 1. Get your Railway URL from the dashboard
echo 2. Update Flutter app with the production URL
echo 3. Build and test your app
echo.
echo Visit Railway dashboard to get your URL:
echo https://railway.app/dashboard
echo.
pause