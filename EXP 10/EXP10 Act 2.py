# Create a BMI health checker app.
"""
Created on Mon Apr 27 15:48:01 2026

@author: swapnil
"""

import streamlit as st

st.set_page_config(page_title="BMI Health Checker", page_icon="⚖️")

st.title("⚖️ BMI Health Checker")
st.write("Calculate your Body Mass Index and check your health category.")

# Sidebar for unit selection
unit = st.sidebar.radio("Select Units:", ("Metric (kg/cm)", "Imperial (lb/in)"))

# Input fields based on units
if unit == "Metric (kg/cm)":
    weight = st.number_input("Weight (kg)", min_value=1.0, value=70.0)
    height_cm = st.number_input("Height (cm)", min_value=50.0, value=170.0)
    height = height_cm / 100  # Convert to meters
else:
    weight_lb = st.number_input("Weight (lb)", min_value=1.0, value=150.0)
    height_in = st.number_input("Height (inches)", min_value=1.0, value=67.0)
    # Conversion for BMI formula
    weight = weight_lb * 0.453592
    height = height_in * 0.0254

if st.button("Calculate BMI"):
    # BMI Formula: weight (kg) / height^2 (m)
    bmi = weight / (height ** 2)
    
    st.divider()
    st.subheader(f"Your BMI: **{bmi:.1f}**")

    # Determine Category and Color
    if bmi < 18.5:
        category = "Underweight"
        color = "blue"
        description = "You may need to consult a healthcare provider about reaching a healthy weight."
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
        color = "green"
        description = "You are in a healthy weight range. Keep it up!"
    elif 25 <= bmi < 30:
        category = "Overweight"
        color = "orange"
        description = "Being overweight may increase the risk of certain health issues."
    else:
        category = "Obese"
        color = "red"
        description = "It is recommended to speak with a doctor regarding your weight and health."

    # Display Result
    st.markdown(f"### Category: :{color}[{category}]")
    st.info(description)

    # Visual Gauge (Progress Bar approximation)
    progress_val = min(max((bmi - 10) / 30, 0.0), 1.0) # Normalized for display
    st.progress(progress_val)
    st.caption("Scale: 15 (Underweight) ——— 25 (Normal) ——— 30+ (Obese)")
