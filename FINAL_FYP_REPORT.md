# FINAL YEAR PROJECT REPORT
# Project Title: AI Career Mentor

---

## Table of Contents

**Chapter 1: Introduction**
- 1.1 Background
- 1.2 Problem Statement
- 1.3 Objectives
- 1.4 Scope

**Chapter 2: Existing System & Proposed System**
- 2.1 Existing System
- 2.2 Limitations of Existing System
- 2.3 Proposed System
- 2.4 Advantages of Proposed System

**Chapter 3: System Analysis**
- 3.1 Functional Requirements
- 3.2 Non-Functional Requirements
- 3.3 Use Case Diagram
- 3.4 Use Case Description

**Chapter 4: System Design**
- 4.1 System Architecture
- 4.2 Database Design (ERD)
- 4.3 API Design
- 4.4 User Interface Design

**Chapter 5: Implementation**
- 5.1 Tools & Technologies
- 5.2 Backend Implementation
- 5.3 Frontend Implementation
- 5.4 AI Integration Module

**Chapter 6: Testing**
- 6.1 Testing Strategy
- 6.2 Test Cases
- 6.3 Result Summary

**Chapter 7: Conclusion & Future Enhancements**
- 7.1 Conclusion
- 7.2 Future Enhancements

**References**

---

## Chapter 1: Introduction

### 1.1 Background
Career counseling is a fundamental requirement for university students seeking to enter the professional job market. Traditionally, this process is manual, involving human mentors and career centers. However, with the rapid growth of the global tech industry, the volume of students requires a more scalable and automated approach. Advanced Artificial Intelligence (AI) now allows for the semantic analysis of documents, making it possible to automate career guidance.

### 1.2 Problem Statement
Students often lack clarity regarding their professional readiness. They face difficulties in receiving objective feedback on their resumes and struggle to identify the specific technical skill gaps that prevent them from securing desired roles. Without a structured learning path, students often waste time on irrelevant resources.

### 1.3 Objectives
*   To design a mobile platform for automated career mentorship.
*   To implement an AI-based resume parser for technical skill extraction.
*   To develop an algorithm that generates personalized, time-bound learning roadmaps.
*   To provide continuous career support through an AI-powered chat interface.

### 1.4 Scope
The scope of this project includes the development of a native Android mobile application and a Python-based RESTful API. It covers user authentication, PDF resume parsing, AI-driven analysis, and roadmap generation. The system is designed for individual students and entry-level professionals.

---

## Chapter 2: Existing System & Proposed System

### 2.1 Existing System
The existing career guidance infrastructure consists of manual counseling sessions and static career portals. Students submit their resumes to university career offices or upload them to job boards that use simple keyword matching to recommend roles.

### 2.2 Limitations of Existing System
*   **Manual Effort**: Human counseling is time-consuming and expensive.
*   **Lack of Personalization**: Static portals provide the same advice to all users.
*   **No Actionable Path**: Existing systems tell you what you lack but do not provide a roadmap to fix it.
*   **Availability**: Career centers are not available 24/7.

### 2.3 Proposed System
The proposed "AI Career Mentor" is an automated solution that provides data-driven career guidance. The system takes a student's resume as input, uses Large Language Models (LLMs) to analyze it, and outputs a personalized learning plan. It acts as an always-available digital counselor.

### 2.4 Advantages of Proposed System
*   **Immediate Feedback**: Users receive resume analysis within seconds.
*   **Tailored Roadmaps**: Each learning path is unique to the user's specific skill gaps.
*   **Cost-Effective**: High-quality mentorship is provided at no cost to the user.
*   **Accessibility**: Available 24/7 through a mobile interface.

---

## Chapter 3: System Analysis

### 3.1 Functional Requirements
*   **User Registration**: Users can create accounts and manage profiles.
*   **PDF Processing**: The system can read and extract text from PDF resumes.
*   **AI Analysis**: The backend performs semantic analysis to identify skills and gaps.
*   **Roadmap View**: The app displays a weekly schedule of learning topics.
*   **Chat Mentor**: An interactive AI chat for career-related queries.

### 3.2 Non-Functional Requirements
*   **Security**: Use of JWT for token-based authentication.
*   **Reliability**: The system provides consistent analysis for similar resumes.
*   **Performance**: The API responds to analysis requests within 15-30 seconds.
*   **Scalability**: The backend can handle multiple concurrent users.

### 3.3 Use Case Diagram
*(Teacher's Note: In MS Word, insert a diagram showing a 'Student' actor connected to Login, Upload Resume, View Roadmap, and Chat with Mentor.)*

### 3.4 Use Case Description
| Use Case Name | Actor | Description |
| :--- | :--- | :--- |
| **Login** | Student | User authenticates using email and password. |
| **Upload Resume** | Student | User selects a PDF file to begin analysis. |
| **Generate Roadmap**| System | Backend processes skills and creates a learning plan. |
| **Chat with Mentor** | Student | User asks career questions to the AI mentor. |

---

## Chapter 4: System Design

### 4.1 System Architecture
The project follows a **Client-Server Architecture**. The Android app serves as the frontend, communicating with the FastAPI backend via RESTful APIs. External AI models (DeepSeek/Gemini) are integrated into the backend as a service.

### 4.2 Database Design (ERD)
The database schema consists of two primary tables:
1.  **Users**: Stores `email`, `password_hash`, and `id`.
2.  **StudentProfiles**: Stores `user_id`, `skills_list`, `roadmap_json`, and `education_info`.
*(Teacher's Note: Insert ER Diagram here showing 1-to-1 relationship between Users and Profiles.)*

### 4.3 API Design
Critical endpoints include:
*   `POST /auth/signup`: User registration.
*   `POST /auth/login`: Authentication and token generation.
*   `POST /analyze-resume`: Resume upload and analysis trigger.
*   `GET /profile`: Retrieval of generated roadmap and profile data.

### 4.4 User Interface Design
The UI is designed using standard **XML Layouts**. Navigation is handled via a bottom navigation bar, providing quick access to the Dashboard, Roadmap, and AI Chat features.

---

## Chapter 5: Implementation

### 5.1 Tools & Technologies
*   **Language**: Kotlin (Android), Python (Backend).
*   **IDE**: Android Studio, VS Code.
*   **Framework**: FastAPI, Jetpack (View Binding).
*   **Database**: PostgreSQL.
*   **AI**: OpenRouter (DeepSeek V3), Google Gemini.

### 5.2 Backend Implementation
The backend is optimized for asynchronous processing. It uses **SQLAlchemy** for database operations and **Pydantic** for data validation. The `pypdf` library handles the extraction of text from PDF binaries.

### 5.3 Frontend Implementation
The Android app is built using the **MVVM** pattern. **Hilt** is used for dependency injection, while **Retrofit** is used for API communication. UI screens are defined in XML to ensure high performance and broad device support.

### 5.4 AI Integration Module
A dedicated orchestration service manages calls to AI providers. It uses prompt engineering to ensure the AI returns a valid JSON structure containing the categorized skills and the week-by-week learning milestones.

---

## Chapter 6: Testing

### 6.1 Testing Strategy
Manual testing was performed to verify system integration. Each module (Auth, Upload, Chat) was tested individually before end-to-end integration testing.

### 6.2 Test Cases
| Test ID | Scenario | Input | Expected Result | Status |
| :--- | :--- | :--- | :--- | :--- |
| TC-01 | User Login | Valid credentials | Success & JWT token | Passed |
| TC-02 | File Upload | Non-PDF file | Error: Invalid format | Passed |
| TC-03 | Skill Extract | Standard resume | List of technical skills | Passed |
| TC-04 | Chatbot | Career query | Relevant advice | Passed |

### 6.3 Result Summary
All critical functional requirements were successfully verified. The system handles standard PDF formats and correctly generates roadmaps within the specified performance window.

---

## Chapter 7: Conclusion & Future Enhancements

### 7.1 Conclusion
The **AI Career Mentor** successfully demonstrates the integration of modern AI with mobile technology to solve career counseling gaps. By replacing manual processes with automated analysis, the system provides students with an immediate and actionable career growth path.

### 7.2 Future Enhancements
*   Implementation of voice-based mock interviews.
*   Direct linkage to job boards for internship applications.
*   Enhanced profile customization with professional portfolio hosting.

---

## References
1. FastAPI Documentation: https://fastapi.tiangolo.com/
2. Android Developers - XML Layouts: https://developer.android.com/guide/topics/ui/declaring-layout
3. Google Gemini API Reference: https://ai.google.dev/
4. Kotlin Language Documentation: https://kotlinlang.org/docs/home.html
