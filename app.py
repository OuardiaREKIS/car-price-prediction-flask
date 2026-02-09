from flask import Flask, request, jsonify, render_template
import pandas as pd
import numpy as np
import pickle

# ======================
# App init
# ======================
app = Flask(__name__)

# ======================
# Load artifacts
# ======================
with open("models/final_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("models/train_features.pkl", "rb") as f:
    train_features = pickle.load(f)

with open("models/brand_te.pkl", "rb") as f:
    brand_te = pickle.load(f)

with open("models/fuel_te_reg.pkl", "rb") as f:
    fuel_te_reg = pickle.load(f)

with open("models/ownership_encoder.pkl", "rb") as f:
    ownership_mapping = pickle.load(f)

with open("models/transmission_encoder.pkl", "rb") as f:
    transmission_mapping = pickle.load(f)

# ======================
# Utils
# ======================
def extract_brand(car_name):
    for brand in brand_te.keys():
        if car_name.startswith(brand):
            return brand
    return "Other"


def preprocess(df):
    """Apply SAME preprocessing as training"""
    CURRENT_YEAR = 2024

    df["age"] = CURRENT_YEAR - df["manufacture"]

    df["ownership_ord"] = df["ownership"].map(ownership_mapping)
    df["transmission_bin"] = df["transmission"].map(transmission_mapping)

    fuel_median = fuel_te_reg["fuel_median"]
    global_median = fuel_te_reg["global_median"]
    alpha = fuel_te_reg["alpha"]

    df["fuel_te_reg"] = df["fuel_type"].map(
        lambda x: alpha * fuel_median.get(x, global_median)
        + (1 - alpha) * global_median
    )

    df["brand"] = df["car_name"].apply(extract_brand)
    df["brand_te"] = df["brand"].map(brand_te).fillna(global_median)

    df = df.drop(
        columns=[
            "manufacture",
            "ownership",
            "transmission",
            "fuel_type",
            "car_name",
            "brand",
        ],
        errors="ignore",
    )

    for col in train_features:
        if col not in df.columns:
            df[col] = 0

    return df[train_features]

# ======================
# HTML Pages
# ======================
@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/predict_form", methods=["POST"])
def predict_form():
    data = {
        "car_name": request.form["car_name"],
        "driven_km": float(request.form["driven_km"]),
        "engine_cc": float(request.form["engine_cc"]),
        "seats": int(request.form["seats"]),
        "manufacture": int(request.form["manufacture"]),
        "fuel_type": request.form["fuel_type"],
        "transmission": request.form["transmission"],
        "ownership": request.form["ownership"],
    }

    df = preprocess(pd.DataFrame([data]))
    prediction = model.predict(df)[0]

    return render_template(
        "index.html",
        prediction_text=f"Estimated price: ${round(float(prediction), 2)}"
    )


# ======================
# API Endpoint
# ======================
@app.route("/predict", methods=["POST"])
def predict_api():
    data = request.get_json()
    if data is None:
        return jsonify({"error": "Invalid JSON input"}), 400

    df = preprocess(pd.DataFrame([data]))
    prediction = model.predict(df)[0]

    return jsonify({
        "predicted_price_dollar": round(float(prediction), 2)
    })

# ======================
# Run app
# ======================
if __name__ == "__main__":
    app.run(debug=True)
