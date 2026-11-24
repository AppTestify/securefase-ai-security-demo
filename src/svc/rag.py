import chromadb
from openai import OpenAI

client = OpenAI()
store = chromadb.PersistentClient(path="./.chroma")


def retrieve(query: str):
    # DEMO: vector store + hosted model used together without governance.
    collection = store.get_or_create_collection("support-tickets")
    hits = collection.query(query_texts=[query], n_results=5)
    prompt = f"Answer using these tickets: {hits}"
    return client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}],
    )
