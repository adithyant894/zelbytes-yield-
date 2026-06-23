import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from datetime import datetime

# ----------------------------
# Page Configuration
# ----------------------------
st.set_page_config(
    page_title="Zelbytes Agritech Yield Forecast",
    page_icon="🍄",
    layout="wide"
)

# ----------------------------
# Cached Model Loader
# ----------------------------
@st.cache_resource
def load_model():
    try:
        return joblib.load("models/champion.joblib")
    except FileNotFoundError:
        st.error(
            "Model file not found. Please check deployment files."
        )
        st.stop()

model = load_model()
LOG_FILE = "prediction_log.csv"

def log_prediction(inputs, prediction):

    row = {
        "timestamp": datetime.now(),
        **inputs,
        "prediction": prediction
    }

    df = pd.DataFrame([row])

    if os.path.exists(LOG_FILE):
        df.to_csv(
            LOG_FILE,
            mode="a",
            header=False,
            index=False
        )
    else:
        df.to_csv(
            LOG_FILE,
            index=False
        )

# ----------------------------
# Title
# ----------------------------
st.title("🍄 Mushroom Yield Forecast")
st.markdown(
    "Predict mushroom yield using environmental sensor readings."
)

# ----------------------------
# Sidebar Inputs
# ----------------------------
st.sidebar.header("Sensor Inputs")

temperature = st.sidebar.slider(
    "Temperature (°C)",
    min_value=10.0,
    max_value=40.0,
    value=25.0,
)

humidity = st.sidebar.slider(
    "Humidity (%)",
    min_value=20.0,
    max_value=100.0,
    value=70.0,
)

co2 = st.sidebar.slider(
    "CO₂ (ppm)",
    min_value=300,
    max_value=2000,
    value=800,
)

# ----------------------------
# Input Data
# ----------------------------
input_df = pd.DataFrame({
    "temperature": [temperature],
    "humidity": [humidity],
    "co2": [co2]
})

# ----------------------------
# Prediction
# ----------------------------
if st.button("Predict Yield"):

    with st.spinner("Generating prediction..."):
        prediction = model.predict(input_df)[0]

    log_prediction(
        input_df.iloc[0].to_dict(),
        prediction
    )

    st.metric(
        label="Predicted Yield",
        value=f"{prediction:.2f} kg"
    )

    st.success(
        f"Predicted Yield: {prediction:.2f} kg"
    )

    st.success(
        f"Predicted Yield: {prediction:.2f} kg"
    )

    # ------------------------
    # Sensitivity Analysis
    # ------------------------
    st.subheader("Humidity Sensitivity Analysis")

    humidity_range = np.linspace(20, 100, 50)

    sensitivity_df = pd.DataFrame({
        "temperature": temperature,
        "humidity": humidity_range,
        "co2": co2
    })

    sensitivity_predictions = model.predict(sensitivity_df)

    chart_df = pd.DataFrame({
        "Humidity": humidity_range,
        "Predicted Yield": sensitivity_predictions
    })

    st.line_chart(
        chart_df.set_index("Humidity")
    )

# ----------------------------
# Metadata
# ----------------------------
with st.expander("Model Information"):

    st.markdown("""
    **Model:** Random Forest Regressor

    **Version:** v1.0

    **Target:** Mushroom Yield Prediction

    **Input Features:**
    - Temperature (°C)
    - Humidity (%)
    - CO₂ (ppm)

    **Metric:** Test MAE (replace with your actual value)
    """)

# ----------------------------
# Validation Warnings
# ----------------------------
if temperature < 15 or temperature > 35:
    st.warning("Temperature is outside the recommended training range.")

if humidity < 30 or humidity > 90:
    st.warning("Humidity is outside the recommended training range.")

if co2 < 400 or co2 > 1500:
    st.warning("CO₂ is outside the recommended training range.")
