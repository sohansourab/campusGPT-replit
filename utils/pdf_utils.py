"""
utils/pdf_utils.py
PDF text extraction helper.
"""

from pypdf import PdfReader


def extract_text_from_pdf(uploaded_file) -> str:
    """
    Extract and concatenate text from all pages of a PDF.
    Works with both file paths and file-like objects (e.g. Streamlit UploadedFile).
    """
    reader = PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text
