from sqlalchemy import Column, Integer, String, ForeignKey, Text, Boolean, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy import JSON
from datetime import datetime
from app.database import Base

class StudentProfile(Base):
    __tablename__ = "student_profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True, nullable=False)
    
    # Common Education Info (for both manual & parsed)
    education_level = Column(String(50), nullable=True)  # e.g., "BS", "MS", "High School"
    field_of_study = Column(String(100), nullable=True)  # e.g., "Computer Science"
    university = Column(String(255), nullable=True)
    current_semester = Column(String(50), nullable=True)
    
    # Skills & Interests (JSON for list storage)
    skills = Column(String, nullable=True)  # Stored as comma-separated string or JSON string
    interests = Column(String, nullable=True) # Stored as comma-separated string
    career_goals = Column(Text, nullable=True)
    
    # AI Analysis & Roadmap Persistence
    skill_analysis = Column(Text, nullable=True)  # JSON String: {score, skills: [{name, level}], missing_skills}
    roadmap_data = Column(Text, nullable=True)    # JSON String: {weeks: [...]}
    
    # Professional Identity (The "Imp Things")
    bio = Column(Text, nullable=True)
    linkedin_url = Column(String(255), nullable=True)
    portfolio_url = Column(String(255), nullable=True)
    profile_picture_url = Column(String(500), nullable=True)
    experience_years = Column(Integer, default=0)
    target_role = Column(String(100), nullable=True)
    
    # Path A: Resume Specifics
    has_resume = Column(Boolean, default=False)
    resume_filename = Column(String(255), nullable=True)
    resume_file_path = Column(String(500), nullable=True)
    parsed_resume_content = Column(Text, nullable=True)  # Full text extracted from PDF
    
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship
    user = relationship("User", back_populates="profile")
