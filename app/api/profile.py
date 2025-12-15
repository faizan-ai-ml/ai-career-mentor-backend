from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.user import User
from app.models.profile import StudentProfile
from app.schemas.profile import ProfileCreate, ProfileResponse, ResumeUploadResponse
from app.dependencies import get_current_user
from app.utils.file_processing import save_upload_file, extract_text_from_file

router = APIRouter(prefix="/profile", tags=["Profile & Resume"])

@router.post("/create", response_model=ProfileResponse)
def create_or_update_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Path B: Create or update profile manually (for students/beginners)
    """
    # Check if profile exists
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    
    if not profile:
        # Create new
        profile = StudentProfile(
            user_id=current_user.id,
            **profile_data.model_dump()
        )
        db.add(profile)
    else:
        # Update existing
        for key, value in profile_data.model_dump(exclude_unset=True).items():
            setattr(profile, key, value)
    
    db.commit()
    db.refresh(profile)
    return profile

@router.post("/upload", response_model=ResumeUploadResponse)
async def upload_resume(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Path A: Upload resume file (PDF/DOCX) -> Extract Text -> Update Profile
    """
    # Validate file type
    if file.content_type not in ["application/pdf", "application/vnd.openxmlformats-officedocument.wordprocessingml.document"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only PDF and DOCX are supported.")
    
    # 1. Save File
    file_path = save_upload_file(file, current_user.id)
    
    # 2. Extract Text
    extracted_text = extract_text_from_file(file_path, file.content_type)
    
    if not extracted_text or len(extracted_text.strip()) < 50:
        # Warning if text extraction failed (e.g. image based PDF)
        message = "File uploaded, but could not extract much text. It might be an image-only PDF."
    else:
        message = "Resume uploaded and analyzed successfully."

    # 3. Update/Create Profile in DB
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    
    if not profile:
        profile = StudentProfile(user_id=current_user.id)
        db.add(profile)
    
    # Update resume fields
    profile.has_resume = True
    profile.resume_filename = file.filename
    profile.resume_file_path = file_path
    profile.parsed_resume_content = extracted_text
    
    # TODO (Phase 3): Use AI to extract skills/education from 'extracted_text' and populate other fields
    
    db.commit()
    
    return {
        "filename": file.filename,
        "parsed_content_preview": extracted_text[:200] + "..." if extracted_text else "",
        "message": message
    }

@router.get("/me", response_model=ProfileResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get current user's profile"""
    profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found. Please create one.")
    
    # Attach user's full name to response
    profile.full_name = current_user.full_name
    return profile
