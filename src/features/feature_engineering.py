import os
from sklearn.feature_extraction.text import TfidfVectorizer
from src.data.preprocessing import clean_text, load_file


# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=500)


# 🔥 Boost important keywords by repeating them
def boost_keywords(text: str, keywords=None, factor=3):
    if not keywords:
        return text
    for kw in keywords:
        text += (" " + kw) * factor
    return text


# Build TF-IDF matrix from resume + job description
def build_tfidf_matrix(resume_path, job_path, keywords=None, factor=3):
    resume_text = clean_text(load_file(resume_path))
    job_text = clean_text(load_file(job_path))

    # Apply keyword boosting
    resume_text = boost_keywords(resume_text, keywords, factor)
    job_text = boost_keywords(job_text, keywords, factor)

    documents = [resume_text, job_text]
    tfidf_matrix = vectorizer.fit_transform(documents)

    return tfidf_matrix, vectorizer


if __name__ == "__main__":
    resume_file = "data/raw/resumes_sample.txt"
    job_file = "data/raw/job_descriptions_sample.txt"

    # Define important domain keywords
    keywords = ["python", "machine learning", "sql", "nlp", "flask"]

    tfidf_matrix, vectorizer = build_tfidf_matrix(
        resume_file, job_file, keywords, factor=3
    )

    print("Vocabulary:", vectorizer.get_feature_names_out())
    print("TF-IDF Matrix:\n", tfidf_matrix.toarray())