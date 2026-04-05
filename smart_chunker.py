"""
Smart Document Chunker for Educational Documents
Handles hierarchical markdown documents with metadata extraction,
page tracking, and intelligent chunking with overlap.
Ensures chunks end at sentence/paragraph boundaries.
"""

import re
import json
import os
from typing import List, Dict, Tuple
from dataclasses import dataclass, asdict
from pathlib import Path


@dataclass
class ChunkMetadata:
    Book: str
    Class: str
    Subject: str
    Chapter: str
    Chapter_Name: str
    title: str
    Page: str


@dataclass
class Chunk:
    chunk_id: int
    content: str
    word_count: int
    metadata: ChunkMetadata


def parse_filename_metadata(filename: str) -> Dict[str, str]:
    name = Path(filename).stem
    parts = name.split('_')
    return {
        "Book": parts[0] if len(parts) > 0 else "",
        "Class": parts[1] if len(parts) > 1 else "",
        "Subject": parts[2] if len(parts) > 2 else "",
        "Chapter": parts[3] if len(parts) > 3 else "",
        "Chapter_Name": "_".join(parts[4:]) if len(parts) > 4 else ""
    }


def extract_page_numbers(text: str) -> List[Tuple[int, int]]:
    page_pattern = r'Page\s*:\s*(\d+)'
    return [(m.start(), int(m.group(1))) for m in re.finditer(page_pattern, text)]


def get_pages_for_range(start_pos: int, end_pos: int, page_markers: List[Tuple[int, int]]) -> str:
    if not page_markers:
        return ""
    pages = set()
    current_page = None
    for marker_pos, page_num in page_markers:
        if marker_pos <= start_pos:
            current_page = page_num
    if current_page:
        pages.add(current_page)
    for marker_pos, page_num in page_markers:
        if start_pos <= marker_pos <= end_pos:
            pages.add(page_num)
    if not pages and page_markers:
        pages.add(page_markers[0][1])
    return ",".join(str(p) for p in sorted(pages))


def clean_text(text: str) -> str:
    text = re.sub(r'!\[.*?\]\(.*?\)', '', text)
    text = re.sub(r'Page\s*:\s*\d+', '', text)
    text = re.sub(r'Reprint\s+\d{4}-\d{2,4}', '', text)
    text = re.sub(r'Fig\s+\d+\.\d+\s*\([ivx]+\)', '', text)
    text = re.sub(r'\n{3,}', '\n\n', text)
    text = re.sub(r' {2,}', ' ', text)
    return text.strip()


def count_words(text: str) -> int:
    return len(text.split())


def extract_headings(text: str) -> List[Tuple[int, int, str, str]]:
    heading_pattern = r'^(#{1,6})\s+(.+?)$'
    return [(m.start(), len(m.group(1)), m.group(2).strip(), m.group(0)) 
            for m in re.finditer(heading_pattern, text, re.MULTILINE)]


def build_hierarchy_title(headings_stack: List[str]) -> str:
    return " > ".join(headings_stack) if headings_stack else ""


def split_into_sections(text: str) -> List[Dict]:
    headings = extract_headings(text)
    sections = []
    
    if not headings:
        return [{'heading': '', 'level': 0, 'content': text, 'start_pos': 0, 'end_pos': len(text)}]
    
    if headings[0][0] > 0:
        pre_content = text[:headings[0][0]].strip()
        if pre_content:
            sections.append({'heading': '', 'level': 0, 'content': pre_content, 
                           'start_pos': 0, 'end_pos': headings[0][0]})
    
    for i, (start_pos, level, heading_text, full_match) in enumerate(headings):
        end_pos = headings[i + 1][0] if i + 1 < len(headings) else len(text)
        content = text[start_pos + len(full_match):end_pos].strip()
        sections.append({'heading': heading_text, 'level': level, 'content': content,
                        'start_pos': start_pos, 'end_pos': end_pos})
    return sections


def split_into_sentences(text: str) -> List[str]:
    """Split text into complete sentences, handling abbreviations and special cases."""
    # Protect common abbreviations
    protected = text
    abbrevs = ['Mr.', 'Mrs.', 'Dr.', 'Prof.', 'Sr.', 'Jr.', 'vs.', 'etc.', 'i.e.', 'e.g.', 'Fig.', 'Eq.', 'No.']
    for abbr in abbrevs:
        protected = protected.replace(abbr, abbr.replace('.', '<<DOT>>'))
    
    # Protect decimal numbers
    protected = re.sub(r'(\d)\.(\d)', r'\1<<DOT>>\2', protected)
    
    sentences = []
    # Split by paragraph breaks first
    paragraphs = re.split(r'\n\n+', protected)
    
    for para in paragraphs:
        if not para.strip():
            continue
        # Split on sentence endings followed by space and capital letter
        parts = re.split(r'(?<=[.!?])\s+(?=[A-Z\d\(])', para)
        for part in parts:
            part = part.strip().replace('<<DOT>>', '.')
            if part:
                sentences.append(part)
    
    return sentences


def get_complete_sentences_overlap(text: str, target_words: int = 30) -> str:
    """Get complete sentences from end of text for overlap."""
    sentences = split_into_sentences(text)
    if not sentences:
        return ""
    
    overlap_sentences = []
    word_count = 0
    
    for sentence in reversed(sentences):
        sentence_words = count_words(sentence)
        if word_count + sentence_words <= target_words + 15:
            overlap_sentences.insert(0, sentence)
            word_count += sentence_words
        else:
            break
    
    if not overlap_sentences and sentences:
        overlap_sentences = [sentences[-1]]
    
    return ' '.join(overlap_sentences)


def chunk_by_sentences(text: str, target_min: int = 180, target_max: int = 250) -> List[str]:
    """Chunk text ensuring chunks end at sentence boundaries. Flexible 180-250 words."""
    sentences = split_into_sentences(text)
    
    if not sentences:
        return [text] if text.strip() else []
    
    chunks = []
    current_sentences = []
    current_words = 0
    
    for sentence in sentences:
        sentence_words = count_words(sentence)
        
        # If adding this sentence stays under max, add it
        if current_words + sentence_words <= target_max:
            current_sentences.append(sentence)
            current_words += sentence_words
        else:
            # Check if current chunk meets minimum
            if current_words >= target_min:
                chunks.append(' '.join(current_sentences))
                current_sentences = [sentence]
                current_words = sentence_words
            else:
                # Current too small - allow overflow up to max+50 to complete sentence
                if current_words + sentence_words <= target_max + 50:
                    current_sentences.append(sentence)
                    current_words += sentence_words
                else:
                    # Save current even if small, start new
                    if current_sentences:
                        chunks.append(' '.join(current_sentences))
                    current_sentences = [sentence]
                    current_words = sentence_words
    
    # Handle remaining
    if current_sentences:
        remaining = ' '.join(current_sentences)
        remaining_words = count_words(remaining)
        
        # If too small and have previous chunks, try to merge
        if remaining_words < target_min and chunks:
            combined_words = count_words(chunks[-1]) + remaining_words
            if combined_words <= target_max + 60:
                chunks[-1] = chunks[-1] + ' ' + remaining
            else:
                chunks.append(remaining)
        else:
            chunks.append(remaining)
    
    return chunks


def smart_chunk_document(content: str, filename: str, target_min: int = 180, 
                         target_max: int = 250, overlap_words: int = 30) -> List[Chunk]:
    """Main chunking function with sentence-boundary awareness."""
    base_metadata = parse_filename_metadata(filename)
    page_markers = extract_page_numbers(content)
    sections = split_into_sections(content)
    
    all_chunks = []
    chunk_id = 1
    heading_stack = []
    
    for section in sections:
        heading = section['heading']
        level = section['level']
        section_content = clean_text(section['content'])
        
        if heading:
            while heading_stack and len(heading_stack) >= level:
                heading_stack.pop()
            heading_stack.append(heading)
        
        title = build_hierarchy_title(heading_stack)
        
        if not section_content:
            continue
        
        pages = get_pages_for_range(section['start_pos'], section['end_pos'], page_markers)
        section_chunks = chunk_by_sentences(section_content, target_min, target_max)
        
        prev_chunk_text = ""
        
        for i, chunk_text in enumerate(section_chunks):
            # Add overlap from previous chunk (complete sentences)
            if i > 0 and prev_chunk_text and overlap_words > 0:
                overlap = get_complete_sentences_overlap(prev_chunk_text, overlap_words)
                if overlap and not chunk_text.startswith(overlap[:40]):
                    chunk_text = overlap + " " + chunk_text
            
            metadata = ChunkMetadata(
                Book=base_metadata['Book'],
                Class=base_metadata['Class'],
                Subject=base_metadata['Subject'],
                Chapter=base_metadata['Chapter'],
                Chapter_Name=base_metadata['Chapter_Name'],
                title=title,
                Page=pages
            )
            
            all_chunks.append(Chunk(chunk_id=chunk_id, content=chunk_text,
                                   word_count=count_words(chunk_text), metadata=metadata))
            prev_chunk_text = chunk_text
            chunk_id += 1
    
    return all_chunks


def process_document(filepath: str) -> Dict:
    filename = os.path.basename(filepath)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    chunks = smart_chunk_document(content, filename)
    return {
        'filename': filename,
        'total_chunks': len(chunks),
        'chunks': [{'chunk_id': c.chunk_id, 'content': c.content, 
                   'word_count': c.word_count, 'metadata': asdict(c.metadata)} for c in chunks]
    }


def process_all_documents(documents_dir: str) -> Dict:
    results = {'total_documents': 0, 'total_chunks': 0, 'documents': []}
    md_files = list(Path(documents_dir).glob('*.md'))
    
    for filepath in sorted(md_files):
        print(f"Processing: {filepath.name}")
        doc_result = process_document(str(filepath))
        results['documents'].append(doc_result)
        results['total_chunks'] += doc_result['total_chunks']
    
    results['total_documents'] = len(results['documents'])
    return results


def generate_markdown_preview(results: Dict) -> str:
    lines = ["# Chunks Preview", "", f"**Total Documents:** {results['total_documents']}",
             f"**Total Chunks:** {results['total_chunks']}", "", "---", ""]
    
    for doc in results['documents']:
        lines.extend([f"## Document: {doc['filename']}", f"**Total Chunks:** {doc['total_chunks']}", ""])
        
        for chunk in doc['chunks']:
            meta = chunk['metadata']
            lines.extend([f"### Chunk {chunk['chunk_id']}", f"**Title:** {meta['title']}",
                         f"**Page:** {meta['Page']}", f"**Words:** {chunk['word_count']}",
                         f"**Book:** {meta['Book']} | **Class:** {meta['Class']} | **Subject:** {meta['Subject']}",
                         f"**Chapter:** {meta['Chapter']} - {meta['Chapter_Name']}", ""])
            for line in chunk['content'].split('\n'):
                lines.append(f"> {line}")
            lines.extend(["", "---", ""])
    
    return '\n'.join(lines)


def generate_metadata_summary(results: Dict) -> Dict:
    """Generate a summary of all metadata including titles/topics per chapter."""
    summary = {
        "total_documents": results['total_documents'],
        "total_chunks": results['total_chunks'],
        "documents_summary": []
    }
    
    for doc in results['documents']:
        doc_summary = {
            "filename": doc['filename'],
            "total_chunks": doc['total_chunks'],
            "metadata": {},
            "titles_hierarchy": [],
            "pages": set()
        }
        
        # Extract unique titles and build hierarchy
        titles_set = set()
        for chunk in doc['chunks']:
            meta = chunk['metadata']
            # Set base metadata once
            if not doc_summary['metadata']:
                doc_summary['metadata'] = {
                    "Book": meta['Book'],
                    "Class": meta['Class'],
                    "Subject": meta['Subject'],
                    "Chapter": meta['Chapter'],
                    "Chapter_Name": meta['Chapter_Name']
                }
            
            # Collect unique titles
            if meta['title']:
                titles_set.add(meta['title'])
            
            # Collect pages
            if meta['Page']:
                for p in meta['Page'].split(','):
                    doc_summary['pages'].add(int(p.strip()))
        
        # Build hierarchical title structure
        title_tree = {}
        for title in sorted(titles_set):
            parts = title.split(' > ')
            current = title_tree
            for part in parts:
                if part not in current:
                    current[part] = {}
                current = current[part]
        
        def tree_to_list(tree, prefix=""):
            result = []
            for key, subtree in tree.items():
                full_title = f"{prefix} > {key}" if prefix else key
                result.append(full_title)
                result.extend(tree_to_list(subtree, full_title))
            return result
        
        doc_summary['titles_hierarchy'] = tree_to_list(title_tree)
        doc_summary['pages'] = sorted(doc_summary['pages'])
        doc_summary['page_range'] = f"{min(doc_summary['pages'])}-{max(doc_summary['pages'])}" if doc_summary['pages'] else ""
        
        summary['documents_summary'].append(doc_summary)
    
    return summary


def save_results(results: Dict, json_path: str, markdown_path: str, metadata_path: str):
    with open(json_path, 'w', encoding='utf-8') as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"JSON output saved to: {json_path}")
    
    with open(markdown_path, 'w', encoding='utf-8') as f:
        f.write(generate_markdown_preview(results))
    print(f"Markdown preview saved to: {markdown_path}")
    
    # Generate and save metadata summary
    metadata_summary = generate_metadata_summary(results)
    with open(metadata_path, 'w', encoding='utf-8') as f:
        json.dump(metadata_summary, f, indent=2, ensure_ascii=False)
    print(f"Metadata summary saved to: {metadata_path}")


if __name__ == "__main__":
    results = process_all_documents("Documents")
    save_results(results, "chunks_output.json", "chunks_preview.md", "metadata_summary.json")
    print(f"\nProcessing complete! Documents: {results['total_documents']}, Chunks: {results['total_chunks']}")
