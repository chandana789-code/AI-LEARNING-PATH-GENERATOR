import streamlit as st

# --------------------------------------------------
# Page Configuration
# --------------------------------------------------
st.set_page_config(
    page_title="AI Learning Path Generator",
    layout="centered"
)

st.title("AI-Powered Personalized Learning Path Generator")
st.write("Enter student details to receive a personalized learning path.")

# --------------------------------------------------
# Learning Paths with Links
# --------------------------------------------------
learning_paths = {
    0: [  # Beginner
        (
            "Conceptual Reading",
            "https://www.geeksforgeeks.org/data-structures/",
            "Build strong fundamentals from scratch"
        ),
        (
            "Basic Quizzes",
            "https://www.hackerrank.com/domains/tutorials",
            "Reinforce concepts with simple quizzes"
        ),
        (
            "Guided Practice",
            "https://leetcode.com/explore/",
            "Practice beginner-level problems"
        )
    ],

    1: [  # Intermediate
        (
            "Video Tutorials",
            "https://www.coursera.org",
            "Structured learning with examples"
        ),
        (
            "Hands-on Coding",
            "https://leetcode.com/problemset/",
            "Solve medium-level coding problems"
        ),
        (
            "Mini Projects",
            "https://github.com/topics/student-projects",
            "Apply concepts in real-world scenarios"
        )
    ],

    2: [  # Advanced
        (
            "Advanced Projects",
            "https://www.kaggle.com/competitions",
            "Work on industry-grade datasets"
        ),
        (
            "Real-world Applications",
            "https://github.com/trending",
            "Contribute to open-source projects"
        ),
        (
            "Mock Interviews",
            "https://www.pramp.com",
            "Prepare for technical interviews"
        ),
        (
            "Capstone Project",
            "https://www.coursera.org/projects",
            "Demonstrate end-to-end expertise"
        )
    ]
}

# --------------------------------------------------
# User Inputs
# --------------------------------------------------
learning_style = st.selectbox(
    "Learning Style",
    ["Visual", "Auditory", "Reading/Writing", "Kinesthetic"]
)

preferred_content = st.selectbox(
    "Preferred Content Type",
    ["Videos", "Articles", "Quizzes", "Projects"]
)

progress = st.slider("Learning Progress (%)", 0, 100, 30)
average_score = st.slider("Average Assessment Score", 0, 100, 45)
completed_courses = st.number_input(
    "Completed Courses",
    min_value=0,
    max_value=20,
    value=1
)
session_time = st.slider(
    "Daily Study Time (minutes)",
    0, 180, 60
)

# --------------------------------------------------
# Rule-Based Cluster Assignment (Baseline Logic)
# --------------------------------------------------
def assign_cluster(progress, avg_score):
    if progress <= 40 and avg_score <= 50:
        return 0   # Beginner
    elif progress <= 75 and avg_score <= 75:
        return 1   # Intermediate
    else:
        return 2   # Advanced

# --------------------------------------------------
# Generate Learning Path
# --------------------------------------------------
if st.button("Generate Learning Path"):

    cluster = assign_cluster(progress, average_score)

    cluster_names = {
        0: "Beginner Learner",
        1: "Intermediate Learner",
        2: "Advanced Learner"
    }

    st.success(f"Student Category: {cluster_names[cluster]}")

    st.subheader("Recommended Learning Path")

    for title, link, description in learning_paths[cluster]:
        with st.expander(title):
            st.write(description)
            st.markdown(f"[Access Resource]({link})")

    st.info(
        "This learning path is generated based on student performance, "
        "learning behavior, and engagement level."
    )

