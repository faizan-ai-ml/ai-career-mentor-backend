from app.config import OPENROUTER_AVAILABLE, GEMINI_AVAILABLE
from app.services.analysis_service import analyze_resume_impl, improve_text_impl
from app.services.roadmap_service import generate_roadmap_impl, get_career_counseling_impl
from app.services.gemini_service import analyze_with_gemini

def analyze_resume(resume_text: str) -> dict:
    """
    Main AI service - tries OpenRouter (DeepSeek) first, then Gemini as backup
    """
    errors = []
    
    if OPENROUTER_AVAILABLE: 
        try:
            print("🚀 Analyzing with OpenRouter...")
            return analyze_resume_impl(resume_text)
        except Exception as e:
            errors.append(f"OpenRouter: {str(e)}")
    
    if GEMINI_AVAILABLE:
        try:
            print("🚀 Fallback to Gemini...")
            return analyze_with_gemini(resume_text)
        except Exception as e: 
            errors.append(f"Gemini: {str(e)}")
            
    # If we get here, both failed or returned fallback inside impl
    # But if impl returns fallback dict, we wouldn't raise exception.
    # So this raise is only if the impls themselves crash hard without fallback.
    raise Exception(f"AI Service Failure: {errors}")

def improve_resume_text(text: str) -> str:
    if OPENROUTER_AVAILABLE:
        return improve_text_impl(text)
    return text

def generate_learning_roadmap(profile_data: dict, duration_weeks: int = 8) -> dict:
    if OPENROUTER_AVAILABLE:
        return generate_roadmap_impl(profile_data, duration_weeks)
    return {"message": "AI service unavailable"}

def chat_with_mentor(message: str, history: list, user_context: dict) -> str:
    """
    Chat with the AI Mentor.
    """
    if GEMINI_AVAILABLE:
        from app.services.gemini_service import chat_with_gemini
        return chat_with_gemini(message, history, user_context)
    
    # Fallback/Primary to OpenRouter if Gemini not preferred (but here we prefer Gemini for chat due to context window)
    if OPENROUTER_AVAILABLE:
         # TODO: Implement OpenRouter Chat if needed
         return "I'm sorry, I can only chat via Gemini right now."
         
    return "AI Service Unavailable"

def get_career_counseling(answers: dict) -> dict:
    if OPENROUTER_AVAILABLE:
        return get_career_counseling_impl(answers)
    return {"message": "AI service unavailable"}