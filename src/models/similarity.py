import glob, os
from sklearn.metrics.pairwise import cosine_similarity
from src.features.feature_engineering import TfidfVectorizer, clean_text, load_file

def rank_resumes(resume_glob, job_path):
    job_text = clean_text(load_file(job_path))
    resume_files = sorted(glob.glob(resume_glob))
    docs = [clean_text(load_file(r)) for r in resume_files]
    docs.append(job_text)
    vec = TfidfVectorizer(max_features=1000, ngram_range=(1,2))
    X = vec.fit_transform(docs)
    job_vec = X[-1]
    scores = []
    for i, rf in enumerate(resume_files):
        score = float(cosine_similarity(X[i], job_vec)[0][0])
        scores.append((os.path.basename(rf), score))
    return sorted(scores, key=lambda x: x[1], reverse=True)

if __name__ == "__main__":
    results = rank_resumes("data/raw/resumes/*.txt", "data/raw/job_descriptions_sample.txt")
    print(results)
