from services.ai_service import ask_llm


def analyze_job(job_text: str):

    prompt = f"""
    Analyze this job description.

    Extract:
    1. Required technical skills
    2. Short summary
    3. Seniority level
    4. Important keywords

    Return response in clean text.

    Job Description:
    {job_text}
    """

    result = ask_llm(prompt)

    return {
        "analysis": result
    }