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

# AI Career Mentor - Backend API

AI-powered career guidance with dual AI provider support (OpenRouter + Gemini backup).

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Get API Keys

**OpenRouter (Primary):**
- Go to https://openrouter.ai/
- Sign up and create API key

**Gemini (Backup):**
- Go to https://makersuite.google.com/app/apikey
- Create free API key

### 3. Configure `.env`
```bash
cp .env.example .env
# Edit .env and add your keys
```

### 4. Test configuration
```bash
python test_env.py
```

### 5. Run server
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### 6. Test API
http://localhost:8000/docs

## API Endpoints

- `GET /` - API info
- `GET /health` - Check AI services status
- `POST /analyze-resume` - Analyze resume

## License
MIT
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
