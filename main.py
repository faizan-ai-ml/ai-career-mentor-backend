from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional

from services.ai_service import analyze_resume
from config import get_config_status

# Initialize FastAPI
app = FastAPI(
    title="AI Career Mentor API",
    description="AI-powered career guidance with OpenRouter + Gemini backup",
    version="1.0.0"
)

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Models
class ResumeRequest(BaseModel):
    resume_text: str

class Career(BaseModel):
    title: str
    match_percent: int

class AnalysisData(BaseModel):
    skills: List[str]
    experience_level: str
    top_careers: List[Career]
    roadmap: str

class AnalysisResponse(BaseModel):
    success: bool
    data: Optional[AnalysisData] = None
    error: Optional[str] = None

# Endpoints
@app.get("/")
async def root():
    return {
        "message": "AI Career Mentor API",
        "status": "running",
        "version": "1.0.0",
        "docs":  "/docs"
    }

@app.get("/health")
async def health():
    config = get_config_status()
    return {
        "status":  "healthy",
        "ai_services": config
    }

@app.post("/analyze-resume", response_model=AnalysisResponse)
async def analyze(request: ResumeRequest):
    try:
        if not request.resume_text or len(request.resume_text. strip()) < 50:
            raise HTTPException(
                status_code=400,
                detail="Resume too short.  Minimum 50 characters."
            )
        
        result = analyze_resume(request.resume_text)
        
        return AnalysisResponse(success=True, data=result)
        
    except HTTPException: 
        raise
    except Exception as e:
        print(f"Error:  {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__": 
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)