from fastapi  import FastAPI
from services.analyzer import analyze_job
from pydantic import BaseModel

app = FastAPI()

class JobRequest(BaseModel):
    job_description: str

# for home directory
@app.get("/")
def home():
    return {"message": "This is Test Api and it is running  successfully."}


# post request to analyze job recive from frontend
@app.post("/analyze-job")
def analyze(request: JobRequest):
    result = analyze_job(request.job_description)
    return result
