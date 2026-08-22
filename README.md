# 📄 AI Resume & Job Description Analyzer

An AI-powered web application that analyzes a candidate's resume against a given Job Description (JD) using Generative AI.

The application extracts information from a resume PDF, compares it with the provided job description, and generates an easy-to-understand analysis including a **resume match score, matching skills, missing skills, keywords, experience match, education match, improvement suggestions, and potential interview questions**.

🔗 **Live Demo:** https://ai-resume-job-description-analyzer-tc46c6qf4vgowvkrrqbrok.streamlit.app/

---

## 🚀 Features

* 📄 Upload a resume in PDF format
* 💼 Paste any Job Description
* 🤖 AI-powered resume analysis using Google Gemini
* 🎯 Generates an overall resume-to-JD match score
* ✅ Identifies matching skills
* ⚠️ Identifies missing skills
* 🔑 Extracts matching and missing keywords
* 💼 Evaluates experience compatibility
* 🎓 Evaluates education compatibility
* 💡 Provides personalized resume improvement suggestions
* 🎤 Generates potential interview questions
* 🌐 Deployed using Streamlit

---

## 🧠 How It Works

The application follows a simple AI-powered document analysis pipeline:

<img width="1472" height="1200" alt="image" src="https://github.com/user-attachments/assets/24402a3c-d933-45c3-804d-423787f78290" />


## 🛠️ Tech Stack

### Frontend / UI

* Streamlit

### Programming Language

* Python

### Generative AI

* Google Gemini API

### Document Processing

* PDF text extraction

### AI Application

* Prompt Engineering
* LLM-based document analysis
* Resume-JD semantic comparison

### Deployment

* Streamlit Community Cloud

### Version Control

* Git
* GitHub

---

## 📁 Project Structure

```text
AI-Resume-JD-Analyzer/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
└── .streamlit/
    └── secrets.toml
```

> **Note:** `secrets.toml` should never be committed to GitHub because it contains your API credentials.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/AI-Resume-JD-Analyzer.git
```

### 2. Navigate to the project

```bash
cd AI-Resume-JD-Analyzer
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

#### Windows

```bash
venv\Scripts\activate
```

#### macOS / Linux

```bash
source venv/bin/activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 API Configuration

This project uses the **Google Gemini API** for Generative AI analysis.

For local development, configure your API key through Streamlit secrets.

Create:

```text
.streamlit/secrets.toml
```

and add:

```toml
GOOGLE_API_KEY = "your_api_key_here"
```

Do **not** upload this file to GitHub.

Your `.gitignore` should contain:

```text
venv/
.env
.streamlit/secrets.toml
__pycache__/
*.pyc
```

---

## ▶️ Run the Application

Start the Streamlit application with:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📊 Example Analysis

The analyzer can generate results such as:

```text
Resume Match Score: 95%

Matching Skills:
✓ Python
✓ Machine Learning
✓ Generative AI
✓ NLP
✓ PyTorch
✓ LangChain
✓ RAG
✓ Azure AI

Missing Skills:
⚠ Advanced MLOps

Experience Match:
✓ Strong match for fresher / 0–1 year requirement

Education Match:
✓ Relevant Bachelor's degree

Resume Improvements:
• Add measurable project achievements
• Highlight deployment experience
• Improve production-related keywords

Interview Questions:
• Explain your RAG implementation.
• How would you evaluate an ML model?
• How would you deploy an AI application?
```

---

## 🎯 Use Cases

This application can help:

* Students evaluate resumes before applying
* Fresh graduates identify skill gaps
* Job seekers tailor resumes to specific job descriptions
* Candidates prepare for technical interviews
* Developers experiment with LLM-powered document analysis

---

## 🔮 Future Improvements

Potential future enhancements include:

* 🔍 RAG-based resume retrieval
* 📚 Vector database integration
* 🧠 Semantic similarity scoring
* 📊 Skill-match visualizations
* 📄 ATS-friendly resume suggestions
* 🔄 Multiple resume comparison
* 🎯 Job-specific resume recommendations
* 📈 Resume scoring history
* 🐳 Docker-based deployment
* ⚙️ Production monitoring and logging

---

## 🧩 RAG Extension

A future version can implement **Retrieval-Augmented Generation (RAG)**.

The architecture could become:

```text
Resume PDF
    ↓
Text Extraction
    ↓
Chunking
    ↓
Embeddings
    ↓
Vector Database
    ↓
Relevant Resume Sections
    ↓
Job Description + Retrieved Context
    ↓
Gemini
    ↓
Detailed Analysis
```

This would allow the system to retrieve the most relevant sections of a resume before generating the final analysis.

---

## 🔒 Security

* API keys are stored using environment variables or Streamlit secrets.
* Sensitive credentials are excluded from Git using `.gitignore`.
* API keys should never be hardcoded in source files.
* Uploaded resumes should be handled carefully because they may contain personal information.

---

## 🌐 Deployment

The application can be deployed using **Streamlit Community Cloud**.

General deployment flow:

```text
GitHub Repository
       ↓
Streamlit Community Cloud
       ↓
Configure Secrets
       ↓
Deploy
       ↓
Public Application URL
```

---

## 📌 Project Highlights

This project demonstrates practical experience with:

* Generative AI
* Large Language Models
* Prompt Engineering
* Python
* Streamlit
* PDF Processing
* Natural Language Processing
* Resume-JD Semantic Analysis
* API Integration
* Cloud Deployment
* Git/GitHub

---

## 👩‍💻 Author

**Sahana Shetty**

B.Tech Information Technology
Generative AI & Deep Learning Enthusiast

* GitHub: https://github.com/sahanashettygithub
* LinkedIn: https://www.linkedin.com/in/sahana-shetty-/

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub!
