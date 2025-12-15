from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, JSON
from sqlalchemy.sql import func
from app.database import Base

class UserEvent(Base):
    __tablename__ = "user_events"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False, index=True)
    event_type = Column(String, nullable=False, index=True) # e.g., 'resume_uploaded', 'roadmap_generated'
    event_data = Column(JSON, nullable=True) # Flexible JSON for event metadata (e.g., {"score": 85})
    session_id = Column(String, nullable=True) # For tracking session flow
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # This table is the raw feed for the Career Intelligence Graph
