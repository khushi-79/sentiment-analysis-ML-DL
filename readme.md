# Sentiment Analysis using Machine Learning & Deep Learning

This project performs sentiment analysis on text data using various machine learning and deep learning models. It classifies the sentiments as **positive**, **negative**, or **neutral**.

## 📁 Project Structure

sentiment-analysis-ML-DL/
│
├── data/ # Raw and preprocessed data
├── models/ # Trained models and checkpoints
├── notebooks/ # Jupyter notebooks for EDA and modeling
├── app.py # Streamlit app script
├── requirements.txt # List of dependencies
└── Dockerfile # For containerization (optional)

bash
Copy
Edit

## ⚙️ Installation

### 1. Clone the repository
git clone https://github.com/khushi-79/sentiment-analysis-ML-DL.git
cd sentiment-analysis-ML-DL

### 2. Create a virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

### 3. Install dependencies
pip install -r requirements.txt

### 🚀 Running the Application
Once dependencies are installed, you can run the Streamlit application locally using:

streamlit run app.py
It will open in your browser at: http://localhost:8501

🧠 Models Used
Logistic Regression

Naive Bayes

Support Vector Machine (SVM)

LSTM (Keras)

📊 Dataset
The project uses a sentiment-labeled dataset (e.g., Twitter, IMDB reviews). Make sure the dataset exists in the data/ directory or update the code accordingly.

📦 Optional: Docker Setup
To build and run using Docker:

docker build -t sentiment-app .
docker run -p 8501:8501 sentiment-app

🙋‍♀️ Author
Khushi Pandya