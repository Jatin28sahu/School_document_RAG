from typing import Dict, Any

from .db import get_db_connection


def delete_chunks_by_metadata(filters: Dict[str, Any]) -> int:
    """Delete chunks that match provided metadata filters. Returns rows deleted."""
    conn = get_db_connection()
    cur = conn.cursor()

    where_clauses = []
    params = []

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

    cur.execute(f"DELETE FROM chunks WHERE {where_sql}", params)
    deleted = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return deleted


def delete_all_chunks() -> int:
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM chunks")
    deleted = cur.rowcount
    conn.commit()
    cur.close()
    conn.close()
    return deleted


def audit_database() -> Dict[str, Any]:
    """Return audit info: total chunks, counts by book/class/subject, missing fields, etc."""
    conn = get_db_connection()
    cur = conn.cursor()

    # Total count
    cur.execute("SELECT COUNT(*) FROM chunks")
    total = cur.fetchone()[0]

    # Counts by book/class/subject
    cur.execute("SELECT book, COUNT(*) FROM chunks GROUP BY book ORDER BY book")
    by_book = [(r[0], r[1]) for r in cur.fetchall()]

    cur.execute("SELECT class_level, COUNT(*) FROM chunks GROUP BY class_level ORDER BY class_level")
    by_class = [(r[0], r[1]) for r in cur.fetchall()]

    cur.execute("SELECT subject, COUNT(*) FROM chunks GROUP BY subject ORDER BY subject")
    by_subject = [(r[0], r[1]) for r in cur.fetchall()]

    # Missing fields
    cur.execute("SELECT COUNT(*) FROM chunks WHERE title IS NULL OR title = ''")
    missing_titles = cur.fetchone()[0]
    cur.execute("SELECT COUNT(*) FROM chunks WHERE chapter_name IS NULL OR chapter_name = ''")
    missing_chapter_names = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "total_chunks": total,
        "counts": {
            "by_book": by_book,
            "by_class": by_class,
            "by_subject": by_subject,
        },
        "missing_fields": {
            "titles": missing_titles,
            "chapter_names": missing_chapter_names,
        },
    }
