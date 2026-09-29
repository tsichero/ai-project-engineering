from fastapi import FastAPI
from pydantic import BaseModel, Field
from .retrieval import retrieve

app = FastAPI(title="AI Project Engineering", version="0.2.0")

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
        return QueryResponse(answer="Insufficient context in the demo knowledge base.", grounded=False, mode="retrieval-only", sources=[])
    context = " ".join(document.text for document in documents)
    return QueryResponse(answer=f"Grounded demo response: {context}", grounded=True, mode="retrieval-only", sources=[document.id for document in documents])
