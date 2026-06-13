"""
modules/career_roadmap.py
Career Roadmap — personalized learning & career plan.
"""

import streamlit as st
from utils import ask_llm
from i18n.translations import t


def _build_prompt(goal: str) -> str:
    return f"""Create a detailed, personalized career roadmap for someone who wants to become a {goal}.

Structure the roadmap as follows:
1. **Overview** — what this career path looks like
2. **Core Skills to Learn** — with priority order
3. **Month-by-Month Timeline** (first 6 months)
4. **Recommended Projects** to build a portfolio
5. **Resources** (free + paid: courses, books, YouTube channels)
6. **Job Titles to Target** along the way
"""


def render() -> None:
    st.markdown(t("roadmap_title"))

    goal = st.text_input(
        t("roadmap_goal_label"),
        placeholder=t("roadmap_goal_placeholder"),
    )

    if st.button(t("roadmap_gen_btn"), type="primary"):
        if not goal.strip():
            st.warning(t("roadmap_warn_no_goal"))
        else:
            with st.spinner(t("roadmap_spinner")):
                roadmap = ask_llm(_build_prompt(goal))
            st.markdown(roadmap)
