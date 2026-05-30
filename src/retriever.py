from qdrant_client import QdrantClient
from qdrant_client.models import Filter, FieldCondition, MatchValue
from sentence_transformers import SentenceTransformer

from config import QDRANT_URL, COLLECTION_NAME, EMBEDDING_MODEL, TOP_K


class Retriever:
    def __init__(self):
        self.client = QdrantClient(url=QDRANT_URL)
        self.model  = SentenceTransformer(EMBEDDING_MODEL)

    def search(self, query: str, domain: str, top_k: int = TOP_K):
        vector = self.model.encode(query).tolist()
        filt   = Filter(must=[
            FieldCondition(key="domain", match=MatchValue(value=domain))
        ])
        hits = self.client.query_points(
            collection_name=COLLECTION_NAME,
            query=vector, limit=top_k,
            with_payload=True, query_filter=filt,
        ).points
        return [{"text": h.payload["text"], "label": h.payload["label"],
                 "score": round(h.score, 4)} for h in hits]