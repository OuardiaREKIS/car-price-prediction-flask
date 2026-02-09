# Car Price Prediction – Flask App

This project aims to estimate the price of a second-hand car based on its characteristics using machine learning.
It includes data analysis, feature engineering, model training, and a Flask web application for real-time predictions.

## Project Overview:

The goal is to help a car dealer (or user) estimate the market value of a used car before buying or selling it.

## The system:
- Trains regression models on historical car data
- Selects the best performing model
- Exposes predictions through a REST API and a web interface


## Project Structure
<pre>
test_comp/
│
├── app.py                 # Flask application
├── test_api.py            # Script to test the API
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
│
├── models/                # Saved models & encoders
│   ├── final_model.pkl
│   ├── train_features.pkl
│   ├── brand_te.pkl
│   ├── fuel_te_reg.pkl
│   ├── ownership_encoder.pkl
│   └── transmission_encoder.pkl
│
├── src/             # Data analysis & training notebooks
│
├── templates/
│   └── index.html         # Web interface
│
└── car_prices_data.csv    # Dataset
</pre>

## How to Run Locally
1️- Create & activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1       # Windows

2️- Install dependencies
pip install -r requirements.txt

3️-Run the Flask app
python app.py

4- Open your browser at: 
http://127.0.0.1:5000

or 

Enpoint locally by running:
python test_api.py


