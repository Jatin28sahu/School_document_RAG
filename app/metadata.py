import json
import os
from typing import Dict, Any

from .db import get_db_connection

METADATA_CACHE: Dict[str, Any] | None = None
METADATA_CACHE_FILE = "metadata_cache.json"


def load_metadata_cache() -> Dict[str, Any]:
    """Load pre-stored metadata cache from JSON file for fast lookups"""
    global METADATA_CACHE
    if METADATA_CACHE is None:
        try:
            if os.path.exists(METADATA_CACHE_FILE):
                with open(METADATA_CACHE_FILE, "r") as f:
                    METADATA_CACHE = json.load(f)
                print(f"✅ Loaded metadata cache from {METADATA_CACHE_FILE}")
            else:
                METADATA_CACHE = {"books": [], "hierarchy": {}}
                print(f"⚠️ No metadata cache found, will use database queries")
        except Exception as e:
            print(f"⚠️ Error loading metadata cache: {e}")
            METADATA_CACHE = {"books": [], "hierarchy": {}}
    return METADATA_CACHE


def invalidate_cache() -> None:
    """Invalidate in-memory cache so next load reads fresh from disk."""
    global METADATA_CACHE
    METADATA_CACHE = None


def save_metadata_cache() -> Dict[str, Any]:
    """Save metadata cache to JSON file after database initialization"""
    global METADATA_CACHE
    conn = get_db_connection()
    cur = conn.cursor()

    cache = {"books": [], "hierarchy": {}}

    # Get all books
    cur.execute("SELECT DISTINCT book FROM chunks WHERE book IS NOT NULL ORDER BY book")
    books = [r[0] for r in cur.fetchall()]
    cache["books"] = books

    for book in books:
        cache["hierarchy"][book] = {"classes": []}

        # Get classes for this book
        cur.execute(
            "SELECT DISTINCT class_level FROM chunks WHERE book = %s AND class_level IS NOT NULL ORDER BY class_level",
            (book,),
        )
        classes = [r[0] for r in cur.fetchall()]
        cache["hierarchy"][book]["classes"] = classes

        for class_level in classes:
            cache["hierarchy"][book][class_level] = {"subjects": []}

            # Get subjects for this book/class
            cur.execute(
                "SELECT DISTINCT subject FROM chunks WHERE book = %s AND class_level = %s AND subject IS NOT NULL ORDER BY subject",
                (book, class_level),
            )
            subjects = [r[0] for r in cur.fetchall()]
            cache["hierarchy"][book][class_level]["subjects"] = subjects

            for subject in subjects:
                cache["hierarchy"][book][class_level][subject] = {"chapters": []}

                # Get chapters for this book/class/subject
                cur.execute(
                    "SELECT DISTINCT chapter_name FROM chunks WHERE book = %s AND class_level = %s AND subject = %s AND chapter_name IS NOT NULL ORDER BY chapter_name",
                    (book, class_level, subject),
                )
                chapters = [r[0] for r in cur.fetchall()]
                cache["hierarchy"][book][class_level][subject]["chapters"] = chapters

                for chapter in chapters:
                    # Get titles for this chapter
                    cur.execute(
                        "SELECT DISTINCT title FROM chunks WHERE book = %s AND class_level = %s AND subject = %s AND chapter_name = %s AND title IS NOT NULL ORDER BY title",
                        (book, class_level, subject, chapter),
                    )
                    titles = [r[0] for r in cur.fetchall()]
                    cache["hierarchy"][book][class_level][subject][chapter] = {"titles": titles}

    cur.close()
    conn.close()

    # Save to file
    cache["generated_at"] = str(os.popen('date -u +"%Y-%m-%dT%H:%M:%SZ"').read().strip())
    cache["version"] = "1.0"

    with open(METADATA_CACHE_FILE, "w") as f:
        json.dump(cache, f, indent=2)

    METADATA_CACHE = cache
    print(f"✅ Saved metadata cache to {METADATA_CACHE_FILE}")
    return cache


def get_cascading_options(selected_filters: Dict[str, Any]) -> Dict[str, list]:
    """Get metadata options from pre-stored cache for fast lookups (no database queries)"""
    cache = load_metadata_cache()

    options = {
        "book": [],
        "class_level": [],
        "subject": [],
        "chapter_name": [],
        "title": [],
    }

    # Get all books from cache
    options["book"] = cache.get("books", [])

    hierarchy = cache.get("hierarchy", {})

    # Get classes based on selected book
    book = selected_filters.get("book")
    if book and book in hierarchy:
        options["class_level"] = hierarchy[book].get("classes", [])

    # Get subjects based on selected book and class
    class_level = selected_filters.get("class_level")
    if book and class_level and book in hierarchy and class_level in hierarchy[book]:
        options["subject"] = hierarchy[book][class_level].get("subjects", [])

    # Get chapter names based on book, class, subject
    subject = selected_filters.get("subject")
    if book and class_level and subject:
        if book in hierarchy and class_level in hierarchy[book] and subject in hierarchy[book][class_level]:
            options["chapter_name"] = hierarchy[book][class_level][subject].get("chapters", [])

    # Get titles based on all previous selections
    chapter_names = selected_filters.get("chapter_name")
    if book and class_level and subject and chapter_names:
        all_titles: list[str] = []
        if isinstance(chapter_names, list):
            for chapter in chapter_names:
                if (
                    book in hierarchy
                    and class_level in hierarchy[book]
                    and subject in hierarchy[book][class_level]
                    and chapter in hierarchy[book][class_level][subject]
                ):
                    all_titles.extend(
                        hierarchy[book][class_level][subject][chapter].get("titles", [])
                    )
        elif chapter_names:
            if (
                book in hierarchy
                and class_level in hierarchy[book]
                and subject in hierarchy[book][class_level]
                and chapter_names in hierarchy[book][class_level][subject]
            ):
                all_titles = hierarchy[book][class_level][subject][chapter_names].get("titles", [])
        options["title"] = sorted(list(set(all_titles)))

    return options
