# 🐍 Virtual Environment Setup Guide

## Quick Setup (Recommended)

### Option 1: Using the Batch Script
Simply double-click `setup_venv.bat` or run:
```bash
setup_venv.bat
```

This will automatically:
- Create the virtual environment
- Activate it
- Upgrade pip
- Install all dependencies

---

## Manual Setup

### Step 1: Create Virtual Environment
```bash
cd ai-career-mentor-backend
python -m venv venv
```

### Step 2: Activate Virtual Environment

**Windows (Command Prompt)**:
```bash
venv\Scripts\activate
```

**Windows (PowerShell)**:
```powershell
venv\Scripts\Activate.ps1
```

**If PowerShell gives error**, run this first (as Administrator):
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

### Step 3: Upgrade pip
```bash
python -m pip install --upgrade pip
```

### Step 4: Install Dependencies
```bash
pip install -r requirements.txt
```

---

## Verify Installation

Check if everything is installed:
```bash
pip list
```

You should see packages like:
- fastapi
- uvicorn
- sqlalchemy
- psycopg2-binary
- python-jose
- passlib
- alembic

---

## Daily Workflow

### Start Working
```bash
# Navigate to project
cd ai-career-mentor-backend

# Activate venv
venv\Scripts\activate

# Your prompt should show (venv) now
```

### Run the Server
```bash
# Make sure venv is activated (you'll see (venv) in prompt)
uvicorn app.main:app --reload
```

### Stop Working
```bash
# Deactivate venv when done
deactivate
```

---

## Troubleshooting

### "python: command not found"
- Install Python from python.org
- Make sure Python is in PATH

### "No module named 'pip'"
```bash
python -m ensurepip --upgrade
```

### Dependencies not installing
```bash
# Update pip first
python -m pip install --upgrade pip

# Then try again
pip install -r requirements.txt
```

### PowerShell Execution Policy Error
```powershell
# Run as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

---

## Check Python Version

```bash
python --version
```

**Required**: Python 3.8 or higher (3.11 recommended)

---

## Virtual Environment Status

To check if venv is activated:
- Look for `(venv)` at the beginning of your command prompt
- Or run: `where python` (should point to venv folder)

---

## Clean Reinstall

If you need to start fresh:

```bash
# Deactivate if active
deactivate

# Delete venv folder
rmdir /s venv

# Create new venv
python -m venv venv

# Activate
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

---

✅ Once setup is complete, you can run the server with:
```bash
uvicorn app.main:app --reload
```
