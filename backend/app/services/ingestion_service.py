import os
from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from app.core.config import settings

class IngestionService:
    def load_documents(self):
        documents=[]
        for file in os.listdir(settings.PDF_DIR):
            if file.endswith(".pdf"):
                loader=PyMuPDFLoader(os.path.join(settings.PDF_DIR,file))
                documents.extend(loader.load())

        return documents
    def split_documents(self,documents):
        splitter=RecursiveCharacterTextSplitter(
            chunk_size=800,
            chunk_overlap=150
        )
        return splitter.split_documents(documents)