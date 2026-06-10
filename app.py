import streamlit as st

st.set_page_config(
    page_title="CampusGPT",
    page_icon="🎓",
    layout="wide"
)

# ---------------------
# Header
# ---------------------

st.title("🎓 CampusGPT")
st.markdown("### AI-Powered Student Success Platform")

# ---------------------
# Sidebar
# ---------------------

module = st.sidebar.radio(
    "Choose Module",
    [
        "🏠 Home",
        "📄 PDF Assistant",
        "📑 Resume Analyzer",
        "🎤 Interview Simulator",
        "🛣 Career Roadmap"
    ]
)

# ---------------------
# Home
# ---------------------

if module == "🏠 Home":

    st.title("🎓 CampusGPT")
    st.caption("AI-Powered Student Success Platform")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Modules", "4")

    with col2:
        st.metric("AI Model", "Groq (LLaMA)")

    with col3:
        st.metric("System", "Stable")

    with col4:
        st.metric("Status", "Ready")

    st.divider()

    c1, c2 = st.columns(2)

    with c1:
        st.info("📄 PDF Assistant\nChat with PDFs using AI")
        st.info("📑 Resume Analyzer\nATS Score & Suggestions")

    with c2:
        st.info("🎤 Interview Simulator\nPractice Interviews")
        st.info("🛣 Career Roadmap\nPersonalized Learning Plan")

# ---------------------
# PDF Assistant
# ---------------------

elif module == "📄 PDF Assistant":

    from utils.pdf_utils import extract_text_from_pdf
    from utils.gemini_helper import ask_gemini

    st.header("📄 PDF Assistant")

    uploaded_pdf = st.file_uploader("Upload PDF", type=["pdf"])

    if uploaded_pdf:

        text = extract_text_from_pdf(uploaded_pdf)
        st.success("PDF Loaded")

        question = st.text_input("Ask a Question")

        if "pdf_answer" not in st.session_state:
            st.session_state.pdf_answer = None

        if st.button("Ask PDF"):

            prompt = f"""
            Answer using PDF content:

            {text[:12000]}

            Question:
            {question}
            """

            st.session_state.pdf_answer = ask_gemini(prompt)

        if st.session_state.pdf_answer:
            st.markdown(st.session_state.pdf_answer)

# ---------------------
# Resume Analyzer
# ---------------------

elif module == "📑 Resume Analyzer":

    from utils.pdf_utils import extract_text_from_pdf
    from utils.gemini_helper import ask_gemini

    st.header("📑 Resume Analyzer")

    uploaded_resume = st.file_uploader("Upload Resume (PDF)", type=["pdf"])

    if uploaded_resume:

        with st.spinner("Reading Resume..."):
            resume_text = extract_text_from_pdf(uploaded_resume)

        st.success("Resume Uploaded")

        if "resume_result" not in st.session_state:
            st.session_state.resume_result = None

        if st.button("Analyze Resume"):

            prompt = f"""
            You are an ATS expert.

            Resume:
            {resume_text}

            Provide:
            - ATS Score
            - Skills
            - Strengths
            - Weaknesses
            - Improvements
            """

            with st.spinner("Analyzing..."):
                st.session_state.resume_result = ask_gemini(prompt)

        if st.session_state.resume_result:
            st.markdown(st.session_state.resume_result)

            st.download_button(
                "📥 Download",
                st.session_state.resume_result,
                file_name="resume_analysis.txt"
            )

# ---------------------
# Interview Simulator
# ---------------------

elif module == "🎤 Interview Simulator":

    from utils.gemini_helper import ask_gemini

    st.header("🎤 Interview Simulator")

    role = st.selectbox(
        "Select Role",
        [
            "Software Engineer",
            "Data Analyst",
            "ML Engineer",
            "Frontend Developer",
            "Backend Developer"
        ]
    )

    if "questions" not in st.session_state:
        st.session_state.questions = None

    if st.button("Generate Questions"):

        prompt = f"Generate 10 interview questions for {role}"

        st.session_state.questions = ask_gemini(prompt)

    if st.session_state.questions:
        st.markdown(st.session_state.questions)

    st.divider()

    st.subheader("Answer Evaluation")

    answer = st.text_area("Your Answer")

    if "eval_result" not in st.session_state:
        st.session_state.eval_result = None

    if st.button("Evaluate Answer"):

        prompt = f"""
        Evaluate answer for {role}:

        {answer}

        Give score + feedback
        """

        st.session_state.eval_result = ask_gemini(prompt)

    if st.session_state.eval_result:
        st.markdown(st.session_state.eval_result)

# ---------------------
# Career Roadmap
# ---------------------

elif module == "🛣 Career Roadmap":

    from utils.gemini_helper import ask_gemini

    st.header("🛣 Career Roadmap Generator")

    goal = st.text_input("Enter Career Goal")

    if "roadmap" not in st.session_state:
        st.session_state.roadmap = None

    if st.button("Generate Roadmap"):

        prompt = f"""
        Roadmap for {goal}:

        Skills, timeline, projects, resources
        """

        st.session_state.roadmap = ask_gemini(prompt)

    if st.session_state.roadmap:
        st.markdown(st.session_state.roadmap)

        st.download_button(
            "📥 Download",
            st.session_state.roadmap,
            file_name="roadmap.txt"
        )