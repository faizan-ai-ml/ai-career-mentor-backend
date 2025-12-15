from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.profile import StudentProfile
from app.dependencies import get_current_user
from app.services.ai_service import analyze_resume, improve_resume_text, generate_learning_roadmap
from app.services.analytics_service import track_event
from pydantic import BaseModel

router = APIRouter(prefix="/ai", tags=["AI Features"])

class ImproveTextRequest(BaseModel):
    text: str

class ImproveTextResponse(BaseModel):
    original: str
    improved: str

class RoadmapResponse(BaseModel):
    roadmap: dict

class CounselorRequest(BaseModel):
    answers: dict

@router.post("/career-counselor")
def career_counselor(
    request: CounselorRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Analyze user's answers to the simulation questions and suggest a career.
    """
    from app.services.ai_service import get_career_counseling # Lazy import to avoid circular dep if any
    
    return get_career_counseling(request.answers)

@router.post("/analyze-resume")
def analyze_my_resume(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Analyzes the user's uploaded resume text.
    User must have uploaded a resume first.
    """
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    
    if not profile or not profile.has_resume or not profile.parsed_resume_content:
        raise HTTPException(status_code=400, detail="No resume found to analyze. Please upload one first.")
    
    # helper logic to perform analysis
    try:
        analysis_result = analyze_resume(profile.parsed_resume_content)
        
        # [CIG] Track Event: Resume Analyzed
        track_event(db, current_user.id, "resume_analyzed", {
            "score": analysis_result.get("score"),
            "missing_skills_count": len(analysis_result.get("missing_skills", []))
        })
        
        return {
            "success": True,
            "data": analysis_result,
            "error": None
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/improve-text", response_model=ImproveTextResponse)
def improve_content(
    request: ImproveTextRequest,
    current_user: User = Depends(get_current_user)
):
    """
    Rewrite a bullet point or professional summary using AI.
    Example Input: "i worked at store"
    Example Output: "Managed daily store operations and facilitated customer transactions..."
    """
    if not request.text or len(request.text) < 3:
        raise HTTPException(status_code=400, detail="Text too short to improve")
        
    improved = improve_resume_text(request.text)
    return {
        "original": request.text,
        "improved": improved
    }

class RoadmapRequest(BaseModel):
    duration: int = 8
    custom_goal: str = None  # User can override/specify goal

@router.post("/roadmap", response_model=RoadmapResponse)
def get_career_roadmap(
    request: RoadmapRequest = Body(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Generate a personalized learning roadmap.
    Uses 'custom_goal' if provided, otherwise falls back to profile goal.
    """
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
        
    # Construct profile dict for AI
    profile_data = {
        "education": profile.education_level,
        "major": profile.field_of_study,
        "interests": profile.interests,
        "goals": request.custom_goal if request.custom_goal else profile.career_goals,
        "has_resume": profile.has_resume,
        "resume_content": profile.parsed_resume_content if profile.has_resume else None
    }
    
    # Explicitly set the target career goal in the data so service knows what to focus on
    if request.custom_goal:
        profile_data['careerGoals'] = request.custom_goal

    roadmap = generate_learning_roadmap(profile_data, request.duration)
    return {"roadmap": roadmap}
