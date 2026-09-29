from dataclasses import dataclass
from .embeddings import EmbeddingService
from .vector_store import InMemoryVectorStore, VectorRecord

@dataclass(frozen=True)
class Document:
    id: str
    text: str

DOCUMENTS = [
    Document("rag", "RAG retrieves relevant context before generation and can reduce unsupported answers."),
    Document("evaluation", "AI evaluation should use fixed cases, explicit criteria, regression tests and documented limitations."),
    Document("api", "FastAPI provides a typed HTTP interface for serving Python application services."),
]

_embedding_service = EmbeddingService()
_store = InMemoryVectorStore([
    VectorRecord(document.id, document.text, _embedding_service.embed([document.text])[0])
    for document in DOCUMENTS
])

def retrieve(question: str, top_k: int = 2) -> list[Document]:
    query_vector = _embedding_service.embed([question])[0]
    ranked = _store.search(query_vector, top_k=top_k)
    return [Document(record.id, record.text) for score, record in ranked if score > 0.0]

def retrieve_scored(question: str, top_k: int = 2) -> list[tuple[float, Document]]:
    query_vector = _embedding_service.embed([question])[0]
    return [(score, Document(record.id, record.text)) for score, record in _store.search(query_vector, top_k=top_k)]
