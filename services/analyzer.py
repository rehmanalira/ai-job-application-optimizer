import json
from services.ai_service import ask_llm


def analyze_job(job_text: str):

    prompt = f"""
You are an API.

Return ONLY valid JSON.

Do NOT explain anything.
Do NOT add markdown.
Do NOT add extra text.

JSON format:
{{
    "summary": "...",
    "skills": [],
    "seniority_level": "...",
    "keywords": [],
    "ats_score_tips": []
}}

Job Description:
{job_text}
"""

    result = ask_llm(prompt)

    try:
        parsed_result = json.loads(result)
        return parsed_result

    except:
        return {
            "error": "AI response parsing failed",
            "raw_response": result
        }