"""
app.py
CampusGPT — AI-Powered Student Success Platform
Entry point for the Streamlit application.
"""

import os
import streamlit as st
from modules import pdf_assistant, resume_analyzer, interview_simulator, career_roadmap
from utils.groq_helper import check_ollama_status
from i18n.translations import t

st.set_page_config(page_title="CampusGPT 🎓", page_icon="🎓", layout="centered")

# ── Sidebar ──────────────────────────────────────────────────────────
with st.sidebar:

    # Language selector (must come first so everything below re-renders in chosen language)
    st.markdown(f"## {t('sidebar_language_label')}")
    locale = st.selectbox(
        t("sidebar_language_label"),
        options=["en", "hi", "te"],
        format_func=lambda x: {"en": "🇬🇧 English", "hi": "🇮🇳 हिन्दी", "te": "🇮🇳 తెలుగు"}[x],
        index=["en", "hi", "te"].index(st.session_state.get("locale", "en")),
        label_visibility="collapsed",
    )
    st.session_state["locale"] = locale

    st.divider()

    # Backend toggle
    st.markdown(f"## {t('sidebar_backend_title')}")
    backend = st.radio(
        t("sidebar_backend_label"),
        ["Groq (Cloud)", "Ollama (Local)"],
        index=0 if st.session_state.get("llm_backend", "Groq") != "Ollama (Local)" else 1,
        help="Groq uses cloud APIs. Ollama runs models fully on your machine.",
    )
    st.session_state["llm_backend"] = backend

    st.divider()

    # Groq section
    if backend == "Groq (Cloud)":
        st.markdown(t("sidebar_groq_title"))
        env_key = os.getenv("GROQ_API_KEY", "")
        if env_key:
            st.success(t("sidebar_groq_server_key"), icon="🔒")
            st.caption(t("sidebar_groq_override"))
        user_key = st.text_input(
            t("sidebar_groq_key_label"),
            type="password",
            placeholder="gsk_...",
            value=st.session_state.get("groq_api_key", ""),
        )
        if user_key:
            st.session_state["groq_api_key"] = user_key
            st.success(t("sidebar_groq_using_key"), icon="🗝️")
        elif not env_key:
            st.warning(t("sidebar_groq_no_key"), icon="⚠️")
        st.caption(t("sidebar_groq_link"))

    # Ollama section
    else:
        st.markdown(t("sidebar_ollama_title"))
        ollama_url = st.text_input(
            t("sidebar_ollama_url_label"),
            value=st.session_state.get("ollama_url", "http://localhost:11434"),
            placeholder="http://localhost:11434",
        )
        st.session_state["ollama_url"] = ollama_url
        ollama_model = st.text_input(
            t("sidebar_ollama_model_label"),
            value=st.session_state.get("ollama_model", "llama3.2"),
            placeholder="llama3.2",
        )
        st.session_state["ollama_model"] = ollama_model
        if st.button(t("sidebar_ollama_check_btn")):
            with st.spinner(t("sidebar_ollama_pinging")):
                ok, msg = check_ollama_status(ollama_url)
            if ok:
                st.success(f"✅ {msg}", icon="🦙")
            else:
                st.error(f"❌ {msg}", icon="🔴")
                st.code("ollama serve", language="bash")

# ── Header ──────────────────────────────────────────────────────────
active_backend = st.session_state.get("llm_backend", "Groq (Cloud)")
backend_badge  = "🦙 Ollama (Local)" if active_backend == "Ollama (Local)" else "☁️ Groq · LLaMA 3.1"

st.markdown(
    "<div style='text-align:center; padding: 20px 0 10px;'>"
    f"<h1 style='font-size:2.4rem;'>🎓 {t('app_title')}</h1>"
    f"<p style='font-size:1.05rem; color:#555;'>"
    f"<strong>{t('app_subtitle')}</strong> · {backend_badge}"
    "</p></div>",
    unsafe_allow_html=True,
)

# ── Tabs ─────────────────────────────────────────────────────────────
tab_home, tab_pdf, tab_resume, tab_interview, tab_roadmap = st.tabs([
    t("tab_home"), t("tab_pdf"), t("tab_resume"), t("tab_interview"), t("tab_roadmap")
])

with tab_home:
    st.markdown(t("home_welcome"))

with tab_pdf:
    pdf_assistant.render()

with tab_resume:
    resume_analyzer.render()

with tab_interview:
    interview_simulator.render()

with tab_roadmap:
    career_roadmap.render()
