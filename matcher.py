# import pdfplumber
# import spacy
# from sklearn.feature_extraction.text import TfidfVectorizer
# from sklearn.metrics.pairwise import cosine_similarity

# nlp = spacy.load("en_core_web_sm")

# def extract_text_from_pdf(file):
#     with pdfplumber.open(file) as pdf:
#         text = ""
#         for page in pdf.pages:
#             page_text = page.extract_text()
#             if page_text:
#                 text += page_text
#     return text

# def preprocess(text):
#     doc = nlp(text.lower())
#     return ' '.join(token.lemma_ for token in doc if not token.is_stop and token.is_alpha)

# def match_resumes(job_desc, resume_texts):
#     documents = [preprocess(job_desc)] + [preprocess(resume) for resume in resume_texts]
#     vectorizer = TfidfVectorizer()
#     tfidf_matrix = vectorizer.fit_transform(documents)
#     job_vector = tfidf_matrix[0]
#     scores = cosine_similarity(job_vector, tfidf_matrix[1:])[0]
#     return scores
