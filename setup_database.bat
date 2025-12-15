@echo off
echo ================================================
echo AI Career Mentor - Database Setup
echo ================================================

REM Activate virtual environment
call venv\Scripts\activate

echo.
echo ✅ Virtual environment activated
echo.

REM Create database tables directly using SQLAlchemy
echo Creating database tables...
python -c "from app.database import Base, engine; Base.metadata.create_all(bind=engine); print('✅ Database tables created successfully!')"

echo.
echo ================================================
echo Database setup complete!
echo ================================================
echo.
echo Next step: Run the server with start_server.bat
echo.
pause
