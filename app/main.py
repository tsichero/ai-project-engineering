from fastapi import FastAPI
from pydantic import BaseModel, Field
from .llm import LLMService
from .retrieval import retrieve

app = FastAPI(title="AI Project Engineering", version="0.3.0")
llm = LLMService()

class QueryRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)

class QueryResponse(BaseModel):
    answer: str
    grounded: bool
    mode: str
    sources: list[str]

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-project-engineering"}

@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    documents = retrieve(request.question)
    if not documents:
        return QueryResponse(answer="Insufficient context in the knowledge base.", grounded=False, mode="no-context", sources=[])
    context = "\n\n".join(f"[{document.id}] {document.text}" for document in documents)
    answer = llm.generate(request.question, context)
    mode = "rag-llm" if llm.mode == "real" else "retrieval-only"
    return QueryResponse(answer=answer, grounded=True, mode=mode, sources=[document.id for document in documents])
