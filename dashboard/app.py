import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page Configuration
# -----------------------------
st.set_page_config(
    page_title="FlowCast",
    page_icon="🚖",
    layout="wide"
)

# -----------------------------
# Sidebar
# -----------------------------
st.sidebar.title("🚖 FlowCast")

st.sidebar.info(
    """
    Predict hourly NYC taxi demand using a trained
    Machine Learning model.
    """
)

st.sidebar.markdown("---")

st.sidebar.success("Model: Random Forest")

# -----------------------------
# Main Page
# -----------------------------
st.title("🚖 FlowCast")

st.subheader("NYC Taxi Demand Prediction")

st.write(
    "Enter the required information below to predict hourly taxi demand."
)



# -----------------------------
# User Inputs
# -----------------------------



st.markdown("## Enter Prediction Inputs")

col1, col2 = st.columns(2)

with col1:
    pickup_location = st.number_input(
        "Pickup Location ID",
        min_value=1,
        value=161
    )

    hour = st.slider(
        "Hour",
        min_value=0,
        max_value=23,
        value=10
    )

    day_of_week = st.selectbox(
        "Day of Week",
        options=list(range(7))
    )

    month = st.selectbox(
        "Month",
        options=list(range(1, 13))
    )

with col2:
    lag_1 = st.number_input(
        "Lag 1",
        value=42.0
    )

    lag_24 = st.number_input(
        "Lag 24",
        value=36.0
    )

    rolling_mean_3 = st.number_input(
        "Rolling Mean (3)",
        value=39.3
    )

    rolling_mean_24 = st.number_input(
        "Rolling Mean (24)",
        value=37.8
    )

    rolling_std_24 = st.number_input(
        "Rolling Std (24)",
        value=4.2
    )

peak_hour = st.checkbox("Peak Hour", value=True)



# -----------------------------
# Load Model
# -----------------------------

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "models" / "best_model.pkl"

model = joblib.load(MODEL_PATH)

# -----------------------------
# Prediction Button
# -----------------------------

if st.button("🚀 Predict Demand"):

    sample_input = pd.DataFrame({
    "PULocationID": [pickup_location],
    "hour": [hour],
    "day_of_week": [day_of_week],
    "month": [month],
    "is_weekend": [1 if day_of_week >= 5 else 0],
    "lag_1": [lag_1],
    "lag_24": [lag_24],
    "rolling_mean_3": [rolling_mean_3],
    "rolling_mean_24": [rolling_mean_24],
    "rolling_std_24": [rolling_std_24],
    "is_peak_hour": [1 if peak_hour else 0]
    })


  
    prediction = model.predict(sample_input)

    st.success(f"🚖 Predicted Taxi Demand: {prediction[0]:.2f}")