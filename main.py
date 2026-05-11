from fastapi  import FastAPI
from services.analyzer import analyze_job
from pydantic import BaseModel
from services.matcher import calculate_match_score
from fastapi import UploadFile, File
import shutil
from services.pdf_parser import extract_text_from_pdf
from services.skill_gap import find_missing_skills
from fastapi.middleware.cors import CORSMiddleware
from services.resume_generator import generate_resume
from services.pdf_generator import create_resume_pdf
from fastapi.responses import FileResponse
import uuid
from fastapi.responses import FileResponse

from fastapi.responses import FileResponse
from services.ats_score import calculate_ats_score
from services.skill_extractor import extract_skills
from services.ai_service import ask_llm
from fastapi import (
    FastAPI,
    UploadFile,
    File,
    Form,
    HTTPException
)
from services.pdf_reader import (
    extract_text_from_pdf
)
app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  # important
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class JobRequest(BaseModel):
    job_description: str

class MatchRequest(BaseModel):
    cv_text: str
    job_skills: list    


class SkillGapRequest(BaseModel):
    cv_text: str
    job_skills: list

class ResumeRequest(BaseModel):
    job_description: str
    old_cv_text: str

# for home directory
@app.get("/")
def home():
    return {"message": "This is Test Api and it is running  successfully."}


# post request to analyze job recive from frontend
@app.post("/analyze-job")
def analyze(request: JobRequest):
    result = analyze_job(request.job_description)
    return result

@app.post("/match-score")
def match_score(request: MatchRequest):

    score = calculate_match_score(
        request.cv_text,
        request.job_skills
    )

    return {
        "match_score": score
    }




@app.post("/upload-cv")
def upload_cv(file: UploadFile = File(...)):

    file_path = f"uploads/{file.filename}"

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    extracted_text = extract_text_from_pdf(file_path)

    return {
        "filename": file.filename,
        "extracted_text": extracted_text[:3000]
    }


@app.post("/skill-gap")
def skill_gap(request: SkillGapRequest):

    missing  = find_missing_skills(
        request.cv_text,
        request.job_skills
    )

    return {
        "missing_skills": missing 
    }



# @app.post("/generate-resume")
# def generate_ats_resume(request: ResumeRequest):

#     generated_resume = generate_resume(
#         request.job_description,
#         request.old_cv_text
#     )

#     filename = f"generated_resume_{uuid.uuid4()}.pdf"

#     create_resume_pdf(
#         generated_resume,
#         filename
#     )

#     return {
#         "generated_resume": generated_resume,
#         "download_file": filename
#     }
@app.post("/generate-resume")

async def generate_resume(

    resume: UploadFile = File(...),

    job_description: str = Form(...)
):

    try:

        pdf_bytes = await resume.read()

        resume_text = extract_text_from_pdf(
            pdf_bytes
        )

        old_score = calculate_ats_score(
            resume_text,
            job_description
        )

        optimized_resume = ask_llm(
            f"""
            Create a professional ATS-friendly resume.

            Resume:
            {resume_text}

            Job Description:
            {job_description}

            Improve:
            - skills
            - ATS keywords
            - formatting
            - achievements
            """
        )

        new_score = calculate_ats_score(
            optimized_resume,
            job_description
        )

        filename = "generated_resume.pdf"

        create_resume_pdf(
            optimized_resume,
            filename
        )

        return {

            "old_score": old_score,

            "new_score": 80,

            "download_url":
            "http://127.0.0.1:8000/download-resume",

            "matched_skills": [],

            "missing_skills": []
        }

    except Exception as e:

        raise HTTPException(
            status_code=500,
            detail=str(e)
        )
    
@app.get("/download-resume")
def download_resume():

    return FileResponse(
        path="generated_resume.pdf",
        media_type="application/pdf",
        filename="ATS_Resume.pdf"
    )