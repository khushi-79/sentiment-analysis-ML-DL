import streamlit as st
import joblib
import pickle
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# Load ML model
log_reg_model = joblib.load("../ml_models/log_reg_model.pkl")
vectorizer = joblib.load("../ml_models/vectorizer.pkl")

# Load DL model
lstm_model = load_model("../dl_models/lstm_model.h5")
with open("../dl_models/tokenizer.pkl", "rb") as f:
    tokenizer = pickle.load(f)

# Settings
max_length = 100  # should match what you used in training

# Streamlit UI
st.title("🧠 Sentiment Analysis App")
st.write("Enter a movie review below. Choose ML or DL model to get the sentiment prediction.")

text = st.text_area("Enter your review:")
model_type = st.radio("Choose Model:", ["ML - Logistic Regression", "DL - LSTM"])

if st.button("Predict"):
    if model_type == "ML - Logistic Regression":
        vec_text = vectorizer.transform([text])
        prediction = log_reg_model.predict(vec_text)[0]
    else:
        seq = tokenizer.texts_to_sequences([text])
        pad = pad_sequences(seq, maxlen=max_length, padding='post')
        prediction = lstm_model.predict(pad)
        prediction = int(prediction[0][0] > 0.5)
    
    sentiment = "😊 Positive" if prediction == 1 else "😠 Negative"
    st.success(f"Predicted Sentiment: {sentiment}")
