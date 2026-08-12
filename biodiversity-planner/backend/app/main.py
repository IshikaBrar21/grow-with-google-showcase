from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.models.request_models import RecommendationRequest
from app.services.location_service import get_coordinates
# from app.services.weather_service import get_weather
from app.services.plant_service import load_plants
from app.recommendation_engine import recommend_plants
from app.models.response_models import RecommendationResponse


app  = FastAPI(
        title="Biodiversity Native Planting Planner",
        version="1.0.0")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allow all methods
    allow_headers=["*"],  # Allow all headers
)

@app.get("/")
def home():
    return {
        "message": "Welcome to the Biodiversity Native Planting Planner!"
    }
 
@app.post("/recommend",response_model=RecommendationResponse)
async def recommend(request: RecommendationRequest):

    coordinates = get_coordinates(request.city)

    if coordinates is None:
        raise HTTPException(status_code=404, detail="Location not found")

    # weather = get_weather(
    #     coordinates["latitude"],
    #     coordinates["longitude"]
    # )

    plants = load_plants()

    recommendations = recommend_plants(
        plants,
        request.sunlight
    )

    return RecommendationResponse(
        location=request.city,
        latitude=coordinates["latitude"],
        longitude=coordinates["longitude"],
        recommendations=recommendations
    )

