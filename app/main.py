from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="AI Project Engineering", version="0.1.0")

class QueryRequest(BaseModel):
    question: str = Field(min_length=1, max_length=2000)

class QueryResponse(BaseModel):
    answer: str
    grounded: bool
    mode: str

@app.get("/health")
def health():
    return {"status": "ok", "service": "ai-project-engineering"}

@app.post("/query", response_model=QueryResponse)
def query(request: QueryRequest):
    return QueryResponse(answer=f"Demo pipeline received: {request.question}", grounded=False, mode="demo")
