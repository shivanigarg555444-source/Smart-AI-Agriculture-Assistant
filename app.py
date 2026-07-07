
import streamlit as st
import joblib
from crop_info import crop_info

# Load Model
model = joblib.load("crop_model.pkl")

# Page Settings
st.set_page_config(
    page_title="Smart AI Agriculture Assistant",
    page_icon="🌾",
    layout="centered"
)

# Title
st.title("🌾 Smart AI Agriculture Assistant")
st.write("Enter Soil and Weather Details")

# User Inputs
N = st.number_input("Nitrogen (N)", min_value=0.0)
P = st.number_input("Phosphorus (P)", min_value=0.0)
K = st.number_input("Potassium (K)", min_value=0.0)
temperature = st.number_input("Temperature (°C)")
humidity = st.number_input("Humidity (%)")
ph = st.number_input("Soil pH")
rainfall = st.number_input("Rainfall (mm)")

# Prediction
if st.button("Predict Crop"):
    sample = [[N, P, K, temperature, humidity, ph, rainfall]]

    prediction = model.predict(sample)
    probabilities = model.predict_proba(sample)
    confidence = max(probabilities[0]) * 100

    crop = prediction[0]
    info = crop_info.get(crop)

    st.success(f"🌾 Recommended Crop: {crop.title()}")
    st.info(f"🎯 Confidence: {confidence:.2f}%")

    if info:
        st.subheader("🌱 Crop Information")

        st.write("🧪 Fertilizer:", info["fertilizer"])
        st.write("💧 Irrigation:", info["irrigation"])
        st.write("🌡 Temperature:", info["temperature"])
        st.write("🌧 Rainfall:", info["rainfall"])
        st.write("🧪 Soil pH:", info["ph"])
        st.write("📅 Season:", info["season"])
        st.write("⏳ Duration:", info["duration"])
        st.write("💦 Water Requirement:", info["water"])

        st.subheader("💡 Farmer Tips")
        for tip in info["tips"]:
            st.write("✔", tip)
