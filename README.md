# AI Job Application Optimizer

An AI-powered system that analyzes job descriptions, extracts required skills, and helps optimize job applications.

## Features

- Extract key technical skills from job descriptions
- Summarize job requirements
- AI-ready backend architecture
- FastAPI REST API
- Swagger API documentation

## Tech Stack

- Python
- FastAPI
- Uvicorn

## Project Structure

```bash
ai-job-optimizer/
│── main.py
│── services/
│    └── analyzer.py
│── requirements.txt
│── README.md
```

## Installation

### Clone repository

```bash
git clone <your-github-url>
cd ai-job-optimizer
```

### Create virtual environment

```bash
python -m venv venv
```

### Activate environment

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

## Run API

```bash
uvicorn main:app --reload
```

## API Documentation

Open:

```bash
http://127.0.0.1:8000/docs
```

## Example Request

```json
{
  "job_description": "We are looking for a Python developer with FastAPI and Docker experience."
}
```

## Example Response

```json
{
  "skills": ["python", "fastapi", "docker"],
  "summary": [
    "We are looking for a Python developer with FastAPI and Docker experience."
  ]
}
```

## Future Improvements

- AI-powered skill extraction
- CV optimization
- Cover letter generation
- ATS keyword matching
- Job tracking dashboard

## Author

Rehman Ali
