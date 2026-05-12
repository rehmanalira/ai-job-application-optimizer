"use client";

import { useState } from "react";
import axios from "axios";

export default function Home() {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    location: "",

    linkedin: "",
    github: "",

    experience: "",
    projects: "",
    education: "",
    skills: "",

    job_description: "",
  });

  const [loading, setLoading] = useState(false);

  const [error, setError] = useState("");

  const [result, setResult] = useState(null);

  function handleChange(e) {
    setFormData({
      ...formData,

      [e.target.name]: e.target.value,
    });
  }

  function validateForm() {
    if (!formData.name.trim()) {
      return "Full Name is required";
    }

    if (!formData.email.trim()) {
      return "Email is required";
    }

    if (!formData.phone.trim()) {
      return "Phone Number is required";
    }

    if (!formData.location.trim()) {
      return "Location is required";
    }

    if (!formData.job_description.trim()) {
      return "Job Description is required";
    }

    return null;
  }

  async function generateResume() {
    const validationError = validateForm();

    if (validationError) {
      setError(validationError);

      return;
    }

    try {
      setLoading(true);

      setError("");

      setResult(null);

      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/generate-resume`,

        formData,
      );

      setResult(response.data);
    } catch (err) {
      console.log(err);

      setError(err?.response?.data?.detail || "Failed to generate resume");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="min-h-screen bg-gradient-to-br from-slate-950 via-slate-900 to-black text-white">
      <div className="max-w-7xl mx-auto px-4 py-10">
        <div className="text-center mb-12">
          <div className="inline-block bg-blue-500/10 border border-blue-500/30 px-6 py-2 rounded-full mb-6">
            <span className="text-blue-400 font-medium">
              AI Powered ATS Resume Generator
            </span>
          </div>

          <h1 className="text-5xl md:text-7xl font-black leading-tight">
            Build a<span className="text-blue-500"> 10/10 ATS </span>
            Resume
          </h1>

          <p className="text-slate-400 mt-6 text-lg max-w-3xl mx-auto leading-relaxed">
            Generate beautiful, professional and recruiter-ready resumes
            tailored perfectly to any job description using AI.
          </p>
        </div>

        <div className="grid lg:grid-cols-3 gap-8">
          <div className="lg:col-span-2 bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-3xl p-8 shadow-2xl">
            <div className="mb-8">
              <h2 className="text-3xl font-bold mb-2">Candidate Information</h2>

              <p className="text-slate-400">
                Fill your professional information carefully.
              </p>
            </div>

            <div className="grid md:grid-cols-2 gap-6">
              <Input
                label="Full Name *"
                name="name"
                placeholder="Muhammad Abdur Rehman"
                handleChange={handleChange}
              />

              <Input
                label="Email *"
                name="email"
                placeholder="your@email.com"
                handleChange={handleChange}
              />

              <Input
                label="Phone Number *"
                name="phone"
                placeholder="+44 7400 000000"
                handleChange={handleChange}
              />

              <Input
                label="Location *"
                name="location"
                placeholder="London, UK"
                handleChange={handleChange}
              />

              <Input
                label="LinkedIn"
                name="linkedin"
                placeholder="linkedin.com/in/username"
                handleChange={handleChange}
              />

              <Input
                label="GitHub"
                name="github"
                placeholder="github.com/username"
                handleChange={handleChange}
              />
            </div>

            <TextArea
              label="Professional Experience"
              name="experience"
              placeholder="Write your experience with proper company names..."
              handleChange={handleChange}
            />

            <TextArea
              label="Projects"
              name="projects"
              placeholder="Describe your best projects..."
              handleChange={handleChange}
            />

            <TextArea
              label="Education"
              name="education"
              placeholder="Your degrees, university etc..."
              handleChange={handleChange}
            />

            <TextArea
              label="Skills"
              name="skills"
              placeholder="Laravel, PHP, React, PostgreSQL, AWS..."
              handleChange={handleChange}
            />

            <TextArea
              label="Job Description *"
              name="job_description"
              placeholder="Paste the complete job description here..."
              handleChange={handleChange}
              height="h-64"
            />

            {error && (
              <div className="mt-6 bg-red-500/10 border border-red-500/40 p-4 rounded-2xl text-red-300">
                {error}
              </div>
            )}

            <button
              onClick={generateResume}
              disabled={loading}
              className="w-full mt-8 bg-blue-600 hover:bg-blue-700 transition-all duration-300 py-5 rounded-2xl text-lg font-bold shadow-lg shadow-blue-600/20 disabled:opacity-50"
            >
              {loading
                ? "Generating Professional Resume..."
                : "Generate ATS Resume"}
            </button>
          </div>

          <div className="space-y-6">
            <div className="bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-3xl p-8">
              <h3 className="text-2xl font-bold mb-6">Features</h3>

              <ul className="space-y-4 text-slate-300">
                <li>✓ ATS Optimized Resume</li>
                <li>✓ AI Tailored Content</li>
                <li>✓ Recruiter Friendly Format</li>
                <li>✓ Professional PDF Export</li>
                <li>✓ Real ATS Keyword Matching</li>
                <li>✓ Modern Resume Structure</li>
              </ul>
            </div>

            {result && (
              <div className="bg-slate-900/80 backdrop-blur-xl border border-slate-800 rounded-3xl p-8">
                <h3 className="text-2xl font-bold mb-8">ATS Dashboard</h3>

                <div className="space-y-6">
                  <div className="bg-slate-950 p-6 rounded-2xl">
                    <p className="text-slate-400 mb-2">Previous ATS Score</p>

                    <h2 className="text-5xl font-black text-red-400">
                      {result.old_score}%
                    </h2>
                  </div>

                  <div className="bg-slate-950 p-6 rounded-2xl">
                    <p className="text-slate-400 mb-2">Optimized ATS Score</p>

                    <h2 className="text-5xl font-black text-green-400">
                      {result.new_score}%
                    </h2>
                  </div>

                  <a
                    href={result.download_url}
                    target="_blank"
                    className="block w-full text-center bg-green-600 hover:bg-green-700 py-4 rounded-2xl text-lg font-bold transition-all duration-300"
                  >
                    Download Resume PDF
                  </a>
                </div>
              </div>
            )}
          </div>
        </div>
      </div>
    </main>
  );
}

function Input({ label, name, placeholder, handleChange }) {
  return (
    <div>
      <label className="block mb-2 text-sm text-slate-300">{label}</label>

      <input
        type="text"
        name={name}
        placeholder={placeholder}
        onChange={handleChange}
        className="w-full bg-slate-800 border border-slate-700 focus:border-blue-500 p-4 rounded-2xl outline-none transition-all"
      />
    </div>
  );
}

function TextArea({ label, name, placeholder, handleChange, height = "h-36" }) {
  return (
    <div className="mt-6">
      <label className="block mb-2 text-sm text-slate-300">{label}</label>

      <textarea
        name={name}
        placeholder={placeholder}
        onChange={handleChange}
        className={`w-full bg-slate-800 border border-slate-700 focus:border-blue-500 p-4 rounded-2xl outline-none transition-all ${height}`}
      />
    </div>
  );
}
