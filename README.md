# AI Career Mentor - Backend API

AI-powered career guidance API that analyzes resumes and generates personalized learning roadmaps.

## Features
- Resume text analysis using Llama 3.1 70B
- Skill extraction and classification
- Career path recommendations
- Personalized 8-week learning roadmaps

## Tech Stack
- FastAPI (Python web framework)
- Groq API (Free LLM)
- Uvicorn (ASGI server)

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get Groq API Key
1. Go to https://console.groq.com/
2. Sign up for free account
3. Create an API key
4. Copy the key

### 3. Create `.env` file
```bash
GROQ_API_KEY=your_key_here
```

### 4. Run the server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Test the API
Open browser:  http://localhost:8000/docs

## API Endpoints

### `POST /analyze-resume`
Analyzes resume text and returns career guidance.

**Request:**
```json
{
  "resume_text": "John Doe\nSoftware Developer\n\nSkills: Python, React..."
}
```

**Response:**
```json
{
  "success": true,
  "data": {
    "skills": ["Python", "React", "SQL"],
    "experience_level": "Intermediate",
    "top_careers": [
      {"title": "Full Stack Developer", "match_percent": 85}
    ],
    "roadmap": "Week 1: .. .\nWeek 2: ..."
  }
}
```

## For Production

### Deploy to Railway: 
1. Go to https://railway.app/
2. Connect GitHub repo
3. Add `GROQ_API_KEY` to environment variables
4. Deploy! 

## License
MIT
