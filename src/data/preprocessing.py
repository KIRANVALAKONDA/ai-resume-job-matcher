import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download resources (first time only)
nltk.download("punkt")

nltk.download("stopwords")

def clean_text(text):
    """Lowercase + remove special characters"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def preprocess(text):
    """Clean + tokenize + remove stopwords"""
    text = clean_text(text)
    tokens = word_tokenize(text)
    tokens = [t for t in tokens if t not in stopwords.words("english")]
    return tokens

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    resume = load_file("data/raw/resumes_sample.txt")
    job = load_file("data/raw/job_descriptions_sample.txt")

    print("Resume tokens:\n", preprocess(resume)[:20])
    print("\nJob tokens:\n", preprocess(job)[:20])
