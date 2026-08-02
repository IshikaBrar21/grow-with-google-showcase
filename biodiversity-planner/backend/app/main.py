
from fastapi import FastAPI
from app.models.request_models import RecommendationRequest

app  = FastAPI(
        title="Biodiversity Native Planting Planner",
        version="1.0.0")
@app.get("/")
def home():
    return "You have reached the backend successfully"
 
@app.post("/recommend")
def recommend(request: RecommendationRequest):
    return {
            "city":request.city,
            "garden_size":request.garden_size,
            "sunlight":request.sunlight,
            "maintenance":request.maintenance
            }

