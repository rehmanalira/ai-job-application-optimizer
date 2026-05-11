import re

TECH_SKILLS = [
    "python",
    "fastapi",
    "django",
    "react",
    "next.js",
    "aws",
    "docker",
    "kubernetes",
    "sql",
    "mongodb",
    "javascript",
    "typescript",
    "git",
    "linux",
    "api",
    "machine learning",
    "ai"
]


def extract_skills(text):

    text = text.lower()

    found_skills = []

    for skill in TECH_SKILLS:

        if re.search(rf"\b{re.escape(skill)}\b", text):

            found_skills.append(skill)

    return list(set(found_skills))