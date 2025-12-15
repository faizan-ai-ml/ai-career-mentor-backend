@echo off
echo ================================================
echo Setting up Python Virtual Environment
echo ================================================

REM Create virtual environment
echo Creating virtual environment...
python -m venv venv

REM Activate virtual environment
echo Activating virtual environment...
call venv\Scripts\activate

REM Upgrade pip
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies from requirements.txt...
pip install -r requirements.txt

echo.
echo ================================================
echo ✅ Setup Complete!
echo ================================================
echo.
echo To activate the virtual environment in the future, run:
echo   venv\Scripts\activate
echo.
echo To deactivate, run:
echo   deactivate
echo.
pause
REM Start the server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

