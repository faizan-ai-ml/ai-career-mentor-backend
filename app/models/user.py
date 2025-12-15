"""
User database model
"""
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class User(Base):
    """
    User model for authentication and profile management
    """
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique=True, index=True, nullable=False)
    password_hash = Column(String(255), nullable=False)
    full_name = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
    
    # Relationships
    profile = relationship("app.models.profile.StudentProfile", back_populates="user", uselist=False)
    
    @property
    def has_profile(self):
        return self.profile is not None
    
    def __repr__(self):
        return f"<User(id={self.id}, email={self.email})>"
