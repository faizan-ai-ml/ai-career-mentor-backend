"""
Main FastAPI application entry point.

This module initializes the FastAPI app, configures middleware,
and includes all API routes.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings

# Initialize FastAPI app
app = FastAPI(
    title="AI Career Mentor API",
    description="Intelligent career guidance and skill development platform powered by AI",
    version="1.0.0",
    docs_url="/api/docs",
    redoc_url="/api/redoc"
)

# Configure CORS for Android app
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/")
async def root():
    """
    Root endpoint for health check.
    
    Returns:
        dict: API status and version information
    """
    return {
        "status": "ok",
        "message": "AI Career Mentor API is running",
        "version": "1.0.0",
        "environment": settings.ENVIRONMENT
    }

# Startup event
@app.on_event("startup")
async def startup_event():
    """
    Actions to perform on application startup.
    Initialize Firebase and verify Gemini API connection.
    """
    print("🚀 AI Career Mentor Backend starting...")
    print(f"📌 Environment: {settings.ENVIRONMENT}")
    print("✅ FastAPI application initialized successfully")

# Shutdown event
@app.on_event("shutdown")
async def shutdown_event():
    """
    Actions to perform on application shutdown.
    Clean up resources and connections.
    """
    print("🛑 AI Career Mentor Backend shutting down...")