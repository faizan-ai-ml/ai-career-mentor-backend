from sqlalchemy.orm import Session
from app.models.analytics import UserEvent
import json

def track_event(db: Session, user_id: int, event_type: str, data: dict = None):
    """
    Core function to feed the Career Intelligence Graph.
    Logs raw behavioral signals (no logic, just capture).
    """
    try:
        event = UserEvent(
            user_id=user_id,
            event_type=event_type,
            event_data=data
        )
        db.add(event)
        db.commit()
    except Exception as e:
        print(f"Failed to track event {event_type}: {e}")
        # Fail silent: Analytics should never crash the user experience
