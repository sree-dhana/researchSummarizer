from app.retrieval.retriever import Retriever

Retriever=Retriever()

docs=Retriever.retrieve("what is this paper about")

for d in docs:
    print(d.page_content[:200])