from fastapi import FastAPI
from app.api.v1.endpoints import chat
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Local AI Chatbot",
    version="1.0.0"
)

app.include_router(chat.router, prefix="/api/v1")


#add cors configurations
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
