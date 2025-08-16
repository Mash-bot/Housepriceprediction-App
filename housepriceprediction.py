import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("house_price_model.pkl", "rb") as f:
    pipeline = pickle.load(f)

st.title("🏠 House Price Prediction App")
st.write("Enter the house details below to predict its sale price:")

# ---- INPUTS ----
GrLivArea = st.number_input("Above Ground Living Area (sq ft)", min_value=300, max_value=6000, value=1500)
TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", min_value=0, max_value=3000, value=800)
GarageArea = st.number_input("Garage Area (sq ft)", min_value=0, max_value=1500, value=400)
OverallQual = st.slider("Overall Quality (1 = Very Poor, 10 = Excellent)", 1, 10, 5)

# Friendly names for MSZoning
zoning_map = {
    "Residential Low Density": "RL",
    "Residential Medium Density": "RM",
    "Residential High Density": "RH",
    "Floating Village Residential": "FV",
    "C (Commercial)": "C"
}

MSZoning_friendly = st.selectbox("Zoning Classification", list(zoning_map.keys()))
MSZoning = zoning_map[MSZoning_friendly]  # Map back to code for the model

# ---- PREDICTION ----
if st.button("Predict Sale Price"):
    input_data = pd.DataFrame({
        "GrLivArea": [GrLivArea],
        "TotalBsmtSF": [TotalBsmtSF],
        "GarageArea": [GarageArea],
        "OverallQual": [OverallQual],
        "MSZoning": [MSZoning]
    })

    prediction = pipeline.predict(input_data)[0]
    st.success(f"💰 Estimated Sale Price: ${prediction:,.2f}")


