# app.py

import streamlit as st
import numpy as np
import pickle



with open("model.pkl", "rb") as file:
    model = pickle.load(file)



st.title("Employee Attrition Prediction")

st.write("Fill the employee details below")


education = st.selectbox(
    "Education",
    (
        "Below College",
        "College",
        "Bachelor",
        "Master",
        "Doctor"
    )
)

environment = st.selectbox(
    "Environment Satisfaction",
    (
        "Low",
        "Medium",
        "High",
        "Very High"
    )
)

job_involvement = st.selectbox(
    "Job Involvement",
    (
        "Low",
        "Medium",
        "High",
        "Very High"
    )
)

job_satisfaction = st.selectbox(
    "Job Satisfaction",
    (
        "Low",
        "Medium",
        "High",
        "Very High"
    )
)

performance = st.selectbox(
    "Performance Rating",
    (
        "Low",
        "Good",
        "Excellent",
        "Outstanding"
    )
)

relationship = st.selectbox(
    "Relationship Satisfaction",
    (
        "Low",
        "Medium",
        "High",
        "Very High"
    )
)

worklife = st.selectbox(
    "Work Life Balance",
    (
        "Bad",
        "Good",
        "Better",
        "Best"
    )
)


education_map = {
    "Below College": 1,
    "College": 2,
    "Bachelor": 3,
    "Master": 4,
    "Doctor": 5
}

satisfaction_map = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Very High": 4
}

performance_map = {
    "Low": 1,
    "Good": 2,
    "Excellent": 3,
    "Outstanding": 4
}

worklife_map = {
    "Bad": 1,
    "Good": 2,
    "Better": 3,
    "Best": 4
}



education_val = education_map[education]

environment_val = satisfaction_map[environment]

job_involvement_val = satisfaction_map[job_involvement]

job_satisfaction_val = satisfaction_map[job_satisfaction]

performance_val = performance_map[performance]

relationship_val = satisfaction_map[relationship]

worklife_val = worklife_map[worklife]



if st.button("Predict"):

    input_data = np.array([[
        education_val,
        environment_val,
        job_involvement_val,
        job_satisfaction_val,
        performance_val,
        relationship_val,
        worklife_val
    ]])

    prediction = model.predict(input_data)

    # =====================================
    # OUTPUT
    # =====================================

    if prediction[0] == 1:

        st.error("Yes - Employee is likely to leave")

    else:

        st.success("No - Employee is likely to stay")