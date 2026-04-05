import json
from typing import Dict, Any

from tqdm import tqdm

from .db import get_db_connection
from .embeddings import get_embedding
from .metadata import save_metadata_cache


def load_chunks_to_db(chunks_json_path: str = "chunks_output.json") -> Dict[str, Any]:
    """Load chunks from JSON file to database and save metadata cache"""
    with open(chunks_json_path, "r") as f:
        data = json.load(f)

    conn = get_db_connection()
    cur = conn.cursor()

    for doc in data.get("documents", []):
        source_file = doc.get("filename", "")
        for chunk in tqdm(doc.get("chunks", []), desc=f"Loading {source_file}"):
            content = chunk.get("content", "")
            meta = chunk.get("metadata", {})
            chunk_id = f"{source_file}_{chunk.get('chunk_id', '')}"

            embedding = get_embedding(content)

            cur.execute(
                """
                INSERT INTO chunks (chunk_id, content, book, class_level, subject, chapter, chapter_name, title, page, source_file, embedding)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                ON CONFLICT (chunk_id) DO NOTHING
                """,
                (
                    chunk_id,
                    content,
                    meta.get("Book"),
                    meta.get("Class"),
                    meta.get("Subject"),
                    meta.get("Chapter"),
                    meta.get("Chapter_Name"),
                    meta.get("title"),
                    meta.get("Page"),
                    source_file,
                    embedding,
                ),
            )

    conn.commit()
    cur.close()
    conn.close()

    # Save metadata cache for fast lookups
    save_metadata_cache()
    return {"status": "ok", "inserted_documents": len(data.get("documents", []))}
