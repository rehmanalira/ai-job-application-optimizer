from fastapi  import FastAPI
from services.analyzer import analyze_job
from pydantic import BaseModel
from services.matcher import calculate_match_score
app = FastAPI()

class JobRequest(BaseModel):
    job_description: str

class MatchRequest(BaseModel):
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