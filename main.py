from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from services.resume_request import ResumeRequest

from services.ai_service import ask_llm
from services.ats_score import calculate_ats_score
from services.latex_resume import build_latex_resume

import subprocess
import uuid
import os

import glob
import os
import subprocess
from fastapi.staticfiles import StaticFiles
app = FastAPI()
app.mount("/generated", StaticFiles(directory="generated"), name="generated")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

os.makedirs("generated", exist_ok=True)

@app.post("/generate-resume")
async def generate_resume(data: ResumeRequest):

    old_resume = f"""
    {data.experience}
    {data.projects}
    {data.skills}
    """

    old_score = calculate_ats_score(
        old_resume,
        data.job_description
    )

    prompt = f"""

You are an expert ATS resume writer.

Generate a highly professional ATS optimized resume.

IMPORTANT RULES:

1. Use REAL professional company names only if experience is provided.

2. If no experience is provided:
DO NOT create fake companies.
Instead create strong project-focused experience professionally.

3. Add strong ATS keywords from the job description naturally.

4. Make the resume look written by a senior recruiter.

5. Focus on:
- ATS optimization
- Professional writing
- Clean formatting
- Strong action verbs
- Technical skills matching

6. Return ONLY LaTeX sections.

JOB DESCRIPTION:
{data.job_description}

CANDIDATE DETAILS:

Name:
{data.name}

Experience:
{data.experience}

Projects:
{data.projects}

Education:
{data.education}

Skills:
{data.skills}

Create these sections exactly:

\\section*{{PROFILE}}

\\section*{{TECHNICAL SKILLS}}

\\section*{{PROFESSIONAL EXPERIENCE}}

\\section*{{PROJECTS}}

\\section*{{EDUCATION}}

Use bullet points professionally.
"""

    ai_content = ask_llm(prompt)

    latex_code = build_latex_resume(data, ai_content)

    file_id = str(uuid.uuid4())

    tex_path = f"generated/{file_id}.tex"

    pdf_path = f"generated/{file_id}.pdf"

    with open(tex_path, "w", encoding="utf-8") as f:

        f.write(latex_code)

  
    subprocess.run(
    [
        "pdflatex",
        "-interaction=nonstopmode",
        "-output-directory",
        "generated",
        tex_path,
    ],
    check=True,
)
    
    # DELETE EXTRA FILES
    base_name = file_id

    for ext in ["aux", "log", "out", "tex"]:
        file_to_delete = f"generated/{base_name}.{ext}"

        if os.path.exists(file_to_delete):
            os.remove(file_to_delete)

        new_score = calculate_ats_score(
            latex_code,
            data.job_description
        )

    return JSONResponse({

        "old_score": old_score,
        "new_score": new_score,
        "download_url": f"http://127.0.0.1:8000/generated/{file_id}.pdf"

    })