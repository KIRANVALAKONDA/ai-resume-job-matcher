from flask import Blueprint, request, jsonify
from src.models.similarity import similarity_score, rank_resumes
from src.data.preprocessing import clean_text
from src.models.persistence import load_vectorizer
import pathlib

api = Blueprint("api", __name__)

@api.route("/match", methods=["POST"])
def match():
    """Compare a single resume to a job description and return similarity score."""
    data = request.get_json(force=True)
    resume_text = clean_text(data.get("resume_text", ""))
    job_text = clean_text(data.get("job_text", ""))

    # Convert to vectors using saved TF-IDF
    vectorizer = load_vectorizer()
    vectors = vectorizer.transform([resume_text, job_text])

    score = similarity_score(vectors[0], vectors[1])
    return jsonify({"similarity_score": float(score)})


@api.route("/rank", methods=["POST"])
def rank():
    """
    Rank multiple resumes against a job description.
    Expects:
    {
        "job_text": "...",
        "resumes": [
            {"name": "Alice", "text": "..."},
            {"name": "Bob", "text": "..."}
        ]
    }
    """
    data = request.get_json(force=True)
    job_text = data.get("job_text", "")
    resumes = data.get("resumes", [])

    # Create temp directory for ranking process
    tmpdir = pathlib.Path("data/tmp")
    tmpdir.mkdir(parents=True, exist_ok=True)

    # Save job description
    jobf = tmpdir / "job.txt"
    jobf.write_text(job_text, encoding="utf-8")

    # Save each resume as a separate file
    for r in resumes:
        (tmpdir / f"{r['name']}.txt").write_text(r["text"], encoding="utf-8")

    # Rank resumes
    results = rank_resumes(
        str(tmpdir / "*.txt").replace("\\", "/").replace("job.txt", "*"),
        str(jobf)
    )

    return jsonify({"results": results})