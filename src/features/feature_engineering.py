import os
from sklearn.feature_extraction.text import TfidfVectorizer
from src.data.preprocessing import clean_text, load_file

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer(max_features=500)

def build_tfidf_matrix(resume_path, job_path):
    resume_text = clean_text(load_file(resume_path))
    job_text = clean_text(load_file(job_path))

    documents = [resume_text, job_text]
    tfidf_matrix = vectorizer.fit_transform(documents)

    return tfidf_matrix, vectorizer

if __name__ == "__main__":
    resume_file = "data/raw/resumes_sample.txt"
    job_file = "data/raw/job_descriptions_sample.txt"

    tfidf_matrix, vectorizer = build_tfidf_matrix(resume_file, job_file)

    print("Vocabulary:", vectorizer.get_feature_names_out()[:20])
    print("\nTF-IDF Matrix:\n", tfidf_matrix.toarray())
