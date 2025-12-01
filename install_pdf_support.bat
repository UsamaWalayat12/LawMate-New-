@echo off
echo ========================================
echo Installing PDF Generation Support
echo ========================================
echo.
echo Installing reportlab library...
pip install reportlab
echo.
echo ========================================
echo Installation Complete!
echo ========================================
echo.
echo You can now use PDF generation features:
echo   python chroma_test.py --generate-pdf
echo.
pause
