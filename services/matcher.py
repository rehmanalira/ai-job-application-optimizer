def calculate_match_score(cv_text: str, job_skills: list):

    cv_text = cv_text.lower()

    matched = 0

    for skill in job_skills:
        if skill.lower() in cv_text:
            matched += 1

    if len(job_skills) == 0:
        return 0

    score = (matched / len(job_skills)) * 100

    return round(score, 2)