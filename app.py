import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Cargar el modelo y el escalador
model = joblib.load("models/regression_model.pkl")
scaler = joblib.load("models/scaler.pkl")

# Cargar el dataset para obtener rangos de entrada
import os
from kaggle.api.kaggle_api_extended import KaggleApi

# Descargar el dataset
api = KaggleApi()
api.authenticate()

dataset = "fedesoriano/the-boston-houseprice-data"
download_path = "datasets"
api.dataset_download_files(dataset, path=download_path, unzip=True)

print(f"Dataset descargado y extraído en: {download_path}")

# Load CSV into a DataFrame
#data = pd.read_csv(f"{path}/boston.csv")   #inicial
data = pd.read_csv(f"{download_path}/boston.csv")

feature_names = data.drop(columns=["MEDV"]).columns

# Interfaz Streamlit
st.title("Boston House Price Prediction")
st.write("Interactive demo: Predict house prices based on different features.")

# Entradas dinámicas para las características
st.sidebar.header("Input Features")
inputs = {}
for feature in feature_names:
    inputs[feature] = st.sidebar.number_input(
        f"{feature}", 
        min_value=float(data[feature].min()), 
        max_value=float(data[feature].max()), 
        value=float(data[feature].mean())
    )

# Convertir inputs a array y predecir
input_array = np.array([list(inputs.values())]).reshape(1, -1)
scaled_input = scaler.transform(input_array)
prediction = model.predict(scaled_input)

# Mostrar resultado
st.subheader("Prediction")
st.write(f"Predicted Median House Price: ${prediction[0]*1000:.2f}")
