import os
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from app.core.config import settings

class FAISSStore:
    def __init__(self):
        self.embeddings=HuggingFaceBgeEmbeddings(
            model_name=settings.EMBEDDING_MODEL
        )
        self.index_path=settings.FAISS_INDEX_PATH

    def exists(self):
        return os.path.exists(self.index_path)
    
    def load(self):
        return FAISS.load_local(self.index_path,self.embeddings,allow_dangerous_deserialization=True)
    
    def save(self,vectorstore):
        vectorstore.save_local(self.index_path)
    
    def create(self,documents):
        vectorstore=FAISS.from_documents(documents,self.embeddings)
        self.save(vectorstore)
        return vectorstore