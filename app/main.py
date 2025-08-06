from fastapi import FastAPI
from app.api.v1.endpoints import chat

app = FastAPI(
    title="Local AI Chatbot",
    version="1.0.0"
)

app.include_router(chat.router, prefix="/api/v1")
