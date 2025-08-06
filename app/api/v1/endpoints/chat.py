from fastapi import APIRouter
from app.schemas.chat_schema import ChatRequest,ChatResponse
from app.services.chat_service import get_chatbot_response

router=APIRouter()

@router.post("/chat",response_model=ChatResponse)
def chat(request:ChatRequest):
    reply=get_chatbot_response(request.message)
    return ChatResponse(response=reply)