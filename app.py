import streamlit as st
import pickle
import numpy as np

with open("heart_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("❤️ Heart Disease Predictor")
st.write("Enter patient details below to predict heart disease risk.")

age = st.slider("Age", 20, 80, 50)
sex = st.selectbox("Sex", [0, 1], format_func=lambda x: "Female" if x == 0 else "Male")
cp = st.slider("Chest Pain Type (0-3)", 0, 3, 1)
trestbps = st.slider("Resting Blood Pressure", 90, 200, 120)
chol = st.slider("Cholesterol", 100, 600, 200)
fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
restecg = st.slider("Resting ECG (0-2)", 0, 2, 1)
thalach = st.slider("Max Heart Rate", 70, 210, 150)
exang = st.selectbox("Exercise Induced Angina", [0, 1], format_func=lambda x: "No" if x == 0 else "Yes")
oldpeak = st.slider("ST Depression", 0.0, 6.0, 1.0)
slope = st.slider("Slope (0-2)", 0, 2, 1)
ca = st.slider("Number of Major Vessels (0-3)", 0, 3, 0)
thal = st.slider("Thal (1-3)", 1, 3, 2)

input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                         restecg, thalach, exang, oldpeak, slope, ca, thal]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    if prediction[0] == 1:
        st.error("⚠️ High risk of heart disease detected.")
    else:
        st.success("✅ Low risk of heart disease.")