from flask import Blueprint, request, jsonify
from src.models.similarity import similarity_score
from src.data.preprocessing import clean_text

api = Blueprint("api", __name__)

@api.route("/match", methods=["POST"])
def match():
    data = request.get_json()
    resume_text = clean_text(data.get("resume_text", ""))
    job_text = clean_text(data.get("job_text", ""))

    # Convert to vectors using your saved TF-IDF
    from src.models.persistence import load_vectorizer
    vectorizer = load_vectorizer()
    vectors = vectorizer.transform([resume_text, job_text])

    score = similarity_score(vectors[0], vectors[1])
    return jsonify({"similarity_score": float(score)})