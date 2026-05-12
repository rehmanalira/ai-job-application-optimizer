# AI ATS Resume Generator

<p align="center">
  <img src="https://img.shields.io/badge/Next.js-15-black?style=for-the-badge&logo=next.js" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi" />
  <img src="https://img.shields.io/badge/TailwindCSS-UI-blue?style=for-the-badge&logo=tailwindcss" />
  <img src="https://img.shields.io/badge/AI-Powered-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/ATS-Optimized-orange?style=for-the-badge" />
</p>

<p align="center">
  AI-powered ATS Resume Builder that generates professional, recruiter-ready resumes tailored to any job description.
</p>

---

# Overview

AI ATS Resume Generator is a full-stack AI application that creates highly optimized resumes based on a user's skills, experience, and target job description.

The platform analyzes job requirements, identifies important keywords, optimizes resume content for Applicant Tracking Systems (ATS), and generates downloadable professional PDF resumes.

Built for modern recruitment workflows and AI-assisted career optimization.

---

# Features

## AI Resume Generation

Generate complete resumes using AI based on:

- Job descriptions
- Skills
- Experience
- Projects
- Education
- Career goals

---

## ATS Optimization Engine

The system evaluates:

- Keyword matching
- Technical skills alignment
- Resume structure
- Section completeness
- Job relevance
- Formatting quality

Provides:

- Previous ATS Score
- Optimized ATS Score
- Keyword analysis

---

## Professional PDF Generation

Automatically generates:

- Clean ATS-friendly resumes
- Professional formatting
- Recruiter-ready layouts
- Downloadable PDF files

Powered using LaTeX for enterprise-level formatting quality.

---

## Modern Full Stack Architecture

### Frontend

- Next.js 15
- React
- Tailwind CSS
- Axios

### Backend

- FastAPI
- Python
- AI Integration
- ATS Analysis Engine
- PDF Generation Pipeline

---

## Responsive UI

- Fully responsive
- Mobile friendly
- Loading states
- Error handling
- Modern dashboard UI

---

# Application Workflow

```text
User Inputs Information
        ↓
AI Analyzes Job Description
        ↓
ATS Engine Extracts Keywords
        ↓
Resume Content Optimized
        ↓
Professional PDF Generated
        ↓
ATS Score Comparison Displayed
        ↓
Resume Download Ready
```

---

# Screenshots

## Dashboard

Add application screenshots here after deployment.

```bash
/public/screenshots/dashboard.png
```

---

# Project Structure

```bash
ai-job-search/
│
├── backend/
│   ├── services/
│   │   ├── ai_service.py
│   │   ├── ats_score.py
│   │   └── pdf_generator.py
│   │
│   ├── generated/
│   ├── templates/
│   ├── main.py
│   ├── requirements.txt
│   └── .env
│
├── frontend/
│   ├── app/
│   ├── components/
│   ├── public/
│   ├── package.json
│   └── .env.local
│
├── README.md
└── .gitignore
```

---

# Installation

# 1. Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-job-search.git
cd ai-job-search
```

---

# Backend Setup

```bash
cd backend
```

Create virtual environment:

## Windows

```bash
python -m venv venv
venv\Scripts\activate
```

## Mac/Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Install LaTeX

Install MiKTeX:

https://miktex.org/download

During installation:

- Enable automatic package installation

Verify installation:

```bash
pdflatex --version
```

---

# Backend Environment Variables

Create `.env`

```env
GEMINI_API_KEY=your_api_key
```

---

# Run Backend

```bash
uvicorn main:app --reload
```

Backend URL:

```bash
http://127.0.0.1:8000
```

---

# Frontend Setup

```bash
cd frontend
npm install
```

Create `.env.local`

```env
NEXT_PUBLIC_API_URL=http://127.0.0.1:8000
```

Run frontend:

```bash
npm run dev
```

Frontend URL:

```bash
http://localhost:3000
```

---

# API Endpoints

## Generate Resume

```http
POST /generate-resume
```

### Request Body

```json
{
  "name": "Muhammad Abdur Rehman",
  "email": "example@gmail.com",
  "phone": "07440241629",
  "location": "London, UK",
  "linkedin": "https://linkedin.com/in/example",
  "github": "https://github.com/example",
  "skills": "Python, FastAPI, React",
  "experience": "Software Engineer",
  "projects": "AI Resume Generator",
  "education": "MSc Information Technology",
  "job_description": "Backend Developer..."
}
```

---

## Download Resume

```http
GET /download/{file_name}
```

---

# ATS Scoring Logic

The ATS engine analyzes:

- Technical keywords
- Experience relevance
- Skills matching
- Contact completeness
- Resume structure
- Resume quality
- Section formatting

Target ATS score:

- 80% to 95%

---

# Future Improvements

- AI Cover Letter Generator
- LinkedIn Profile Optimizer
- Resume Version Management
- Job Auto Apply System
- Recruiter Analytics Dashboard
- AI Interview Preparation
- Multi-language Support
- Multi-template Support

---

# Deployment

## Frontend

Recommended:

- Vercel

## Backend

Recommended:

- Render
- Railway

---

# Performance Goals

- Fast resume generation
- Professional PDF quality
- High ATS optimization
- Recruiter-friendly formatting
- Mobile responsive experience

---

# Why This Project Matters

This project demonstrates:

- AI integration
- Full-stack development
- Real-world problem solving
- API engineering
- PDF generation systems
- ATS optimization logic
- Modern UI/UX implementation
- Production-ready architecture

---

# License

MIT License

---

# Author

## Muhammad Abdur Rehman

### LinkedIn

https://linkedin.com/in/rehmanalira

### GitHub

https://github.com/rehmanalira
