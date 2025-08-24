from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/match', methods=['POST'])
def match():
    data = request.get_json()
    resume_text = data.get('resume_text', '')
    job_text = data.get('job_text', '')
    
    # Simple keyword-based match score
    resume_words = set(resume_text.lower().split())
    job_words = set(job_text.lower().split())
    common_words = resume_words.intersection(job_words)
    
    score = len(common_words) / max(len(job_words), 1)
    
    return jsonify({
        'resume_text': resume_text,
        'job_text': job_text,
        'match_score': round(score, 2),
        'common_words': list(common_words)
    })

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)