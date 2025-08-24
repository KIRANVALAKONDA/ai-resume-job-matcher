from flask import Flask, request, jsonify, send_from_directory
import os

def create_app():
    # Serve static files from ../web
    app = Flask(__name__, static_folder="../web", static_url_path="")

    # Home page (serves index.html)
    @app.get("/")
    def home_page():
        return send_from_directory(app.static_folder, "index.html")

    # Simple keyword-based match API
    @app.route('/match', methods=['POST'])
    def match():
        data = request.get_json(force=True)
        resume_text = data.get('resume_text', '')
        job_text = data.get('job_text', '')

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

    # Register other API blueprints if needed
    from src.routes.api import api
    app.register_blueprint(api)

    return app

if __name__ == "__main__":
    # Run directly for development
    create_app().run(host='127.0.0.1', port=5000, debug=True)