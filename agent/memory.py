import faiss
import numpy as np
import os
from langchain_openai import OpenAIEmbeddings

class Memory:
    def __init__(self, path="data/vector_store"):
        self.path = path
        self.embeddings = OpenAIEmbeddings()

        self.index = faiss.IndexFlatL2(1536)
        self.texts = []

        if os.path.exists(f"{path}/index.faiss"):
            self.index = faiss.read_index(f"{path}/index.faiss")
            with open(f"{path}/texts.txt", "r", encoding="utf-8") as f:
                self.texts = f.read().split("\n---\n")

    def add(self, text):
        if isinstance(text, list):
            for t in text:
                self._add_single(t)
        else:
            self._add_single(text)

        self._persist()

    def _add_single(self, text):
        vector = self.embeddings.embed_query(text)
        vector = np.array([vector], dtype="float32")
        self.index.add(vector)
        self.texts.append(text)

    def search(self, query, k=3):
        if len(self.texts) == 0:
            return ""

        vector = self.embeddings.embed_query(query)
        vector = np.array([vector], dtype="float32")
        _, indices = self.index.search(vector, k)

        return "\n\n".join([self.texts[i] for i in indices[0]])

    def _persist(self):
        os.makedirs(self.path, exist_ok=True)
        faiss.write_index(self.index, f"{self.path}/index.faiss")
        with open(f"{self.path}/texts.txt", "w", encoding="utf-8") as f:
            f.write("\n---\n".join(self.texts))
