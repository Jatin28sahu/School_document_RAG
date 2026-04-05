from typing import Dict, Any, List

from openai import OpenAI

from .queries import search_similar, get_content_by_filters
from .embeddings import get_client


def qa_mode(query: str, filters: Dict[str, Any]):
    """Simple Q&A mode using vector search and GPT model."""
    results = search_similar(query, filters, top_k=5)
    context = "\n\n".join(
        [f"[Source: {r[9]}, Chapter: {r[5]} - {r[6]}, Topic: {r[7]}]\n{r[1]}" for r in results]
    )

    client: OpenAI = get_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are a helpful educational assistant. Answer based on the provided context. Always cite sources used.",
            },
            {
                "role": "user",
                "content": f"Context:\n{context}\n\nQuestion: {query}\n\nProvide a detailed answer and cite which sources you used.",
            },
        ],
    )

    sources = [
        {
            "file": r[9],
            "chapter": f"{r[5]} - {r[6]}",
            "topic": r[7],
            "similarity": f"{r[10]:.2%}",
        }
        for r in results
    ]
    return response.choices[0].message.content, sources


def generate_questions(
    filters: Dict[str, Any], q_type: str, difficulty: str, num_questions: int, marks: int | None = None
):
    """Generate questions based on selected filters"""
    results = get_content_by_filters(filters)
    content = "\n\n".join([f"[{r[4]} - {r[5]}: {r[6]}]\n{r[0]}" for r in results])

    if q_type == "MCQ":
        prompt = f"""Generate {num_questions} MCQ questions from this content.
Difficulty Level: {difficulty}

Format each question as:
## Question [N]
**Question:** [question text]

**Options:**
A) [option]
B) [option]
C) [option]
D) [option]

---

After ALL questions, provide:

## Answer Key with Explanations

### Question [N]
**Correct Answer:** [Option Letter]
**Explanation:** [Detailed explanation why this is correct and why others are wrong]

---

Content to generate questions from:
{content}"""
    else:
        prompt = f"""Generate {num_questions} brief answer questions ({marks} marks each) from this content.
Difficulty Level: {difficulty}

Format each question as:
## Question [N] ({marks} marks)
**Question:** [question text]

---

After ALL questions, provide:

## Detailed Answers with Marking Scheme

### Answer [N]
**Answer:** [Detailed comprehensive answer]

**Marking Scheme ({marks} marks):**
- [X marks] - [Point 1]
- [X marks] - [Point 2]
- [X marks] - [Point 3]
(breakdown should total {marks} marks)

---

Content to generate questions from:
{content}"""

    client: OpenAI = get_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert teacher creating exam questions. Generate high-quality questions appropriate for the specified difficulty level.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=4000,
    )
    return response.choices[0].message.content


def generate_notes(filters: Dict[str, Any]):
    """Generate 60-minute lecture notes"""
    results = get_content_by_filters(filters)
    content = "\n\n".join([f"[{r[4]} - {r[5]}: {r[6]}]\n{r[0]}" for r in results])

    topics = list(set([r[6] for r in results if r[6]]))
    chapters = list(set([f"{r[4]} - {r[5]}" for r in results]))

    prompt = f"""Create comprehensive 60-minute lecture notes for a teacher on the following topics.

Topics covered: {', '.join(topics[:5])}
From chapters: {', '.join(chapters[:3])}

Include the following sections:

## 📚 Topic Overview
Brief introduction and importance of the topic

## 🎯 Learning Objectives
What students will learn by the end of this lecture

## 📖 Main Content
Detailed explanation with:
- Clear explanations
- Real-world examples and analogies
- Step-by-step breakdowns where applicable

## 📐 Formulas & Key Equations
All important formulas with explanations of each variable

## 📝 Glossary
Key terms and their definitions

## 🔬 Real-life Applications
- Current real-world implementations
- Latest developments and examples
- Practical applications students can relate to

## 🎮 Student Activities
- Hands-on activities
- Discussion questions
- Practical exercises to reinforce learning

## ⏱️ Suggested Time Breakdown (60 minutes)
- Introduction: X min
- Main content: X min
- Activities: X min
- Q&A: X min

Content to base the notes on:
{content}"""

    client: OpenAI = get_client()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "system",
                "content": "You are an expert teacher creating engaging and comprehensive lecture notes. Make the content accessible, practical, and engaging for students.",
            },
            {"role": "user", "content": prompt},
        ],
        max_tokens=4000,
    )
    return response.choices[0].message.content
