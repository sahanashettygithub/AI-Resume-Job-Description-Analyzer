import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

print("API key loaded:", bool(GOOGLE_API_KEY))

import streamlit as st

from resume_parser import extract_resume_text
from analyzer import analyze_resume


# Page configuration
st.set_page_config(
    page_title="AI Resume & JD Analyzer",
    page_icon="📄",
    layout="wide"
)


# Title
st.title("📄 AI Resume & Job Description Analyzer")

st.write(
    "Upload your resume and paste a job description "
    "to analyze your resume using Generative AI."
)

st.divider()


# Upload and Job Description
col1, col2 = st.columns(2)


with col1:

    st.subheader("📄 Resume")

    resume_file = st.file_uploader(
        "Upload your resume PDF",
        type=["pdf"]
    )


with col2:

    st.subheader("💼 Job Description")

    job_description = st.text_area(
        "Paste the job description here",
        height=300,
        placeholder="Paste the complete job description..."
    )


st.divider()


# Analyze button
if st.button("🚀 Analyze Resume", use_container_width=True):

    if resume_file is None:

        st.error("Please upload your resume.")

    elif not job_description.strip():

        st.error("Please paste the job description.")

    elif not GOOGLE_API_KEY:

        st.error("Gemini API key is not configured.")

    else:

        with st.spinner("Analyzing your resume..."):

            try:

                # Extract resume text
                resume_text = extract_resume_text(resume_file)

                # Analyze resume
                result = analyze_resume(
                    resume_text,
                    job_description
                )

                st.success("Analysis completed!")

                st.divider()


                # Match Score
                st.subheader("🎯 Resume Match Score")

                score = result["match_score"]

                st.metric(
                    label="Overall Match",
                    value=f"{score}%"
                )

                st.progress(score / 100)


                # Summary
                st.subheader("📝 Summary")

                st.write(result["summary"])


                # Matching and Missing Skills
                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("✅ Matching Skills")

                    for skill in result["matching_skills"]:
                        st.success(skill)


                with col2:

                    st.subheader("⚠️ Missing Skills")

                    for skill in result["missing_skills"]:
                        st.warning(skill)


                # Keywords
                col1, col2 = st.columns(2)

                with col1:

                    st.subheader("🔑 Matching Keywords")

                    for keyword in result["matching_keywords"]:
                        st.write(f"• {keyword}")


                with col2:

                    st.subheader("🔎 Missing Keywords")

                    for keyword in result["missing_keywords"]:
                        st.write(f"• {keyword}")


                # Experience
                st.subheader("💼 Experience Match")

                st.write(result["experience_match"])


                # Education
                st.subheader("🎓 Education Match")

                st.write(result["education_match"])


                # Improvements
                st.subheader("💡 Resume Improvements")

                for improvement in result["improvements"]:
                    st.info(improvement)


                # Interview Questions
                st.subheader("🎤 Possible Interview Questions")

                for i, question in enumerate(
                    result["interview_questions"],
                    1
                ):

                    st.write(f"**{i}.** {question}")


            except Exception as e:

                st.error(
                    f"Something went wrong while analyzing the resume: {e}"
                )