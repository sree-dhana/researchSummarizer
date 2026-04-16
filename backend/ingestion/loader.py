from pathlib import Path

from langchain_community.document_loaders import PyPDFDirectoryLoader


PROJECT_ROOT = Path(__file__).resolve().parents[2]
PAPERS_DIR = PROJECT_ROOT / "data" / "papers"

def load_papers():

    loader = PyPDFDirectoryLoader(str(PAPERS_DIR))
    documents = loader.load()

    return documents