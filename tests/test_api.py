from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    response = client.get("/health")
    assert response.status_code == 200

def test_query_contract():
    response = client.post("/query", json={"question": "What is RAG?"})
    assert response.status_code == 200
    body = response.json()
    assert body["mode"] == "demo"
    assert body["grounded"] is False

def test_query_requires_question():
    response = client.post("/query", json={"question": ""})
    assert response.status_code == 422
