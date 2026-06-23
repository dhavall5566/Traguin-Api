"""Extract plain text from PDF uploads, preserving page order.

Uses pypdf (pure Python, no system deps). Table-heavy PDFs may lose column
alignment vs pdfplumber, but travel brochures are LLM-friendly once page order
and section breaks are kept — the downstream Groq step reconstructs structure.
"""

from __future__ import annotations

import io

from pypdf import PdfReader


def extract_pdf_text(file_bytes: bytes, *, max_pages: int | None = None) -> str:
    reader = PdfReader(io.BytesIO(file_bytes))
    pages: list[str] = []
    for index, page in enumerate(reader.pages):
        if max_pages is not None and index >= max_pages:
            break
        text = page.extract_text() or ""
        cleaned = text.strip()
        if cleaned:
            pages.append(f"--- Page {index + 1} ---\n{cleaned}")
    if not pages:
        raise ValueError("No readable text found in PDF.")
    return "\n\n".join(pages)
