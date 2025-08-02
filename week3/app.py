import streamlit as st
import joblib
import numpy as np

model = joblib.load("Farm_Irrigation_System.pkl")

st.title("Farm Irrigation System")
st.write("Predict irrigation requirement using sensor data")

cols = st.columns(4)

inputs = []
for i in range(20):
    col = cols[i % 4]
    val = st.number_input(f"Sensor {i}", value=0.0)
    inputs.append(val)

if st.button("Predict"):
    input_array = np.array([inputs])
    prediction = model.predict(input_array)[0]
    st.success(f"Prediction for parcels: {prediction}")
