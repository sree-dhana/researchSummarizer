from langchain_community.embeddings import HuggingFaceBgeEmbeddings

def get_embedding_model():
    embeddings=HuggingFaceBgeEmbeddings(
        model_name="intfloat/e5-base-v2",
        model_kwargs={"device":"cuda"},
        encode_kwargs={"normalize_embeddings":True}
    )
    return embeddings
