from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

HF_API_TOKEN = "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"

API_URL = "https://router.huggingface.co/hf-inference/models/google/flan-t5-large"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json"
}


class CodeRequest(BaseModel):
    code: str


@app.get("/")
def home():
    return {"message": "AI Code Reviewer running"}


@app.post("/review")
async def review_code(req: CodeRequest):

    prompt = f"""
    Review this code and give:
    - bad practices
    - security issues
    - refactoring suggestions
    - complexity score

    Code:
    {req.code}
    """

    payload = {
        "inputs": prompt
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    return {"review": response.text}