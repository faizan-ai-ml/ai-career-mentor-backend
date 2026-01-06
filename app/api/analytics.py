from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.exc import OperationalError
from sqlalchemy.orm import Session
from sqlalchemy import func
from datetime import datetime, timedelta
from app.database import get_db
from app.models.user import User
from app.models.analytics import UserEvent
from app.dependencies import get_current_user
from pydantic import BaseModel

router = APIRouter(prefix="/analytics", tags=["Analytics"])

class StatResponse(BaseModel):
    streak_days: int
    total_activities: int
    resume_score_history: list[int]
    activity_graph: list[int] # Last 7 days activity count

@router.get("/stats", response_model=StatResponse)
def get_user_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    try:
        # 1. Calculate Streak
        end_date = datetime.utcnow()
        start_date = end_date - timedelta(days=7)
        
        events_last_7_days = db.query(UserEvent)\
            .filter(UserEvent.user_id == current_user.id)\
            .filter(UserEvent.created_at >= start_date)\
            .all()
        
        # Group by date
        activity_map = {}
        for i in range(7):
            day = (start_date + timedelta(days=i)).date()
            activity_map[day] = 0
    
        distinct_days = set()
        for event in events_last_7_days:
            day = event.created_at.date()
            if day in activity_map:
                activity_map[day] += 1
            distinct_days.add(day)
    
        streak = len(distinct_days)
    
        # 2. Get Score History
        score_events = db.query(UserEvent)\
            .filter(UserEvent.user_id == current_user.id)\
            .filter(UserEvent.event_type == 'resume_analyzed')\
            .order_by(UserEvent.created_at.asc())\
            .limit(5)\
            .all()
        
        scores = []
        for e in score_events:
            if e.event_data and 'score' in e.event_data:
                scores.append(e.event_data['score'])
        
        if not scores:
            scores = [60, 65, 70]
    
        return {
            "streak_days": streak,
            "total_activities": len(events_last_7_days),
            "resume_score_history": scores,
            "activity_graph": list(activity_map.values())
        }
    except OperationalError:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail="Database temporarily unavailable. Please retry."
        )
