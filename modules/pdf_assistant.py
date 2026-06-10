"""
modules/pdf_assistant.py
PDF Assistant — chat with any PDF using LLaMA via Groq.
"""

import streamlit as st
from utils import ask_llm, extract_text_from_pdf


def _build_prompt(text: str, question: str) -> str:
    return f"""Answer the question using only the content from the PDF below.

PDF Content:
{text[:12000]}

Question:
{question}
"""


def render() -> None:
    st.markdown("## 📄 PDF Assistant\nUpload any PDF and ask questions about its content.")

    pdf_file = st.file_uploader("Upload PDF", type=["pdf"])
    question = st.text_area("Your Question", placeholder="What is the main topic of this document?")

    if st.button("Ask", type="primary"):
        if pdf_file is None:
            st.warning("⚠️ Please upload a PDF first.")
        elif not question.strip():
            st.warning("⚠️ Please enter a question.")
        else:
            text = extract_text_from_pdf(pdf_file)
            if not text.strip():
                st.warning("⚠️ Could not extract text from this PDF.")
            else:
                with st.spinner("Thinking…"):
                    answer = ask_llm(_build_prompt(text, question))
                st.markdown(answer)
