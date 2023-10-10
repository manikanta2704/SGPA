import streamlit as st
import time
from numpy import mean

# Define a function to calculate SGPA
def calculate_sgpa(grades, credits):
    total_credits = sum(credits)
    sgpa = sum(grade_points[g] * c for g, c in zip(grades, credits)) / total_credits
    return sgpa

# Define grade points
grade_points = {
    "A+": 10,
    "A": 9,
    "B": 8,
    "C": 7,
    "D": 6,
    "E": 5,
    "F": 0,
}

# Custom CSS styling for the app
st.markdown(
    """
    <style>
    body {
        background-color: #f0f0f0;
    }
    .stApp {
        max-width: 600px;
        margin: 0 auto;
    }
    .stButton button {
        background-color: #007BFF;
        color: #fff;
        border: none;
        border-radius: 5px;
        padding: 10px 20px;
        cursor: pointer;
    }
    .stButton button:hover {
        background-color: #0056b3;
    }
    .result-box {
        padding: 20px;
        margin-top: 20px;
        border: 2px solid #ddd;
        border-radius: 5px;
        background-color: #fff;
    }
    .pass {
        color: green;
    }
    .fail {
        color: red;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Streamlit app title and heading
st.title("SGPA & CGPA Calculator")
st.header("Calculate SGPA")

# Create inputs for subject grades and credits
num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=8, value=1)

grades = []
credits = []

for i in range(num_subjects):
    grade = st.selectbox(f"Select Grade for Subject {i + 1}", list(grade_points.keys()))
    credit = st.selectbox(f"Select Credits for Subject {i + 1}", [1, 1.5, 2])
    grades.append(grade)
    credits.append(credit)

# Calculate SGPA
if st.button("Calculate SGPA"):
    sgpa = calculate_sgpa(grades, credits)
    st.markdown("<div class='result-box'>", unsafe_allow_html=True)
    st.markdown(f"<p>SGPA: <span class='sgpa'>{sgpa:.2f}</span></p>", unsafe_allow_html=True)
    
    # Check if the student passed or failed
    if 'F' not in grades:
        st.markdown("<p class='pass'>Result: Pass</p>", unsafe_allow_html=True)
    else:
        st.markdown("<p class='fail'>Result: Fail</p>", unsafe_allow_html=True)
    
    # Show percentage equivalent
    total_points = sum(grade_points[g] * c for g, c in zip(grades, credits))
    max_possible = sum(max(grade_points.values()) * c for c in credits)
    percentage = (total_points / max_possible) * 100
    st.markdown(f"<p>Percentage Equivalent: {percentage:.2f}%</p>", unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Animate the result message
    st.markdown('<style>div.result-box{animation: fadeIn 2s;}</style>', unsafe_allow_html=True)
    st.markdown('<script>setTimeout(function() {document.querySelector(".result-box").style.animation = "fadeOut 2s";}, 4000);</script>', unsafe_allow_html=True)
