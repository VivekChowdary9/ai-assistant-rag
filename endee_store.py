from endee import Endee
from embedder import Embedder
import uuid

class EndeeStore:
    def __init__(self):
        self.db = Endee()
        self.embedder = Embedder()

    def add_documents(self, documents):
        embeddings = self.embedder.embed(documents)

        for text, vector in zip(documents, embeddings):
            self.db.add(
                id=str(uuid.uuid4()),
                vector=vector,
                metadata={"text": text}
            )

    def search(self, query, top_k=5):
        query_vector = self.embedder.embed([query])[0]

        results = self.db.search(
            vector=query_vector,
            top_k=top_k
        )

        return [item["metadata"]["text"] for item in results]
