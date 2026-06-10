"""
app.py
CampusGPT — AI-Powered Student Success Platform
Entry point for the Streamlit application.
"""

import streamlit as st
from modules import pdf_assistant, resume_analyzer, interview_simulator, career_roadmap

st.set_page_config(page_title="CampusGPT 🎓", page_icon="🎓", layout="centered")

# ── Header ──────────────────────────────────────────────────────────
st.markdown(
    "<div style='text-align:center; padding: 20px 0 10px;'>"
    "<h1 style='font-size:2.4rem;'>🎓 CampusGPT</h1>"
    "<p style='font-size:1.05rem; color:#555;'>"
    "<strong>AI-Powered Student Success Platform</strong> · Groq × LLaMA 3.1"
    "</p></div>",
    unsafe_allow_html=True,
)

# ── Tabs ─────────────────────────────────────────────────────────────
tab_home, tab_pdf, tab_resume, tab_interview, tab_roadmap = st.tabs(
    ["🏠 Home", "📄 PDF Assistant", "📑 Resume Analyzer", "🎤 Interview Simulator", "🛣️ Career Roadmap"]
)

with tab_home:
    st.markdown(
        """
## Welcome to CampusGPT 👋

Your all-in-one AI companion for academic and career success, powered by **LLaMA 3.1** via **Groq**.

| Module | Description |
|---|---|
| 📄 **PDF Assistant** | Upload any PDF and ask questions about its content |
| 📑 **Resume Analyzer** | Get your ATS score, strengths, gaps & improvement tips |
| 🎤 **Interview Simulator** | Practice role-specific interviews with AI feedback |
| 🛣️ **Career Roadmap** | Receive a personalised, month-by-month learning plan |

> **Tip:** Select a tab above to get started. Each module is independent — no sign-in required.
        """
    )

with tab_pdf:
    pdf_assistant.render()

with tab_resume:
    resume_analyzer.render()

with tab_interview:
    interview_simulator.render()

with tab_roadmap:
    career_roadmap.render()
