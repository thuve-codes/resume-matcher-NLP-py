import streamlit as st
import pdfplumber
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load spaCy model once
nlp = spacy.load("en_core_web_sm")

def extract_text_from_pdf(pdf_file):
    text = ""
    with pdfplumber.open(pdf_file) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text
    return text

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]
    return " ".join(tokens)

def match_resumes(job_desc, resume_texts):
    docs = [preprocess(job_desc)] + [preprocess(text) for text in resume_texts]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(docs)
    job_vec = tfidf_matrix[0]
    scores = cosine_similarity(job_vec, tfidf_matrix[1:])[0]
    return scores

def main():
    st.title("📄 Resume Scanner & Matcher")

    st.markdown("Paste your **Job Description** below and upload **Resume PDFs** to rank matching scores.")

    job_desc = st.text_area("Job Description", height=200)

    uploaded_files = st.file_uploader("Upload Resume PDFs", accept_multiple_files=True, type=["pdf"])

    if st.button("Match Resumes"):
        if not job_desc.strip():
            st.error("Please enter the Job Description.")
            return
        if not uploaded_files:
            st.error("Please upload at least one resume PDF.")
            return
        
        with st.spinner("Processing resumes..."):
            resume_texts = [extract_text_from_pdf(file) for file in uploaded_files]
            scores = match_resumes(job_desc, resume_texts)

            results = sorted(
                zip([file.name for file in uploaded_files], scores),
                key=lambda x: x[1],
                reverse=True,
            )

        st.success("Done! Here are the matching scores:")
        for filename, score in results:
            st.write(f"**{filename}** — Similarity Score: {score*100:.2f}%")

if __name__ == "__main__":
    main()
