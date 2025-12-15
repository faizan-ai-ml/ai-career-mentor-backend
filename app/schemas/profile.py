from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

# Shared properties
class ProfileBase(BaseModel):
    education_level: Optional[str] = None
    field_of_study: Optional[str] = None
    university: Optional[str] = None
    current_semester: Optional[str] = None
    skills: Optional[str] = None  # Received as comma-separated string
    interests: Optional[str] = None
    career_goals: Optional[str] = None

# Properties to receive on profile creation (Manual - Path B)
class ProfileCreate(ProfileBase):
    pass

# Properties to receive on update
class ProfileUpdate(ProfileBase):
    pass

# Response model
class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    full_name: Optional[str] = None
    has_resume: bool
    resume_filename: Optional[str] = None
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

# Schema for File Upload Response
class ResumeUploadResponse(BaseModel):
    filename: str
    parsed_content_preview: str
    message: str
