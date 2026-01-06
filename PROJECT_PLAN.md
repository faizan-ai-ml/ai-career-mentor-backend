# AI Career Mentor - Development Task Checklist

## Current Status: Phase 1 Backend Complete ✅ | Starting Android Development 🤖

### Phase 1: Foundation & Authentication
- [x] Backend: Project setup and database configuration
- [x] Backend: Implement User Model and Schemas
- [x] Backend: Authentication API (Signup/Login/JWT)
- [x] Backend: AI Service Integration (DeepSeek/Gemini)
- [x] Android: Project Setup (MVVM, Hilt, Retrofit)
- [x] Android: Login & Signup Screens (Jetpack Compose)
- [x] Android: API Integration & Token Management
- [x] Phase 1 Verification (End-to-End Testing)
  - [x] Build auth endpoints (signup, login, refresh, me)
  - [x] Test with Postman
  - [x] Set up Retrofit for networking
  - [x] Set up Room database for local caching
- [x] Android: Authentication UI and logic
  - [x] Create Login screen
  - [x] Create Signup screen
  - [x] Build AuthViewModel
  - [x] Implement token storage
  - [x] Set up navigation
  - [x] Test authentication flow

### Phase 2: Resume Management
- [x] Backend: Resume upload and storage
  - [x] Create Resume model and schema
  - [x] Set up file storage (Local Filesystem)
  - [x] Implement resume parser (PDF/DOCX extraction)
  - [x] Build resume endpoints (upload, list, get, delete)
  - [x] Add file validation
- [x] Android: Resume upload and Profile Builder UI
  - [x] Create Welcome Screen (Selection)
  - [x] Create Resume Upload screen
  - [x] Create Profile Creation screen (Beginner flow)
  - [x] Implement file picker
  - [x] Build ProfileViewModel
  - [x] Implement upload progress
  - [x] Create Resume List screen (Dashboard integration)
  - [x] **Smart Navigation** (Auto-Login & Profile Check)

### Phase 3: AI Career Coach (The "Brain")
- [x] Backend: AI Service Integration
  - [x] Setup Gemini 1.5 Flash client (via OpenRouter)
  - [x] Create `analyze_resume` endpoint (Score & Feedback)
  - [x] Create `improve_content` endpoint (AI Rewriting)
  - [x] Create `generate_roadmap` endpoint
  - [x] Create `career_counselor` endpoint (New!)
- [x] Android: AI Features UI
  - [x] "Resume Analysis" Card (Score visualization & Radar Chart)
  - [x] "Career Counselor" Screen (Simulation Questions)
  - [x] "Roadmap" Timeline View (Persisted & Interactive)
  - [x] "AI Writer" (Improve my profile text)

### Phase 4: Resume Builder (The "Output")
- [ ] Backend: PDF Generation (Skipped by User Request)
- [x] **Analysis Results UI** (Replacement)
  - [x] Create `AnalysisScreen` (Score, Skills, Matches)
  - [x] Visualize Missing Skills & Experience Level
  - [x] Connect "AI Analysis" button to this screen

### Phase 4: Learning Roadmap
- [x] Backend: Roadmap generation
  - [x] Create Roadmap model and schema
  - [x] Build roadmap generation prompt
  - [x] Create roadmap endpoints (GET/POST/UPDATE)
  - [x] Implement progress tracking (Persisted in DB)
- [x] Android: Roadmap visualization
  - [x] Create Roadmap screen
  - [x] Display 8-week timeline
  - [x] Build expandable week cards
  - [x] Add task completion checkboxes (Interactive)
  - [x] Build RoadmapViewModel (With persistence loading)
  - [x] Show progress indicator (Real-time)

### Phase 5: Polish & Enhancement
- [ ] Backend: Production readiness
  - [ ] Add user profile endpoints
  - [ ] Implement rate limiting
  - [ ] Add caching layer
  - [ ] Optimize queries
  - [ ] Add error logging
  - [ ] Create API documentation
- [ ] Android: UX enhancements
  - [x] Create Home Dashboard
  - [ ] Add dark mode
  - [ ] Implement animations
  - [x] Create profile screen (via Welcome/Wizard)
  - [ ] Add settings screen
  - [ ] Implement offline mode
  - [ ] Add onboarding
  - [x] Polish UI/UX (Clickable links, Expandable roadmap, Interactive Goal Setting)
  - [x] Fix: Session Persistence (Increased JWT expiry to 7 days)

### Phase 5.5: UI/UX 2.0 Overhaul (The "Professional" Look)
- [x] **Backend: Data for Dashboard**
  - [x] API: `GET /api/analytics/stats` (Streak, Roadmap Progress, Resume Score History)
- [x] **Android: Core Navigation**
  - [x] Component: `BottomNavigationBar` (Home, Roadmap, Profile)
  - [x] Screen: `MainScreen` (Scaffold for tabs)
- [x] **Android: Screen Redesign - Premium Edition**
  - [x] `HomeScreen`: Gradient Hero Card + Quick Actions + Progress Stats
  - [x] `ProfileScreen`: Enhanced with modern gradient header + Stat badges
  - [x] `RoadmapScreen`: Visual Timeline improvements
  - [x] **UI 3.0: Professional Polish** (NEW)
    - [x] Replace all emojis with Vector Icons
    - [x] Redesign AI Analysis button (Clean/Professional)
    - [x] Redesign Roadmap generation button
    - [x] **Stable Connectivity:** Added `START_BACKEND_STABLE.bat` (Unified Startup)
    - [x] **Backend Resiliency:** Added SQLite Fallback to prevent hangs (Network-Proof)
  - [x] Backend: Add Professional Fields (Bio, LinkedIn)
  - [x] Android: Edit Profile Dialog

### Phase 6: Career Intelligence Infrastructure (The "Co-Founder" Layer)
- [ ] **Data Foundation (Module 8 & 1)**
  - [ ] Schema: Create `UserEvent` table (Behavioral Signals)
  - [ ] Service: Implement `AnalyticsService` (Event Logger)
  - [ ] API: Add event tracking to `roadmap` and `counselor` endpoints
- [ ] **Intelligence Systems**
  - [ ] Design: Career Readiness Score Algorithm (Module 4)
  - [ ] Design: Weekly Check-In Logic (Module 3)
  - [ ] Schema: Add `market_demand_weight` to Roadmap Steps (Module 5)
- [ ] **Monetization & State**
  - [ ] Schema: Add `SubscriptionTier` and `UsageLimits` (Module 7)

### Phase 7: Dynamic Intelligence & Strict Validation 🛡️
- [x] Backend: Strict Education Validation
  - [x] Define `EducationLevel` Enum
  - [x] Update `ProfileCreate/Update` schemas
  - [x] Handle validation errors gracefully
- [x] Backend: Field-Agnostic AI Logic
  - [x] Refactor `analysis_service.py` prompt (Remove tech-bias)
  - [x] Update `roadmap_service.py` prompt (Dynamic field handling)
  - [x] Implement lack-of-skill suggestions for non-tech fields
  - [x] Update AI fallbacks to be generic
- [x] Android: Professional Education Dropdown
  - [x] Implement `ExposedDropdownMenuBox` in `ProfileCreationScreen`
  - [x] Add Education Dropdown to `EditProfileDialog`
  - [x] Update `Constants` with International Education Levels
- [x] Verification: Test with non-tech personas (Chef, Designer, etc.)

### Phase 8: Mobile UX - Global Scrolling Fixes 📜
- [x] Android: Restore full touch-scroll functionality
  - [x] Add `verticalScroll` to `LoginScreen`
  - [x] Add `verticalScroll` to `SignupScreen`
  - [x] Add `verticalScroll` to `CareerCounselorScreen` (Question & Result)
  - [x] Add `verticalScroll` to `RoadmapScreen` empty state
  - [x] Audit `HomeScreen` for nested scroll conflicts
- [x] Verification: Test scrolling on small screen simulations

### Phase 9: Robust Error Handling 🛡️
- [ ] Android: Parse detailed error messages from backend
  - [ ] Implement JSON error parsing in `AuthRepository`
  - [ ] Update `signup` and `login` flows to show real error details
- [ ] Verification: Test with expected errors (e.g. duplicate email)

### Phase 10: Bug Fix - Dashboard Loading Error 🛠️
- [x] Backend: Make `EducationLevel` resilient in `ProfileBase` schema
- [x] Backend: Restore missing `BaseModel` import (Resolved 500 error)
- [x] Backend: Make `ProfileResponse` resilient to NULL timestamps and missing fields
- [x] Android: Show dynamic error messages in `HomeScreen`
- [x] Verification: Dashboard loads correctly with legacy data

### Phase 11: Refine AI Analysis & Interactivity 🤖
- [x] Android: Auto-Skip logic in `CareerCounselorScreen` (Skips questions if Target Role exists)
- [x] Android: UI Polish for Quick Action Buttons (Better Spacing & Colors)
- [x] Android: Verify Resume Upload Button functionality

### Phase 12: Functional Verification ✅
- [x] Verify "AI Analysis" flow (Smart Skip vs. Question Mode)
- [x] Verify "Resume" button (Opens Upload)
- [x] Verify "Roadmap" button (Switches Tabs)
- [x] **Global Button Audit:** Verified & Fixed "View All", "Daily Goal", and Recommendation Cards. All are now clickable.

### Phase 13: Real-Time Chat Implementation 💬
- [x] Backend: `/ai/chat` endpoint and `ChatRequest` DTO
- [x] Backend: `chat_with_mentor` service logic (Gemini)
- [x] Android: `ChatScreen` UI (Message List, Input, Send)
- [x] Android: `AiApi` & `AiRepository` chat methods
- [x] Android: Connect "Counselor" button to Chat Screen
- [x] Android: Connect "Counselor" button to Chat Screen

### Phase 14: User Requested Enhancements (Gap Analysis) 🎯
#### Onboarding & Profile
- [ ] **Onboarding Slides:** Intro screens explaining features (Skip/Next).
- [ ] **Profile Picture:** Real image upload (replace initials placeholder).

#### Dashboard & Interaction
- [ ] **Notifications:** Local notifications for Daily Goals / Reminders.
- [ ] **Search/Filter:** Search mentors/courses (Mock/Real implementation).

#### Chat Polish
- [ ] **Typing Indicators:** Visual feedback while AI is generating.
- [ ] **Persistent History:** Save chat sessions to local Database (Room).
