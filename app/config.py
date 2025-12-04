"""
Configuration management for AI Career Mentor Backend.

This module loads and validates environment variables using Pydantic Settings.
All sensitive data should be stored in .env file and never committed to git.
"""

from pydantic_settings import BaseSettings
from typing import List
import os

class Settings(BaseSettings):
    """
    Application settings loaded from environment variables.
    
    Attributes:
        GEMINI_API_KEY: API key for Google Gemini AI
        FIREBASE_CREDENTIALS_PATH: Path to Firebase credentials JSON file
        FIREBASE_STORAGE_BUCKET: Firebase storage bucket name
        JWT_SECRET_KEY: Secret key for JWT token generation
        JWT_ALGORITHM: Algorithm used for JWT (default: HS256)
        ACCESS_TOKEN_EXPIRE_MINUTES: Token expiration time in minutes
        ENVIRONMENT: Application environment (development/production)
        CORS_ORIGINS: List of allowed CORS origins for Android/Web apps
    """
    
    # Gemini AI Configuration
    GEMINI_API_KEY: str
    
    # Firebase Configuration
    FIREBASE_CREDENTIALS_PATH: str = "firebase-credentials.json"
    FIREBASE_STORAGE_BUCKET: str
    
    # JWT Configuration
    JWT_SECRET_KEY: str
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 10080  # 7 days
    
    # Application Configuration
    ENVIRONMENT: str = "development"
    CORS_ORIGINS: List[str] = ["http://localhost:3000", "http://localhost:8081"]
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# Global settings instance
settings = Settings()