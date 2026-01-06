# AI Career Mentor - Quick Start Guide

## For Investor Presentation

### One-Click Startup

```bash
cd d:\ai-career-mentor-backend
PRESENTATION_MASTER.bat
```

This script automatically:
1. ✅ Checks Docker is running
2. ✅ Starts PostgreSQL database
3. ✅ Starts FastAPI backend
4. ✅ Connects your phone via ADB
5. ✅ Verifies Android app configuration

### What You Need

- Docker Desktop (running)
- Phone connected via USB
- USB Debugging enabled on phone
- Android Studio open

### The Script Handles

- Port cleanup (kills any process on 8000)
- Docker container management
- Database migrations
- ADB reverse proxy setup
- Health checks

### If Something Goes Wrong

The script will tell you exactly what to do. Just follow the on-screen instructions.

### Manual Shutdown

```bash
docker-compose down
```

---

**Ready to impress investors!** 🚀
