from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse

from backend.schemas import CustomerData
from backend.predictor import predict_churn

app = FastAPI(title="Customer Churn Prediction App")

# -------------------- CORS --------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],   # dev ke liye ok
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------- API ROUTE --------------------
@app.post("/predict")
def predict(data: CustomerData):
    return predict_churn(data.dict())

# -------------------- STATIC FILES --------------------
# frontend folder ko /static URL pe serve karega
app.mount("/static", StaticFiles(directory="frontend", html=True), name="static")

# -------------------- HOME ROUTE --------------------
# root URL se direct UI open ho jaayega
@app.get("/")
def home():
    return RedirectResponse(url="/static/index.html")
