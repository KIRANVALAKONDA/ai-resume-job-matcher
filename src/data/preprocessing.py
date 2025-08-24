import re

def clean_text(text):
    """Basic text cleaning"""
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    return text

def load_file(path):
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

if __name__ == "__main__":
    resume = load_file("data/raw/resumes_sample.txt")
    job = load_file("data/raw/job_descriptions_sample.txt")

    print("Clean Resume:\n", clean_text(resume)[:200])
    print("\nClean Job:\n", clean_text(job)[:200])
