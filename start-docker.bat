@echo off
echo ============================================
echo AI Career Mentor - Docker Deployment
echo ============================================
echo.

REM Check if Docker is running
docker info >nul 2>&1
if errorlevel 1 (
    echo [ERROR] Docker is not running!
    echo Please start Docker Desktop and try again.
    pause
    exit /b 1
)

echo [OK] Docker is running
echo.

echo Starting services...
echo This will:
echo  - Start PostgreSQL database
echo  - Run database migrations
echo  - Start FastAPI backend
echo.

docker-compose up --build

pause
