from pydantic import BaseModel

class ResumeRequest(BaseModel):

    name: str
    email: str
    phone: str
    location: str

    linkedin: str = ""
    github: str = ""

    experience: str = ""
    projects: str = ""
    education: str = ""
    skills: str = ""

    job_description: str