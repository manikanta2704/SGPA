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
num_subjects = st.number_input("Number of Subjects", min_value=1, max_value=9, value=1)

grades = []
credits = []

for i in range(num_subjects):
    grade = st.selectbox(f"Select Grade for Subject {i + 1}", list(grade_points.keys()))
    credit = st.selectbox(f"Select Credits for Subject {i + 1}", [1.5, 2, 3])
    grades.append(grade)
    credits.append(credit)

# Calculate SGPA
if st.button("Calculate SGPA"):
    sgpa = calculate_sgpa(grades, credits)
    st.write("<div class='result-box'>", unsafe_allow_html=True)
    st.write(f"<p>SGPA: <span class='sgpa'>{sgpa:.2f}</span></p>")
    
    # Check if the student passed or failed
    if 'F' not in grades:
        st.write("<p class='pass'>Result: Pass</p>")
    else:
        st.write("<p class='fail'>Result: Fail</p>")
    
    # Show percentage equivalent
    total_points = sum(grade_points[g] * c for g, c in zip(grades, credits))
    max_possible = sum(max(grade_points.values()) * c for c in credits)
    percentage = (total_points / max_possible) * 100
    st.write(f"<p>Percentage Equivalent: {percentage:.2f}%</p>")
    st.write("</div>", unsafe_allow_html=True)
    
    # Animate the result message
    st.write('<style>div.result-box{animation: fadeIn 2s;}</style>', unsafe_allow_html=True)
    st.write('<script>setTimeout(function() {document.querySelector(".result-box").style.animation = "fadeOut 2s";}, 4000);</script>', unsafe_allow_html=True)
    
# Calculate CGPA
st.header("Calculate CGPA")
num_semesters = st.number_input("Number of Semesters", min_value=1, max_value=8, value=1)

sgpas = []
for i in range(num_semesters):
    sgpa = st.number_input(f"Enter SGPA for Semester {i + 1}", min_value=0.0, max_value=10.0, value=9.0)
    sgpas.append(sgpa)

if st.button("Calculate CGPA"):
    cgpa = mean(sgpas)
    st.write("<div class='result-box'>", unsafe_allow_html=True)
    st.write(f"<p>CGPA: <span class='cgpa'>{cgpa:.2f}</span></p>")
    
    # Animate the result message
    st.write('<style>div.result-box{animation: fadeIn 2s;}</style>', unsafe_allow_html=True)
    st.write('<script>setTimeout(function() {document.querySelector(".result-box").style.animation = "fadeOut 2s";}, 4000);</script>', unsafe_allow_html=True)
    
    # Show percentage equivalent
    total_points = sum(credits)
    max_possible = total_points * max(grade_points.values())
    percentage = (total_points / max_possible) * 100
    st.write(f"<p>Percentage Equivalent: {percentage:.2f}%</p>")
    st.write("</div>", unsafe_allow_html=True)

# Footer with instructions
st.markdown("""
<style>
.footer {
    text-align: center;
    font-size: 14px;
    padding: 10px;
}
</style>
<div class="footer">
    <p>Enter SGPA as a decimal (e.g., 9.5 for A+)</p>
    <p>For CGPA, enter the SGPA for each semester.</p>
</div>
""", unsafe_allow_html=True)
