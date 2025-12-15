"""
AI Career Mentor - FastAPI Main Application
"""
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from sqlalchemy.orm import Session

# Import routers
from app.api.auth import router as auth_router
from app.api.profile import router as profile_router
from app.api.ai_features import router as ai_router

# Import existing services
from app.services.ai_service import analyze_resume
from app.config import get_config_status

# Import database
from app.database import engine, Base, get_db
from app.dependencies import get_current_user
from app.models.user import User
from app.models.analytics import UserEvent

# Create database tables
Base.metadata.create_all(bind=engine)

# Initialize FastAPI
app = FastAPI(
    title="AI Career Mentor API",
    description="AI-powered career guidance with resume analysis and personalized roadmaps",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS Configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(auth_router)
app.include_router(profile_router)
app.include_router(ai_router)


# ===== AI Analysis Models (from original code) =====

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


# ===== Root Endpoints =====

@app.get("/")
async def root():
    """
    API root endpoint - Welcome message
    """
    return {
        "message": "AI Career Mentor API",
        "status": "running",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "authentication": "/auth",
            "health": "/health",
            "analyze_resume": "/analyze-resume"
        }
    }


@app.get("/health")
async def health_check():
    """
    Health check endpoint - Check API and AI services status
    """
    config = get_config_status()
    return {
        "status": "healthy",
        "database": "connected",
        "ai_services": config
    }


# ===== AI Analysis Endpoints (from original code, now protected) =====

@app.post("/analyze-resume", response_model=AnalysisResponse)
async def analyze(
    request: ResumeRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Analyze resume and generate career recommendations
    
    **Requires authentication** - Include JWT token in Authorization header
    
    - Extracts skills from resume
    - Determines experience level
    - Suggests matching careers
    - Generates learning roadmap
    """
    try:
        if not request.resume_text or len(request.resume_text.strip()) < 50:
            raise HTTPException(
                status_code=400,
                detail="Resume too short. Minimum 50 characters."
            )
        
        # Call AI service to analyze resume
        result = analyze_resume(request.resume_text)
        
        return AnalysisResponse(success=True, data=result)
        
    except HTTPException:
        raise
    except Exception as e:
        print(f"Error analyzing resume: {str(e)}")
        raise HTTPException(status_code=500, detail=str(e))


# ===== Development Server =====

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
