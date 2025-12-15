import google.generativeai as genai
import json
import re
from app.config import GEMINI_API_KEY, GEMINI_MODEL

def analyze_with_gemini(resume_text: str) -> dict:
    """
    Analyzes resume using Google Gemini (backup service)
    """
    try:
        genai.configure(api_key=GEMINI_API_KEY)
        model = genai.GenerativeModel(GEMINI_MODEL)
        
        prompt = create_analysis_prompt(resume_text)
        
        response = model.generate_content(prompt)
        raw_content = response.text
        
        return parse_ai_response(raw_content, resume_text)
        
    except Exception as e: 
        print(f"Gemini error: {str(e)}")
        raise Exception(f"Gemini failed: {str(e)}")

def create_analysis_prompt(resume_text: str) -> str:
    """Creates the analysis prompt"""
    return f"""You are an expert career counselor.  Analyze this resume and provide detailed career guidance.

RESUME TEXT: 
{resume_text}

YOUR TASK:
1. Extract ALL technical and soft skills mentioned
2. Determine experience level (Beginner/Intermediate/Advanced)
3. Recommend top 2-3 career paths with match percentages
4. Create a detailed 8-week learning roadmap for the best career match

OUTPUT FORMAT (strict JSON):
{{
  "skills": ["skill1", "skill2", "skill3"],
  "experience_level": "Beginner/Intermediate/Advanced",
  "top_careers": [
    {{"title": "Career Title 1", "match_percent": 85}},
    {{"title": "Career Title 2", "match_percent": 75}}
  ],
  "roadmap": "Week 1: [Topic]\\n- Task 1\\n- Task 2\\n\\nWeek 2: [Topic]\\n- Task 1\\n- Task 2\\n\\n[Continue for 8 weeks]"
}}

Return ONLY valid JSON, no extra text."""

def parse_ai_response(raw_content: str, resume_text: str) -> dict:
    """Parses AI response and validates JSON"""
    try: 
        cleaned = re.sub(r'```json\n?|\n?```', '', raw_content)
        data = json.loads(cleaned)
        
        required = ["skills", "experience_level", "top_careers", "roadmap"]
        for field in required:
            if field not in data:
                raise ValueError(f"Missing field: {field}")
        
        return data
        
    except json.JSONDecodeError:
        return create_fallback_response(resume_text)

def create_fallback_response(resume_text:  str) -> dict:
    """Creates fallback response if AI fails"""
    common_skills = ["Python", "JavaScript", "Communication", "Leadership"]
    found_skills = [s for s in common_skills if s.lower() in resume_text.lower()]
    
    if not found_skills:
        found_skills = ["Communication", "Problem Solving"]
    
    return {
        "skills": found_skills[:8],
        "experience_level":  "Intermediate",
        "top_careers": [
            {"title": "Software Developer", "match_percent": 75}
        ],
        "roadmap": "Week 1-8: Focus on practical projects and learning."
    }