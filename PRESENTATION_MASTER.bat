@echo off
setlocal enabledelayedexpansion
title AI CAREER MENTOR - PROFESSIONAL PRESENTATION MODE

echo ================================================
echo 💎 AI CAREER MENTOR - PRESENTATION MODE 💎
echo ================================================

:: 1. Cleanup
echo [1/3] Preparing Environment...
d:
cd d:\ai-career-mentor-backend
:: Force kill any process using port 8000
for /f "tokens=5" %%a in ('netstat -ano ^| findstr :8000 ^| findstr LISTENING') do (
    taskkill /F /PID %%a >nul 2>&1
)
taskkill /F /IM python.exe /T /FI "STATUS eq RUNNING" >nul 2>&1
echo ✅ Clean state achieved (Port 8000 is free).

:: 2. Setup Bridge
echo.
echo [2/3] Connecting Phone via USB Bridge...
set "ADB=E:\Newfolder\platform-tools\adb.exe"

:check_device
"%ADB%" devices | findstr /C:"device" | findstr /V "List" > nul
if %errorlevel% neq 0 (
    cls
    echo ================================================
    echo 💎 AI CAREER MENTOR - PRESENTATION MODE 💎
    echo ================================================
    echo.
    echo 🛑 ACTION REQUIRED: Please connect your phone!
    echo.
    echo 1. Plug in USB Cable
    echo 2. Enable "USB Debugging" in phone settings
    echo 3. Click "Allow" on your phone screen
    echo.
    echo Waiting for phone...
    timeout /t 3 > nul
    goto :check_device
)

echo ✅ Phone Detected.
"%ADB%" reverse tcp:8000 tcp:8000
echo ✅ Bridge Established (localhost:8000)

:: 3. Launch Backend
echo.
echo [3/3] Launching AI Backend...
echo ================================================
echo 🚀 PROJECT IS READY FOR PRESENTATION
echo ================================================
echo.
call venv\Scripts\activate
uvicorn app.main:app --host 0.0.0.0 --port 8000
pause
