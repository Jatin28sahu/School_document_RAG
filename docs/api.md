# School Document RAG API Documentation

Base URL: http://localhost:8000

Authentication: None (local development). Ensure your OpenAI API key is set in `.env` for generation endpoints.

## Startup behavior
- On startup, the FastAPI app ensures the database has the `pgvector` extension and the `chunks` table (non-destructive).
- It attempts to generate the metadata cache from the database (if chunks exist).

## Schemas

Filters:
```
{
  "book": string | null,
  "class_level": string | null,
  "subject": string | null,
  "chapter_name": string[] | null,
  "title": string[] | null
}
```

QARequest:
```
{
  "query": string,
  "filters": Filters | null
}
```

QuestionsRequest:
```
{
  "filters": Filters,
  "q_type": "MCQ" | "BRIEF",
  "difficulty": "Very Easy" | "Easy" | "Medium" | "Hard" | "Very Hard",
  "num_questions": number,
  "marks": number | null   // required when q_type = "BRIEF"
}
```

NotesRequest:
```
{
  "filters": Filters
}
```

## Endpoints

### GET /metadata
Load the current metadata cache (books, classes, subjects, chapters, titles).

Response 200:
```
{
  "books": ["NCERT_12TH", ...],
  "hierarchy": { ... },
  "generated_at": "2026-03-29T15:00:00Z",
  "version": "1.0"
}
```

### POST /metadata/refresh
Regenerates the metadata cache from the DB.

Response 200: same shape as GET /metadata.

### POST /qa
Performs semantic search and returns a GPT-generated answer with sources.

Request body (QARequest):
```
{
  "query": "Explain electrolysis.",
  "filters": {"book":"NCERT_12TH","class_level":"12TH","subject":"Chemistry"}
}
```

Response 200:
```
{
  "answer": "...",
  "sources": [
    {"file":"NCERT_12TH_Chemistry_Chapter-2_Electrochemistry.md","chapter":"2 - Electrochemistry","topic":"Electrolysis","similarity":"92.13%"},
    ... up to 5 ...
  ]
}
```

### POST /questions
Generates questions (MCQ or BRIEF) based on filters.

Request body (QuestionsRequest):
```
{
  "filters": {"book":"NCERT_12TH","class_level":"12TH","subject":"Physics","chapter_name":["Electrostatic"]},
  "q_type": "MCQ",
  "difficulty": "Medium",
  "num_questions": 5
}
```

Response 200:
```
{
  "content": "# Generated Questions\n...markdown..."
}
```

Notes:
- For `q_type = "BRIEF"`, include `"marks": <int>` in the request.

### POST /notes
Generates 60-minute lecture notes based on filters.

Request body (NotesRequest):
```
{
  "filters": {"book":"NCERT_12TH","class_level":"12TH","subject":"Physics","chapter_name":["Current-Electricity"]}
}
```

Response 200:
```
{
  "content": "# Lecture Notes\n...markdown..."
}
```

### DELETE /chunks
Deletes chunks that match the provided metadata filters.

Request body (Filters):
```
{
  "book": "NCERT_12TH",
  "subject": "Maths"
}
```

Response 200:
```
{"deleted": 123}
```

Side effects: Regenerates metadata cache after deletion.

### DELETE /chunks/all
Deletes all chunks.

Response 200:
```
{"deleted": 14237}
```

Side effects: Regenerates metadata cache after deletion.

### GET /audit
Returns aggregate statistics for auditing the database.

Response 200:
```
{
  "total_chunks": 14237,
  "counts": {
    "by_book": [["NCERT_12TH", 5123], ...],
    "by_class": [["12TH", 10000], ...],
    "by_subject": [["Physics", 3400], ...]
  },
  "missing_fields": {
    "titles": 23,
    "chapter_names": 7
  }
}
```

## Error handling
- 422 Unprocessable Entity: Pydantic validation errors (e.g., wrong types)
- 500 Internal Server Error: DB connectivity issues, missing environment variables, or OpenAI API errors

## Tips
- Ensure the DB is populated: run `python smart_chunker.py` then load via the Streamlit sidebar ("Load Chunks to Database").
- Use `POST /metadata/refresh` after ingestion or deletions to keep the cache current.
