
from fastapi import FastAPI
from app.models.request_models import RecommendationRequest
from app.services.location_service import get_coordinates
from app.services.weather_service import get_weather


app  = FastAPI(
        title="Biodiversity Native Planting Planner",
        version="1.0.0")
@app.get("/")
def home():
    return "You have reached the backend successfully"
 
@app.post("/recommend")
async def recommend(request: RecommendationRequest):

    coordinates = get_coordinates(request.city)

    if coordinates is None:
        return {
            "error": "Location not found"
        }

    weather = get_weather(
        coordinates["latitude"],
        coordinates["longitude"]
    )

    return {
        "location": request.city,
        "coordinates": coordinates,
        "weather": weather
    }

