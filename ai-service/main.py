import os
from typing import List, Dict
from fastapi import FastAPI
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(title="Resume AI Service", version="0.1.0")

class ExtractRequest(BaseModel):
    text: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/extract-skills")
def extract_skills(req: ExtractRequest) -> Dict[str, List[str]]:
    # Very simple keyword matcher for Week 2 stub
    keywords = {
        "python","django","fastapi","react","node","postgresql","aws",
        "docker","git","nlp","spacy","transformers","javascript","rest",
        "api","pandas","numpy","scikit-learn","machine learning","ml"
    }
    text = req.text.lower()
    found = sorted({k for k in keywords if k in text})
    return {"skills": found}
