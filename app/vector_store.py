from dataclasses import dataclass
import math

@dataclass(frozen=True)
class VectorRecord:
    id: str
    text: str
    vector: list[float]

class InMemoryVectorStore:
    def __init__(self, records: list[VectorRecord]):
        self.records = records

    @staticmethod
    def _cosine(a: list[float], b: list[float]) -> float:
        denominator = math.sqrt(sum(x*x for x in a)) * math.sqrt(sum(y*y for y in b))
        return sum(x*y for x, y in zip(a, b)) / denominator if denominator else 0.0

    def search(self, query_vector: list[float], top_k: int = 2) -> list[tuple[float, VectorRecord]]:
        ranked = [(self._cosine(query_vector, record.vector), record) for record in self.records]
        ranked.sort(key=lambda item: (-item[0], item[1].id))
        return ranked[:top_k]
