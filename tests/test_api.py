from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200

def test_query_returns_grounded_context():
    response = client.post("/query", json={"question": "What is RAG?"})
    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "retrieval-only"
    assert body["grounded"] is True
    assert body["sources"]

def test_query_safe_fallback_without_context():
    response = client.post("/query", json={"question": "What is quantum gardening?"})
    assert response.status_code == 200
    body = response.json()
    assert body["grounded"] is False
    assert body["sources"] == []

def test_query_requires_question():
    assert client.post("/query", json={"question": ""}).status_code == 422
