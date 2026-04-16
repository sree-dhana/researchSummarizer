from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]
def create_retriever(vector_store):

    retriever=vector_store.as_retriever(
        search_kwargs={"k":4}
    )
    return retriever