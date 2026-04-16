from pathlib import Path
from langchain_text_splitters import RecursiveCharacterTextSplitter

PROJECT_ROOT = Path(__file__).resolve().parents[2]

def chunk_documents(documents):
    splitter=RecursiveCharacterTextSplitter(
        chunk_size=800,
        chunk_overlap=150
    )

    chunks=splitter.split_documents(documents)

    return chunks