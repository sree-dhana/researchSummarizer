from fastapi import APIRouter,Depends
from pydantic import BaseModel, Field
from app.services.rag_service import RAGService
from app.api.dependencies import get_rag_service

router=APIRouter()

rag_service=RAGService()

class ChatRequest(BaseModel):
    question: str = Field(..., min_length=3)

@router.post("/ask")
def ask_questions(request: ChatRequest,rag_service:RAGService=Depends(get_rag_service)):
    return rag_service.answer(request.question)
