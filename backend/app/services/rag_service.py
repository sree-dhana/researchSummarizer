from app.retrieval.retriever import Retriever 
from app.llm.router import LLMRouter

class RAGService:
    def __init__(self):
        self.retriever=Retriever()
        self.llm=LLMRouter().get_reasoning_llm()

    def answer(self,query: str):
        docs=self.retriever.retrieve(query)

        context = "\n\n---\n\n".join([
        doc.page_content for doc in docs
        ])
        print("=== CONTEXT ===")
        print(context[:1000])
        unique_sources = []
        seen = set()
        for doc in docs:
            key = (doc.metadata.get("source"), doc.metadata.get("page"))
            if key not in seen:
                seen.add(key)
                unique_sources.append(doc.metadata)
        prompt=f"""
You are a precise research assistant.

STRICT RULES:
- Answer ONLY using the given context
- DO NOT guess or assume
- DO NOT use words like "likely", "suggests", "probably"
- If information is incomplete, say exactly what is missing
- Quote or paraphrase clearly from context

Context:
{context}

Question:
{query}

Answer:
"""
        response=self.llm.generate(prompt)
        return{
            "answer":response,
            "sources":unique_sources
        }
