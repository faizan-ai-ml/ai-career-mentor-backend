@echo off
echo.
echo ====================================================
echo    AI CAREER MENTOR - BUILDING APK
echo ====================================================
echo.

if not exist "gradlew.bat" (
    echo [ERROR] Please move this script to your ANDROID project root!
    echo (The folder that contains gradlew.bat)
    pause
    exit /b
)

echo [1/2] Cleaning previous builds...
call gradlew.bat clean

echo [2/2] Building Debug APK...
call gradlew.bat assembleDebug

if %errorlevel% neq 0 (
    echo.
    echo [ERROR] Build failed! Check the errors above.
    pause
    exit /b
)

echo.
echo ====================================================
echo    SUCCESS! APK CREATED SUCCESSFULLY
echo ====================================================
echo.
echo Your APK is located at:
echo app\build\outputs\apk\debug\app-debug.apk
echo.
pause
