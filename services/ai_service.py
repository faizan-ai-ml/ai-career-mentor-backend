from config import OPENROUTER_AVAILABLE, GEMINI_AVAILABLE
from services.openrouter_service import analyze_with_openrouter
from services.gemini_service import analyze_with_gemini

def analyze_resume(resume_text: str) -> dict:
    """
    Main AI service - tries OpenRouter first, then Gemini as backup
    """
    errors = []
    
    # Try OpenRouter first (DeepSeek)
    if OPENROUTER_AVAILABLE: 
        try:
            print("🚀 Trying OpenRouter (DeepSeek)...")
            result = analyze_with_openrouter(resume_text)
            print("✅ OpenRouter succeeded!")
            return result
        except Exception as e:
            error_msg = f"OpenRouter failed: {str(e)}"
            print(f"❌ {error_msg}")
            errors. append(error_msg)
    
    # Fallback to Gemini
    if GEMINI_AVAILABLE:
        try:
            print("🚀 Trying Gemini (backup)...")
            result = analyze_with_gemini(resume_text)
            print("✅ Gemini succeeded!")
            return result
        except Exception as e: 
            error_msg = f"Gemini failed: {str(e)}"
            print(f"❌ {error_msg}")
            errors.append(error_msg)
    
    # Both failed
    raise Exception(f"All AI services failed: {', '.join(errors)}")