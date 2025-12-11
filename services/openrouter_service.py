from openai import OpenAI
import json
import re
from config import OPENROUTER_API_KEY, OPENROUTER_MODEL, OPENROUTER_BASE_URL

def analyze_with_openrouter(resume_text: str) -> dict:
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
                    "content": "You are a professional career counselor.  Always respond with valid JSON only."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            temperature=0.7,
            max_tokens=2500
        )
        
        raw_content = response.choices[0].message.content
        return parse_ai_response(raw_content, resume_text)
        
    except Exception as e:
        print(f"OpenRouter error: {str(e)}")
        raise Exception(f"OpenRouter failed: {str(e)}")

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
  "roadmap":  "Week 1: [Topic]\\n- Task 1\\n- Task 2\\n\\nWeek 2: [Topic]\\n- Task 1\\n- Task 2\\n\\n[Continue for 8 weeks]"
}}

IMPORTANT: 
- Be specific and actionable
- Base recommendations on current job market demands
- Make roadmap realistic (8-12 hours per week)
- Include free learning resources
- Return ONLY valid JSON, no extra text"""

def parse_ai_response(raw_content: str, resume_text: str) -> dict:
    """Parses AI response and validates JSON"""
    try:
        # Remove markdown code blocks if present
        cleaned = re.sub(r'```json\n? |\n?```', '', raw_content)
        data = json.loads(cleaned)
        
        # Validate required fields
        required = ["skills", "experience_level", "top_careers", "roadmap"]
        for field in required:
            if field not in data:
                raise ValueError(f"Missing field: {field}")
        
        return data
        
    except json. JSONDecodeError: 
        print("JSON parse failed, using fallback")
        return create_fallback_response(resume_text)

def create_fallback_response(resume_text: str) -> dict:
    """Creates fallback response if AI fails"""
    common_skills = [
        "Python", "JavaScript", "Java", "React", "Node.js", "SQL",
        "Machine Learning", "Data Analysis", "Communication", "Leadership"
    ]
    
    found_skills = [s for s in common_skills if s. lower() in resume_text.lower()]
    
    if not found_skills:
        found_skills = ["Communication", "Problem Solving", "Teamwork"]
    
    return {
        "skills": found_skills[: 8],
        "experience_level":  "Intermediate",
        "top_careers":  [
            {"title": "Software Developer", "match_percent": 75},
            {"title": "Data Analyst", "match_percent": 65}
        ],
        "roadmap": "Week 1-8: Focus on building practical projects and learning industry-standard tools."
    }