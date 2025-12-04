# 🎯 **AI CAREER MENTOR - COMPLETE BACKEND DOCUMENTATION**

---

## 📋 **PROJECT OVERVIEW**

### **What We're Building:**
An intelligent AI-powered career mentorship platform that provides personalized career guidance, skill development roadmaps, and continuous learning support through conversational AI. 

### **Target Users:**
- Fresh graduates seeking career direction
- Professionals looking to upskill or change careers
- Students planning their career path

### **Core Value Proposition:**
Instead of generic career advice, our AI analyzes resumes, understands individual backgrounds, and creates personalized learning roadmaps with ongoing AI mentorship.

---

## 🏗️ **BACKEND ARCHITECTURE**

```
┌─────────────────────────────────────────────────────────┐
│                   ANDROID APP (Frontend)                 │
└─────────────────────┬───────────────────────────────────┘
                      │ REST API Calls
                      ▼
┌─────────────────────────────────────────────────────────┐
│              FASTAPI BACKEND (Python)                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │  API Routes (Endpoints)                         │   │
│  │  • /auth (Login/Register)                       │   │
│  │  • /resume (Upload & Analysis)                  │   │
│  │  • /roadmap (Generate Learning Path)            │   │
│  │  • /progress (Track & AI Check-ins)             │   │
│  └──────────────────┬──────────────────────────────┘   │
│                     ▼                                    │
│  ┌─────────────────────────────────────────────────┐   │
│  │  Services (Business Logic)                      │   │
│  │  • Gemini AI Service (AI Operations)            │   │
│  │  • Firebase Service (Database & Auth)           │   │
│  │  • Resume Parser (PDF Processing)               │   │
│  └─────────────────┬───────────────────────────────┘   │
└────────────────────┼───────────────────────────────────┘
                     ▼
┌─────────────────────────────────────────────────────────┐
│            EXTERNAL SERVICES                             │
│  • Google Gemini AI (AI Processing)                     │
│  • Firebase Firestore (Database)                        │
│  • Firebase Storage (Resume PDFs)                       │
│  • Firebase Auth (User Authentication)                  │
└─────────────────────────────────────────────────────────┘
```

---

## 🎯 **BACKEND FUNCTIONALITIES**

### **1. User Authentication & Management**
- User registration with email/password
- Secure login with JWT tokens
- Token-based session management
- User profile storage in Firebase

### **2. Resume Upload & Analysis**
- PDF resume upload
- Extract text from resume using PyPDF2
- AI-powered resume analysis using Gemini:
  - Extract skills, experience, education
  - Identify career strengths and gaps
  - Suggest improvement areas

### **3. Personalized Roadmap Generation**
- Generate custom learning roadmap based on:
  - Current skills from resume
  - Career goals (user input)
  - Industry trends
- Roadmap includes:
  - Skills to learn (ordered by priority)
  - Recommended resources (courses, books, projects)
  - Estimated timeline
  - Milestones and checkpoints

### **4. Progress Tracking**
- Track completed skills/milestones
- Update progress percentage
- Store completion dates

### **5. AI-Powered Check-ins**
- Weekly/bi-weekly AI mentor conversations
- Ask questions about learning
- Get personalized advice
- Adjust roadmap based on progress

### **6. Data Persistence**
- All user data stored in Firebase Firestore
- Resume PDFs stored in Firebase Storage
- Secure and scalable cloud infrastructure

---

## 🛠️ **TECHNOLOGY STACK**

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Framework** | FastAPI | High-performance Python web framework |
| **AI Engine** | Google Gemini AI | Resume analysis, roadmap generation, conversational AI |
| **Database** | Firebase Firestore | NoSQL cloud database for user data |
| **Storage** | Firebase Storage | Cloud storage for resume PDFs |
| **Authentication** | Firebase Auth + JWT | Secure user authentication |
| **PDF Processing** | PyPDF2 | Extract text from resume PDFs |
| **Security** | python-jose, passlib | JWT tokens and password hashing |
| **Server** | Uvicorn | ASGI server for FastAPI |
| **Deployment** | Render/Railway | Cloud hosting platform |

---

## 📁 **PROJECT STRUCTURE**

```
ai-career-mentor-backend/
├── . env                          # Environment variables (NOT in git)
├── . env.example                  # Template for environment setup
├── . gitignore                    # Git ignore rules
├── requirements.txt              # Python dependencies
├── runtime.txt                   # Python version
├── README.md                     # Project documentation
├── app/
│   ├── __init__.py              # Package initialization
│   ├── config.py                # Configuration management
│   ├── main.py                  # FastAPI app entry point
│   ├── services/
│   │   ├── __init__.py
│   │   ├── gemini_service.py    # AI operations
│   │   ├── firebase_service.py  # Database & auth
│   │   └── resume_parser.py     # PDF processing
│   ├── api/
│   │   ├── __init__.py
│   │   └── routes/
│   │       ├── __init__.py
│   │       ├── auth.py          # Authentication endpoints
│   │       ├── resume.py        # Resume operations
│   │       ├── roadmap.py       # Roadmap generation
│   │       └── progress.py      # Progress tracking
│   ├── models/
│   │   ├── __init__.py
│   │   ├── user.py              # User data models
│   │   ├── resume.py            # Resume data models
│   │   └── roadmap.py           # Roadmap data models
│   └── utils/
│       ├── __init__.py
│       └── helpers.py           # Helper functions
└── tests/
    ├── __init__.py
    └── test_api.py              # API tests
```

---

## 🗺️ **COMPLETE DEVELOPMENT PLAN**

---

### **PHASE 1: Core Infrastructure Setup** ✅ (MOSTLY DONE)
**Goal:** Set up project foundation and configuration

**Tasks:**
- ✅ Project structure created
- ✅ Configuration management (`config.py`)
- ✅ FastAPI app initialization (`main.py`)
- ✅ Environment variables setup
- ⏳ Complete README documentation

**Deliverables:**
- Working FastAPI server
- Health check endpoint working
- Environment properly configured

---

### **PHASE 2: Services Layer (AI & Firebase)** 🔥 **NEXT**
**Goal:** Build core business logic services

**Tasks:**
1. Create `gemini_service.py` - AI operations
2. Create `firebase_service.py` - Database & auth
3. Create `resume_parser.py` - PDF processing
4. Test all services independently

**Deliverables:**
- Gemini AI working (can analyze text)
- Firebase connected (can read/write data)
- PDF parsing working

---

### **PHASE 3: Data Models**
**Goal:** Define all request/response schemas

**Tasks:**
1. Create user models
2. Create resume models
3.  Create roadmap models
4. Add validation rules

**Deliverables:**
- All Pydantic models defined
- Request/response schemas ready

---

### **PHASE 4: Authentication API**
**Goal:** Implement user registration and login

**Tasks:**
1. Create auth routes (`/register`, `/login`)
2. JWT token generation
3. Password hashing
4. Protected route middleware

**Deliverables:**
- Users can register
- Users can login and get tokens
- Token validation working

---

### **PHASE 5: Resume API**
**Goal:** Resume upload and AI analysis

**Tasks:**
1.  Create resume upload endpoint
2.  Integrate resume parser
3.  Integrate Gemini AI for analysis
4. Store resume data in Firebase

**Deliverables:**
- Upload PDF resume
- Get AI-powered analysis
- Data persisted in database

---

### **PHASE 6: Roadmap API**
**Goal:** Generate personalized learning roadmaps

**Tasks:**
1. Create roadmap generation endpoint
2. Use Gemini to create custom roadmap
3. Store roadmap in Firebase
4.  Fetch user's roadmap

**Deliverables:**
- Generate roadmap based on resume + goals
- Retrieve roadmap for user
- Update roadmap

---

### **PHASE 7: Progress Tracking API**
**Goal:** Track learning progress and AI check-ins

**Tasks:**
1. Create progress update endpoint
2. Create AI check-in endpoint
3.  Track milestones completion

**Deliverables:**
- Update progress on skills
- AI conversational check-ins
- Progress history

---

### **PHASE 8: Testing & Documentation**
**Goal:** Ensure quality and usability

**Tasks:**
1.  Write API tests
2. Complete README
3. API documentation (Swagger)
4. Error handling improvements

**Deliverables:**
- Comprehensive tests
- Clear setup instructions
- Well-documented API

---

### **PHASE 9: Deployment**
**Goal:** Deploy backend to production

**Tasks:**
1. Setup Render/Railway account
2. Configure environment variables
3. Deploy backend
4. Test production API

**Deliverables:**
- Live backend URL
- All endpoints accessible
- Ready for Android integration

---

### **PHASE 10: Android App Development** 📱
**Goal:** Build Android frontend

**Tasks:**
- UI/UX design
- API integration
- Testing
- Play Store deployment
