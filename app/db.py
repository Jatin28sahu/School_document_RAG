import os
import psycopg2

DB_CONFIG = {
    "host": os.getenv("POSTGRES_HOST", "localhost"),
    "port": os.getenv("POSTGRES_PORT", "5432"),
    "database": os.getenv("POSTGRES_DB", "school_rag"),
    "user": os.getenv("POSTGRES_USER", "raguser"),
    "password": os.getenv("POSTGRES_PASSWORD", "ragpassword123"),
}


def get_db_connection():
    return psycopg2.connect(**DB_CONFIG)


def ensure_database():
    """Ensure pgvector extension and chunks table exist. Non-destructive."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS chunks (
            id SERIAL PRIMARY KEY,
            chunk_id TEXT UNIQUE,
            content TEXT,
            book TEXT,
            class_level TEXT,
            subject TEXT,
            chapter TEXT,
            chapter_name TEXT,
            title TEXT,
            page TEXT,
            source_file TEXT,
            embedding vector(1536)
        )
        """
    )
    # Helpful indexes for filter queries
    cur.execute("CREATE INDEX IF NOT EXISTS idx_chunks_book ON chunks(book)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_chunks_class ON chunks(class_level)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_chunks_subject ON chunks(subject)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_chunks_chapter_name ON chunks(chapter_name)")
    cur.execute("CREATE INDEX IF NOT EXISTS idx_chunks_title ON chunks(title)")
    conn.commit()
    cur.close()
    conn.close()


def init_database():
    """Drop and recreate the chunks table. Destructive. Mirrors original behavior."""
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector")
    cur.execute("DROP TABLE IF EXISTS chunks")
    cur.execute(
        """
        CREATE TABLE chunks (
            id SERIAL PRIMARY KEY,
            chunk_id TEXT UNIQUE,
            content TEXT,
            book TEXT,
            class_level TEXT,
            subject TEXT,
            chapter TEXT,
            chapter_name TEXT,
            title TEXT,
            page TEXT,
            source_file TEXT,
            embedding vector(1536)
        )
        """
    )
    conn.commit()
    cur.close()
    conn.close()
