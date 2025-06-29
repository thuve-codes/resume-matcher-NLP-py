# 📄 Resume Matcher (Streamlit App)

This is a smart Resume Scanner & Matcher tool built with **Streamlit**, **spaCy**, and **scikit-learn**. It allows you to upload multiple resume PDFs and compare them against a job description using **TF-IDF vectorization** and **cosine similarity**, then ranks the resumes based on match score.

---

## 🚀 Features

- 📥 Upload multiple resume PDFs
- 📄 Paste a custom job description
- ⚡ Preprocess text using NLP (spaCy)
- 📊 Score and rank resumes based on textual similarity
- 🖥️ Clean, interactive Streamlit UI

---

## 🧠 Tech Stack

- **Python 3.8+**
- [Streamlit](https://streamlit.io/)
- [spaCy](https://spacy.io/)
- [scikit-learn](https://scikit-learn.org/)
- [pdfplumber](https://github.com/jsvine/pdfplumber)

---

## 🔧 How to Run

1. **Clone the repo**

```bash
git clone https://github.com/yourusername/resume-matcher.git
cd resume-matcher

python -m venv venv
venv\Scripts\activate     # On Windows
source venv/bin/activate  # On macOS/Linux

pip install -r requirements.txt
python -m spacy download en_core_web_sm

streamlit run app.py


---
