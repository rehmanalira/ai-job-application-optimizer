def find_missing_skills(cv_text: str, job_skills: list):

    cv_text = cv_text.lower()

    missing = []

    for skill in job_skills:
        if skill.lower() not in cv_text:
            missing.append(skill)

    return missing