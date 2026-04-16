from pathlib import Path
from langchain_classic.chains import RetrievalQA
from backend.llm.model import get_llm


PROJECT_ROOT = Path(__file__).resolve().parents[2]
def create_rag_chain(retriever):
    llm=get_llm()
    qa_chain=RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True
    )

    return qa_chain