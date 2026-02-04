@echo off
title Phishing Detection System Server
color 0A
echo ========================================
echo   PHISHING & FRAUD DETECTION SYSTEM
echo ========================================
echo.
echo Checking Python installation...
python --version
echo.
echo Installing/Checking dependencies...
pip install -r requirements.txt --quiet
echo.
echo ========================================
echo   Starting Server...
echo ========================================
echo.
echo Server will start at: http://localhost:5000
echo.
echo Press Ctrl+C to stop the server
echo.
echo ========================================
echo.
python app.py
pause

