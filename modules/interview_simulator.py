"""
modules/interview_simulator.py
Interview Simulator — generate questions and evaluate answers.
"""

import streamlit as st
from utils import ask_llm

ROLES = [
    "Software Engineer",
    "Data Analyst",
    "ML Engineer",
    "Frontend Developer",
    "Backend Developer",
]


def generate_questions(role: str) -> str:
    if not role:
        return "⚠️ Please select a role."
    prompt = (
        f"Generate 10 realistic, role-specific interview questions for a {role} position. "
        "Number each question and include a mix of technical, behavioural, and situational questions."
    )
    return ask_llm(prompt)


def evaluate_answer(role: str, answer: str) -> str:
    if not answer.strip():
        return "⚠️ Please enter your answer before evaluating."
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
    st.markdown("## 🎤 Interview Simulator\nPractice role-specific interviews and get AI feedback on your answers.")

    role = st.selectbox("Select Role", ROLES, index=0)

    if st.button("Generate Questions", type="primary"):
        with st.spinner("Generating questions…"):
            questions = generate_questions(role)
        st.markdown(questions)

    st.markdown("---")
    st.markdown("### ✍️ Answer Evaluation")

    answer = st.text_area(
        "Your Answer",
        placeholder="Type your answer to one of the questions above…",
        height=150,
    )

    if st.button("Evaluate Answer"):
        with st.spinner("Evaluating…"):
            feedback = evaluate_answer(role, answer)
        st.markdown(feedback)
