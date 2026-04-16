import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from backend.ingestion.embeddings import get_embedding_model

embeddings=get_embedding_model()

vector=embeddings.embed_query("what is transformer architecture")

print("vector length",len(vector))
print(vector[:10])