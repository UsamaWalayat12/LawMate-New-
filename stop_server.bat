@echo off
echo ============================================================
echo    Stopping Pakistani Legal RAG Assistant API Server
echo ============================================================
echo.

taskkill /F /IM python.exe /FI "WINDOWTITLE eq *backend_api*" 2>nul

if %ERRORLEVEL% EQU 0 (
    echo ✓ Server stopped successfully
) else (
    echo ℹ No server process found running
)

echo.
pause
