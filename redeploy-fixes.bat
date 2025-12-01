@echo off
echo ================================================
echo Redeploying FIXED Code to Railway
echo ================================================
echo.
echo This will deploy the updated code with:
echo   - Fixed filtering logic (200 -^> 50 chars)
echo   - Fallback to return results
echo   - Better error messages
echo.
echo ================================================
pause

echo.
echo Step 1: Checking Railway CLI...
railway --version
if %errorlevel% neq 0 (
    echo ERROR: Railway CLI not found!
    echo Please install from: https://railway.app/cli
    pause
    exit /b 1
)
echo OK: Railway CLI found
echo.

echo Step 2: Deploying updated code to Railway...
echo.
echo IMPORTANT: This will upload your FIXED code to Railway
echo.
railway up

echo.
echo ================================================
echo Deployment Complete!
echo ================================================
echo.
echo Next Steps:
echo 1. Wait 2-3 minutes for Railway to rebuild
echo 2. Test your chatbot in the Flutter app
echo 3. You should now get real answers instead of "no evidence"
echo.
echo Check deployment status:
echo https://railway.app/dashboard
echo.
pause
