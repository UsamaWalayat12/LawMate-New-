@echo off
echo ============================================================
echo    Installing API Dependencies
echo ============================================================
echo.
echo This will install FastAPI and required packages...
echo.

pip install -r api_requirements.txt

echo.
echo ============================================================
if %ERRORLEVEL% EQU 0 (
    echo ✓ Installation completed successfully!
    echo.
    echo You can now start the server with: start_server.bat
) else (
    echo ✗ Installation failed. Please check the error messages above.
)
echo ============================================================
echo.
pause
