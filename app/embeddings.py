import os
from typing import List
from openai import OpenAI


_client: OpenAI | None = None


def get_client() -> OpenAI:
    global _client
    if _client is None:
        _client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return _client


def get_embedding(text: str) -> List[float]:
    """Get embedding using text-embedding-3-small"""
    client = get_client()
    response = client.embeddings.create(input=text, model="text-embedding-3-small")
    return response.data[0].embedding
