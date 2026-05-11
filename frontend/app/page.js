"use client";

import { useState } from "react";

import axios from "axios";

import {
  Upload,
  FileText,
  Sparkles,
  Loader2,
  Download,
  CheckCircle2,
  AlertCircle,
} from "lucide-react";

import { motion } from "framer-motion";

import toast, { Toaster } from "react-hot-toast";

export default function Home() {
  const [jobDescription, setJobDescription] = useState("");

  const [resumeFile, setResumeFile] = useState(null);

  const [loading, setLoading] = useState(false);

  const [dashboard, setDashboard] = useState(null);

  async function analyzeJob() {
    if (!resumeFile || !jobDescription) {
      toast.error("Upload resume and job description");

      return;
    }

    try {
      setLoading(true);

      const formData = new FormData();

      formData.append("resume", resumeFile);

      formData.append("job_description", jobDescription);

      const response = await axios.post(
        `${process.env.NEXT_PUBLIC_API_URL}/generate-resume`,

        formData,

        {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        },
      );

      setDashboard(response.data);

      toast.success("Resume optimized successfully");
    } catch (error) {
      console.error(error);

      toast.error("Something went wrong");
    } finally {
      setLoading(false);
    }
  }

  return (
    <div className="min-h-screen bg-slate-50">
      <Toaster />

      {/* HERO */}

      <section className="max-w-6xl mx-auto px-6 py-16">
        <motion.div
          initial={{ opacity: 0, y: 40 }}
          animate={{ opacity: 1, y: 0 }}
          className="text-center"
        >
          <div className="inline-flex items-center gap-2 bg-blue-100 text-blue-700 px-4 py-2 rounded-full text-sm font-medium">
            <Sparkles size={16} />
            AI-Powered ATS Resume Optimizer
          </div>

          <h1 className="mt-6 text-5xl font-bold tracking-tight text-slate-900">
            Build a Recruiter-Ready Resume
          </h1>

          <p className="mt-6 text-lg text-slate-600 max-w-2xl mx-auto">
            Upload your existing resume and job description to generate a
            professional ATS-optimized CV.
          </p>
        </motion.div>

        {/* MAIN CARD */}

        <motion.div
          initial={{ opacity: 0, y: 30 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ delay: 0.2 }}
          className="mt-14 bg-white rounded-3xl shadow-xl border border-slate-200 p-8"
        >
          {/* Upload */}

          <div className="grid md:grid-cols-2 gap-8">
            <div>
              <label className="text-sm font-semibold text-slate-700">
                Upload Resume PDF
              </label>

              <div className="mt-3 border-2 border-dashed border-slate-300 rounded-2xl p-10 text-center hover:border-blue-500 transition">
                <Upload className="mx-auto text-slate-400" />

                <input
                  type="file"
                  accept=".pdf"
                  className="mt-4"
                  onChange={(e) => setResumeFile(e.target.files[0])}
                />

                <p className="mt-3 text-sm text-slate-500">PDF only</p>
              </div>
            </div>

            {/* Job Description */}

            <div>
              <label className="text-sm font-semibold text-slate-700">
                Job Description
              </label>

              <textarea
                rows={12}
                placeholder="Paste job description..."
                className="mt-3 w-full rounded-2xl border border-slate-300 p-4 outline-none focus:ring-2 focus:ring-blue-500"
                value={jobDescription}
                onChange={(e) => setJobDescription(e.target.value)}
              />
            </div>
          </div>

          {/* BUTTON */}

          <button
            onClick={analyzeJob}
            disabled={loading}
            className="mt-8 w-full bg-blue-600 hover:bg-blue-700 text-white py-4 rounded-2xl font-semibold transition flex items-center justify-center gap-3"
          >
            {loading ? (
              <>
                <Loader2 className="animate-spin" />
                Optimizing Resume...
              </>
            ) : (
              <>
                <Sparkles size={20} />
                Generate ATS Resume
              </>
            )}
          </button>
        </motion.div>

        {/* RESULTS */}

        {dashboard && (
          <motion.div
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            className="mt-12 grid lg:grid-cols-3 gap-6"
          >
            {/* ATS */}

            <div className="bg-white rounded-3xl shadow-lg p-6 border">
              <h2 className="text-xl font-bold">ATS Analysis</h2>

              <div className="mt-6 space-y-4">
                <div className="bg-slate-100 p-4 rounded-2xl">
                  <p className="text-sm text-slate-500">Previous ATS Score</p>

                  <h3 className="text-3xl font-bold">{dashboard.old_score}%</h3>
                </div>

                <div className="bg-green-100 p-4 rounded-2xl">
                  <p className="text-sm text-green-700">Optimized ATS Score</p>

                  <h3 className="text-3xl font-bold text-green-700">
                    {dashboard.new_score}%
                  </h3>
                </div>
              </div>
            </div>

            {/* Skills */}

            <div className="bg-white rounded-3xl shadow-lg p-6 border">
              <h2 className="text-xl font-bold">Skills Matched</h2>

              <div className="mt-6 flex flex-wrap gap-2">
                {dashboard.matched_skills.map((skill, index) => (
                  <span
                    key={index}
                    className="bg-blue-100 text-blue-700 px-3 py-2 rounded-full text-sm flex items-center gap-2"
                  >
                    <CheckCircle2 size={14} />

                    {skill}
                  </span>
                ))}
              </div>
            </div>

            {/* Missing */}

            <div className="bg-white rounded-3xl shadow-lg p-6 border">
              <h2 className="text-xl font-bold">Missing Skills</h2>

              <div className="mt-6 flex flex-wrap gap-2">
                {dashboard.missing_skills.map((skill, index) => (
                  <span
                    key={index}
                    className="bg-red-100 text-red-700 px-3 py-2 rounded-full text-sm flex items-center gap-2"
                  >
                    <AlertCircle size={14} />

                    {skill}
                  </span>
                ))}
              </div>
            </div>

            {/* DOWNLOAD */}

            <div className="lg:col-span-3 bg-white rounded-3xl shadow-lg p-8 border text-center">
              <FileText className="mx-auto text-blue-600" size={48} />

              <h2 className="mt-4 text-2xl font-bold">
                Optimized Resume Ready
              </h2>

              <p className="mt-2 text-slate-500">
                Download your ATS-friendly professional resume.
              </p>

              <a
                href={dashboard.download_url}
                target="_blank"
                className="inline-flex items-center gap-3 mt-6 bg-blue-600 hover:bg-blue-700 text-white px-8 py-4 rounded-2xl font-semibold transition"
              >
                <Download size={18} />
                Download Resume PDF
              </a>
            </div>
          </motion.div>
        )}
      </section>
    </div>
  );
}
