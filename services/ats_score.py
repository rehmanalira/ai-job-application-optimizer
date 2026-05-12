import re

def calculate_ats_score(text, job_description):

    text = text.lower()

    job_description = job_description.lower()

    keywords = re.findall(r'\b[a-zA-Z]+\b', job_description)

    keywords = list(set(keywords))

    matched = 0

    for keyword in keywords:

        if keyword in text:

            matched += 1

    if len(keywords) == 0:

        return 0

    score = int((matched / len(keywords)) * 100)

    if score > 98:
        score = 98

    return score