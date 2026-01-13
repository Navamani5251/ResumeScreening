import streamlit as st
import pandas as pd
import numpy as np
import PyPDF2
import re

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -------------------- CONFIG --------------------
st.set_page_config(page_title="AI Resume Screening ATS", layout="wide")

# -------------------- SKILLS DATABASE --------------------
ROLE_SKILLS = {
    "Java Developer": [
        "java", "spring", "spring boot", "hibernate",
        "sql", "mysql", "rest api", "oops"
    ],
    "Python Developer": [
        "python", "django", "flask", "pandas",
        "numpy", "machine learning", "sql"
    ],
    "Data Analyst": [
        "excel", "sql", "python", "power bi",
        "tableau", "statistics", "pandas"
    ]
}

ROLE_JD = {
    "Java Developer": """
    We are looking for a Java Developer with strong knowledge of Java,
    OOP concepts, Spring Boot, REST APIs, SQL databases, and backend development.
    Experience with Hibernate and MySQL is a plus.
    """,

    "Python Developer": """
    Looking for a Python Developer skilled in Python, Flask or Django,
    data handling using Pandas and NumPy, and basic SQL knowledge.
    """,

    "Data Analyst": """
    Seeking a Data Analyst with skills in Excel, SQL, Python,
    data visualization using Power BI or Tableau, and statistics.
    """
}

# -------------------- FUNCTIONS --------------------

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.lower()


def extract_skills(text, skill_list):
    found = []
    for skill in skill_list:
        if re.search(r"\b" + re.escape(skill) + r"\b", text):
            found.append(skill)
    return found


def calculate_similarity(jd, resume):
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([jd, resume])
    similarity = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return similarity


def generate_verdict_summary(similarity, matched_skills, missing_skills, threshold=0.6):
    score = round(similarity * 100, 2)

    if similarity >= threshold:
        return (
            f"✅ **ACCEPTED**\n\n"
            f"The resume shows strong alignment with the job description "
            f"(Match Score: {score}%). The candidate possesses key required skills "
            f"such as {', '.join(matched_skills[:5])}."
        )

    summary = (
        f"❌ **REJECTED**\n\n"
        f"The resume was rejected due to a low job match score ({score}%). "
    )

    if missing_skills:
        summary += (
            f"Important required skills missing include: "
            f"{', '.join(missing_skills[:5])}. "
        )

    if not matched_skills:
        summary += "Very few relevant technical skills were identified. "

    summary += (
        "The candidate is advised to update the resume to better match "
        "the job requirements."
    )

    return summary


# -------------------- UI --------------------

st.title("🤖 AI-Powered Resume Screening System (ATS)")

st.subheader("📌 Select Job Role")
role = st.selectbox("Job Role", list(ROLE_JD.keys()))

jd_text = ROLE_JD[role]
required_skills = ROLE_SKILLS[role]

st.subheader("📄 Upload Resume (PDF only)")
resume_file = st.file_uploader("Upload Resume", type=["pdf"])

if resume_file:
    resume_text = extract_text_from_pdf(resume_file)

    similarity = calculate_similarity(jd_text, resume_text)

    matched_skills = extract_skills(resume_text, required_skills)
    missing_skills = list(set(required_skills) - set(matched_skills))

    status = "Accepted" if similarity >= 0.6 else "Rejected"

    # -------------------- RESULTS --------------------
    st.subheader("📊 Screening Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric("Match Score (%)", round(similarity * 100, 2))
        st.metric("Final Status", status)

    with col2:
        st.write("**Matched Skills**")
        st.success(", ".join(matched_skills) if matched_skills else "None")

        st.write("**Missing Skills**")
        st.error(", ".join(missing_skills) if missing_skills else "None")

    # -------------------- VERDICT SUMMARY --------------------
    st.subheader("🧠 Professional ATS Verdict")
    verdict = generate_verdict_summary(similarity, matched_skills, missing_skills)
    st.write(verdict)

    # -------------------- DOWNLOAD RESULT --------------------
    result_df = pd.DataFrame([{
        "Role": role,
        "Match Score (%)": round(similarity * 100, 2),
        "Matched Skills": ", ".join(matched_skills),
        "Missing Skills": ", ".join(missing_skills),
        "Final Status": status
    }])

    st.download_button(
        label="⬇ Download Screening Result (CSV)",
        data=result_df.to_csv(index=False),
        file_name="ATS_Result.csv",
        mime="text/csv"
    )
