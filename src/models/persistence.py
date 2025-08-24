import joblib

def save_vectorizer(vec, path="models/tfidf_vectorizer.joblib"):
    joblib.dump(vec, path)

def load_vectorizer(path="models/tfidf_vectorizer.joblib"):
    return joblib.load(path)
