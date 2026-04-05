# School Document RAG

A maintainable, modular Retrieval-Augmented Generation (RAG) system for school documents with:
- Streamlit UI for Q&A, Question Generator, and Lecture Notes
- FastAPI backend with endpoints for metadata, RAG modes, deletion, and auditing
- PostgreSQL + pgvector for embeddings storage

## Features
- Modular codebase split into app/db, app/metadata, app/ingest, app/embeddings, app/queries, app/ragmodes, app/admin
- FastAPI endpoints:
  1) GET /metadata – load metadata cache JSON
  2) POST /qa – Q&A via vector search
  3) POST /questions – question generation from selected filters
  4) POST /notes – lecture notes generation
  5) DELETE /chunks – delete chunks by metadata
  6) DELETE /chunks/all – delete all chunks
  7) GET /audit – audit database stats
- DB auto-initialization on FastAPI startup (pgvector extension and chunks table ensured)
- Streamlit filter selections auto-refresh the metadata cache

## Architecture
```
app/
  db.py           # DB config, ensure/init tables
  metadata.py     # metadata cache load/save/invalidate + cascading options
  embeddings.py   # OpenAI client + embedding helper
  queries.py      # SQL queries for search and content retrieval
  ragmodes.py     # QA, question generation, lecture notes
  ingest.py       # Load chunks_output.json into DB and build cache
  admin.py        # Delete by metadata, delete all, audit

rag_app.py        # Streamlit application (keeps original main() UX)
fastapi_app.py    # FastAPI application (REST endpoints)
smart_chunker.py  # Generates chunks_output.json from Documents/*.md
```

## Prerequisites
- Docker (optional, for Postgres)
- Python 3.10+
- OpenAI API key in `.env`

Create `.env` file:
```
OPENAI_API_KEY=sk-...
POSTGRES_HOST=localhost
POSTGRES_PORT=5432
POSTGRES_DB=school_rag
POSTGRES_USER=raguser
POSTGRES_PASSWORD=ragpassword123
```

## Start Postgres with pgvector
```
docker-compose up -d postgres
```

## Install dependencies
```
pip install -r requirements.txt
```

## Prepare data
Place your Markdown documents in the `Documents/` directory. Then run the chunker:
```
python smart_chunker.py
```
This produces `chunks_output.json`, `chunks_preview.md`, and `metadata_summary.json`.

## Load data into DB & run Streamlit UI
```
streamlit run rag_app.py
```
In the sidebar:
- Initialize Database
- Load Chunks to Database (embeddings will be generated)
- Refresh Metadata Cache

When you select filters, the metadata cache will auto-refresh to keep the hierarchy up-to-date.

## Run FastAPI server
FastAPI auto-initializes DB (non-destructive) and generates metadata cache at startup.
```
uvicorn fastapi_app:app --reload --host 0.0.0.0 --port 8000
```

Open the interactive docs at:
- Swagger UI: http://localhost:8000/docs
- ReDoc: http://localhost:8000/redoc

## API Overview (see docs/api.md for full details)
- GET /metadata
- POST /metadata/refresh
- POST /qa
- POST /questions
- POST /notes
- DELETE /chunks
- DELETE /chunks/all
- GET /audit

### Example requests
Load metadata cache:
```
curl http://localhost:8000/metadata
```

Q&A:
```
curl -X POST http://localhost:8000/qa \
  -H 'Content-Type: application/json' \
  -d '{
        "query": "Explain electrolysis.",
        "filters": {"book":"NCERT_12TH","class_level":"12TH","subject":"Chemistry"}
      }'
```

Generate questions:
```
curl -X POST http://localhost:8000/questions \
  -H 'Content-Type: application/json' \
  -d '{
        "filters": {"book":"NCERT_12TH","class_level":"12TH","subject":"Physics","chapter_name":["Electrostatic"]},
        "q_type": "MCQ",
        "difficulty": "Medium",
        "num_questions": 5
      }'
```

Delete chunks by metadata:
```
curl -X DELETE http://localhost:8000/chunks \
  -H 'Content-Type: application/json' \
  -d '{"book":"NCERT_12TH","subject":"Maths"}'
```

Audit DB:
```
curl http://localhost:8000/audit
```

## Notes
- The Streamlit app preserves the original functionality and layout while using the new modular backend.
- FastAPI endpoints regenerate the metadata cache after deletions to keep filters accurate.
- pgvector is used with a 1536-dim embedding (text-embedding-3-small).

## Troubleshooting
- Ensure Docker Postgres is running and accessible on the configured host/port.
- Check `.env` for correct credentials.
- If you encounter issues, please report using `/reportbug` with details.
