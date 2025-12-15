from app.database import SessionLocal
from app.models.user import User

def check_user():
    try:
        db = SessionLocal()
        user = db.query(User).filter(User.email == 'nextstep9500@gmail.com').first()
        if user:
            print(f"User FOUND: {user.email}")
            print(f"ID: {user.id}")
        else:
            print("User NOT found")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    check_user()
