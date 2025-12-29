import streamlit as st
import pandas as pd
import joblib
import numpy as np

# Load the trained model and scaler
model = joblib.load("models/ridge_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Streamlit App UI
st.title("House Price Prediction App")

st.write("Enter house features to predict SalePrice")

# Example inputs (keep minimal)
gr_liv_area = st.number_input("Above Ground Living Area in SquareFeet", value=1500)
overall_qual = st.slider("Overall Quality", 1, 10, 5)

# Prepare input data
input_data = pd.DataFrame({
    "GrLivArea": [gr_liv_area],
    "OverallQual": [overall_qual]
})

# Align columns with training data and perform scaling and prediction
# Ensure all features used in training are present
input_data = input_data.reindex(columns=scaler.feature_names_in_, fill_value=0) # Align columns with training data

scaled_input = scaler.transform(input_data)

prediction = model.predict(scaled_input)

# Display prediction
st.subheader("Predicted Sale Price")
#Real Price(Inverse log transformation of the predicted value)
predicted_price = np.expm1(prediction)[0] # Convert back from log scale(expm1)
st.write(f"${predicted_price:,.0f}")
