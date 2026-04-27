# To implement Streamlit applications in Python, specifically:
""" 1. To use virtual environments and launch Streamlit applications
 2. To accept user input using Streamlit widgets
 3. To display various types of content using Streamlit display functions

Created on Mon Apr 27 14:19:22 2026

@author: swapnil
"""

import streamlit as st

# Title and header
st.title("Simple Streamlit Application")
st.header("User Input and Display Demo")

# User input widgets
name = st.text_input("Enter your name:")
age = st.number_input("Enter your age:", min_value=1, max_value=100)
color = st.selectbox("Choose your favorite color:", ["Red", "Blue", "Green"])

# Button
if st.button("Submit"):
 st.success("Data submitted successfully!")
st.write("Name:", name)
st.write("Age:", age)
st.write("Favorite Color:", color)

# Display text and markdown
st.markdown("### This is a Markdown heading")
st.text("This is plain text output")
