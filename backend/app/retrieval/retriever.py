from app.vectorstore.faiss_store import FAISSStore
from app.services.ingestion_service import IngestionService
from app.core.logging import logger 
class Retriever:
    def __init__(self):
        self.store=FAISSStore()

        if self.store.exists():
            logger.info("Loading existing FAISS index")
            self.vectorstore=self.store.load()

        else:
            logger.info("Creating faiss index 1st time")
            ingestion=IngestionService()

            docs=ingestion.load_documents()
            chunks=ingestion.split_documents(docs)

            self.vectorstore=self.store.create(chunks)
            
    def retrieve(self,query:str,k:int=8):
        return self.vectorstore.similarity_search(query,k=k)
    