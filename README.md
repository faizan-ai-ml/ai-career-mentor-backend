# 🚀 **AI CAREER MENTOR - Complete Startup Documentation**

## **📋 Project Overview**

**Name:** AI Career Mentor  
**Purpose:** AI-powered mobile app that analyzes resumes and generates personalized career guidance & learning roadmaps  
**Target Users:** Job seekers, career changers, students  
**Monetization:** Freemium model (basic free, advanced features paid)

---

## **🏗️ Tech Stack (100% FREE)**

### **Backend:**
- **Framework:** FastAPI (Python)
- **Database:** PostgreSQL (Free tier:  Supabase or Neon. tech)
- **AI Services:** 
  - OpenRouter API (Free tier - DeepSeek/Llama models)
  - Gemini API (Free tier - backup)
- **File Storage:** Cloudinary (Free tier) or Supabase Storage
- **Authentication:** Supabase Auth (Free)
- **Hosting:** Railway. app or Render.com (Free tier)

### **Frontend (Android App):**
- **Language:** Kotlin
- **Framework:** Jetpack Compose (Modern Android UI)
- **Architecture:** MVVM + Clean Architecture
- **Networking:** Retrofit + OkHttp
- **Database (Local):** Room Database
- **Dependency Injection:** Hilt/Dagger
- **Image Loading:** Coil

### **DevOps & Tools:**
- **Version Control:** GitHub
- **API Testing:** Postman (Free)
- **Database Management:** DBeaver (Free)
- **Android IDE:** Android Studio (Free)

---

## **📁 Repository Structure**

### **Backend Repo:** `ai-career-mentor-backend`
```
ai-career-mentor-backend/
├── app/
│   ├── __init__.py
│   ├── main.py                    # FastAPI app entry
│   ├── config.py                  # Configuration & environment
│   ├── database. py                # PostgreSQL connection
│   ├── dependencies.py            # FastAPI dependencies
│   │
│   ├── models/                    # SQLAlchemy ORM models
│   │   ├── __init__.py
│   │   ├── user. py
│   │   ├── resume.py
│   │   ├── analysis.py
│   │   └── roadmap.py
│   │
│   ├── schemas/                   # Pydantic schemas (request/response)
│   │   ├── __init__.py
│   │   ├── user.py
│   │   ├── resume.py
│   │   ├── analysis.py
│   │   └── roadmap.py
│   │
│   ├── api/                       # API routes
│   │   ├── __init__.py
│   │   ├── auth.py                # Login, signup, token
│   │   ├── resume.py              # Upload, list, delete
│   │   ├── analysis.py            # Analyze resume
│   │   └── roadmap.py             # Get/update roadmap
│   │
│   ├── services/                  # Business logic
│   │   ├── __init__.py
│   │   ├── ai_service.py          # Main AI orchestrator
│   │   ├── openrouter_service.py  # OpenRouter integration
│   │   ├── gemini_service.py      # Gemini backup
│   │   ├── resume_parser.py       # Resume text extraction
│   │   ├── skill_extractor.py     # Skill identification
│   │   └── roadmap_generator.py   # Roadmap creation
│   │
│   ├── utils/                     # Helpers
│   │   ├── __init__.py
│   │   ├── security.py            # Password hashing, JWT
│   │   ├── validators.py          # Input validation
│   │   └── helpers.py             # Common utilities
│   │
│   └── tests/                     # Unit tests
│       ├── __init__.py
│       ├── test_auth.py
│       ├── test_resume.py
│       └── test_analysis.py
│
├── alembic/                       # Database migrations
│   ├── versions/
│   └── env. py
│
├── .env.example                   # Environment template
├── .gitignore
├── requirements.txt               # Python dependencies
├── alembic.ini                    # Migration config
├── README.md
└── Dockerfile                     # For deployment
```

### **Frontend Repo:** `ai-career-mentor-android`
```
ai-career-mentor-android/
├── app/
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/yourname/aicareermentor/
│   │   │   │   ├── MainActivity. kt
│   │   │   │   │
│   │   │   │   ├── data/              # Data layer
│   │   │   │   │   ├── local/         # Room database
│   │   │   │   │   │   ├── dao/
│   │   │   │   │   │   ├── entities/
│   │   │   │   │   │   └── AppDatabase.kt
│   │   │   │   │   │
│   │   │   │   │   ├── remote/        # API calls
│   │   │   │   │   │   ├── api/
│   │   │   │   │   │   │   ├── AuthApi.kt
│   │   │   │   │   │   │   ├── ResumeApi.kt
│   │   │   │   │   │   │   └── AnalysisApi.kt
│   │   │   │   │   │   ├── dto/       # Data transfer objects
│   │   │   │   │   │   └── RetrofitClient.kt
│   │   │   │   │   │
│   │   │   │   │   ├── repository/    # Repository pattern
│   │   │   │   │   │   ├── AuthRepository.kt
│   │   │   │   │   │   ├── ResumeRepository. kt
│   │   │   │   │   │   └── AnalysisRepository.kt
│   │   │   │   │   │
│   │   │   │   │   └── models/        # Domain models
│   │   │   │   │
│   │   │   │   ├── domain/            # Business logic
│   │   │   │   │   ├── usecase/
│   │   │   │   │   │   ├── LoginUseCase.kt
│   │   │   │   │   │   ├── AnalyzeResumeUseCase.kt
│   │   │   │   │   │   └── GetRoadmapUseCase. kt
│   │   │   │   │   └── Result.kt      # Result wrapper
│   │   │   │   │
│   │   │   │   ├── presentation/      # UI layer
│   │   │   │   │   ├── auth/
│   │   │   │   │   │   ├── LoginScreen.kt
│   │   │   │   │   │   ├── SignupScreen.kt
│   │   │   │   │   │   └── AuthViewModel.kt
│   │   │   │   │   │
│   │   │   │   │   ├── home/
│   │   │   │   │   │   ├── HomeScreen.kt
│   │   │   │   │   │   └── HomeViewModel.kt
│   │   │   │   │   │
│   │   │   │   │   ├── resume/
│   │   │   │   │   │   ├── ResumeUploadScreen.kt
│   │   │   │   │   │   ├── ResumeListScreen.kt
│   │   │   │   │   │   └── ResumeViewModel.kt
│   │   │   │   │   │
│   │   │   │   │   ├── analysis/
│   │   │   │   │   │   ├── AnalysisScreen.kt
│   │   │   │   │   │   └── AnalysisViewModel. kt
│   │   │   │   │   │
│   │   │   │   │   ├── roadmap/
│   │   │   │   │   │   ├── RoadmapScreen.kt
│   │   │   │   │   │   └── RoadmapViewModel.kt
│   │   │   │   │   │
│   │   │   │   │   ├── components/    # Reusable UI
│   │   │   │   │   ├── navigation/    # Nav graph
│   │   │   │   │   └── theme/         # App theme
│   │   │   │   │
│   │   │   │   ├── di/                # Dependency injection
│   │   │   │   │   ├── AppModule.kt
│   │   │   │   │   ├── NetworkModule.kt
│   │   │   │   │   └── DatabaseModule.kt
│   │   │   │   │
│   │   │   │   └── utils/             # Utilities
│   │   │   │       ├── Constants.kt
│   │   │   │       ├── SharedPrefs.kt
│   │   │   │       └── Extensions.kt
│   │   │   │
│   │   │   ├── res/                   # Resources
│   │   │   │   ├── drawable/
│   │   │   │   ├── values/
│   │   │   │   └── xml/
│   │   │   │
│   │   │   └── AndroidManifest.xml
│   │   │
│   │   └── test/                      # Unit tests
│   │
│   └── build.gradle. kts               # App dependencies
│
├── gradle/
├── build.gradle.kts                   # Project config
├── settings.gradle.kts
├── . gitignore
└── README.md
```

---

## **🎯 Phase-Based Development Plan**

Each phase updates **BOTH** backend and Android app repos! 

---

### **📱 PHASE 1: Authentication & User Management**

#### **Backend Tasks:**
1. ✅ Setup FastAPI project structure
2. ✅ Configure PostgreSQL database (Supabase/Neon)
3. ✅ Create User model (id, email, password_hash, created_at)
4. ✅ Implement JWT authentication
5. ✅ Create API endpoints: 
   - `POST /auth/signup` - User registration
   - `POST /auth/login` - User login
   - `POST /auth/refresh` - Refresh token
   - `GET /auth/me` - Get current user
6. ✅ Add password hashing (bcrypt)
7. ✅ Add input validation
8. ✅ Test with Postman

#### **Android Tasks:**
1. ✅ Setup Android project with Jetpack Compose
2. ✅ Setup Retrofit for API calls
3. ✅ Setup Room database for local storage
4. ✅ Setup Hilt for dependency injection
5. ✅ Create Login Screen UI
6. ✅ Create Signup Screen UI
7. ✅ Implement AuthViewModel
8. ✅ Implement token storage (SharedPreferences)
9. ✅ Setup navigation (Login → Home)
10. ✅ Test authentication flow

**Deliverables:**
- Working login/signup in Android app
- Backend API with authentication
- Token-based security

---

### **📄 PHASE 2: Resume Upload & Storage**

#### **Backend Tasks:**
1. ✅ Create Resume model (id, user_id, filename, text_content, uploaded_at)
2. ✅ Setup file storage (Cloudinary/Supabase Storage)
3. ✅ Create resume parser (extract text from PDF/DOCX)
4. ✅ Create API endpoints:
   - `POST /resume/upload` - Upload resume file
   - `GET /resume/list` - List user's resumes
   - `GET /resume/{id}` - Get specific resume
   - `DELETE /resume/{id}` - Delete resume
5. ✅ Add file validation (size, type)
6. ✅ Associate resumes with users

#### **Android Tasks:**
1. ✅ Create Resume Upload Screen UI
2. ✅ Implement file picker (PDF/DOCX)
3. ✅ Create ResumeViewModel
4. ✅ Implement file upload with progress
5. ✅ Create Resume List Screen
6. ✅ Display uploaded resumes
7. ✅ Add delete resume functionality
8. ✅ Add loading states & error handling

**Deliverables:**
- Users can upload resumes from Android app
- Backend stores and manages resume files
- Users can view/delete their resumes

---

### **🤖 PHASE 3: AI Resume Analysis**

#### **Backend Tasks:**
1. ✅ Create Analysis model (id, resume_id, skills, experience_level, analysis_date)
2. ✅ Integrate OpenRouter API (DeepSeek model)
3. ✅ Integrate Gemini API (backup)
4. ✅ Create structured prompts for: 
   - Skill extraction (return JSON array)
   - Experience level detection (Junior/Mid/Senior)
   - Top 5 career matches with % scores
5. ✅ Create API endpoint:
   - `POST /analysis/analyze/{resume_id}` - Analyze resume
   - `GET /analysis/{resume_id}` - Get analysis results
6. ✅ Parse AI responses into structured data
7. ✅ Store analysis in database

#### **Android Tasks:**
1. ✅ Create Analysis Screen UI
2. ✅ Display extracted skills (chips/tags)
3. ✅ Display experience level (badge)
4. ✅ Display career matches (cards with %)
5. ✅ Create AnalysisViewModel
6. ✅ Add "Analyze Resume" button
7. ✅ Show loading animation during analysis
8. ✅ Cache analysis results locally

**Deliverables:**
- Resume analysis with skill extraction
- Experience level detection
- Career recommendations
- Beautiful UI showing results

---

### **🗺️ PHASE 4: Learning Roadmap Generation**

#### **Backend Tasks:**
1. ✅ Create Roadmap model (id, analysis_id, week_number, tasks, resources)
2. ✅ Create roadmap generation prompt: 
   - 8-week personalized plan
   - Based on skills gap and target career
   - Include specific resources (courses, books, projects)
3. ✅ Create API endpoints:
   - `POST /roadmap/generate/{analysis_id}` - Generate roadmap
   - `GET /roadmap/{analysis_id}` - Get roadmap
   - `PATCH /roadmap/{id}/week/{week}` - Mark week complete
4. ✅ Structure roadmap as JSON (week-by-week)
5. ✅ Add progress tracking

#### **Android Tasks:**
1. ✅ Create Roadmap Screen UI
2. ✅ Display 8-week timeline
3. ✅ Show expandable week cards
4. ✅ Display tasks and resources per week
5. ✅ Add checkboxes for task completion
6. ✅ Create RoadmapViewModel
7. ✅ Show progress indicator (% complete)
8. ✅ Add ability to mark weeks as complete

**Deliverables:**
- 8-week personalized learning roadmap
- Interactive week-by-week view
- Progress tracking
- Resource links

---

### **✨ PHASE 5: Polish & Enhancement**

#### **Backend Tasks:**
1. ✅ Add user profile endpoint
2. ✅ Add analytics (track usage)
3. ✅ Implement rate limiting
4. ✅ Add caching (Redis - free tier)
5. ✅ Optimize database queries
6. ✅ Add comprehensive error logging
7. ✅ Write API documentation (Swagger)
8. ✅ Add health check endpoint

#### **Android Tasks:**
1. ✅ Create Home Dashboard
2. ✅ Add dark mode support
3. ✅ Implement pull-to-refresh
4. ✅ Add animations & transitions
5. ✅ Create profile screen
6. ✅ Add settings screen
7. ✅ Implement offline mode
8. ✅ Add onboarding screens
9. ✅ Polish UI/UX
10. ✅ Add app icon & splash screen

**Deliverables:**
- Production-ready backend
- Polished Android app
- Smooth user experience
- Professional UI

---

### **🚀 PHASE 6: Deployment & Launch**

#### **Backend Tasks:**
1. ✅ Deploy to Railway/Render
2. ✅ Setup production database
3. ✅ Configure environment variables
4. ✅ Setup CI/CD (GitHub Actions)
5. ✅ Add monitoring (free tier)
6. ✅ Setup backup strategy

#### **Android Tasks:**
1. ✅ Generate signed APK
2. ✅ Test on real devices
3. ✅ Create Google Play listing
4. ✅ Prepare screenshots & description
5. ✅ Submit to Google Play Store
6. ✅ Setup crash reporting (Firebase)

**Deliverables:**
- Live backend API
- Published Android app
- Ready for users! 

---

## **📊 Database Schema**

```sql
-- Users table
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    full_name VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Resumes table
CREATE TABLE resumes (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    filename VARCHAR(255) NOT NULL,
    file_url TEXT NOT NULL,
    text_content TEXT,
    uploaded_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Analysis table
CREATE TABLE analysis (
    id SERIAL PRIMARY KEY,
    resume_id INTEGER REFERENCES resumes(id) ON DELETE CASCADE,
    skills JSONB NOT NULL,
    experience_level VARCHAR(50) NOT NULL,
    top_careers JSONB NOT NULL,
    analyzed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Roadmaps table
CREATE TABLE roadmaps (
    id SERIAL PRIMARY KEY,
    analysis_id INTEGER REFERENCES analysis(id) ON DELETE CASCADE,
    roadmap_data JSONB NOT NULL,
    progress INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## **🔑 Key Features Summary**

1. **User Authentication** - Secure JWT-based auth
2. **Resume Upload** - PDF/DOCX support
3. **AI Analysis** - Skill extraction, experience level
4. **Career Matching** - Top 5 careers with match %
5. **8-Week Roadmap** - Personalized learning plan
6. **Progress Tracking** - Mark tasks complete
7. **Offline Support** - Local caching in Android
8. **Beautiful UI** - Modern Jetpack Compose
9. **Free Tier** - All services use free tiers

---

## **📝 Agent Handoff Instructions**

Any agent continuing this project should: 
1. Read this complete documentation first
2. Check which phase is currently active
3. Look at both backend and Android repos
4. Complete remaining tasks in current phase
5. Test thoroughly before moving to next phase
6. Update documentation if making changes
7. Follow the exact folder structure outlined above
