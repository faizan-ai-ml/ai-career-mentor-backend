from pydantic import BaseModel
from typing import Optional, List, Union
from datetime import datetime
from enum import Enum

class EducationLevel(str, Enum):
    SECONDARY = "Secondary School"
    HIGHER_SECONDARY = "Higher Secondary"
    DIPLOMA = "Diploma"
    BACHELORS = "Bachelor's Degree"
    MASTERS = "Master's Degree"
    DOCTORATE = "Doctorate"
    OTHER = "Other"

# Shared properties
class ProfileBase(BaseModel):
    education_level: Optional[Union[EducationLevel, str]] = None
    field_of_study: Optional[str] = None
    university: Optional[str] = None
    current_semester: Optional[str] = None
    skills: Optional[str] = None  # Received as comma-separated string
    interests: Optional[str] = None
    career_goals: Optional[str] = None
    # Professional Identity
    bio: Optional[str] = None
    linkedin_url: Optional[str] = None
    portfolio_url: Optional[str] = None
    profile_picture_url: Optional[str] = None
    experience_years: Optional[int] = 0
    target_role: Optional[str] = None

# Properties to receive on profile creation (Manual - Path B)
class ProfileCreate(ProfileBase):
    full_name: Optional[str] = None

# Properties to receive on update
class ProfileUpdate(ProfileBase):
    full_name: Optional[str] = None

# Response model
class ProfileResponse(ProfileBase):
    id: int
    user_id: int
    full_name: Optional[str] = None
    profile_picture_url: Optional[str] = None
    has_resume: bool = False
    resume_filename: Optional[str] = None
    skill_analysis: Optional[str] = None
    roadmap_data: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Schema for File Upload Response
class ResumeUploadResponse(BaseModel):
    filename: str
    parsed_content_preview: str
    message: str
