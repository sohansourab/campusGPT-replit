"""
modules/career_roadmap.py
Career Roadmap — personalized learning & career plan.
"""

import streamlit as st
from utils import ask_llm


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


def generate_roadmap(goal: str) -> str:
    if not goal.strip():
        return "⚠️ Please enter a career goal."
    return ask_llm(_build_prompt(goal))


def render() -> None:
    st.markdown("## 🛣️ Career Roadmap Generator\nGet a personalized, step-by-step plan to reach your career goal.")

    goal = st.text_input(
        "Career Goal",
        placeholder="e.g. Machine Learning Engineer, Full Stack Developer, Data Scientist…",
    )

    if st.button("Generate Roadmap", type="primary"):
        if not goal.strip():
            st.warning("⚠️ Please enter a career goal.")
        else:
            with st.spinner("Building your roadmap…"):
                roadmap = generate_roadmap(goal)
            st.markdown(roadmap)
