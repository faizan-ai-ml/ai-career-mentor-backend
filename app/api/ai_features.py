from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from fastapi import APIRouter, Depends, HTTPException, Body, status
from app.database import get_db
from app.models.user import User
from app.models.profile import StudentProfile
from app.dependencies import get_current_user
from app.services.ai_service import analyze_resume, improve_resume_text, generate_learning_roadmap
from app.services.analytics_service import track_event
from pydantic import BaseModel
import json

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
    try:
        profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
        
        if not profile or not profile.has_resume or not profile.parsed_resume_content:
            raise HTTPException(status_code=400, detail="No resume found to analyze. Please upload one first.")
        
        # helper logic to perform analysis
        analysis_result = analyze_resume(profile.parsed_resume_content)
        
        profile.skill_analysis = json.dumps(analysis_result)
        db.commit()
        
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
    except OperationalError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database temporarily unavailable. Please retry."
        )
    except Exception as e:
        db.rollback()
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
    try:
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
        
        # SAVE to DB (Initialize status)
        for week in roadmap.get("weeks", []):
            week["status"] = "LOCKED" if week["week"] > 1 else "CURRENT"
            week["completed_tasks"] = []
            
        # Serialize to JSON string
        profile.roadmap_data = json.dumps(roadmap)
        db.commit()
        
        return {"roadmap": roadmap}
    except OperationalError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database temporarily unavailable. Please retry."
        )

@router.get("/roadmap", response_model=RoadmapResponse)
def get_existing_roadmap(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Get the currently active roadmap from the database.
    """
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    if not profile or not profile.roadmap_data:
        raise HTTPException(status_code=404, detail="No roadmap found. Please generate one.")
        
    try:
        # Deserialize from JSON string
        roadmap = json.loads(profile.roadmap_data)
        return {"roadmap": roadmap}
    except json.JSONDecodeError:
        raise HTTPException(status_code=500, detail="Corrupt roadmap data")

class ProgressUpdate(BaseModel):
    week: int
    task_index: int
    completed: bool

@router.post("/roadmap/progress")
def update_roadmap_progress(
    update: ProgressUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Update the completion status of a specific task in the roadmap.
    """
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    if not profile or not profile.roadmap_data:
        raise HTTPException(status_code=404, detail="No roadmap found.")
        
    try:
        roadmap = json.loads(profile.roadmap_data)
        weeks = roadmap.get("weeks", [])
        
        # Find the week
        target_week = next((w for w in weeks if w["week"] == update.week), None)
        if not target_week:
            raise HTTPException(status_code=404, detail="Week not found")
            
        # Update task status
        # We store completed tasks indices in a list "completed_tasks"
        completed_tasks = set(target_week.get("completed_tasks", []))
        
        if update.completed:
            completed_tasks.add(update.task_index)
        else:
            completed_tasks.discard(update.task_index)
            
        target_week["completed_tasks"] = list(completed_tasks)
        
        # Logic to auto-unlock next week?
        # If all tasks in current week are done -> Unlock next?
        # For now, keep it simple.
        
        # Serialize back to string
        profile.roadmap_data = json.dumps(roadmap)
        db.commit()
        
        return {"success": True, "roadmap": roadmap}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

class ChatRequest(BaseModel):
    message: str
    history: list = [] # List of {"role": "user"|"model", "content": "..."}

@router.post("/chat")
def chat_endpoint(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Real-time chat with the AI Career Mentor.
    """
    from app.services.ai_service import chat_with_mentor
    
    # Optional: Fetch profile to give AI context about user
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    user_context = {}
    if profile:
        user_context = {
            "name": profile.full_name or current_user.email.split('@')[0],
            "role": profile.target_role or "Aspiring Professional",
            "education": profile.education_level or "Unknown",
            "skills": profile.parsed_resume_content if profile.has_resume else "Unknown"
        }

    response = chat_with_mentor(request.message, request.history, user_context)
    return {"response": response}

class ChatRequest(BaseModel):
    message: str
    history: list = [] # List of {"role": "user"|"model", "content": "..."}

@router.post("/chat")
def chat_endpoint(
    request: ChatRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Real-time chat with the AI Career Mentor.
    """
    from app.services.ai_service import chat_with_mentor
    
    # Optional: Fetch profile to give AI context about user
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    user_context = {}
    if profile:
        user_context = {
            "name": profile.full_name or current_user.email.split('@')[0],
            "role": profile.target_role or "Aspiring Professional",
            "education": profile.education_level or "Unknown",
            "skills": profile.parsed_resume_content if profile.has_resume else "Unknown"
        }

    response = chat_with_mentor(request.message, request.history, user_context)
    return {"response": response}
