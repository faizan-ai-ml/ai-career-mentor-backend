"""
Database configuration and session management for PostgreSQL (Neon)
"""
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# Get database URL from environment
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("DATABASE_URL environment variable is not set")

# Enforce SSL ONLY for cloud databases (Neon), not for local/Docker
# Local Docker PostgreSQL doesn't support SSL
is_cloud_db = "neon.tech" in DATABASE_URL or "supabase" in DATABASE_URL or "amazonaws" in DATABASE_URL

if is_cloud_db and "sslmode=" not in DATABASE_URL:
    separator = "&" if "?" in DATABASE_URL else "?"
    DATABASE_URL += f"{separator}sslmode=require"

# Create SQLAlchemy engine with production-hardened configuration
engine = create_engine(
    DATABASE_URL,
    pool_pre_ping=True,      # Check connection validity at request time
    pool_recycle=300,        # Recycle connections every 5 minutes
    pool_size=5,             # Production pool size
    max_overflow=10          # Balanced overflow
)

# Create SessionLocal class
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create Base class for models
Base = declarative_base()

def get_db():
    """
    FastAPI dependency providing a database session per request.
    Ensures the session is closed after the request is finished.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
