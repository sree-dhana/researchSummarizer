from pathlib import Path

from langchain_community.vectorstores import FAISS


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DEFAULT_FAISS_DIR = PROJECT_ROOT / "data" / "faiss_index"


def _resolve_index_dir(persist_dir: str | Path | None = None) -> Path:
	return Path(persist_dir) if persist_dir else DEFAULT_FAISS_DIR


def create_vector_store(chunks, embeddings, persist_dir: str | Path | None = None):
	if not chunks:
		raise ValueError("Cannot create FAISS index from empty chunks.")

	index_dir = _resolve_index_dir(persist_dir)
	index_dir.mkdir(parents=True, exist_ok=True)

	vector_store = FAISS.from_documents(chunks, embeddings)
	vector_store.save_local(str(index_dir))
	return vector_store


def load_vector_store(embeddings, persist_dir: str | Path | None = None):
	index_dir = _resolve_index_dir(persist_dir)
	index_file = index_dir / "index.faiss"

	if not index_file.exists():
		raise FileNotFoundError(f"No FAISS index found at: {index_file}")

	return FAISS.load_local(
		str(index_dir),
		embeddings,
		allow_dangerous_deserialization=True,
	)


def get_or_create_vector_store(
	chunks,
	embeddings,
	persist_dir: str | Path | None = None,
	rebuild: bool = False,
):
	index_dir = _resolve_index_dir(persist_dir)
	index_file = index_dir / "index.faiss"

	if not rebuild and index_file.exists():
		return load_vector_store(embeddings, persist_dir=index_dir)

	return create_vector_store(chunks, embeddings, persist_dir=index_dir)
