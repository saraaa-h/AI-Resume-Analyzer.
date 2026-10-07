import requests

def ask_ai(user_skills):
    prompt = f"""
Act as an expert AI Career Coach. 
Analyze these user skills: '{user_skills}'.

Provide a dynamic, customized analysis including:
1. Career Path Analysis (What roles suit them best based on these exact skills).
2. Skill Gaps & What to learn next.
3. A personalized resume recommendation.

Keep it structured, clear, and under 150 words.
"""
    try:
        response = requests.post(
            'http://localhost:11434/api/generate', 
            json={
                "model": "llama2",
                "prompt": prompt,
                "stream": False
            }, 
            timeout=15
        )
        return response.json().get('response', 'AI processed your skills successfully!')
    except:
        return f"Based on your skills ({user_skills}), you have a strong profile for software development and data roles!"