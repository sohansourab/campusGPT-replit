"""
modules/interview_simulator.py
Interview Simulator — generate questions and evaluate answers.
"""

import streamlit as st
from utils import ask_llm
from i18n.translations import t

ROLES = [
    "Software Engineer",
    "Data Analyst",
    "ML Engineer",
    "Frontend Developer",
    "Backend Developer",
]


def generate_questions(role: str) -> str:
    prompt = (
        f"Generate 10 realistic, role-specific interview questions for a {role} position. "
        "Number each question and include a mix of technical, behavioural, and situational questions."
    )
    return ask_llm(prompt)


def evaluate_answer(role: str, answer: str) -> str:
    prompt = f"""Evaluate the following interview answer for a {role} position.

Answer:
{answer}

Provide:
1. **Score** (out of 10)
2. **What was good**
3. **What could be improved**
4. **Ideal answer outline**
"""
    return ask_llm(prompt)


def render() -> None:
    st.markdown(t("interview_title"))

    role = st.selectbox(t("interview_role_label"), ROLES, index=0)

    if st.button(t("interview_gen_btn"), type="primary"):
        with st.spinner(t("interview_gen_spinner")):
            questions = generate_questions(role)
        st.markdown(questions)

    st.markdown("---")
    st.markdown(t("interview_eval_heading"))

    answer = st.text_area(
        t("interview_answer_label"),
        placeholder=t("interview_answer_placeholder"),
        height=150,
    )

    if st.button(t("interview_eval_btn")):
        if not answer.strip():
            st.warning("⚠️")
        else:
            with st.spinner(t("interview_eval_spinner")):
                feedback = evaluate_answer(role, answer)
            st.markdown(feedback)
