from fastapi  import FastAPI
from services.analyzer import analyze_job
from pydantic import BaseModel
from services.matcher import calculate_match_score
from fastapi import UploadFile, File
import shutil
from services.pdf_parser import extract_text_from_pdf
from services.skill_gap import find_missing_skills
app = FastAPI()

class JobRequest(BaseModel):
    job_description: str

class MatchRequest(BaseModel):
    cv_text: str
    job_skills: list    


class SkillGapRequest(BaseModel):
    cv_text: str
    job_skills: list



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

