import joblib
import pandas as pd

model = joblib.load("model/churn_model.pkl")
encoders = joblib.load("model/encoders.pkl")

def predict_churn(data: dict):
    df = pd.DataFrame([data])

    for col, encoder in encoders.items():
        if col in df.columns:
            df[col] = encoder.transform(df[col])

    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]

    return {
        "churn_prediction": "Yes" if prediction == 1 else "No",
        "churn_probability": round(probability * 100, 2)
    }
