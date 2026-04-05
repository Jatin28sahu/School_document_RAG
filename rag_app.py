"""
School Document RAG Application
Three modes: Q&A, Question Generator, Notes Generator
"""
import os
import json
import streamlit as st
from dotenv import load_dotenv

from app.db import init_database, get_db_connection
from app.ingest import load_chunks_to_db
from app.metadata import (
    save_metadata_cache,
    load_metadata_cache,
    get_cascading_options,
    invalidate_cache,
)
from app.ragmodes import qa_mode, generate_questions, generate_notes

# Load environment variables
load_dotenv()

def render_hierarchical_filters(prefix=""):
    """Render hierarchical filter dropdowns - Book → Class → Subject → Chapter Name → Title"""
    
    # Get current selections from session state
    current_book = st.session_state.get(f"{prefix}_book", None)
    current_class = st.session_state.get(f"{prefix}_class_level", None)
    current_subject = st.session_state.get(f"{prefix}_subject", None)
    current_chapters = st.session_state.get(f"{prefix}_chapter_name", [])
    current_titles = st.session_state.get(f"{prefix}_title", [])
    
    # Build current selections dict for cascading options
    current_selections = {
        "book": current_book,
        "class_level": current_class,
        "subject": current_subject,
        "chapter_name": current_chapters,
        "title": current_titles
    }
    
    # Get available options based on current selections
    options = get_cascading_options(current_selections)
    
    filters = {}
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Book selection
        book_options = ["-- Select Book --"] + options.get("book", [])
        book_idx = 0
        if current_book and current_book in options.get("book", []):
            book_idx = book_options.index(current_book)
        selected_book = st.selectbox("📚 Book", book_options, index=book_idx, key=f"{prefix}_book_sel")
        filters["book"] = selected_book if selected_book != "-- Select Book --" else None
        
        # Update session state
        if filters["book"] != current_book:
            st.session_state[f"{prefix}_book"] = filters["book"]
            st.session_state[f"{prefix}_class_level"] = None
            st.session_state[f"{prefix}_subject"] = None
            st.session_state[f"{prefix}_chapter_name"] = []
            st.session_state[f"{prefix}_title"] = []
            # Auto refresh metadata cache when selection changes
            save_metadata_cache()
        
        # Class selection
        if filters["book"]:
            class_options = ["-- Select Class --"] + options.get("class_level", [])
            class_idx = 0
            if current_class and current_class in options.get("class_level", []):
                class_idx = class_options.index(current_class)
            selected_class = st.selectbox("🎓 Class", class_options, index=class_idx, key=f"{prefix}_class_sel")
            filters["class_level"] = selected_class if selected_class != "-- Select Class --" else None
            
            if filters["class_level"] != current_class:
                st.session_state[f"{prefix}_class_level"] = filters["class_level"]
                st.session_state[f"{prefix}_subject"] = None
                st.session_state[f"{prefix}_chapter_name"] = []
                st.session_state[f"{prefix}_title"] = []
                save_metadata_cache()
        else:
            st.selectbox("🎓 Class", ["Select Book first..."], disabled=True, key=f"{prefix}_class_disabled")
            filters["class_level"] = None
    
    with col2:
        # Subject selection
        if filters.get("class_level"):
            subject_options = ["-- Select Subject --"] + options.get("subject", [])
            subject_idx = 0
            if current_subject and current_subject in options.get("subject", []):
                subject_idx = subject_options.index(current_subject)
            selected_subject = st.selectbox("📖 Subject", subject_options, index=subject_idx, key=f"{prefix}_subject_sel")
            filters["subject"] = selected_subject if selected_subject != "-- Select Subject --" else None
            
            if filters["subject"] != current_subject:
                st.session_state[f"{prefix}_subject"] = filters["subject"]
                st.session_state[f"{prefix}_chapter_name"] = []
                st.session_state[f"{prefix}_title"] = []
                save_metadata_cache()
        else:
            st.selectbox("📖 Subject", ["Select Class first..."], disabled=True, key=f"{prefix}_subject_disabled")
            filters["subject"] = None
        
        # Chapter Name multi-select
        if filters.get("subject"):
            chapter_options = options.get("chapter_name", [])
            selected_chapters = st.multiselect(
                "📑 Chapter Name (multi-select)", 
                chapter_options,
                default=[c for c in current_chapters if c in chapter_options],
                key=f"{prefix}_chapter_sel"
            )
            filters["chapter_name"] = selected_chapters
            st.session_state[f"{prefix}_chapter_name"] = selected_chapters
            save_metadata_cache()
        else:
            st.multiselect("📑 Chapter Name", [], disabled=True, key=f"{prefix}_chapter_disabled")
            filters["chapter_name"] = []
    
    # Title multi-select (full width)
    if filters.get("chapter_name") and len(filters["chapter_name"]) > 0:
        title_options = options.get("title", [])
        selected_titles = st.multiselect(
            "🏷️ Topics/Titles (multi-select)", 
            title_options,
            default=[t for t in current_titles if t in title_options],
            key=f"{prefix}_title_sel"
        )
        filters["title"] = selected_titles
        st.session_state[f"{prefix}_title"] = selected_titles
        save_metadata_cache()
    else:
        st.multiselect("🏷️ Topics/Titles", [], disabled=True, 
                       help="Select at least one chapter first", key=f"{prefix}_title_disabled")
        filters["title"] = []
    
    return filters

def main():
    st.set_page_config(page_title="School RAG System", layout="wide", page_icon="📚")
    
    st.title("📚 School Document RAG System")
    st.markdown("---")
    
    # Sidebar for setup
    with st.sidebar:
        st.header("⚙️ Setup")
        
        if st.button("🔧 Initialize Database", use_container_width=True):
            with st.spinner("Initializing database..."):
                init_database()
            st.success("✅ Database initialized!")
        
        if st.button("📥 Load Chunks to Database", use_container_width=True):
            with st.spinner("Loading chunks and generating embeddings..."):
                load_chunks_to_db()
            st.success("✅ Chunks loaded & cache generated!")
        
        if st.button("🔄 Refresh Metadata Cache", use_container_width=True):
            with st.spinner("Regenerating metadata cache..."):
                save_metadata_cache()
            st.success("✅ Metadata cache refreshed!")
        
        st.markdown("---")
        st.markdown("### 📊 Database Info")
        try:
            conn = get_db_connection()
            cur = conn.cursor()
            cur.execute("SELECT COUNT(*) FROM chunks")
            count = cur.fetchone()[0]
            cur.close()
            conn.close()
            st.metric("Total Chunks", count)
        except Exception:
            st.warning("Database not initialized")
    
    # Check if database is ready
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT COUNT(*) FROM chunks")
        chunk_count = cur.fetchone()[0]
        cur.close()
        conn.close()
        
        if chunk_count == 0:
            st.warning("⚠️ No chunks in database. Please click 'Load Chunks to Database' in the sidebar.")
            return
    except Exception as e:
        st.error("❌ Database not ready. Please click 'Initialize Database' first.")
        return
    
    # Mode selection
    mode = st.selectbox(
        "🎯 Select Mode",
        ["📝 Q&A Mode", "❓ Question Generator", "📖 Notes Generator"],
        key="mode_select"
    )
    
    st.markdown("---")
    
    if mode == "📝 Q&A Mode":
        st.header("🔍 Question & Answer Mode")
        st.markdown("Ask questions and get answers from your documents with source citations.")
        
        # Hierarchical Filters
        with st.expander("🔽 Filter Documents (Hierarchical: Book → Class → Subject → Chapter → Topics)", expanded=True):
            filters = render_hierarchical_filters("qa")
        
        # Query input
        query = st.text_area("💬 Ask your question:", height=100, placeholder="Enter your question here...")
        
        if st.button("🔍 Search & Answer", type="primary", use_container_width=True):
            if query:
                with st.spinner("Searching and generating answer..."):
                    answer, sources = qa_mode(query, filters)
                
                st.markdown("### 📝 Answer")
                st.markdown(answer)
                
                st.markdown("### 📚 Sources Used (Top 5)")
                for i, s in enumerate(sources, 1):
                    with st.expander(f"Source {i}: {s['file']} ({s['similarity']} match)"):
                        st.write(f"**Chapter:** {s['chapter']}")
                        st.write(f"**Topic:** {s['topic']}")
            else:
                st.warning("Please enter a question.")
    
    elif mode == "❓ Question Generator":
        st.header("📝 Question Generator")
        st.markdown("Generate MCQ or Brief answer questions from selected topics.")
        
        # Hierarchical Filters
        with st.expander("🔽 Select Content (Hierarchical: Book → Class → Subject → Chapter → Topics)", expanded=True):
            filters = render_hierarchical_filters("qgen")
        
        col1, col2 = st.columns(2)
        
        with col1:
            q_type = st.radio("📋 Question Type", ["MCQ", "BRIEF"], horizontal=True)
            difficulty = st.select_slider(
                "📊 Difficulty Level",
                options=["Very Easy", "Easy", "Medium", "Hard", "Very Hard"],
                value="Medium"
            )
        
        with col2:
            num_q = st.number_input("🔢 Number of Questions", min_value=1, max_value=20, value=5)
            if q_type == "BRIEF":
                marks = st.slider("📌 Marks per Question", min_value=1, max_value=10, value=5)
            else:
                marks = None
        
        if st.button("✨ Generate Questions", type="primary", use_container_width=True):
            # Pre-check using DB to ensure content exists
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
            if filters.get("chapter_name") and len(filters["chapter_name"]) > 0:
                placeholders = ",".join(["%s"] * len(filters["chapter_name"]))
                where_clauses.append(f"chapter_name IN ({placeholders})")
                params.extend(filters["chapter_name"])
            where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
            cur.execute(f"SELECT COUNT(*) FROM chunks WHERE {where_sql}", params)
            count_check = cur.fetchone()[0]
            cur.close()
            conn.close()
            if count_check == 0:
                st.warning("⚠️ No content found. Please select at least Book, Class, Subject, and Chapter.")
            else:
                with st.spinner(f"Generating {num_q} {q_type} questions..."):
                    result = generate_questions(filters, q_type, difficulty, num_q, marks)
                
                st.markdown("### 📄 Generated Questions")
                st.markdown(result)
                
                st.download_button(
                    "📥 Download Questions (Markdown)",
                    result,
                    f"questions_{q_type}_{difficulty}.md",
                    mime="text/markdown",
                    use_container_width=True
                )
    
    else:  # Notes Generator
        st.header("📖 Notes Generator for Teachers")
        st.markdown("Generate comprehensive 60-minute lecture notes with real-world examples.")
        
        # Hierarchical Filters
        with st.expander("🔽 Select Content (Hierarchical: Book → Class → Subject → Chapter → Topics)", expanded=True):
            filters = render_hierarchical_filters("notes")
        
        if st.button("✨ Generate Lecture Notes", type="primary", use_container_width=True):
            # Simple existence check
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
            if filters.get("chapter_name") and len(filters["chapter_name"]) > 0:
                placeholders = ",".join(["%s"] * len(filters["chapter_name"]))
                where_clauses.append(f"chapter_name IN ({placeholders})")
                params.extend(filters["chapter_name"])
            where_sql = " AND ".join(where_clauses) if where_clauses else "1=1"
            cur.execute(f"SELECT COUNT(*) FROM chunks WHERE {where_sql}", params)
            count_check = cur.fetchone()[0]
            cur.close()
            conn.close()
            if count_check == 0:
                st.warning("⚠️ No content found. Please select at least Book, Class, Subject, and Chapter.")
            else:
                with st.spinner("Generating comprehensive lecture notes..."):
                    notes = generate_notes(filters)
                
                st.markdown("### 📄 Generated Lecture Notes")
                st.markdown(notes)
                
                st.download_button(
                    "📥 Download Notes (Markdown)",
                    notes,
                    "lecture_notes.md",
                    mime="text/markdown",
                    use_container_width=True
                )

if __name__ == "__main__":
    main()
