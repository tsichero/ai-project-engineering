from dataclasses import dataclass

@dataclass(frozen=True)
class Document:
    id: str
    text: str

DOCUMENTS = [
    Document("rag", "RAG retrieves relevant context before generation and can reduce unsupported answers."),
    Document("evaluation", "AI evaluation should use fixed cases, explicit criteria, regression tests and documented limitations."),
    Document("api", "FastAPI provides a typed HTTP interface for serving Python application services."),
]

def retrieve(question: str, top_k: int = 2) -> list[Document]:
    terms = {term.lower().strip(".,?!") for term in question.split() if len(term) > 2}
    scored = []
    for document in DOCUMENTS:
        words = {term.lower().strip(".,?!") for term in document.text.split()}
        score = len(terms & words)
        scored.append((score, document))
    scored.sort(key=lambda item: (-item[0], item[1].id))
    return [doc for score, doc in scored[:top_k] if score > 0]
