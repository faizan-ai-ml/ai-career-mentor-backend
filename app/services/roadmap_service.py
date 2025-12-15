from openai import OpenAI
import json
import re
from app.config import OPENROUTER_API_KEY, OPENROUTER_MODEL, OPENROUTER_BASE_URL

def generate_roadmap_impl(profile_data: dict, duration_weeks: int = 8) -> dict:
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        
        resume_context = ""
        if profile_data.get('resume_content'):
             resume_context = f"\nRESUME CONTEXT:\n{profile_data['resume_content'][:2000]}...\n(Tailor the roadmap level based on these existing skills)"

        prompt = f"""Create a highly detailed {duration_weeks}-week learning roadmap for a "{profile_data.get('careerGoals', 'Tech Professional')}".
Profile: {json.dumps(profile_data)}
{resume_context}

REQUIREMENTS:
1. Career Goal: Be specific (derive from Resume if unclear).
2. For EACH WEEK ({duration_weeks} total), provide:
   - Topic: Main theme.
   - Tasks: 3 actionable steps.
   - Resources: 2 SPECIFIC, CLICKABLE-STYLE titles (e.g. "Course: 'Name' on Platform").

OUTPUT JSON:
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
                {"role": "system", "content": "You are a senior technical mentor. Return valid JSON only."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=3000
        )
        
        raw_content = response.choices[0].message.content
        cleaned = re.sub(r'```json\n?|\n?```', '', raw_content).strip()
        return json.loads(cleaned)
        
    except Exception as e:
        print(f"Roadmap Error: {str(e)}")
        return {
            "career_goal": "Software Engineering",
            "weeks": [
                {"week": 1, "topic": "Foundations", "tasks": ["Review Core Concepts"], "resources": ["Official Documentation"]}
            ]
        }

def get_career_counseling_impl(answers: dict) -> dict:
    try:
        client = OpenAI(
            api_key=OPENROUTER_API_KEY,
            base_url=OPENROUTER_BASE_URL
        )
        prompt = f"""Analyze career archetype based on: {json.dumps(answers)}
        Output JSON: {{ "archetype": "...", "suggested_role": "...", "reasoning": "...", "recommended_path": "..." }}"""
        
        response = client.chat.completions.create(
            model=OPENROUTER_MODEL,
            messages=[{"role": "system", "content": "Career psychologist. JSON only."},{"role": "user", "content": prompt}],
            max_tokens=1000
        )
        cleaned = re.sub(r'```json\n?|\n?```', '', response.choices[0].message.content).strip()
        return json.loads(cleaned)
    except Exception as e:
        print(f"Counselor Error: {str(e)}")
        return {
             "archetype": "The Builder",
             "suggested_role": "Software Engineer",
             "reasoning": "Standard fallback due to error.",
             "recommended_path": "CS Fundamentals"
        }
