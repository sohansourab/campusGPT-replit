"""
modules/resume_analyzer.py
Resume Analyzer — ATS scoring and improvement suggestions.
"""

import streamlit as st
from utils import ask_llm, extract_text_from_pdf
from i18n.translations import t


def _build_prompt(resume_text: str) -> str:
    return f"""You are an expert ATS (Applicant Tracking System) evaluator and career coach.

Resume:
{resume_text}

Provide a structured analysis with:
1. **ATS Score** (out of 100) with justification
2. **Key Skills Identified**
3. **Strengths**
4. **Weaknesses / Gaps**
5. **Improvement Suggestions** (specific, actionable)
"""


def render() -> None:
    st.markdown(t("resume_title"))

    pdf_file = st.file_uploader(t("resume_upload_label"), type=["pdf"])

    if st.button(t("resume_analyze_btn"), type="primary"):
        if pdf_file is None:
            st.warning(t("resume_warn_no_file"))
        else:
            text = extract_text_from_pdf(pdf_file)
            if not text.strip():
                st.warning(t("resume_warn_no_text"))
            else:
                with st.spinner(t("resume_spinner")):
                    result = ask_llm(_build_prompt(text))
                st.markdown(result)
