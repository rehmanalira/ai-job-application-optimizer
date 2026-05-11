# AI Resume Optimizer

AI-powered ATS Resume Optimization Platform that transforms resumes into recruiter-ready CVs tailored to real job descriptions using modern AI workflows.

---

## Overview

This project helps job seekers improve their resumes automatically by:

- Uploading an existing resume PDF
- Providing a target job description
- Generating an optimized ATS-friendly resume
- Improving recruiter readability
- Increasing keyword relevance
- Exporting a professional PDF resume

The platform combines AI, PDF processing, ATS analysis, and modern frontend engineering into a real-world SaaS-style application.

---

# Features

## AI Resume Optimization

- Resume rewriting using AI
- ATS keyword enhancement
- Skills optimization
- Professional formatting
- Recruiter-friendly structure

## ATS Analysis Dashboard

- Previous ATS score
- Optimized ATS score
- Keyword matching
- Missing skills analysis
- Resume improvement insights

## Resume Processing

- PDF upload support
- Automatic PDF text extraction
- Professional PDF generation
- Clean ATS-compatible layouts

## Modern UI/UX

- Responsive design
- Dark modern interface
- Loading states
- Error handling
- Smooth animations

---

# Tech Stack

## Frontend

- Next.js 15
- React
- Tailwind CSS
- Framer Motion
- Axios
- Lucide React

## Backend

- FastAPI
- Python
- ReportLab
- PyMuPDF

## AI Integration

- Gemini API
- OpenAI compatible architecture

---

# Project Architecture

```bash
frontend/
├── app/
├── components/
├── public/
├── styles/
└── .env.local

backend/
├── services/
│   ├── ai_service.py
│   ├── ats_score.py
│   ├── pdf_reader.py
│   └── pdf_generator.py
├── generated/
├── main.py
└── requirements.txt
```
