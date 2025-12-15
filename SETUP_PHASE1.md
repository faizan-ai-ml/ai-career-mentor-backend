# AI Career Mentor Backend - Phase 1 Setup Guide

## 📋 What You've Got

All Phase 1 (Authentication) backend files are now created:

### Core Files
- ✅ `app/database.py` - Database connection & session management
- ✅ `app/dependencies.py` - FastAPI auth dependencies
- ✅ `app/main.py` - Main FastAPI application (updated)

### Models & Schemas
- ✅ `app/models/user.py` - User database model
- ✅ `app/schemas/user.py` - Pydantic validation schemas

### Security & Utilities
- ✅ `app/utils/security.py` - Password hashing & JWT tokens
- ✅ `app/utils/validators.py` - Input validation

### API Endpoints
- ✅ `app/api/auth.py` - Authentication routes:
  - `POST /auth/signup` - User registration
  - `POST /auth/login` - User login
  - `GET /auth/me` - Get current user
  - `POST /auth/refresh` - Refresh token
  - `DELETE /auth/account` - Delete account

### Configuration
- ✅ `requirements.txt` - Updated with all dependencies
- ✅ `.env.example` - Environment variables template
- ✅ `alembic.ini` - Database migration config
- ✅ `alembic/env.py` - Alembic environment

---

## 🚀 Setup Instructions

### Step 1: Install Dependencies

```bash
# Activate virtual environment (if not already active)
cd ai-career-mentor-backend
venv\Scripts\activate  # Windows

# Install all dependencies
pip install -r requirements.txt
```

### Step 2: Set Up Database

**Option A: Using Supabase (Recommended - Free)**
1. Go to https://supabase.com
2. Create a new project
3. Go to Project Settings > Database
4. Copy the "Connection String" (URI format)
5. Replace `[YOUR-PASSWORD]` with your database password

**Option B: Using Neon.tech (Also Free)**
1. Go to https://neon.tech
2. Create a new project
3. Copy the connection string from dashboard

**Option C: Local PostgreSQL**
```bash
# Install PostgreSQL locally
# Format: postgresql://username:password@localhost:5432/database_name
```

### Step 3: Configure Environment Variables

1. Copy `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```

2. Edit `.env` file with your actual values:
   ```env
   # MUST CHANGE THESE:
   DATABASE_URL=postgresql://your_database_connection_string
   SECRET_KEY=generate_using_openssl_rand_hex_32
   
   # AI Services (for Phase 3, optional for now):
   OPENROUTER_API_KEY=your_key_here
   GEMINI_API_KEY=your_key_here
   ```

3. Generate a secure SECRET_KEY:
   ```bash
   # On Windows with Git Bash or WSL:
   openssl rand -hex 32
   
   # Or use Python:
   python -c "import secrets; print(secrets.token_hex(32))"
   ```

### Step 4: Initialize Database

```bash
# Initialize Alembic
alembic init alembic

# Create initial migration
alembic revision --autogenerate -m "Initial migration - create users table"

# Apply migration to database
alembic upgrade head
```

### Step 5: Run the Server

```bash
# Start FastAPI development server
uvicorn app.main:app --reload

# Server will start at: http://localhost:8000
# API docs available at: http://localhost:8000/docs
```

---

## 🧪 Testing the API

### 1. Open Swagger Docs
Visit: http://localhost:8000/docs

### 2. Test Signup
```json
POST /auth/signup
{
  "email": "test@example.com",
  "password": "SecurePass123",
  "full_name": "Test User"
}
```

### 3. Test Login
```json
POST /auth/login
{
  "email": "test@example.com",
  "password": "SecurePass123"
}
```
**Copy the `access_token` from response!**

### 4. Test Protected Endpoint
1. Click the "Authorize" button in Swagger UI
2. Enter: `Bearer YOUR_ACCESS_TOKEN`
3. Try: `GET /auth/me`

### 5. Test Resume Analysis (Protected)
```json
POST /analyze-resume
{
  "resume_text": "Experienced Python developer with 5 years of experience in Django and FastAPI..."
}
```

---

## 📁 Project Structure

```
ai-career-mentor-backend/
├── app/
│   ├── __init__.py
│   ├── main.py              ← Main FastAPI app
│   ├── database.py          ← DB connection
│   ├── dependencies.py      ← Auth dependencies
│   │
│   ├── models/
│   │   └── user.py          ← User model
│   │
│   ├── schemas/
│   │   └── user.py          ← Request/response schemas
│   │
│   ├── api/
│   │   └── auth.py          ← Auth endpoints
│   │
│   ├── utils/
│   │   ├── security.py      ← JWT & password hashing
│   │   └── validators.py    ← Input validation
│   │
│   └── services/
│       └── ai_service.py    ← Existing AI service
│
├── alembic/                 ← Database migrations
├── .env                     ← Your config (don't commit!)
├── .env.example             ← Template
├── requirements.txt         ← Dependencies
└── README.md
```

---

## 🔍 Troubleshooting

### Database Connection Error
```
sqlalchemy.exc.OperationalError: could not connect to server
```
**Fix**: Check your `DATABASE_URL` in `.env` file is correct

### Import Errors
```
ModuleNotFoundError: No module named 'app'
```
**Fix**: Make sure you're running from the project root and all `__init__.py` files exist

### JWT Token Error
```
Could not validate credentials
```
**Fix**: 
1. Check `SECRET_KEY` is set in `.env`
2. Make sure you're including the token as: `Authorization: Bearer YOUR_TOKEN`

### Migration Errors
```
alembic.util.exc.CommandError
```
**Fix**: Make sure database is running and `DATABASE_URL` is correct

---

## ✅ Phase 1 Checklist

- [x] Backend project structure
- [x] Database configuration
- [x] User model
- [x] Authentication endpoints
- [x] JWT token system
- [x] Password hashing
- [x] Input validation
- [x] API documentation

**Next**: Test everything, then move to Phase 1 Android! 🎉

---

## 📚 Learning Resources

- **FastAPI**: https://fastapi.tiangolo.com/tutorial/
- **SQLAlchemy**: https://docs.sqlalchemy.org/en/20/
- **Alembic**: https://alembic.sqlalchemy.org/en/latest/
- **JWT**: https://jwt.io/introduction

---

## 🎯 What's Next?

Once backend Phase 1 is working:
1. Build Android Phase 1 (Login/Signup UI)
2. Connect Android to this backend
3. Test end-to-end authentication flow
4. Move to Phase 2 (Resume Upload)
