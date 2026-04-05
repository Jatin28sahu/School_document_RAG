from typing import Dict, List, Any

from .db import get_db_connection
from .embeddings import get_embedding


def search_similar(query: str, filters: Dict[str, Any] | None = None, top_k: int = 5):
    """Search for similar chunks with optional metadata filters"""
    query_embedding = get_embedding(query)
    conn = get_db_connection()
    cur = conn.cursor()

    # Convert embedding to string format for pgvector
    embedding_str = "[" + ",".join(map(str, query_embedding)) + "]"

    where_clauses: List[str] = []
    params: List[Any] = []

    if filters:
        if filters.get("book"):
            where_clauses.append("book = %s")
            params.append(filters["book"])
        if filters.get("class_level"):
            where_clauses.append("class_level = %s")
            params.append(filters["class_level"])
        if filters.get("subject"):
            where_clauses.append("subject = %s")
            params.append(filters["subject"])
        if filters.get("chapter_name"):
            chapter_names = filters["chapter_name"]
            if isinstance(chapter_names, list) and len(chapter_names) > 0:
                placeholders = ",".join(["%s"] * len(chapter_names))
                where_clauses.append(f"chapter_name IN ({placeholders})")
                params.extend(chapter_names)
            elif chapter_names:
                where_clauses.append("chapter_name = %s")
                params.append(chapter_names)
        if filters.get("title"):
            titles = filters["title"]
            if isinstance(titles, list) and len(titles) > 0:
                placeholders = ",".join(["%s"] * len(titles))
                where_clauses.append(f"title IN ({placeholders})")
                params.extend(titles)

    where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"

    # Build query with proper parameter ordering
    query_sql = f"""
        SELECT chunk_id, content, book, class_level, subject, chapter, chapter_name, title, page, source_file,
               1 - (embedding <=> %s::vector) as similarity
        FROM chunks 
        WHERE {where_sql}
        ORDER BY embedding <=> %s::vector 
        LIMIT %s
    """

    # Parameters: embedding for similarity calc, filter params, embedding for ordering, limit
    all_params = [embedding_str] + params + [embedding_str, top_k]

    cur.execute(query_sql, all_params)

    results = cur.fetchall()
    cur.close()
    conn.close()
    return results


def get_content_by_filters(filters: Dict[str, Any]):
    """Get all content matching the filters"""
    conn = get_db_connection()
    cur = conn.cursor()

    where_clauses: List[str] = []
    params: List[Any] = []

    if filters.get("book"):
        where_clauses.append("book = %s")
        params.append(filters["book"])
    if filters.get("class_level"):
        where_clauses.append("class_level = %s")
        params.append(filters["class_level"])
    if filters.get("subject"):
        where_clauses.append("subject = %s")
        params.append(filters["subject"])
    if filters.get("chapter_name"):
        chapter_names = filters["chapter_name"]
        if isinstance(chapter_names, list) and len(chapter_names) > 0:
            placeholders = ",".join(["%s"] * len(chapter_names))
            where_clauses.append(f"chapter_name IN ({placeholders})")
            params.extend(chapter_names)
        elif chapter_names:
            where_clauses.append("chapter_name = %s")
            params.append(chapter_names)
    if filters.get("title"):
        titles = filters["title"]
        if isinstance(titles, list) and len(titles) > 0:
            placeholders = ",".join(["%s"] * len(titles))
            where_clauses.append(f"title IN ({placeholders})")
            params.extend(titles)

    where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"

    cur.execute(
        f"""
        SELECT content, book, class_level, subject, chapter, chapter_name, title
        FROM chunks WHERE {where_sql}
        ORDER BY chapter, title
        """,
        params,
    )

    results = cur.fetchall()
    cur.close()
    conn.close()
    return results
