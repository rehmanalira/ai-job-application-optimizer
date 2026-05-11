# from services.ai_service import ask_llm


# def generate_resume(job_description, old_cv):

#     prompt = f"""
#     You are a professional ATS resume writer.

#     Rewrite the candidate's resume according to the given job description.

#     Requirements:
#     - Make it ATS optimized
#     - Professional UK style
#     - Improve bullet points
#     - Add strong action verbs
#     - Keep information truthful
#     - Prioritize matching skills
#     - Make it highly professional
#     - Return clean resume text only

#     JOB DESCRIPTION:
#     {job_description}

#     OLD CV:
#     {old_cv}
#     """

#     result = ask_llm(prompt)

#     return result

from services.ai_service import ask_llm


def generate_resume(job_description, old_cv):

    prompt = f"""
You are an elite UK ATS resume writer.

Your task:
Rewrite the candidate's CV specifically for the provided job description.

STRICT REQUIREMENTS:

1. ATS optimized
2. Professional UK resume style
3. Strong measurable bullet points
4. Modern formatting
5. Improve wording professionally
6. Use powerful action verbs
7. Prioritize matching keywords from the job description
8. Make recruiter-friendly
9. Keep information truthful
10. Return HIGH QUALITY professional resume

FORMAT:

FULL NAME
Phone | Email | LinkedIn | GitHub

PROFESSIONAL SUMMARY

TECHNICAL SKILLS

WORK EXPERIENCE

PROJECTS

EDUCATION

CERTIFICATIONS

ADDITIONAL INFORMATION

IMPORTANT:
- Maximize ATS score
- Include keywords from job description naturally
- Match technical skills carefully
- Rewrite bullet points to align with the role
- Optimize for recruiter screening systems

JOB DESCRIPTION:
{job_description}

OLD CV:
{old_cv}
"""

    return ask_llm(prompt)