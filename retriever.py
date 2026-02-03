class Retriever:
    def __init__(self, store):
        self.store = store

    def retrieve(self, query, top_k=5):
        return self.store.search(query, top_k)
