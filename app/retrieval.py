from dataclasses import dataclass
import re

@dataclass(frozen=True)
class Document:
    id: str
    text: str

DOCUMENTS = [
    Document("rag", "RAG retrieves relevant context before generation and can reduce unsupported answers."),
    Document("evaluation", "AI evaluation should use fixed cases, explicit criteria, regression tests and documented limitations."),
    Document("api", "FastAPI provides a typed HTTP interface for serving Python application services."),
]

def _terms(text: str) -> set[str]:
    return {term for term in re.findall(r"[a-zA-ZÀ-ÿ0-9]+", text.lower()) if len(term) > 2}

def retrieve(question: str, top_k: int = 2) -> list[Document]:
    terms = _terms(question)
    scored = []
    for document in DOCUMENTS:
        score = len(terms & _terms(document.text))
        scored.append((score, document))
    scored.sort(key=lambda item: (-item[0], item[1].id))
    return [doc for score, doc in scored[:top_k] if score > 0]
