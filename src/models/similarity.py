from sklearn.metrics.pairwise import cosine_similarity
from src.features.feature_engineering import build_tfidf_matrix

def calculate_similarity(resume_path, job_path):
    tfidf_matrix, vectorizer = build_tfidf_matrix(resume_path, job_path)

    # Resume is [0], Job description is [1]
    resume_vec = tfidf_matrix[0]
    job_vec = tfidf_matrix[1]

    similarity = cosine_similarity(resume_vec, job_vec)
    return similarity[0][0]  # single similarity score

if __name__ == "__main__":
    resume_file = "data/raw/resumes_sample.txt"
    job_file = "data/raw/job_descriptions_sample.txt"

    score = calculate_similarity(resume_file, job_file)
    print(f"Similarity Score: {score:.4f}")
