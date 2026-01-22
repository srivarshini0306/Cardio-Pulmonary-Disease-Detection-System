import streamlit as st
import numpy as np

from config import LUNG_CLASSES
from audio.heart_preprocessing import load_heart_audio, extract_heart_mfcc
from audio.lung_preprocessing import extract_lung_mfcc
from model.heart_model_loader import load_heart_model
from model.lung_model_loader import load_lung_model
from ui.visualizations import plot_waveform

st.set_page_config(page_title="Cardio–Pulmonary AI", layout="centered")
st.title("🫀🫁 Cardio–Pulmonary Disease Detection System")

mode = st.sidebar.selectbox("Select Diagnosis Type", ["Heart Murmur", "Lung Disease"])
uploaded_file = st.file_uploader("Upload Audio File (.wav / .mp3)", type=["wav", "mp3"])

heart_model = load_heart_model()
lung_model = load_lung_model()

if uploaded_file is not None:

    if mode == "Heart Murmur":
        y, sr = load_heart_audio(uploaded_file)
        st.pyplot(plot_waveform(y, sr))

        X = extract_heart_mfcc(y, sr)
        preds = heart_model.predict(X)
        st.success(f"Predicted Class: {np.argmax(preds)}")
        st.write("Probabilities:", preds)

    elif mode == "Lung Disease":
        X = extract_lung_mfcc(uploaded_file)
        preds = np.squeeze(lung_model.predict(X))

        cls = np.argmax(preds)
        st.success(f"Predicted Disease: {LUNG_CLASSES[cls]}")
        st.info(f"Confidence: {preds[cls]*100:.2f}%")

        st.bar_chart({LUNG_CLASSES[i]: preds[i] for i in range(len(LUNG_CLASSES))})
