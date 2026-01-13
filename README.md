# 🤖 AI-Powered Resume Screening System (ATS)

An AI-driven Applicant Tracking System (ATS) developed using **Python, Natural Language Processing (NLP), and Machine Learning** to automate resume screening against role-based job descriptions. This project demonstrates how NLP techniques can be applied to real-world recruitment problems by providing accurate, transparent, and explainable resume evaluations.

---

## 👤 Author

**Navamani Kandan**  
Undergraduate Student  
V.S.B. College of Engineering Technical Campus  

---

## 📌 Project Overview

Manual resume screening is time-consuming and often inconsistent. This system automates the process by analyzing resumes, extracting relevant skills, measuring similarity with job descriptions, and generating a professional verdict explaining why a resume is accepted or rejected. The goal is to simulate how modern ATS platforms assist recruiters in shortlisting candidates efficiently.

---

## ✨ Key Features

- 📄 Upload resumes in **PDF format**
- 🎯 Role-based job descriptions (Java Developer, Python Developer, Data Analyst)
- 🧠 Resume–job matching using **TF-IDF and Cosine Similarity**
- 🛠️ Automatic **skill extraction and skill gap analysis**
- 📝 **Explainable AI verdict** with acceptance/rejection reasons
- 📊 Match score and final screening status
- 📥 Downloadable screening report (CSV)
- ⚡ Interactive web interface using Streamlit

---

## 🧪 Technologies Used

- Python  
- Streamlit  
- Scikit-learn  
- PyPDF2  
- Pandas  
- NumPy  
- Natural Language Processing (NLP)

---

## 🔍 How the System Works

1. Select a job role  
2. Upload a resume in PDF format  
3. Text is extracted from the resume  
4. TF-IDF converts text into numerical vectors  
5. Cosine similarity calculates the match score  
6. Skills are compared to identify gaps  
7. A final verdict with explanation is generated  

---

## ▶️ Installation & Execution

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Navamani5251/ResumeScreening/
cd ResumeScreening
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Run the Application
bash
Copy code
streamlit run app.py
📂 Project Structure
lua
Copy code
ai-resume-ats/
│── app.py
│── requirements.txt
│── README.md
│── .gitignore
🎯 Use Cases
Automated resume shortlisting

Skill gap identification

Internship and placement screening demos

Academic AI/ML project submissions

🚀 Future Enhancements
Recruiter login system

Resume improvement suggestions

Online deployment

Advanced NLP-based skill extraction

🎓 Academic & Career Relevance
This project demonstrates practical skills in NLP, Machine Learning, Explainable AI, and Streamlit deployment, making it suitable for academic evaluation, internships, and placement portfolios.

📜 License
This project is intended for educational and demonstration purposes only.
