from fastapi import FastAPI, HTTPException
import joblib
import os
from utils import send_alert_email

app = FastAPI()

MODEL_PATH = "model.pkl"

@app.get("/")
def root():
    return {"message": "KT Practical Exam - FastAPI Server Running"}

@app.post("/predict")
def predict(payload: dict):
    try:
        required_keys = ["sqft", "bedrooms", "bathrooms"]

        # Validate input
        for key in required_keys:
            if key not in payload:
                raise ValueError(f"Missing key: {key}")

        # Load model
        model = joblib.load(MODEL_PATH)

        # Prepare input
        input_data = [[
            payload["sqft"],
            payload["bedrooms"],
            payload["bathrooms"]
        ]]

        prediction = model.predict(input_data)[0]

        return {"prediction": float(prediction)}

    except Exception as e:
        send_alert_email(f"Prediction failed: {str(e)}")
        raise HTTPException(status_code=500, detail="Prediction failed")
