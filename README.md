# Sentiment Analysis using Machine Learning & Deep Learning

This project performs sentiment analysis on text data using various machine learning and deep learning models. It classifies sentiments as **positive**, **negative**, or **neutral**.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/khushi-79/sentiment-analysis-ML-DL.git
cd sentiment-analysis-ML-DL
````

### 2. Create a virtual environment (optional but recommended)

```bash
python -m venv venv
# For Linux/Mac
source venv/bin/activate

# For Windows
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

After installing dependencies, launch the Streamlit app with:

```bash
streamlit run app.py
```

Then open your browser and go to:
[http://localhost:8501](http://localhost:8501)

---

## 🧠 Models Used

* Logistic Regression
* LSTM (Keras)

---

## 📊 Dataset

The project uses a sentiment-labeled dataset (e.g., Twitter, IMDB reviews).
Ensure that the data is available inside the `data/` directory or update the file paths accordingly in the code.
