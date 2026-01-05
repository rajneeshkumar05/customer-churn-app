import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib
import os

# Create model directory
os.makedirs("model", exist_ok=True)

# 1. Load dataset
df = pd.read_csv("data/churn.csv")

# 2. Drop customerID (not useful)
df.drop("customerID", axis=1, inplace=True)

# 3. Handle missing values
df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
df.dropna(inplace=True)

# 4. Encode categorical columns
label_encoders = {}

for col in df.select_dtypes(include="object"):
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# 5. Split features & target
X = df.drop("Churn", axis=1)
y = df["Churn"]

# 6. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 7. Train model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)

# 8. Evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# 9. Save model & encoders
joblib.dump(model, "model/churn_model.pkl")
joblib.dump(label_encoders, "model/encoders.pkl")

print("✅ Model & encoders saved successfully!")
