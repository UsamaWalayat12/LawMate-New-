@echo off
echo ============================================================
echo    Checking API Server Status
echo ============================================================
echo.

curl -s http://localhost:8000/health >nul 2>&1

if %ERRORLEVEL% EQU 0 (
    echo ✓ Server is RUNNING at http://localhost:8000
    echo.
    curl http://localhost:8000/api/status
) else (
    echo ✗ Server is NOT running
    echo.
    echo To start the server, run: start_server.bat
)

echo.
echo ============================================================
pause
