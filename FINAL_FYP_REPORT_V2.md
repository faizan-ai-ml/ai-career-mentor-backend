## Chapter 1: Introduction

### 1.1 Background
The transition from academic life to professional careers, or switching between different industries, is a critical phase for individuals regardless of their professional domain. In the contemporary global job market, the requirements for various roles are constantly evolving, creating a significant gap between traditional education and dynamic industry expectations in fields ranging from Technology and Business to Healthcare and the Arts. Career counseling serves as the bridge for this gap, but manual mentorship is often localized and hard to scale for the general public.

Artificial Intelligence (AI), particularly Large Language Models (LLMs), has matured to a point where it can perform complex semantic analysis of text across any discipline. This project explores the application of AI in the field of universal career mentorship by developing an automated system that can analyze resumes, identify cross-disciplinary skill deficiencies, and generate actionable learning roadmaps for any career path.

### 1.2 Problem Statement
Job seekers and professionals across all sectors face three primary challenges:
1.  **Objective Feedback**: Individuals lack access to consistent, objective feedback on their resumes to understand how they are perceived by recruiters in different industries.
2.  **Skill Gap Identification**: It is difficult for professionals to identify the specific technical or soft skills they are missing when aiming for a promotion or a career pivot.
3.  **Lack of Actionable Path**: Even when the goal is clear, finding a structured, time-bound learning path that includes high-quality resources for diverse niches is a significant hurdle.

### 1.3 Objectives
The core objectives of this project are:
*   To design and develop a universal native Android application for career mentorship available to users of all backgrounds.
*   To implement a robust Python FastAPI backend capable of handling multi-disciplinary career data.
*   To integrate advanced AI models for semantic parsing of both technical and non-technical resumes.
*   To automate the creation of week-by-week learning roadmaps uniquely tailored to any career goal, whether in the Tech sector or beyond.

### 1.4 Scope
This project encompasses a full-stack mobile solution designed for a general audience. The system includes:
*   **User Management Module**: Secure registration, login, and JWT-based authentication.
*   **Resume Parsing Service**: Domain-agnostic extraction of structured data from PDF files.
*   **AI Orchestration Layer**: A backend service that translates any professional background into a structured roadmap.
*   **Roadmap Module**: A dynamic UI that renders personalized learning paths for any industry.

The project is designed to be fully inclusive, supporting careers in Engineering, Management, Healthcare, Creative Arts, and vocational trades.

---

## Chapter 2: Existing System & Proposed System

### 2.1 Existing System
The current career guidance ecosystem primarily relies on two methods:
1.  **University Career Centers**: Students meet with human advisors who manually review resumes and give verbal advice.
2.  **Online Job Portals**: Websites like LinkedIn, Indeed, or local job boards allow users to upload resumes. These systems often use simple keyword matching to suggest jobs but rarely provide guidance on how to improve.

### 2.2 Limitations of Existing System
*   **Scalability Issues**: Human mentors cannot cater to thousands of students simultaneously, leading to long wait times.
*   **Subjectivity**: Different human advisors may give conflicting advice based on personal bias.
*   **Limited Availability**: University offices operate only during business hours, whereas students often work on their career preparation late at night.
*   **Generic Outputs**: Online portals suggest jobs based on what is *in* the resume, not what is *missing* for the user's dream job. They do not provide a "how-to" guide for learning.

### 2.3 Proposed System
The proposed "AI Career Mentor" is an end-to-end automated system that replaces manual review with professional AI analysis. The student uploads a PDF resume and specifies a target career goal. The system then performs a semantic gap analysis and constructs a complete learning program.

### 2.4 Advantages of Proposed System
*   **Precision**: AI identifies skills that keyword-checkers miss, such as project accomplishments and technical proficiency levels.
*   **Customization**: No two roadmaps are identical; the plan is built specifically based on what the user does *not* know.
*   **Accessibility**: The system is hosted on the cloud and accessible via a mobile app 24/7.
*   **Integration**: Combines analysis, planning, and resource recommendation in a single platform.

---

## Chapter 3: System Analysis

### 3.1 Functional Requirements
The system must satisfy the following functional requirements:
*   **FR-1: User Authentication**: The system shall allow users to register using an email and password and verify identity via JWT.
*   **FR-2: Resume PDF Upload**: Users shall be able to upload PDF files from their device storage.
*   **FR-3: Semantic Extraction**: The backend shall extract skills, education, and experience from the uploaded PDF.
*   **FR-4: Roadmap Generation**: The system shall generate a week-by-week learning path in a structured JSON format.
*   **FR-5: Interactive Chat**: The app shall provide a chat interface for users to ask career-related questions to the AI.
*   **FR-6: Progress Tracking**: The system shall save the generated roadmap for the user to view at any time.

### 3.2 Non-Functional Requirements
*   **NFR-1: Performance**: Resume analysis and roadmap generation shall complete within 20-30 seconds.
*   **NFR-2: Security**: All passwords shall be hashed using Bcrypt before storage.
*   **NFR-3: Usability**: The mobile interface shall follow Material Design guidelines for ease of use.
*   **NFR-4: Availability**: The API should have an uptime of 99.9% when deployed on cloud infrastructure.

### 3.3 Use Case Diagram
The Use Case Diagram for the AI Career Mentor involves one primary actor: the **Student User**.
*(Teacher's Note: For your MS Word report, draw a diagram with a Student actor connected to the following Use Cases: Register, Login, Upload Resume, View Skill Gaps, Access Learning Roadmap, and Chat with Mentor.)*

### 3.4 Use Case Descriptions

**Use Case: Upload Resume & Generate Analysis**
| Item | Description |
| :--- | :--- |
| **Actor** | Student User |
| **Pre-condition** | User is logged into the application. |
| **Main Flow** | 1. User selects 'Upload' from the dashboard.<br>2. User chooses a PDF file.<br>3. System extracts text and sends to backend.<br>4. Backend calls AI for gap analysis.<br>5. System displays results. |
| **Post-condition**| Roadmap is saved to the user's profile. |

**Use Case: Chat with AI Mentor**
| Item | Description |
| :--- | :--- |
| **Actor** | Student User |
| **Pre-condition** | Profile analysis has been completed. |
| **Main Flow** | 1. User opens 'Chat' screen.<br>2. User enters a query (e.g., 'How do I start with React?').<br>3. System provides a response based on user context. |
| **Post-condition**| Conversation history is updated. |

---

## Chapter 4: System Design

### 4.1 System Architecture
The system utilizes a modern **Client-Server Architecture**. 
*   **Frontend**: A native Android application built with **Kotlin**. It handles the presentation layer using the **MVVM** pattern to ensure a clean separation between UI (XML) and business logic.
*   **Backend**: A **FastAPI** server that acts as the core engine. It manages the database, authentication, and the orchestration of AI services.
*   **AI Layer**: External APIs (OpenRouter and Gemini) are consumed by the backend to perform the intelligence-heavy tasks.

### 4.2 Database Design (ERD)
The database is structured to minimize redundancy while providing quick access to user data.
*   **Users Table**: Stores `id` (PK), `email` (Unique), `password_hash`, and `created_at`.
*   **StudentProfiles Table**: Linked to the Users table via `user_id` (FK). It stores `skills`, `education`, `resume_path`, and the serialized `roadmap_data` in JSON format.
*(Teacher's Note: Insert ER Diagram here showing a 1-to-1 relationship between the Users and StudentProfiles tables.)*

### 4.3 API Design
The backend is built as a RESTful API. Key endpoints include:
*   `POST /auth/signup`: Validates data and creates a new user record.
*   `POST /auth/login`: Verifies credentials and returns a JWT Bearer token.
*   `POST /analyze-resume`: Accepts a multipart form-data (PDF) and returns the JSON analysis.
*   `GET /profile/me`: Retrieves the current user's profile and saved roadmaps.

### 4.4 User Interface Design
The UI is designed for high accessibility. 
*   **XML Layouts**: Used to define a responsive interface that works on various screen sizes.
*   **Navigation**: Implemented using a Bottom Navigation View for quick switching between Dashboard, Roadmap, and Chat.
*   **Style**: Uses a professional dark-themed aesthetic with blue primary accents to signify trust and mentorship.

---

## Chapter 5: Implementation

### 5.1 Tools & Technologies
The development environment consisted of:
*   **Android Studio**: For mobile app development using Kotlin.
*   **VS Code**: For backend development using Python.
*   **PostgreSQL**: For relational data storage.
*   **Git/GitHub**: For version control.
*   **Localtunnel / Koyeb**: For making the local API accessible to the mobile device.

### 5.2 Backend Implementation
The backend is implemented using **FastAPI**.
*   **Dependency Injection**: Used for sharing database sessions across different routes.
*   **Authentication**: Implemented using `OAuth2PasswordBearer`. The backend generates a JWT token upon successful login which is then required for all protected routes.
*   **PDF Extraction**: The `pypdf` library extracts raw text from user-uploaded PDF files, which is then cleaned of special characters before being sent to the AI.

### 5.3 Mobile App Implementation
The Android app is built using **Kotlin**.
*   **MVVM Pattern**: ViewModels handle the logic and data fetching, while Fragments render the UI from XML files.
*   **Networking**: **Retrofit** is used to handle HTTP requests. A custom `AuthInterceptor` is implemented to automatically attach the JWT token to every request.
*   **View Binding**: Enabled to allow for safe and direct access to UI views without using `findViewById`.

### 5.4 AI Career Recommendation Module
This is the "Brain" of the system.
1.  **Prompt Engineering**: The backend constructs a detailed prompt containing the user's extracted resume text and their career goal.
2.  **JSON Constraints**: The AI is instructed to return data in a strict JSON format so the mobile app can parse it into a list of "Weeks" and "Topics".
3.  **Fallback Logic**: The system is designed to use **OpenRouter (DeepSeek V3)** as the primary model and **Google Gemini 1.5** as a fallback in case of API rate limits or downtime.

---

## Chapter 6: Testing

### 6.1 Testing Strategy
A multi-tier testing strategy was employed:
*   **Unit Testing**: Individual backend functions (like password hashing and PDF text extraction) were tested for correctness.
*   **Integration Testing**: Verified the communication between the Android app and the FastAPI server.
*   **System Testing**: Conducted end-to-end tests from account creation to roadmap generation on a physical Android device.

### 6.2 Test Cases

**Table 6.1: Authentication Test Cases**
| ID | Test Scenario | Input | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | Create New User | Valid email/password | Account created; redirected to Dashboard | Passed |
| TC-02 | Login with Invalid Email | Wrong email | Error: "Invalid credentials" | Passed |
| TC-03 | JWT Token Expiry | Expired token | System prompts for re-login | Passed |

**Table 6.2: Core Feature Test Cases**
| ID | Test Scenario | Input | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-04 | PDF Resume Upload | Valid 1MB PDF | Analysis starts; loading bar appears | Passed |
| TC-05 | Roadmap Calculation | Resume text | A list of 8 unique weeks is generated | Passed |
| TC-06 | AI Chat Response | "How to learn SQL?" | AI provides links/tips in Chat screen | Passed |

### 6.3 Result Summary
The system successfully met all functional objectives. During testing, it was confirmed that the AI could distinguish between different career goals (e.g., a student with the same resume received different roadmaps when changing their goal from "Data Scientist" to "Web Developer").

---

## Chapter 7: Conclusion & Future Enhancements

### 7.1 Conclusion
The **AI Career Mentor** project successfully demonstrates that a combination of mobile technology and Generative AI can provide highly effective career guidance. By moving away from static repositories and human-dependent systems, we have created a platform that empowers students to take control of their professional growth. The use of **XML layouts** and **FastAPI** ensures that the system is both performant and maintainable for future developers.

### 7.2 Future Enhancements
In future versions, the project can be expanded with the following features:
*   **Mock Interview Module**: Using Text-to-Speech (TTS) to conduct technical interviews based on the generated roadmap.
*   **LinkedIn Integration**: Fetching real-time job openings that match the user’s newly acquired skills.
*   **Gamification**: Adding badges and certificates as users complete their weekly roadmap milestones.

---

## References
1. FastAPI Official Documentation - [fastapi.tiangolo.com](https://fastapi.tiangolo.com/)
2. Android Developers Guide (XML Layouts) - [developer.android.com](https://developer.android.com/)
3. SQLAlchemy 2.0 Docs - [sqlalchemy.org](https://www.sqlalchemy.org/)
4. OpenRouter API Documentation - [openrouter.ai](https://openrouter.ai/docs)
5. Kotlin Coroutines Guide - [kotlinlang.org](https://kotlinlang.org/docs/coroutines-overview.html)
