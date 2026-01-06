from openai import OpenAI
import json
import re
from app.config import OPENROUTER_API_KEY, OPENROUTER_MODEL, OPENROUTER_BASE_URL

def analyze_resume_impl(resume_text: str) -> dict:
    """
    Analyzes resume using DeepSeek via OpenRouter
    """
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        
        prompt = create_analysis_prompt(resume_text)
        
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional career counselor. Always respond with valid JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2500
        )
        
        if not response.choices or not response.choices[0].message.content:
             print("OpenRouter returned empty response")
             return create_fallback_response(resume_text)

        raw_content = response.choices[0].message.content
        return parse_ai_response(raw_content, resume_text)
        
    except Exception as e:
        print(f"OpenRouter Analysis Error: {str(e)}")
        return create_fallback_response(resume_text)

def create_analysis_prompt(resume_text: str) -> str:
    return f"""You are an expert career counselor. Analyze this resume/profile text and provide detailed career guidance that is STRICTLY based on the user's provided skills and interests.

RESUME/PROFILE TEXT: 
{resume_text}

YOUR TASK:
1. Extract ALL skills (technical, vocational, soft, or domain-specific) mentioned.
2. Determine experience level (Beginner/Intermediate/Advanced) based on the context of their specific field.
3. RATE the profile (0-100) based on clarity and evidence of expertise in their chosen area.
4. Identify KEY MISSING skills that the user needs to progress or excel in their specific field of interest.
5. Recommend 2-3 career paths that ACCURATELY reflect the user's field. 
   - DO NOT map unrelated careers (e.g., if they are a chef, don't suggest web development).
   - If they are in a non-technical field (e.g., chef, craftsmen, artist), suggest careers strictly within that domain.
6. Create a BRIEF summary of next steps tailored to their specific industry.

OUTPUT FORMAT (strict JSON):
{{
  "skills": ["skill1", "skill2", "skill3"],
  "score": 85,
  "missing_skills": ["Specific Field Skill 1", "Specific Field Skill 2"],
  "experience_level": "Beginner/Intermediate/Advanced",
  "top_careers": [
    {{"title": "Role matching their skills", "match_percent": 85}},
    {{"title": "Specialized role in their field", "match_percent": 75}}
  ],
  "roadmap": "Focus on mastering [Specific Skill] and gaining experience in [Specific Area]. Consider [Industry-specific recommendation]."
}}

IMPORTANT: Return ONLY valid JSON. Be field-agnostic and honor the user's unique background."""

def parse_ai_response(raw_content: str, resume_text: str) -> dict:
    try:
        cleaned = re.sub(r'```json\n?|\n?```', '', raw_content).strip()
        data = json.loads(cleaned)
        
        required = ["skills", "experience_level", "top_careers"]
        for field in required:
            if field not in data:
                # If partial data, try to salvage
                print(f"Missing field {field} in response")
        
        return data
        
    except json.JSONDecodeError: 
        print("JSON parse failed, using fallback")
        return create_fallback_response(resume_text)

def create_fallback_response(resume_text: str) -> dict:
    common_skills = [
        "Python", "JavaScript", "Java", "React", "Node.js", "SQL",
        "Machine Learning", "Data Analysis", "Communication", "Leadership"
    ]
    found_skills = [s for s in common_skills if s.lower() in resume_text.lower()]
    if not found_skills:
        found_skills = ["Communication", "Problem Solving", "Teamwork"]
    
    return {
        "skills": found_skills[:8],
        "score": 70,
        "missing_skills": ["Cloud Basics", "System Design"],
        "experience_level": "Intermediate",
        "top_careers": [
            {"title": "Software Developer", "match_percent": 70},
            {"title": "Quality Assurance", "match_percent": 60}
        ],
        "roadmap": "Focus on building practical projects and learning industry-standard tools."
    }

def improve_text_impl(original_text: str) -> str:
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        prompt = f"""Rewrite to be professional and actionable: "{original_text}" """
        
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[{"role": "user", "content": prompt}],
            max_tokens=500
        )
        return response.choices[0].message.content.strip()
    except Exception:
        return original_text
