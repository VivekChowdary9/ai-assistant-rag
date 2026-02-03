from endee import Endee
from embedder import Embedder

class EndeeStore:
    def __init__(self):
        self.embedder = Embedder()
        self.db = Endee(collection_name="documents")

    def add_documents(self, docs):
        embeddings = self.embedder.embed(docs)
        for i, doc in enumerate(docs):
            self.db.add(
                id=str(i),
                vector=embeddings[i],
                metadata={"text": doc}
            )

    def search(self, query, top_k=3):
        query_vector = self.embedder.embed([query])[0]

        results = self.db.query(
            vector=query_vector,
            top_k=top_k
        )

        return [item["metadata"]["text"] for item in results]
