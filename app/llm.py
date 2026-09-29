import json
import os
from urllib import request
from urllib.error import HTTPError, URLError

class LLMService:
    def __init__(self) -> None:
        self.mode = os.getenv("LLM_MODE", "demo").lower()
        self.model = os.getenv("LLM_MODEL", "")
        self.base_url = os.getenv("LLM_BASE_URL", "https://api.openai.com/v1").rstrip("/")
        self.api_key = os.getenv("LLM_API_KEY", "")

    def generate(self, question: str, context: str) -> str:
        if self.mode == "demo":
            return f"Grounded demo response: {context}"
        if self.mode != "real":
            raise RuntimeError("Unsupported LLM_MODE. Use 'demo' or 'real'.")
        if not self.api_key or not self.model:
            raise RuntimeError("LLM_API_KEY and LLM_MODEL are required when LLM_MODE=real.")
        payload = {"model": self.model, "messages": [
            {"role": "system", "content": "Answer using only the supplied context. If the context is insufficient, say so."},
            {"role": "user", "content": f"Context:\n{context}\n\nQuestion: {question}"},
        ], "temperature": 0}
        req = request.Request(f"{self.base_url}/chat/completions", data=json.dumps(payload).encode("utf-8"), headers={"Authorization": f"Bearer {self.api_key}", "Content-Type": "application/json"}, method="POST")
        try:
            with request.urlopen(req, timeout=30) as response:
                body = json.loads(response.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError) as exc:
            raise RuntimeError(f"LLM request failed: {exc}") from exc
        return body["choices"][0]["message"]["content"].strip()
