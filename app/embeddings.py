import hashlib
import math
import os
import re

class EmbeddingService:
    """Local deterministic embeddings for tests, with optional real model mode."""
    def __init__(self, dimensions: int = 128) -> None:
        self.mode = os.getenv("EMBEDDING_MODE", "local").lower()
        self.dimensions = dimensions
        self._model = None

    def _local_embedding(self, text: str) -> list[float]:
        vector = [0.0] * self.dimensions
        tokens = re.findall(r"[a-zA-ZÀ-ÿ0-9]+", text.lower())
        for token in tokens:
            digest = hashlib.sha256(token.encode("utf-8")).digest()
            index = int.from_bytes(digest[:4], "big") % self.dimensions
            sign = 1.0 if digest[4] % 2 == 0 else -1.0
            vector[index] += sign
        norm = math.sqrt(sum(value * value for value in vector)) or 1.0
        return [value / norm for value in vector]

    def embed(self, texts: list[str]) -> list[list[float]]:
        if self.mode == "local":
            return [self._local_embedding(text) for text in texts]
        if self.mode == "sentence-transformers":
            if self._model is None:
                from sentence_transformers import SentenceTransformer
                self._model = SentenceTransformer(os.getenv("EMBEDDING_MODEL", "all-MiniLM-L6-v2"))
            return self._model.encode(texts, normalize_embeddings=True).tolist()
        raise RuntimeError("Unsupported EMBEDDING_MODE. Use 'local' or 'sentence-transformers'.")
