from pathlib import Path 
from langchain_ollama import ChatOllama

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def get_llm():
    llm=ChatOllama(
        model="mistral",
        temperature=0.3
    )
    return llm
