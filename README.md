# AI-Powered Resume & Job Matcher 🚀

An AI-powered platform that analyzes resumes (NLP) and matches them with job postings.

---

## ✨ Features
- Upload resumes (PDF/DOCX) → extract skills & experience (NLP)
- Recruiters post jobs with required skills
- Matching engine ranks jobs for each resume
- React frontend + Django REST API + FastAPI AI microservice
- PostgreSQL DB (local Docker or AWS RDS)

---

## 🛠 Tech Stack
**Frontend:** React (CRA) + Axios  
**Backend:** Django + Django REST Framework + CORS  
**AI/NLP:** FastAPI + spaCy + Transformers  
**DB:** PostgreSQL  
**Infra:** Docker Compose (dev), AWS (prod)

---

## ⚡ Quickstart (Local, without Docker)
1. Create `.env` from template:
   ```bash
   cp backend/.env.example backend/.env
   ```
2. Start PostgreSQL (localhost:5432) and update `backend/.env` if needed.
3. Backend:
   ```bash
   cd backend
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   python manage.py migrate
   python manage.py runserver
   ```
   API: http://127.0.0.1:8000/test/
4. AI service:
   ```bash
   cd ai-service
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   uvicorn main:app --reload --port 8001
   ```
   Health: http://127.0.0.1:8001/health

---

## 🐳 Quickstart (Docker)
1. Provide env files:
   ```bash
   cp backend/.env.example backend/.env
   cp ai-service/.env.example ai-service/.env
   ```
2. Run all services:
   ```bash
   docker-compose up --build
   ```
   - Django → http://127.0.0.1:8000/test/
   - FastAPI → http://127.0.0.1:8001/health
   - PostgreSQL → localhost:5432

---

## 📅 4-Week Roadmap

### Week 1: Setup & Foundations
- Repo, README, .gitignore
- Django + DRF + CORS + Postgres
- AI FastAPI scaffold
- Test endpoints + Postman

### Week 2: Models + Upload + AI
- Models: User, Job, Resume
- Resume upload API
- `/extract-skills` integration
- React upload page (CRA)

### Week 3: Matching + Dashboards + Auth
- Matching engine + `/api/match`
- Candidate & Recruiter dashboards
- JWT auth

### Week 4: Deploy + CI/CD
- AWS RDS + EC2 + S3 + CloudFront
- GitHub Actions for CI/CD
- Docs & Postman collection

---

## Project Structure
```
resume-job-matcher/
├── backend/           # Django backend
├── ai-service/        # FastAPI microservice
├── docker-compose.yml
└── README.md
```

---

## License
MIT
