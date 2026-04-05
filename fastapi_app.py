from typing import Optional, List, Dict, Any

from fastapi import FastAPI
from pydantic import BaseModel

from app.db import ensure_database
from app.metadata import load_metadata_cache, save_metadata_cache
from app.ragmodes import qa_mode, generate_questions, generate_notes
from app.admin import delete_chunks_by_metadata, delete_all_chunks, audit_database


class Filters(BaseModel):
    book: Optional[str] = None
    class_level: Optional[str] = None
    subject: Optional[str] = None
    chapter_name: Optional[List[str]] = None
    title: Optional[List[str]] = None


class QARequest(BaseModel):
    query: str
    filters: Optional[Filters] = None


class QuestionsRequest(BaseModel):
    filters: Filters
    q_type: str
    difficulty: str
    num_questions: int
    marks: Optional[int] = None


class NotesRequest(BaseModel):
    filters: Filters


app = FastAPI(title="School Document RAG API", version="1.0.0")


@app.on_event("startup")
def on_startup():
    # Ensure DB is initialized non-destructively
    ensure_database()
    # Ensure metadata cache exists
    try:
        save_metadata_cache()
    except Exception:
        # If table empty, cache generation may not be necessary
        pass


@app.get("/metadata")
def get_metadata():
    """Return the current metadata cache."""
    return load_metadata_cache()


@app.post("/metadata/refresh")
def refresh_metadata():
    """Regenerate metadata cache from DB."""
    return save_metadata_cache()


@app.post("/qa")
def qa_endpoint(req: QARequest):
    filters_dict: Dict[str, Any] = req.filters.dict() if req.filters else {}
    answer, sources = qa_mode(req.query, filters_dict)
    return {"answer": answer, "sources": sources}


@app.post("/questions")
def questions_endpoint(req: QuestionsRequest):
    filters_dict: Dict[str, Any] = req.filters.dict()
    content = generate_questions(filters_dict, req.q_type, req.difficulty, req.num_questions, req.marks)
    return {"content": content}


@app.post("/notes")
def notes_endpoint(req: NotesRequest):
    filters_dict: Dict[str, Any] = req.filters.dict()
    content = generate_notes(filters_dict)
    return {"content": content}


@app.delete("/chunks")
def delete_by_metadata(filters: Filters):
    filters_dict: Dict[str, Any] = filters.dict()
    deleted = delete_chunks_by_metadata(filters_dict)
    # Refresh metadata cache after deletion
    try:
        save_metadata_cache()
    except Exception:
        pass
    return {"deleted": deleted}


@app.delete("/chunks/all")
def delete_all():
    deleted = delete_all_chunks()
    try:
        save_metadata_cache()
    except Exception:
        pass
    return {"deleted": deleted}


@app.get("/audit")
def audit():
    return audit_database()
