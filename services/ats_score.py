import re

from collections import Counter


def clean_text(text):

    text = text.lower()

    text = re.sub(r'[^a-zA-Z0-9 ]', '', text)

    return text.split()


def calculate_ats_score(
    resume_text,
    job_description
):

    resume_words = clean_text(
        resume_text
    )

    job_words = clean_text(
        job_description
    )

    resume_counter = Counter(
        resume_words
    )

    job_counter = Counter(
        job_words
    )

    matched_keywords = 0

    total_keywords = len(
        set(job_words)
    )

    for word in set(job_words):

        if word in resume_counter:

            matched_keywords += 1

    score = int(
        (matched_keywords / total_keywords)
        * 100
    )

    if score > 95:
        score = 95

    return max(score, 35)