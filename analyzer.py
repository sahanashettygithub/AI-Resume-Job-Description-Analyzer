import os
import json

from dotenv import load_dotenv
import google.generativeai as genai


# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("Analyzer API key loaded:", bool(GOOGLE_API_KEY))


# Configure Gemini
if not GOOGLE_API_KEY:
    raise ValueError("GOOGLE_API_KEY is not configured.")

genai.configure(api_key=GOOGLE_API_KEY)


# Gemini model
model = genai.GenerativeModel("gemini-2.5-flash")


def analyze_resume(resume_text, job_description):

    prompt = f"""
You are an expert ATS resume analyzer and technical recruiter.

Analyze the candidate's resume against the provided job description.

RESUME:
{resume_text}

JOB DESCRIPTION:
{job_description}

Return ONLY valid JSON using exactly this structure:

{{
    "match_score": 0,
    "summary": "",
    "matching_skills": [],
    "missing_skills": [],
    "matching_keywords": [],
    "missing_keywords": [],
    "experience_match": "",
    "education_match": "",
    "improvements": [],
    "interview_questions": []
}}

Rules:

1. match_score must be an integer between 0 and 100.
2. matching_skills should contain skills clearly present in the resume and relevant to the job.
3. missing_skills should contain important skills from the job description that are not clearly demonstrated in the resume.
4. Do not invent experience.
5. Be realistic about the candidate's qualifications.
6. improvements should be specific and actionable.
7. Generate 5 interview questions relevant to the job.
8. Return ONLY JSON.
"""

    response = model.generate_content(prompt)

result = response.text.strip()

# Remove Markdown code fences
if result.startswith("```"):
    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

try:
    return json.loads(result)

except json.JSONDecodeError:
    # Try to extract the JSON object
    start = result.find("{")
    end = result.rfind("}") + 1

    if start != -1 and end != 0:
        result = result[start:end]

    return json.loads(result)
