from fastapi import APIRouter, Depends, HTTPException, status, UploadFile, File, Form
from sqlalchemy.exc import OperationalError
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
    try:
        # Check if profile exists
        profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
        
        if not profile:
            # Create new
            profile = StudentProfile(
                user_id=current_user.id,
                **profile_data.model_dump(exclude={'full_name'})
            )
            db.add(profile)
        else:
            # Update existing
            for key, value in profile_data.model_dump(exclude_unset=True, exclude={'full_name'}).items():
                setattr(profile, key, value)
        
        # Update User Full Name if provided
        if profile_data.full_name:
            current_user.full_name = profile_data.full_name
            db.add(current_user)

        db.commit()
        db.refresh(profile)
        
        # Manually attach full_name for response
        profile.full_name = current_user.full_name
        return profile
    except OperationalError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database temporarily unavailable. Please retry."
        )

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

    try:
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
        
        db.commit()
        
        return {
            "filename": file.filename,
            "parsed_content_preview": extracted_text[:200] + "..." if extracted_text else "",
            "message": message
        }
    except OperationalError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database temporarily unavailable. Please retry."
        )

@router.post("/upload-picture", response_model=ProfileResponse)
async def upload_profile_picture(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """
    Upload a profile picture (JPEG/PNG)
    """
    if file.content_type not in ["image/jpeg", "image/png", "image/jpg"]:
        raise HTTPException(status_code=400, detail="Invalid file type. Only JPEG and PNG images are allowed.")
    
    # Save file (reusing save_upload_file logic but maybe organizing better later)
    # Ideally should be in 'uploads/avatars' but simple 'uploads' is fine for now
    file_path = save_upload_file(file, current_user.id, sub_folder="avatars")
    
    try:
        profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
        if not profile:
            profile = StudentProfile(user_id=current_user.id)
            db.add(profile)
            
        profile.profile_picture_url = file_path # In production this would be a public URL
        db.commit()
        db.refresh(profile)
        
        profile.full_name = current_user.full_name
        return profile
    except OperationalError:
        db.rollback()
        raise HTTPException(status_code=503, detail="Database unavailable")

@router.get("/me", response_model=ProfileResponse)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    """Get current user's profile"""
    try:
        profile = db.query(StudentProfile).filter(StudentProfile.user_id == current_user.id).first()
        if not profile:
            raise HTTPException(status_code=404, detail="Profile not found. Please create one.")
        
        # Attach user's full name to response
        profile.full_name = current_user.full_name
        return profile
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database temporarily unavailable. Please retry."
        )
