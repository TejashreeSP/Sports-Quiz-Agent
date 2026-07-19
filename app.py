import streamlit as st

from src.database import setup_and_populate_db
from src.generator import generate_quiz

# -------------------------
# Page Configuration
# -------------------------
st.set_page_config(
    page_title="AI Sports Quiz Generator",
    page_icon="🏆",
    layout="centered"
)

# -------------------------
# Initialize Database
# -------------------------
setup_and_populate_db()

# -------------------------
# Title
# -------------------------
st.title("🏆 AI-Powered Sports Quiz Generator")

st.write(
    "Generate engaging sports quizzes using **ChromaDB + Web Search + Gemini AI**."
)

# -------------------------
# Sidebar
# -------------------------
st.sidebar.header("Quiz Settings")

sport = st.sidebar.selectbox(
    "Select Sport",
    [
        "Cricket",
        "Football",
        "Basketball",
        "Tennis",
        "Badminton"
    ]
)

difficulty = st.sidebar.selectbox(
    "Difficulty",
    [
        "Easy",
        "Medium",
        "Hard"
    ]
)

num_questions = st.sidebar.selectbox(
    "Number of Questions",
    [4, 5]
)


if st.button("Generate Quiz"):

    with st.spinner("Generating quiz..."):

        quiz = generate_quiz(
            sport=sport,
            difficulty=difficulty,
            num_questions=num_questions
        )

    st.success("Quiz Generated Successfully!")

    st.markdown("---")

    st.markdown(quiz)


if st.button("Regenerate Quiz"):

    with st.spinner("Generating a new quiz..."):

        quiz = generate_quiz(
            sport=sport,
            difficulty=difficulty,
            num_questions=num_questions
        )

    st.success("New Quiz Generated!")

    st.markdown("---")

    st.markdown(quiz)