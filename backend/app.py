from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from chatbot import get_response

app = FastAPI()

# Allow frontend to access backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {"message": "SkillNovus AI Backend Running"}

@app.get("/chat")
def chat(question: str):
    answer = get_response(question)
    return {"response": answer}