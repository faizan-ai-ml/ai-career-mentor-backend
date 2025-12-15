from openai import OpenAI
import json
import re
from app.config import OPENROUTER_API_KEY, OPENROUTER_MODEL, OPENROUTER_BASE_URL

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

def improve_text_with_openrouter(original_text: str) -> str:
    """
    Improves resume text to be more professional and impact-oriented
    """
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        
        prompt = f"""You are a professional resume writer. Rewrite the following text to be more professional, actionable, and result-oriented. Use strong action verbs.
        
        Original Text: "{original_text}"
        
        Rewritten Text (Return ONLY the rewritten text, nothing else):"""
        
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {"role": "system", "content": "You are a professional resume editor."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=500
        )
        
        return response.choices[0].message.content.strip()
        
    except Exception as e:
        print(f"OpenRouter Improve Text Error: {str(e)}")
        # Fallback: Return original text if AI fails
        return original_text

def generate_roadmap_with_openrouter(profile_data: dict, duration_weeks: int = 8) -> dict:
    """
    Generates a personalized learning roadmap based on user profile
    """
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        
        prompt = f"""Create a highly detailed {duration_weeks}-week learning roadmap for this student to become a "{profile_data.get('careerGoals', 'Tech Professional')}".
        Profile: {json.dumps(profile_data)}
        
        REQUIREMENTS:
        1. Career Goal: Be specific (e.g., "Full Stack Developer", "AI Engineer").
        2. For EACH WEEK (Total {duration_weeks} weeks), provide:
           - Topic: Main theme.
           - Tasks: 3 concrete actionable steps (e.g. "Build a Weather App", "Watch CS50 Lecture 3").
           - Resources: 2 SPECIFIC, REAL courses or video titles (e.g., "Course: 'React - The Complete Guide' on Udemy", "YouTube: 'Python Crash Course' by Traversy Media").
        
        OUTPUT JSON structure:
        {{
            "career_goal": "Target Role",
            "weeks": [
                {{
                    "week": 1, 
                    "topic": "Topic Name", 
                    "tasks": ["Task 1", "Task 2"],
                    "resources": ["Resource 1", "Resource 2"]
                }}
            ]
        }}
        """
        
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {"role": "system", "content": "You are a senior technical mentor. Provide concrete, clickable resource names. Return valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=3000
        )
        
        raw_content = response.choices[0].message.content
        cleaned = re.sub(r'```json\n?|\n?```', '', raw_content)
        return json.loads(cleaned)
        
    except Exception as e:
        print(f"OpenRouter Roadmap Error: {str(e)}")
        # Fallback
        return {
            "career_goal": "Software Engineering",
            "weeks": [
                {"week": 1, "topic": "Foundations", "tasks": ["Review Core Concepts", "Setup Environment"]},
                {"week": 2, "topic": "Advanced Topics", "tasks": ["Build a small project", "Learn version control"]}
            ]
        }

def get_career_counseling_with_openrouter(answers: dict) -> dict:
    """
    Analyzes user's 'Simulation' answers to suggest a career.
    """
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        
        prompt = f"""Analyze this student's thinking style based on these 3 scenarios to suggest the PERFECT tech career.
        
        1. THE BLANK PAGE TEST (Visual vs Logical):
           User Chose: "{answers.get('q1', 'Unknown')}"
           (Context: A=Draw Design/Visible, B=Write Logic/Invisible)
           
        2. THE JELLYBEAN TEST (Intuitive vs Analytical):
           User Chose: "{answers.get('q2', 'Unknown')}"
           (Context: A=Gut/Product, B=Count/Data)
           
        3. THE BROKEN THING TEST (Grit/Depth):
           User Chose: "{answers.get('q3', 'Unknown')}"
           (Context: A=Restart/Surface, B=Google Error/Deep Dive)

        TASK:
        1. Determine their "Archetype" (e.g., The Builder, The Analyst, The Visualist).
        2. Suggest top 2 Roles (e.g., Frontend Dev, Data Scientist, DevOps).
        3. Keep it encouraging but honest.

        OUTPUT JSON:
        {{
            "archetype": "The Creative Builder",
            "suggested_role": "Frontend Developer",
            "reasoning": "You chose to design first (Visual) and trust your gut (Intuitive). You love seeing things come to life.",
            "recommended_path": "Focus on React, UI/UX Design, and CSS Animations."
        }}
        """
        
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[
                {"role": "system", "content": "You are a career psychologist. Return valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1000
        )
        
        raw_content = response.choices[0].message.content
        cleaned = re.sub(r'```json\n?|\n?```', '', raw_content)
        return json.loads(cleaned)
        
    except Exception as e:
        print(f"OpenRouter Counselor Error: {str(e)}")
        # Fallback
        return {
            "archetype": "The Logical Builder",
            "suggested_role": "Software Engineer",
            "reasoning": "You show a balance of logic and problem solving.",
            "recommended_path": "General Computer Science Foundation"
        }