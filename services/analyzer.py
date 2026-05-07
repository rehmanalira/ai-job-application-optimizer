import re

COMMON_SKILLS = [
    "python", "java", "javascript", "react", "node", "sql",
    "aws", "docker", "kubernetes", "machine learning",
    "ai", "nlp", "fastapi", "django"
]

def extract_skills(job_text: str):
    job_text_lower = job_text.lower()
    found_skills = []

    for skill in COMMON_SKILLS:
        if skill in job_text_lower:
            found_skills.append(skill)

    return list(set(found_skills))


def summarize_job(job_text: str):
    sentences = re.split(r'(?<=[.!?]) +', job_text)
    return sentences[:2]  # first 2 sentences as simple summary


def analyze_job(job_text: str):
    skills = extract_skills(job_text)
    summary = summarize_job(job_text)

    return {
        "skills": skills,
        "summary": summary
    }