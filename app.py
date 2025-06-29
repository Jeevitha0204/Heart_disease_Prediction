
import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("heart_model.pkl", "rb"))

st.title("Heart Disease Prediction App")

age = st.slider("Age", 20, 80)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
trestbps = st.slider("Resting BP", 80, 200)
chol = st.slider("Cholesterol", 100, 600)
fbs = st.selectbox("Fasting Blood Sugar > 120", [0, 1])
restecg = st.selectbox("Resting ECG", [0, 1, 2])
thalach = st.slider("Max Heart Rate", 60, 220)
exang = st.selectbox("Exercise Induced Angina", [0, 1])
oldpeak = st.slider("Oldpeak", 0.0, 6.0, step=0.1)
slope = st.selectbox("Slope", [0, 1, 2])
ca = st.selectbox("Major Vessels Colored", [0, 1, 2, 3, 4])
thal = st.selectbox("Thal", [1, 2, 3])

input_data = np.array([[age, sex, cp, trestbps, chol, fbs, restecg,
                        thalach, exang, oldpeak, slope, ca, thal]])

if st.button("Predict"):
    prediction = model.predict(input_data)
    st.success("Low Risk" if prediction[0]==0 else "High Risk")
