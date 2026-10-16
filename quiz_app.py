# WHY/DESIGN:
# This app uses Streamlit’s session_state to maintain quiz progress across reruns,
# ensuring the current question, score, and answer status persist after each user action.
# A single quiz selector in the sidebar controls which question set is loaded, and
# switching quiz types resets progress to prevent mixed state. The main content area
# dynamically renders questions, multiple‑choice options, feedback, and navigation.
# A results screen records completed quizzes and allows restarting. Sidebar controls
# provide clear navigation and a persistent list of finished quizzes, creating a clean,
# predictable user experience.



import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Quiz App", page_icon="📝", layout="wide")

#---Initialize Session State----

if "quiz" not in st.session_state:
    st.session_state["quiz"]=[ 
        {"text": "Welcome to the Quiz App! Challenge yourself and Good Luck",
         "time":datetime.now().strftime("%H:%M")}
    ]



if "current_question" not in st.session_state:
    st.session_state.current_question = 0

if "score" not in st.session_state:
    st.session_state.score = 0

if "answered" not in st.session_state:
    st.session_state.answered = False

if "completed_quizzes" not in st.session_state:
    st.session_state.completed_quizzes = []


html_questions = [
    {
        "question": "What does HTML stand for?",
        "options": [
            "Hyper Text Markup Language",
            "High Tech Modern Language",
            "Hyperlink Transfer Modeling Language",
            "Home Tool Markup Language"
        ],
        "answer": 0
    },
    {
        "question": "Which tag is used to create a hyperlink?",
        "options": ["<link>", "<a>", "<href>", "<url>"],
        "answer": 1
    },
    {
        "question": "Which tag inserts an image?",
        "options": ["<img>", "<picture>", "<src>", "<image>"],
        "answer": 0
    },
    {
        "question": "Which HTML element represents the largest heading?",
        "options": ["<h6>", "<h3>", "<h1>", "<header>"],
        "answer": 2
    },
    {
        "question": "Which attribute is required for the <img> tag?",
        "options": ["alt", "href", "title", "src"],
        "answer": 3
    }
]

python_questions = [
    {
        "question": "Which keyword defines a function in Python?",
        "options": ["func", "define", "def", "lambda"],
        "answer": 2
    },
    {
        "question": "What is the correct file extension for Python files?",
        "options": [".py", ".python", ".pt", ".p"],
        "answer": 0
    },
    {
        "question": "Which data type is immutable?",
        "options": ["list", "dictionary", "tuple", "set"],
        "answer": 2
    },
    {
        "question": "What does the len() function do?",
        "options": [
            "Returns the number of items",
            "Returns the last element",
            "Returns the type of a variable",
            "Returns the memory size"
        ],
        "answer": 0
    },
    {
        "question": "Which operator is used for exponentiation?",
        "options": ["^", "**", "//", "exp()"],
        "answer": 1
    }
]

sql_questions = [
    {
        "question": "Which SQL command retrieves data from a table?",
        "options": ["GET", "SELECT", "FETCH", "RETURN"],
        "answer": 1
    },
    {
        "question": "Which clause filters rows in a SELECT query?",
        "options": ["ORDER BY", "WHERE", "GROUP BY", "FILTER"],
        "answer": 1
    },
    {
        "question": "Which SQL keyword sorts results?",
        "options": ["SORT", "ORDER BY", "ARRANGE", "GROUP BY"],
        "answer": 1
    },
    {
        "question": "Which command inserts new data?",
        "options": ["ADD", "INSERT INTO", "UPDATE", "PUT"],
        "answer": 1
    },
    {
        "question": "Which SQL function counts rows?",
        "options": ["SUM()", "COUNT()", "TOTAL()", "ROWS()"],
        "answer": 1
    }
]

quiz_types = {
    "HTML": html_questions,
    "Python": python_questions,
    "SQL": sql_questions
}


#----Sidebar: Tag Filters-----

with st.sidebar:

    quiz_choice = st.selectbox("Choose Quiz Type", ["HTML", "Python", "SQL"], key="quiz_type_selector")

    st.divider()

    st.write("### Completed Quizzes")
    if st.session_state.completed_quizzes:
        for q in st.session_state.completed_quizzes:
            st.write(f"- {q}")
    else:
        st.write("No quizzes completed yet.")

    if st.button("Reset All Progress"):
        st.session_state.completed_quizzes = []
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()


# Initialize last_quiz_choice if needed
if "last_quiz_choice" not in st.session_state:
    st.session_state.last_quiz_choice = quiz_choice

# If user switches quiz type, reset quiz progress
if quiz_choice != st.session_state.last_quiz_choice:
    st.session_state.current_question = 0
    st.session_state.score = 0
    st.session_state.answered = False
    st.session_state.last_quiz_choice = quiz_choice

# Load the correct question list
questions = quiz_types[quiz_choice]
#---Main Content Header----

icons = {
    "HTML": "🌐",
    "Python": "🐍",
    "SQL": "🗄️"
}

st.title(f"{icons[quiz_choice]} {quiz_choice} Quiz")

# ---------------------------------------------------------
# MAIN QUIZ CONTENT
# ---------------------------------------------------------

# If quiz is finished, show results
if st.session_state.current_question >= len(questions):
    st.subheader("Quiz Complete!")
    st.write(f"Your final score: {st.session_state.score} / {len(questions)}")

    # Add quiz to completed list
    if quiz_choice not in st.session_state.completed_quizzes:
        st.session_state.completed_quizzes.append(quiz_choice)



    if st.button("Restart Quiz"):
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.answered = False
        st.rerun()

else:
    # Show progress
    st.write(f"Question {st.session_state.current_question + 1} of {len(questions)}")
    st.progress((st.session_state.current_question + 1) / len(questions))

    # Get current question
    q = questions[st.session_state.current_question]

    # Display question
    st.subheader(q["question"])

    # Display options
    selected = st.radio("Choose an answer:", q["options"], key=f"q_{st.session_state.current_question}")

    # Submit button
    if st.button("Submit Answer"):
        st.session_state.answered = True
        if q["options"].index(selected) == q["answer"]:
            st.success("Correct!")
            st.session_state.score += 1
        else:
            st.error("Incorrect!")
            st.write(f"Correct answer: **{q['options'][q['answer']]}**")

    # Next button (only after answering)
    if st.session_state.answered:
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.session_state.answered = False
            st.rerun()
