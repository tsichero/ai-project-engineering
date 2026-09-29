from app.retrieval import retrieve, retrieve_scored

def test_embedding_retrieval_finds_expected_document():
    docs = retrieve("What is RAG?", top_k=1)
    assert docs
    assert docs[0].id == "rag"

def test_retrieval_scores_are_ranked():
    ranked = retrieve_scored("What should AI evaluation use?", top_k=2)
    assert ranked[0][0] >= ranked[1][0]
    assert ranked[0][1].id == "evaluation"
