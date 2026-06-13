"""
modules/pdf_assistant.py
PDF Assistant — chat with any PDF using LLaMA via Groq or Ollama.
"""

import streamlit as st
from utils import ask_llm, extract_text_from_pdf
from i18n.translations import t


def _build_prompt(text: str, question: str) -> str:
    return f"""Answer the question using only the content from the PDF below.

PDF Content:
{text[:12000]}

Question:
{question}
"""


def render() -> None:
    st.markdown(t("pdf_title"))

    pdf_file = st.file_uploader(t("pdf_upload_label"), type=["pdf"])
    question = st.text_area(t("pdf_question_label"), placeholder=t("pdf_question_placeholder"))

    if st.button(t("pdf_ask_btn"), type="primary"):
        if pdf_file is None:
            st.warning(t("pdf_warn_no_file"))
        elif not question.strip():
            st.warning(t("pdf_warn_no_question"))
        else:
            text = extract_text_from_pdf(pdf_file)
            if not text.strip():
                st.warning(t("pdf_warn_no_text"))
            else:
                with st.spinner(t("pdf_spinner")):
                    answer = ask_llm(_build_prompt(text, question))
                st.markdown(answer)
