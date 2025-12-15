@echo off
echo ================================================
echo Starting AI Career Mentor Backend Server
echo ================================================

REM Activate virtual environment
call venv\Scripts\activate

echo.
echo ✅ Virtual environment activated
echo.
echo Starting FastAPI server...
echo Server will be available at: http://localhost:8000
echo API Documentation at: http://localhost:8000/docs
echo.
echo Press Ctrl+C to stop the server
echo ================================================
echo.

REM Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
