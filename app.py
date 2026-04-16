from backend.ingestion.loader import load_papers
from backend.ingestion.chunker import chunk_documents
from backend.ingestion.embeddings import get_embedding_model
from vectorstore.faiss_store import get_or_create_vector_store
from backend.retrieval.retriever import create_retriever
from backend.rag.rag_chain import create_rag_chain

print("Loading papers...")
documents = load_papers()

print("Chunking documents...")
chunks = chunk_documents(documents)

print("Loading embedding model...")
embeddings = get_embedding_model()

print("Creating vector database...")
vector_store = get_or_create_vector_store(chunks, embeddings, rebuild=False)

retriever = create_retriever(vector_store)

qa_chain = create_rag_chain(retriever)
while True:

    query = input("\nAsk a research question: ")

    result = qa_chain.invoke({"query": query})

    print("\nAnswer:")
    print(result["result"])

    print("\nSources:")
    for doc in result["source_documents"]:
        print(doc.metadata)