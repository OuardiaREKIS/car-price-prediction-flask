import requests

url = "http://127.0.0.1:5000/predict"

payload = {
    "car_name": "Hyundai Verna 1.4 VTVT",
    "driven_km": 90228,
    "engine_cc": 2982,
    "seats": 5,
    "manufacture": 2014,
    "fuel_type": "Petrol",
    "transmission": "Manual",
    "ownership": "1st Owner"
}

print("Sending request...")

response = requests.post(url, json=payload)

print("Status code:", response.status_code)
print("Raw response text:", response.text)

try:
    print("JSON response:", response.json())
except Exception as e:
    print("JSON decode error:", e)
