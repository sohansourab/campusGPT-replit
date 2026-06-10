"""
modules/resume_analyzer.py
Resume Analyzer — ATS scoring and improvement suggestions.
"""

import streamlit as st
from utils import ask_llm, extract_text_from_pdf


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
    st.markdown("## 📑 Resume Analyzer\nGet an ATS score, strengths, weaknesses, and tailored improvement tips.")

    pdf_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if st.button("Analyze Resume", type="primary"):
        if pdf_file is None:
            st.warning("⚠️ Please upload your resume as a PDF.")
        else:
            text = extract_text_from_pdf(pdf_file)
            if not text.strip():
                st.warning("⚠️ Could not extract text from this PDF.")
            else:
                with st.spinner("Analyzing…"):
                    result = ask_llm(_build_prompt(text))
                st.markdown(result)
