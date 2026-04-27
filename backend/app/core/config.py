import os
from dotenv import load_dotenv

load_dotenv()


class Settings:
    def __init__(self):
        self.MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

        if not self.MISTRAL_API_KEY:
            raise ValueError(
                "MISTRAL_API_KEY is missing in .env file"
            )

        self.MODEL_NAME = os.getenv(
            "MODEL_NAME",
            "mistral-large"
        )

        self.EMBEDDING_MODEL = os.getenv(
            "EMBEDDING_MODEL",
            "all-MiniLM-L6-v2"
        )

        self.FAISS_INDEX_PATH = os.getenv(
            "FAISS_INDEX_PATH",
            "./faiss_index"
        )

        self.PDF_DIR = os.getenv(
            "PDF_DIR",
            "./data/raw"
        )


settings = Settings()