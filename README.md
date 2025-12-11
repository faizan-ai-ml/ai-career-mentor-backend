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

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get OpenRouter API Key (FREE)
1. Go to https://openrouter.ai/
2. Sign up for free account
3. Go to "Keys" section
4. Create an API key
5. Copy the key

### 3. Create `.env` file
```bash
OPENROUTER_API_KEY=sk-or-v1-your_key_here
OPENROUTER_MODEL=deepseek/deepseek-chat
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
```

### 4. Run the server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 5. Test the API
Open browser: http://localhost:8000/docs

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
